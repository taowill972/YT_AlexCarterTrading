import os
import sys
import re
import json
import base64
import time
import socket
import urllib.request
import urllib.error
from pathlib import Path
from typing import List, Dict, Any, Optional

from config import (
    GEMINI_KEYS_FILE,
    VISUAL_GEMINI_MODEL,
    AUDIO_GEMINI_MODEL,
    CHANNEL_NAME
)

socket.setdefaulttimeout(45)

def _load_keys(filepath: Path) -> List[str]:
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            keys = [k.strip() for k in f if k.strip() and not k.startswith("#")]
        if keys:
            return keys
    raise ValueError(f"Fichier de clés introuvable ou vide : {filepath}")

_GEMINI_KEYS = _load_keys(GEMINI_KEYS_FILE)
_KEY_IDX = [0]
STATS = {"api_calls": 0, "rotations": 0, "failures": 0}

def call_gemini(parts: List[Dict[str, Any]], model: str = VISUAL_GEMINI_MODEL, retries: int = 5) -> str:
    """Appel résilient avec rotation automatique sur pool de clés et repli modèle."""
    models_to_try = [model, "gemini-3.5-flash", "gemini-3.8-flash"]

    for m in models_to_try:
        for attempt in range(retries):
            key = _GEMINI_KEYS[_KEY_IDX[0] % len(_GEMINI_KEYS)]
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={key}"
            payload = json.dumps({"contents": [{"parts": parts}]}).encode("utf-8")
            req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})

            try:
                with urllib.request.urlopen(req, timeout=35) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    cands = data.get("candidates", [])
                    if cands and "content" in cands[0] and "parts" in cands[0]["content"]:
                        STATS["api_calls"] += 1
                        return cands[0]["content"]["parts"][0].get("text", "")
            except urllib.error.HTTPError as e:
                _KEY_IDX[0] += 1
                STATS["rotations"] += 1
                if e.code in (429, 503, 500):
                    time.sleep(1.2)
                    continue
                err_text = e.read().decode("utf-8", "ignore")[:150]
                print(f"[Gemini] HTTPError {e.code} sur {m}: {err_text}", flush=True)
            except Exception as e:
                _KEY_IDX[0] += 1
                time.sleep(1.2)

    STATS["failures"] += 1
    return ""

def translate_title_fr(title_en: str) -> str:
    prompt = (
        f"Tu es un traducteur expert en vulgarisation financière, trading algorithmique et agents IA pour la chaîne {CHANNEL_NAME}.\n"
        "Traduis ce titre de vidéo YouTube de l'anglais vers un français captivant, élégant, professionnel et fidèle.\n"
        "Garde les noms de marques, protocoles et outils intacts (Claude Code, Grok Bots, Muse Wonder, Pine Script, TradingView, Blofin, WEEX, Python, etc.).\n"
        "Réponds STRICTEMENT avec le titre traduit uniquement, sans guillemets ni fioritures.\n\n"
        f"Titre : {title_en}"
    )
    res = call_gemini([{"text": prompt}], model=AUDIO_GEMINI_MODEL)
    return res.strip().replace('"', '') if res else title_en

