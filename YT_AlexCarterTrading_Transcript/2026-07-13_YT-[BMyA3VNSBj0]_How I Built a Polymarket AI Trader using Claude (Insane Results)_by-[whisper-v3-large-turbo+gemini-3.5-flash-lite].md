# 🎬 How I Built a Polymarket AI Trader using Claude (Insane Results)

> **Chaîne** : [Alex Carter](https://www.youtube.com/@AlexCarterTrading)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=BMyA3VNSBj0](https://www.youtube.com/watch?v=BMyA3VNSBj0)  
> **Date de publication** : 20260713  
> **Durée** : 00:10:34  
> **Identifiant vidéo** : `BMyA3VNSBj0`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **How I Built a Polymarket AI Trader using Claude (Insane Results)**, Alex Carter détaille une approche stratégique et pratique du trading et de l'automatisation par agents IA.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **TradingView & Claude Code** : Analyse technique avancée et automatisation algorithmique.

### 🔑 Points Clés & Enseignements Stratégiques
- Respect rigoureux du ratio risque/rendement et du money management.
- Automatisation méthodique des déclencheurs d'ordres via des agents intelligents.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:24]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Everyone's been trying to connect Claude to Polymarket. I tried it too. And for the first week, I just watched it lose money. Then I realized why. When everyone's running the same setup, the edge is gone. Asking Claude to predict markets is what everyone's doing. And it doesn't work anymore. What accurately works is Claude with the right tools. In this video, I'll show you the three tools I use and exactly how to set the whole thing up.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:00:24 - 00:00:57]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> here's the core insight and this is the thing most people completely miss you should stop S and Claude to predict the market but ask it to find the people who already predict well on polymarket every single trade is on chain that means the top wallets the ones with 70 80 even 90 percent win rates their entire playbook is public every entry every exit every position size it's all there so instead of competing with them I built a system that finds them, scores them, and copies them automatically. So that's how we trade smarter

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:00:57 - 00:01:31]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> with Alex Carter. Now, this is the Falcon leaderboard. Top wallets on here are genuinely running plus 15 to 20 percent over 15 days. And I can tell you already, get any of the three tools I'm about to show you wrong and you lose money like everyone else. There are only three tools you actually need to run the whole setup. Tool one finds the wallets. Tool two, which is clawed, This picks the best three prediction market traders and tool three copies the trades automatically, gasless and within seconds. I'll walk you through all of it step by step so you can run this exact

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:01:31 - 00:01:52]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> setup yourself. Let's get into it. So the first tool is the Falcon API. You can find it at api.polymarketanalytics.com. The link is in the description below. You just need to create an account using your email address. After you logged in, you can see your API keys. You can see the application, the API key itself, and the status of the API.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:01:53 - 00:02:19]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> You can click on the Copy button here on the right side to copy it completely. Store this API key somewhere offline, as you will use this later when installing MCP server. What Falcon API does is get data and rank Polymarket wallets by win rate, ROI, and drawdown. and this is where the edge actually lives because most people are just going to the native poly market leaderboard and copying whoever made the most money last week. That's not a strategy.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:02:19 - 00:02:52]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> That's just chasing. What I do is filter properly. The filters I use are the following. First, win rate must be above 65%. Second is the trader must have a minimum 100 trades. So we're not copying someone who got lucky on three markets. Third, their drawdown must be below 25%. That last one is important. A wallet can have an 80% win rate and still blow up if they size into one bad market. The drawdown filter protects you from that. Now, let me show you what happens when you don't use this. See that? Number four has a high win rate, but it was flagged suspicious since

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:02:52 - 00:03:27]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> it has a higher drawdown than the others. That's not a signal. That's noise. And if you copy that wallet, you're just gambling with extra steps. So once you've applied the filters, you get a clean shortlist. From that shortlist, Claude does the heavy lifting. Tool 2 is Claude Desktop with the Falcon MCP connected. The MCP or Model Context Protocol is what lets Claude actually read the Falcon data directly. So instead of me copy-pasting wallet stats into Claude manually, Claude pulls the leaderboard, reads the metrics, and reasons through which wallets to pick. To install this,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:03:27 - 00:04:02]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> go to Quick Start Guide on Falcon API, and here you can see the step-by-step on how to install MCP. For this, I'm using Claude code, and I'll just say to Claude, add this server name with this S-S-E-U-R-L. And after a couple of minutes, it will say to restart your Claude to fully install it. Use this prompt to check the connection, and this is where you'll use your API keys earlier. From here, you are now connected to all endpoints provided by Falcon API. From copy trading, arbitrage, market intel and social signals. Now I have this prompt this forces Claude to weight consistency over

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:04:02 - 00:04:27]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> peak returns. Not the wallet that had one insane week. The wallet that's been quietly profitable across 200 trades in different market categories. And that weighing consistency over ROI. That's the whole game. Took about 30 iterations to get right. The full version of this prompt with edge case handling is in my WAP group. It is available on the link below. I'm not sharing it publicly here because the logic behind it is the whole edge.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:04:28 - 00:04:48]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And here's what Claude actually does when you run it. It scores and ranks each wallet that's a composite of win rate, ROI, and drawdown. And then it picks three wallets diversified across categories. Sports, crypto, politics. You don't want three wallets all trading the same market type. If one category goes quiet, the other two are still running.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:04:48 - 00:05:09]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> The exact wallets I'm copying right now are in my WAP group as well. I'm not sharing them publicly because once they're out, they get front run and the edge disappears. That's just how this works. So Claude gives you three wallets. Now you need something to actually execute the copies. Tool three is Polygon. This is the Telegram bot that actually copies the trades.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:05:09 - 00:05:42]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> And I want to be clear about why this matters. Without Polygon, this strategy literally cannot run. Polymarket's native interface doesn't automate anything. you'd have to manually mirror every trade and by the time you do that the price has already moved top wallets fire trades in liquid markets that reprice fast by the time you manually mirror it through a browser the price has already moved polygun mirrors within seconds that speed is the whole point here's how you set it up go to telegram and search for polygun sniper bot you

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:05:42 - 00:06:18]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> open the bot type start and it instantly generates a wallet for you and the first thing i checked before I put any money in, it's non-custodial. You own the keys, you can export them and leave anytime. That matters. If the bot ever disappears, your funds are still yours. To deposit, you click wallet right here. You can deposit from Polygon, Solana, ETH, BNB, or Polymarket wallet. It auto bridges, so you don't need to be on a specific chain. And the minimum is $10 USDC, which means you can test this with $10 before you put any real size in once you're funded

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:06:18 - 00:06:49]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> you go to copy trade then add copy trade and paste in the wallet address Claude selected for copy mode I use portfolio weighted that means if the wallet trades two percent of their portfolio you trade two percent of yours it scales with them I tried fixed dollar amount early on and it didn't work well portfolio weighted is the right setting here and then this is critical you cap per trade size at at 5 to 10 percent of your balance. I'll tell you exactly why in a second. Slippage I set to 2 percent.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:06:49 - 00:07:24]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> That's been fine for the markets I'm copying. If you're copying a wallet that trades very niche, low liquidity markets, you might want to go a little higher. And on top of that, every copy trade is gasless. When you're mirroring high frequency wallets, gas fees stack up fast. Polygon sponsors the gas, so that's not eating into your positions. That's a real cost structure win. The fee is 1% flat, by the way. No hidden spread on the copy trade prices like some other bots do. What you see is what you pay. Hit confirm and you're live. Polygon handles everything from

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:07:24 - 00:07:59]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> there. Automatic within seconds of the wallet you're copying making a move. So here's my actual setup right now. Three wallets. One in crypto markets, one in sports, one in politics. That's the diversification. If one category goes sideways, you're not fully exposed. Now, the 5 to 10 percent per trade cap. Let me tell you why that rule exists. First time I ran this, I set per trade size to 20 percent. One of the wallets I was copying took a big position on a sports market I didn't understand. I lost about four hundred dollars in three hours. That's why I cap every trade at five

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:07:59 - 00:08:26]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> to ten percent now. And I cap exposure per single market at ten percent of total balance. It sounds conservative, but it's what keeps you in the game long enough for the edge to compound. The other rule. Refresh your wallet list every 14 days. Wallets drift. A wallet that was printing last month might be cold this month. Claude rescores them. You swap out the underperformers. You keep going. So let me just walk you through the full interface so you know exactly where everything is.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:08:27 - 00:08:49]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Here on the main menu, you can see your current positions, your available balance, and your active copy trades. If you click into copy trade, you can see each wallet you're following. Click on manage and you can toggle notifications on or off by clicking on unmute and mute and edit or remove any of them at any time by clicking on delete. Over here in markets, you can browse by category.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:08:50 - 00:09:14]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Politics, Sports, Crypto, Trump, Finance, Geopolitics, Volume, or Trending. You can also view and trade directly inside the bot if you want to place manual trades on top of the copy trading. And in portfolio, you can see all your open and closed positions. You can click into any individual trade to see the full details. That's the whole setup. Three tools running together.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:09:14 - 00:09:48]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Falcon finds the wallets. Claude picks the best three. Polygon copies them automatically. Over the next few years, there are going to be two kinds of traders. The ones using AI to find edges like this and the ones still doing everything manually. Same market, very different outcome. I'm launching the AI Trade Edge community. Every prompt, bot, agent, and step-by-step guide I personally use all in one place. TradingView integration, Telegram trading, hyperliquid whale tracking, it's already inside. And everything I build going forward gets added straight in.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:09:48 - 00:10:25]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> $79.99 a month. First 100 members lock in that rate permanently. After that, the price goes up. link is in the description and the link in the description is also my Polygon referral. You get 10% off trading fees. I get a small cut of the platform's fee. That's it. No course, no paid signal group on top of that. If you're going to use Polygon anyway, using the link costs you nothing and supports the channel. If you want to see the full demo on how to set up automated trade execution using Telegram and TradingView, check the video popping up on screen right now.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:10:25 - 00:10:33]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> If you found this useful, leave a like. It really does help the channel. Subscribe if you haven't already, and I will see you in the next one.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

