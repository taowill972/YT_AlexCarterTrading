# 🎬 I Rebuilt a Nobel Prize Quant Strategy Using Claude Code

> **Chaîne** : [Alex Carter](https://www.youtube.com/@AlexCarterTrading)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=o9ZVi4vdy9c](https://www.youtube.com/watch?v=o9ZVi4vdy9c)  
> **Date de publication** : 20260723  
> **Durée** : 00:10:12  
> **Identifiant vidéo** : `o9ZVi4vdy9c`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **I Rebuilt a Nobel Prize Quant Strategy Using Claude Code**, Alex Carter détaille une approche stratégique et pratique du trading et de l'automatisation par agents IA.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **TradingView & Claude Code** : Analyse technique avancée et automatisation algorithmique.

### 🔑 Points Clés & Enseignements Stratégiques
- Respect rigoureux du ratio risque/rendement et du money management.
- Automatisation méthodique des déclencheurs d'ordres via des agents intelligents.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:25]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> There's one calculation that every quant desk on the planet runs every single morning, and it's got nothing to do with which way the market's going. Most traders don't even know the real question it's answering, and at the center of it sits an equation that actually won a Nobel Prize in economics. So in this video, I'm going to rebuild the way a real quant thinks, and I'm going to give you the exact skill file to run it yourself using Claude Code.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:00:25 - 00:01:01]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Here's exactly what you're walking away with, a simple explanation of the method, no math background needed. A clawed code skill that runs this on literally any asset you trade. A custom trading view indicator that puts the entire framework directly on your chart. And I'm going to show you the GitHub where you can grab all of it for free. Full credit to Miles Deutscher, who actually built this repo. So make sure you go check out his stuff too. And once we're done with the theory, I'm going to walk you through setting up an exchange, depositing funds, and opening your first position. So you're not just watching this, you're actually using it by

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:01:01 - 00:01:35]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> the end. So why am I making this video? I've been deep in these markets for years now and what's happened with AI over the last couple of years is honestly insane. Stuff that used to sit locked behind a hedge fund's quant desk you can now compress into a single skill file and run yourself for free from your laptop. So today I wanted to take a real concept that actual quant funds use every single day and turn it into something you can tangibly use. That's the whole point of this channel now, giving you access to the same tools the big desks have. So before we get into the model,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:01:35 - 00:02:11]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> let's talk about what a quant actually is. Quant just means quantitative analysts, people who study math, physics, or computer science and get paid insane salaries at funds to basically replace opinion with real measurement. Now here's the thing, for every single trade you take, there's really only two questions. First is which way, meaning which direction do I think price is going? And second is how much, meaning how much am I actually willing to stake on this? Most retail traders treat which way as the entire game. Position size is an afterthought. But here's

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:02:11 - 00:02:45]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> what's crazy. Which way is actually the weakest, least reliable signal in trading? It's barely answerable. How much is the one variable that's full in your control? So quants flip it, minimum effort on the question you can't really answer, maximum rigor on the one you can. That's the whole game, and that's why some traders with a lower win rate are more profitable than traders with a way higher win rate, because they understand sizing. So instead of staring at price, quants look at something called volatility, basically how hard the market's moving, independent of direction.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:02:45 - 00:03:06]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> I'm going to call it the violent score. Now, here's why this is actually predictable. Market chaos doesn't show up randomly. It clusters. Think March 2020 in the S&P or the FTX collapse in Bitcoin in 2022. Completely different assets. Same pattern. The easiest way to think about this is earthquakes.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:03:06 - 00:03:30]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> A major earthquake tells you nothing about which direction a building falls, but it tells you with way higher confidence that more shaking is coming. That's exactly how a quant reads a violent trading day. Zero info on direction, but a ton of info on tomorrow's volatility. So now the fun part. In 2003, economist Robert Engel won a Nobel Prize for solving this exact problem.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:03:31 - 00:03:49]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> His model is called ARCH. His student, Tim Bollersleff, extended it into what DES still use today, which is now GARCH, or Generalized Autoregressive Conditional Heteroscedasticity. I know, absolute tongue twister, but stick with me. Basically, GARCH forecasts tomorrow's volatility as three things aided together.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:03:49 - 00:04:25]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> The base level the asset always carries, its personality, a fraction of today's shock, and a fraction of today's overall violence level, which is basically the market's memory. When this was tested on Bitcoin's full 15-year history, the memory component carried 85% of the weight, meaning volatility is almost as persistent as it's mathematically possible to be, which is exactly why this is forecastable. And keep in mind, this model says nothing about direction. It only tells you how violent tomorrow might be. So how does this actually turn into a

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:04:25 - 00:04:50]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> real position size? The logic is simple. Your risk equals your size multiplied by the market's violence. You can't control the violence, so you control the size. Step one, set your max tolerance. Institutions usually run around 15% annualized. Step two, read the current violence level. Let's say the market's sitting at 30% annualized right now. Step three, divide. 15 over 30 equals half.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:04:50 - 00:05:16]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So if a signal fires today, you're only taking half your normal size. Think of it like cruise control. The road's gradient keeps changing, but your speed stays steady. Same idea. The market's violence changes daily, but your account risk stays constant. All right, so here's how you actually get this running on your own computer. Full credit here. This entire skill was built by Miles Deutscher, so definitely go check out his stuff. This wouldn't exist without him.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:05:16 - 00:05:53]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Everything we just walked through, I've got the link to the GitHub down in the description. Once you're on the repo, you'll see the installation path. Copy that, then open Claude Code. Paste it in. If you're on Terminal, forward slash plugin should work. If you're on the app and it errors, just swap the forward slash for the word Claude. Once that's done, it installs and verifies the scale automatically. Now you can literally just talk to it. So you could say, what's the volatility forecast on Bitcoin? And it'll run the actual Garch method straight from the repo and give you a real number. Annualized volatility, whether we're in a calm or storm regime, and a one day

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:05:53 - 00:06:18]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> ahead forecast. In the repo, there's also a pine script file called the storm gauge. Copy that, head into trading view, click the pine editor icon, paste it in, click add to chart, and now you've got the entire framework. Violence percentage, regime, sizing suggestion, sitting directly on your chart. All right guys, now let's actually put this to work. Step one is setting up your exchange.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:06:18 - 00:06:40]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> For this, we're using 2Bit. This is a no KYC exchange partially backed by Bybit and Huobi. so there's real credibility behind it and right now they're running some genuinely insane bonuses. To sign up and claim your bonus, click the first link in the description. Enter your email, set a password, hit sign up. That's it. Account creation takes under a minute.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:06:41 - 00:07:17]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Step two is depositing funds. Once you're logged in, go to assets, click deposit, and select your coin. I recommend USDT since that's the main pair for futures. Choose your network. I'd go with TRC20 it's fast and the fees are low. You'll get a wallet address, copy that and send your funds from your external wallet or another exchange. If you don't have crypto yet, no problem. Just click buy crypto, choose your currency, enter your amount and follow the on-ramp steps. Once your funds land, go to assets, click transfer, select USDT and move it from spot to futures. Keep in mind your funds

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:07:17 - 00:07:39]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> need to be in your futures wallet to actually trade. Step three, opening your first position, click derivatives, then USDTM futures. This is the main trading interface. Trading pair top left, chart in the center, order book on the right, and your order panel on the far right. First, pick your margin mode. I'd recommend isolated so your risk is limited to just that trade.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:07:40 - 00:07:58]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Next, set your leverage. 2Bit lets you go up to 150 times, but for beginners, keep it at 5 times to 10 times max. Choose market order for instant execution, enter your position size, and set your take profit and stop loss. You can do this by price or by P&L, whichever is easier for you.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:07:58 - 00:08:31]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Then click buy slash long or sell slash short to open your position. You can track it under your positions panel. Entry price, unrealized P&L, and your liquidation price will all show up there. Now, if you want to take this even further and have a trade open automatically on your exchange the moment a signal fires, I've got you covered. I put together a private group where I share all my use cases for Claude Code from integrating it with Telegram, TradingView, and searching for whales on Hyperliquid. All automatically. Everything I showed you today, it's all inside the group.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:08:31 - 00:08:53]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And I'm constantly adding new stuff, new strategies, new prompts, new integrations. Every time I build something new, it goes straight in there. The price is $79.99 a month. And honestly, when you think about what this actually is, the most cutting-edge AI trading setup available to retail traders right now, constantly updated with everything included.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:08:53 - 00:09:22]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Inside, there is also a full agentic trading course. 2.5 hours. Beginner to expert. No coding background needed. By the end of it, you will have your own AI trading system running live. Something most retail traders do not even know is possible right now. $79.99 a month. One good trade covers it. And the first 100 members lock in that rate permanently. After that, the price goes up. The link is in the description. You genuinely cannot afford to miss this.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:09:23 - 00:09:55]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So that's the full breakdown. The Nobel Prize model real quant deaths run every morning turned into a skill you can run yourself for free. Massive credit again to Miles Deutscher for building this out. Go show him some love. If you want to see a full demo of how I trade using only my telegram, the full demo of all use case on TradingView, and how I track the biggest trades of whales on Hyperliquid automatically click the video popping on screen right now and if you want the full step-by-step guide on how to build your own agentic trading system using Claude that video

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:09:55 - 00:10:12]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> is popping up on screen as well. Go and check that out next. If you found this valuable smash that like button it genuinely helps the channel. Subscribe if you're not already because I'm going to keep building more of these AI trading skills and turning them into videos like this. I'll see you guys in the next one peace out

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