def process_multimodal_block(
    candidate_frames: List[Dict[str, Any]],
    timestamp_str: str,
    text_en: str,
    audio_slice_path: Optional[Path] = None
) -> Dict[str, Any]:
    default_res = {
        "verbatim_fr": text_en,
        "valid_frame_indices": [],
        "frame_captions": {},
        "interface": "Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.",
        "contenu": "Explications orales des stratégies et mise en contexte méthodologique du marché.",
        "action": "Explications face caméra et analyse conceptuelle des marchés."
    }

    # 1. Audio Verbatim mot à mot intégral en Français
    if audio_slice_path and audio_slice_path.exists() and audio_slice_path.stat().st_size > 0:
        try:
            with open(audio_slice_path, "rb") as af:
                b64_audio = base64.b64encode(af.read()).decode("utf-8")
            audio_prompt = (
                f"Tu es un transcripteur et traducteur expert pour la chaîne YouTube '{CHANNEL_NAME}' (segment {timestamp_str}).\n"
                "Écoute attentivement le segment audio ci-joint.\n"
                "CONSIGNE STRICTE :\n"
                "- Transcris et traduis ce discours intégralement mot pour mot en français (100% en français, fidèle, sans aucun résumé, sans omission ni paraphrase).\n"
                "- Conserve les termes techniques de trading, noms de modèles (Claude Code, Grok Bots, Pine Script, chandeliers, stop-loss, take-profit...) et chiffres exacts.\n"
                "- Si c'est un silence ou de la musique sans parole, écris : [Séquence sonore / Musique d'ambiance].\n"
                "Réponds uniquement avec le texte complet en français, sans aucun commentaire méta."
            )
            res_audio = call_gemini([
                {"inline_data": {"mime_type": "audio/mp3", "data": b64_audio}},
                {"text": audio_prompt}
            ], model=AUDIO_GEMINI_MODEL)
            if res_audio and res_audio.strip():
                default_res["verbatim_fr"] = res_audio.strip()
        except Exception as e:
            print(f"[Gemini-Client] Erreur transcription audio directe : {e}", flush=True)

    elif text_en and text_en.strip():
        audio_prompt = (
            f"Tu es un traducteur et transcripteur professionnel pour la chaîne {CHANNEL_NAME} (segment {timestamp_str}).\n"
            f"Voici le discours audio anglais exact prononcé dans ce segment :\n"
            f'"""\n{text_en}\n"""\n\n'
            "Traduis ce discours mot pour mot intégralement en français, naturel et sans AUCUNE coupure ni résumé.\n"
            "Si c'est musical ou sans parole, indique : [Séquence sonore / Ambiance musicale].\n"
            "Réponds uniquement avec le texte français complet mot pour mot."
        )
        for _ in range(3):
            verbatim_fr = call_gemini([{"text": audio_prompt}], model=AUDIO_GEMINI_MODEL)
            if verbatim_fr and verbatim_fr.strip():
                default_res["verbatim_fr"] = verbatim_fr.strip()
                break
            time.sleep(1.0)

    # 2. Analyse visuelle multimodale via Gemini 3.5 Flash-Lite
    n_imgs = len(candidate_frames)
    if n_imgs == 0:
        return default_res

    img_list_txt = "\n".join([f"- Image #{i+1} : horodatage @ {cf.get('timestamp_str', '')}" for i, cf in enumerate(candidate_frames)])
    visual_prompt = (
        f"Tu es un analyste visuel pour la chaîne {CHANNEL_NAME} (segment {timestamp_str}).\n"
        f"Contexte audio du segment : {default_res['verbatim_fr'][:300]}\n\n"
        f"Tu as reçu {n_imgs} capture(s) d'écran candidate(s) :\n{img_list_txt}\n\n"
        "DIRECTIVE DE SÉLECTION D'IMAGES :\n"
        "- Retiens impérativement les images de démonstrations réelles : graphiques TradingView, code Pine Script / Python, terminaux de commandes (Claude Code, Grok Bots, scripts CLI), interfaces de brokers/échanges (Blofin, WEEX, Bybit), backtests, métriques et carnets d'ordres.\n"
        "- Élimine les images purement floues ou les gros plans statiques du présentateur qui parle sans aucun graphique ni élément visuel pertinent.\n\n"
        "Format STRICT obligatoire de ta réponse :\n"
        "[VALID_IMAGES] <numéros séparés par virgule (ex: 1, 2) ou AUCUNE>\n"
    )
    for i in range(n_imgs):
        visual_prompt += f"[DESC_IMAGE_{i+1}] <légende concise décrivant précisément ce qui est visible à l'écran>\n"
    visual_prompt += (
        "[INTERFACE] <logiciels, terminaux, graphiques, courtiers ou sites web montrés>\n"
        "[CONTENU] <indicateurs techniques, code source, prompts, configurations ou données chiffrées affichées à l'écran>\n"
        "[ACTION] <action, analyse graphique, exécution de backtest ou manipulation effectuée>"
    )

    visual_parts: List[Dict[str, Any]] = [{"text": visual_prompt}]
    for cf in candidate_frames:
        img_path = cf.get("path")
        if img_path and isinstance(img_path, Path) and img_path.exists() and img_path.stat().st_size > 0:
            try:
                with open(img_path, "rb") as f:
                    b64_img = base64.b64encode(f.read()).decode("utf-8")
                visual_parts.append({
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": b64_img
                    }
                })
            except Exception:
                pass

    raw_vis = ""
    for _ in range(3):
        raw_vis = call_gemini(visual_parts, model=VISUAL_GEMINI_MODEL)
        if raw_vis and raw_vis.strip():
            break
        time.sleep(1.0)

    if not raw_vis:
        return default_res

    res = dict(default_res)
    try:
        valid_indices = []
        frame_captions = {}
        if "[VALID_IMAGES]" in raw_vis:
            raw_val = raw_vis.split("[VALID_IMAGES]")[1]
            for m in ["[DESC_IMAGE_", "[INTERFACE]", "[CONTENU]", "[ACTION]"]:
                if m in raw_val:
                    raw_val = raw_val.split(m)[0]
            raw_val = raw_val.strip().upper()

            if "AUCUNE" not in raw_val and "NONE" not in raw_val and "ZERO" not in raw_val:
                if "TOUTES" in raw_val or "TOUT" in raw_val or "ALL" in raw_val:
                    valid_indices = list(range(n_imgs))
                else:
                    for token in re.findall(r'\b\d+\b', raw_val):
                        num = int(token)
                        if 1 <= num <= n_imgs:
                            valid_indices.append(num - 1)

        for i in range(n_imgs):
            tag = f"[DESC_IMAGE_{i+1}]"
            if tag in raw_vis:
                part_desc = raw_vis.split(tag)[1]
                for next_tag in [f"[DESC_IMAGE_{j+1}]" for j in range(i+1, n_imgs)] + ["[INTERFACE]", "[CONTENU]", "[ACTION]"]:
                    if next_tag in part_desc:
                        part_desc = part_desc.split(next_tag)[0]
                desc_text = part_desc.strip().lstrip(": -").strip()
                if desc_text and not desc_text.startswith("<"):
                    frame_captions[i] = desc_text

        res["valid_frame_indices"] = sorted(list(set(valid_indices)))
        res["frame_captions"] = frame_captions

        if "[INTERFACE]" in raw_vis:
            p_i = raw_vis.split("[INTERFACE]")[1]
            for m in ["[CONTENU]", "[ACTION]"]:
                if m in p_i:
                    p_i = p_i.split(m)[0]
            res["interface"] = p_i.strip()

        if "[CONTENU]" in raw_vis:
            p_c = raw_vis.split("[CONTENU]")[1]
            if "[ACTION]" in p_c:
                p_c = p_c.split("[ACTION]")[0]
            res["contenu"] = p_c.strip()

        if "[ACTION]" in raw_vis:
            res["action"] = raw_vis.split("[ACTION]")[1].strip()

    except Exception as e:
        print(f"[Gemini-Visual] Erreur parsing bloc visuel : {e}", flush=True)

    return res

