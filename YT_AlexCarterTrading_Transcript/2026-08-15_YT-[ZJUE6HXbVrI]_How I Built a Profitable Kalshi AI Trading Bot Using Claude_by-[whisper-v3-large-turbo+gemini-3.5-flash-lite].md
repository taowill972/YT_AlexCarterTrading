# 🎬 How I Built a Profitable Kalshi AI Trading Bot Using Claude

> **Chaîne** : [Alex Carter](https://www.youtube.com/@AlexCarterTrading)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=ZJUE6HXbVrI](https://www.youtube.com/watch?v=ZJUE6HXbVrI)  
> **Date de publication** : 20260815  
> **Durée** : 00:10:53  
> **Identifiant vidéo** : `ZJUE6HXbVrI`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **How I Built a Profitable Kalshi AI Trading Bot Using Claude**, Alex Carter détaille une approche stratégique et pratique du trading et de l'automatisation par agents IA.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **TradingView & Claude Code** : Analyse technique avancée et automatisation algorithmique.

### 🔑 Points Clés & Enseignements Stratégiques
- Respect rigoureux du ratio risque/rendement et du money management.
- Automatisation méthodique des déclencheurs d'ordres via des agents intelligents.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:21]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Prediction markets like Kalshi have exploded with opportunity, but manually refreshing order books to catch mispriced event contracts is almost impossible. So, in this video, I'll show you how I built a profitable, automated Kalshi trading bot using Claude, and how you can build your own bot today, even if you don't know how to write a single line of code.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:00:21 - 00:00:40]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So, let's get into it. All right, so first let's talk about why this even works because I want you to understand the why before we touch any setup. Calci contracts are binary. A market either resolves yes or no, nothing in between. That sounds simple, but it's actually what makes this so exploitable.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:00:41 - 00:01:00]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Because when an outcome only has two states, the price is really just the market's live guess at a probability. And probabilities move fast, way faster than most retail traders can manually track. Here's the mistake most people make. They're staring at CalShe's website hitting refresh, trying to catch a mispriced contract with their eyes.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:01:00 - 00:01:20]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> But CalShe's REST API updates on a polling basis, while the actual events, a Fed statement, a tweet, a price candle closing, happen in real time. That gap between what's live and what's reflected in the order book is literally where the edge lives. A bot doesn't blink, doesn't refresh late, and doesn't get emotional about a position.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:01:21 - 00:01:43]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> That's the entire game. So here's the actual framework I built this bot around, and it's four pieces. First is market data scanning. The bot is constantly pulling live order book data across the markets you tell it to watch. Second is edge detection. This is where it compares the current price against what it calculates the fair probability should be, based on the data feed you give it.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:01:43 - 00:02:03]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Third is risk slash position sizing. Once it finds an edge, it doesn't just YOLO the whole account in. It sizes the trade based on rules you set, max exposure per trade, max open positions, that kind of thing. Fourth is automated execution. It fires the order directly through CalShe's API. No manual clicking required.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:02:03 - 00:02:38]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> That's it. Scan, detect, size, execute. Every bot I'm going to show you later runs on some version of this loop. Now, some of you are already thinking, why not just use whatever model just came out this week? And look, you can. new models are dropping constantly and a lot of them are genuinely impressive. But for this specific job, Claude is still what I build on and here's why. It's just better at holding long, structured logic without losing the thread. It's more reliable when you're wiring up real API calls with real money attached and it lets you describe a strategy in plain English and

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:02:38 - 00:02:58]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> actually turn it into working automation. When you're connecting something directly to your trading account pretty good isn't good enough. You want the model that doesn't randomly hallucinate a step. That's Claude. All right, let's get into the actual setup. This part is actually very simple. Let me walk you through it. So to get started, you need to download the Claude desktop app.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:02:59 - 00:03:18]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Head over to claude.com slash download. You'll see the download page right here. You'll see download options for Mac and Windows. Just click on your operating system and the download will start automatically. Once it's installed and you open it up, you'll land on the main interface. It looks similar to a chat window, but this is where all the power lives.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:03:18 - 00:03:40]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So to get started, you're going to want to create an account. You can sign up with Google, Apple, or just your email. Link is down below if you want to go straight there. And by the way, if you sign up through my link on predictions, you get up to a $500 bonus once you start trading. and on perps, that crypto up or down market, you get a $25 bonus just for getting started.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:03:40 - 00:04:17]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So definitely worth grabbing that before you jump in. If you don't see the prompt right away, just go up to the top right where it says sign up and you'll see those same options. Pretty standard process. They'll ask you to verify a couple things, but once you're in, you've basically got access to everything you're seeing on my screen right now. All right, so now let's talk about funding your account because this is where people get a little confused. Up in the top right, click those three lines and go to add funds. That's one way in. You can also click deposit cash right on the home page and you'll see three instant transfer options. Card, Google Pay, and

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:04:17 - 00:04:51]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> crypto. If you click on more options, you'll also see wire transfer, which takes at least one business day and that one has a $1,000 minimum but no maximum. So that's more for people moving bigger amounts. Now here's something important. You know, if you connect your card or Google Pay, there's a 0% processing fee on those, which is honestly great. So you're not getting hit just for depositing. So personally, if you want the fastest option, I just connect your card or Google Pay directly and you're in within seconds. But if you've got crypto already, you can go that route

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:04:51 - 00:05:25]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> too. Click on the crypto option and you'll see three choices. Secure deposit, standard deposit, and buy crypto. On secure deposit, you can connect your account directly from exchanges like Coinbase, Uphold, Cash App, and a few others. Or if you've got crypto sitting in a wallet, you can connect Metamask, Phantom, Trust Wallet, and more. If your exchange isn't listed, you can do a standard deposit instead, just like a normal crypto transfer. Choose your token, like USDT, pick your network, click show address, copy that address, and go paste it

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:05:25 - 00:05:59]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> into your exchange to send it over. Just keep in mind there's a $3 minimum on that. And if you don't have crypto at all, you can just buy it instantly using your card through providers like Coinbase, Cash App, or Robinhood right inside the app. If you're just starting out, I suggest having a daily max deposit no more than $500, which honestly is plenty for most people getting going. And connecting your card or bank also makes withdrawals way faster since it goes right back to the same place. Now before we set up the bot, let's get your API keys first. Click the three lines again

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:05:59 - 00:06:35]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> and click on account and security. Scroll down to the bottom and click on create key. Give it a nickname, something like Kalshi Automated Trading. To have it trade for you, click on full access, then click create. It will give you two codes. Save them for later, something like sticky notes or notepad. Note that this will only be shown once, so copy it carefully. Now moving into the bots, there will be a password prompt. Just enter your password. Then just enter your CalShe API key and your private key and save. You also have the option to include your open router and Polymarket wallet

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:06:35 - 00:07:04]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> key here. Now I already created my own bots for you to try. Let me run through them quickly. First is the BTC 15-minute arbitrage. This runs on CalShe and Polymarket. They both run 15-minute Bitcoin up or down markets. When buying up on one venue and down on the other costs less than $1 combined, the bot buys both sides and keeps the difference at settlement. It runs itself, executes automatically as soon as both your CalShe and Polymarket keys are set.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:07:05 - 00:07:23]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Second is the CalShe times Polymarket arbitrage. This one matches the same event on both exchanges and flags at the moment yes on one side plus no on the other costs under $1 after fees. This one signals only. You take the trade, the bot just does the watching so you don't have to.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:07:24 - 00:07:45]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Third is Smart Money Scanner. Here you can do one click and it will give you a detailed report report. It shows you the top performing polymarket wallets this week and where today's CalShe money is flowing. It's honestly the fastest way to see what Sharp Money is doing before you size up. When you run it, it fetches the week's most profitable wallet straight from the leaderboard and lists their positions.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:07:45 - 00:08:06]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> You can see the live log right here and their bets updating in real time. You can also build your own bots here and connect them directly to your CallShe account. From Python to Claude to TradingView to other models like GPT, Gemini, DeepSeek, and more. Now, if you want all of this already built for you, I've got it on my WAP group.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:08:06 - 00:08:27]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Links below. More on that in a bit. All right, now let's see how it actually works using a Claude bot. Click on Trading Bots, click New Bot, and select Claude Bot. Here you can add a name and describe your strategy in words. Be very detailed here. This is literally where you tell it what you want the bot to do. After that, click Create Bot, and there you have it.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:08:27 - 00:08:50]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Your trading bot is ready to run. For example, on one of the bots I created, the Bitcoin 15-minute arbitrage, you can see the name, the description, equity, the orders placed, profit and loss, and the balance curve. It's all right here. You can also edit some of the settings, window trigger, contracts per side, seconds between scans, and max money working at once.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:08:51 - 00:09:14]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Once you're done, just click Save Settings. All right, and look, for the next few years, two kinds of prediction market traders are going to exist. The ones using AI and the ones still doing everything manually. Same markets, very different outcomes. Here's how you get on the right side of that. Inside my AI Trade Edge community, I've got every prompt, every bot, every template I personally use, all in one place.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:09:15 - 00:09:35]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Remember those CalShe bots I mentioned earlier? You get all of them in there. A Bitcoin 15-minute arbitrage bot, a CalShe polymarket pricing bot, and a smart money bot tracking where the big wallets are moving. Plus, you can code your own using Python, Claude, TradingView, or any available model available to you right now.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:09:35 - 00:09:53]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> There's also a full agentic trading course, 2.5 hours, beginner to expert, no coding needed. By the end, you'll have your own AI trading system running live, $79.99 a month. One good trade covers it. First 100 members lock that rate in for good.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:09:54 - 00:10:13]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Links in the description. You genuinely cannot afford to miss this. So that's really the whole system. Scan, detect, size, execute, all running while you're doing literally anything else. I've been running variations of this myself and the difference between watching charts all day versus letting the bot watch for you is honestly not close.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:10:14 - 00:10:32]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Two quick things before you go. Make sure you sign up through the link below so you actually get that $500 predictions bonus and the $25 perps bonus. That's real money working for you before you even place a trade. And second, get into the WAP group so you can grab these bots directly or vibe code your own versions with Claude.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:10:32 - 00:10:53]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> If you want watch the full walkthrough on how to use Kalshi, even if you're a complete beginner, check the video popping screen right now. And if you want the full step-by-step guide on how to build your own agentic trading system using Claude, that video is popping up on screen as well. If this helped, drop a like, subscribe for more of these, and I'll see you in the next one.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