def generate_executive_summary(video_title: str, full_verbatim_fr: str, tools_detected: List[str]) -> str:
    tools_str = ", ".join(tools_detected) if tools_detected else "TradingView, Claude Code, Grok Bots, Pine Script, Scalping, Cryptomonnaies"
    prompt = (
        f"Tu es un analyste expert en trading quantitatif, intelligence artificielle et automatisation de stratégies pour la chaîne {CHANNEL_NAME}.\n"
        f"Vidéo intitulée : « {video_title} ».\n"
        f"Technologies, outils & concepts abordés : {tools_str}\n\n"
        f"Transcription intégrale de la vidéo en français :\n\"\"\"\n{full_verbatim_fr[:12000]}\n\"\"\"\n\n"
        "Rédige une synthèse exécutive structurée, dense, fluide et très riche en enseignements concrets en français.\n"
        "Tu DOIS STRICTEMENT employer ces titres de niveau 3 exacts :\n"
        "### 💡 Résumé\n"
        "(2 à 3 paragraphes immersifs et précis expliquant le cœur de la vidéo, les indicateurs et stratégies décortiqués, et les démonstrations de trading présentées)\n\n"
        "### 🛠️ Outils, Modèles & Logiciels Présentés\n"
        "(Liste à puces exhaustive avec nom de l'outil/modèle/plateforme en gras et une phrase explicative percutante)\n\n"
        "### 🔑 Points Clés & Enseignements Stratégiques\n"
        "(8 à 12 points clés détaillés, analytiques et actionnables résumant les configurations graphiques, règles de risk management, points d'entrée/sortie et méthodologies présentées)"
    )

    res = call_gemini([{"text": prompt}], model=AUDIO_GEMINI_MODEL)
    if not res:
        res = (
            "### 💡 Résumé\n"
            f"Dans cette vidéo intitulée **{video_title}**, Alex Carter détaille une approche stratégique et pratique du trading et de l'automatisation par agents IA.\n\n"
            "### 🛠️ Outils, Modèles & Logiciels Présentés\n"
            "- **TradingView & Claude Code** : Analyse technique avancée et automatisation algorithmique.\n\n"
            "### 🔑 Points Clés & Enseignements Stratégiques\n"
            "- Respect rigoureux du ratio risque/rendement et du money management.\n"
            "- Automatisation méthodique des déclencheurs d'ordres via des agents intelligents."
        )
    return res