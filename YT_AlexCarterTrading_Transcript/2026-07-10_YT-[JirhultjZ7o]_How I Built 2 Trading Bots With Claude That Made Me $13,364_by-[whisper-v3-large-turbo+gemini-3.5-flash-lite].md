# 🎬 How I Built 2 Trading Bots With Claude That Made Me $13,364

> **Chaîne** : [Alex Carter](https://www.youtube.com/@AlexCarterTrading)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=JirhultjZ7o](https://www.youtube.com/watch?v=JirhultjZ7o)  
> **Date de publication** : 20260710  
> **Durée** : 00:19:30  
> **Identifiant vidéo** : `JirhultjZ7o`  
> **Transcription & Analyse** : `whisper-v3-large-turbo+gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
Dans cette vidéo intitulée **How I Built 2 Trading Bots With Claude That Made Me $13,364**, Alex Carter détaille une approche stratégique et pratique du trading et de l'automatisation par agents IA.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **TradingView & Claude Code** : Analyse technique avancée et automatisation algorithmique.

### 🔑 Points Clés & Enseignements Stratégiques
- Respect rigoureux du ratio risque/rendement et du money management.
- Automatisation méthodique des déclencheurs d'ordres via des agents intelligents.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:00 - 00:00:37]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> I just took two of the most popular crypto trading strategies on the internet, handed them to Claude, and turned them into fully automated pine scripts on TradingView. No coding, no guessing, no watching charts all day. And what I found was actually kind of crazy. Both strategies, when automated properly, started flagging signals I was completely missing manually. One of them even caught a clean long entry on Bitcoin that I would have slept through. In this video I'm going to show you exactly how I did it. I will walk you through two strategies. The exact prompts I gave Claude. How to import the pine scripts into TradingView in

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:00:37 - 00:01:12]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> seconds. How to refine the strategies and how to set up alerts so TradingView does the watching for you. And stick around until the end because I will show you how to get all my prompts, strategies and setups and how to build your own agentic trading bot with Claude that can trade crypto, stocks, indices, and more. So let's get into it. All right, guys, step number one, sign up for an exchange. For this strategy, we're going to be using UBIT. This is one of my favorite exchanges for futures trading right now, and they've got some serious bonuses for new users,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:01:12 - 00:01:35]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> up to $50,000 in bonuses just for signing up and trading using my link down below. If UBIT doesn't work for you, you can use Blofen as an alternative. Blofen doesn't require mandatory KYC verification for basic trading, which means you can start trading immediately. Plus, new users can earn up to $5,000 USDT through deposit and trading volume bonuses.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:01:36 - 00:02:12]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> I'll link both down below. Once you're on the UBIT page, you can sign up with your email, your phone number, or connect via Google or Apple ID. For this tutorial, I'll use email. just enter your details create a strong password agree to the terms of service and click sign up enter the email verification code and your account is ready the whole process takes less than 30 seconds and keep in mind ubit is a non-kyc platform you do not need to complete identity verification to start trading that makes it accessible even in restricted regions and it

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:02:12 - 00:02:48]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> means you can start trading almost instantly after signing up. Go to your wallet and click deposit. Select the cryptocurrency you want to deposit. USDT is ideal for trading. Then select your deposit network. I recommend TRC20. It's fast and the fees are very low. You'll then see your personal deposit address. Copy it carefully. Go to your current exchange or wallet. Paste the address and send your funds. Always send a small test amount first, maybe $10 to $20, just to confirm everything arrives correctly before sending the full amount. This is very important. Sending on

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:02:48 - 00:03:17]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> the wrong network can mean losing your funds. If you don't have crypto yet and want to buy directly on UBIT, that's also possible. But for this, you will need to complete KYC first. Go to your profile icon on the homepage and click KYC. Click verify now. Provide your email, your personal information, your verification documents, and a selfie. Once that's approved, you can use the quick buy option on UBIT to purchase crypto directly with fiat currency using a credit or debit card.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:03:18 - 00:03:39]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> If you already have crypto on another exchange or wallet, you can skip KYC entirely and just deposit directly, which is the faster option for most people. All right, now I'm going to show you two strategies that I handed to Claude. The first one uses Bollinger Bands and RSI. The second one uses Dantian Channels, the LWTI indicator and volume.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:03:39 - 00:04:11]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Both are completely different in how they work but both can be automated using the exact same process. Let me walk you through strategy one first. All right now for the strategy itself we're going to be using TradingView. I have a link down below to my TradingView link. If you use that you will get a small discount when you purchase the pro version. I'm going to use the Bitcoin chart. The first thing you need to do is set up the Bollinger Bands on your trading view. Now go to the indicators, type Bollinger Bands, and click on this one. Then you'll need to change the default setting right

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:04:11 - 00:04:46]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> over here for this specific trading strategy. Go to the length section, set it as 30, and keep the standard deviation at 2. If you want to customize your choice, don't forget that the central line represents the moving average based on the length value and the lower and upper lines are standard deviation lines. Now that you have the Bellinger band set up it's time to add RSI relative strength index. For this head over to indicators again and type in RSI. Click on the top result which should be the relative strength index. Now you should make sure that the upper band is on the number 70

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:04:46 - 00:05:20]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> and the lower band is on 30. rsi is a very helpful tool for determining if a cryptocurrency is being overbought or oversold if it's above 70 it means it's overbought if it's below 30 it's oversold now let's compare these two indicators to find potentially profitable trades if the price goes above the top bollinger band you can enter a short position but if the price goes below the the bottom Bollinger Band you can enter a long position. Sometimes the price may cross those bands a few times and you can see a lot of false signals right over

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:05:20 - 00:05:56]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> here. In fact if you acted on every single signal you would probably lose a lot of money. So we cannot do that for sure. To solve this problem you're going to add our second indicator RSI. If the price dropped below the lower Bollinger Band and the RSI falls to the lower level around 30 you will open a long position. But if the price goes above the upper Bollinger Band and the RSI reaches around 70 level, it's time to open a short position. Let me get you some examples here. If the price starts to fall below the lower Bollinger Band, as you can see here, but the RSI is not quite at its ideal

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:05:56 - 00:06:24]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> level yet, that shows that it's oversold, you can hold on until the RSI dips to the 30 level, which eventually will reach, as you can see here. Just when the RSI drops to the 30 level or below, you will see that the Bitcoin price is on the lower Bollinger Band or below. Then you can jump on a long position on Bybit or Bitunix. As you can see, after you open your long position, the price bounces back up as predicted. If you like to open short positions, the strategy is the same.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:06:25 - 00:06:58]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Just open a short position if the Bitcoin price reaches the upper Bollinger Band and at the same time reaches the overbought zone on the RSI, the 70 level or above. One thing to notice is that if the market moves sideways, this strategy is not the best. Most trading strategies have a hard time predicting market movements in those conditions. But back to the chart, you can see here that the Bitcoin price drops below the Bollinger Band, where the RSI is in the oversold zone. But the problem is that the price continues crashing even more. If you entered the trade right here,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:06:59 - 00:07:32]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> you would suffer a massive loss. To avoid this money loss, you need to pay attention to detecting the earliest signs of big price movements even before they happen. Check out how the Bollinger bands are skinny now and close together. You can see the market is moving sideways, which is not good. Plus the RSI moves also in between the lower and upper lines and doesn't go above or below the major points of overbought and oversold. All of this is a very, very big red flag. We don't want to go in here. In these cases, just avoid the trade at all. But let me show you the perfect

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:07:32 - 00:08:09]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> example to open the perfect trade that will give you that expected 92% win rate. Here, the price is falling below the lower Bollinger Band and then goes back above again. But then the price starts to come back down, making a new lower low from the previous low. But if you take a look at the RSI, you can see that the RSI just made a higher low. That's bullish divergence. Bullish divergence is characterized by the formation of progressively lower lows by the price candles. At the same time, the RSI forms progressively higher lows. This is one of your best chances to open a long position

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:08:09 - 00:08:41]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> because you will have a high chance to profit. On the other hand, if the price is pumping to the upper Bollinger Band and then comes back down again, then the price starts to go up again, making a new higher high from the previous high. But if you take a look at the RSI, you can see the RSI just made a new lower high. That's a bearish divergence. The perfect opportunity to open a short position. Using the Bollinger Bands and the RSI at the same time, it's a very, very, very good strategy, and I've had so much success with that,

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:08:41 - 00:09:04]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> as you can clearly see here. Now that is strategy one, but I want to show you a second strategy as well because this one is completely different and honestly just as powerful. This one uses three indicators on a five-minute chart. It is a scalping setup so it is designed for quick moves throughout the day and when all three conditions line up at the same time the signal is very very clean.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:09:05 - 00:09:40]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Open trading view and select the trade-in pair you want to trade. For this example I'll use Bitcoin USDT. Next click on the time frame selector and choose the five-minute chart. This is a scalping strategy so we're looking for quick moves throughout the day. Now let's add the indicators. Indicator number one is the Donchian Channels. Click on the indicators tab, type Donchian Channels and select it. Click on the indicator settings, go to inputs, and change the length to 96. Then go to style and change the colors of the upper and lower bands to red so they're easier to see. Here's how this

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:09:40 - 00:10:13]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> indicator works. You'll see three lines on your chart. The middle line acts as a mean reversion point. If the price is above this line, we're in bullish momentum. If it's below, we're in bearish momentum. The upper and lower red bands act as dynamic support and resistance levels. When price reaches these levels, it often gets rejected, but they can also act as breakout points. Now here's the problem with using this indicator alone. When the market moves sideways, these bands get really close together and you'll get false breakout signals that can cause you to lose trades.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:10:14 - 00:10:34]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> That's why we need two more confirmation indicators. Indicator number two is LWTI or Larry Williams Large Trade Index. Click on indicators, type LWTI or Larry Williams Large Trade Index, and select it. Go to settings, click inputs, and change the period to 25. Then change the smoothing period to 20.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:10:34 - 00:10:55]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> This indicator helps us identify when large traders are entering the market. When it's green, it confirms bullish momentum. When it's red, it confirms bearish momentum. Indicator number three, volume. Click on indicators. Type volume and select the standard volume indicator. Go to settings, click inputs, and change the MA length to 30.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:10:56 - 00:11:20]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Then go to style, enable the volume moving average, and change its color to white. This indicator shows us when there's actual momentum behind a move, not just a small fluctuation. Now we have all three indicators set up. Let me show you exactly how to use them. For a long position you need three things. Price must touch or break above the upper red Donchian band. The LWTI indicator must be green.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:11:21 - 00:11:43]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> This confirms bullish momentum from large traders. Volume bars must be above the white moving average line and green. This shows there's real buying pressure not just consolidation. Once all three conditions are met you open your long position. Set your stop loss just below the middle orange line of the Dungeon channels. Set your take profit at a two to one risk reward ratio.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:11:44 - 00:12:20]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So if you're risking $20, you're aiming to make $40. Let me show you an example on the chart. Right here, you can see the price touched the upper band, the LWT, I was green, and volume was above the white line and also green. This is a perfect long entry. You would enter here, set your stop loss below the middle line, and your take profit would be hit right here for a clean winning trade. For a short position, the rules are reversed. Price must touch or break below the lower red Duncan band. The LWTI indicator must be red, confirming bearish momentum. Volume bars

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:12:20 - 00:12:54]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> must be above the white line and red, showing strong selling pressure. Once all three conditions are met, use open your short position. Set your stop loss just above the middle orange line. Set your take profit at a two to one risk reward ratio. Here's an example. Price hit the lower band LWTI turned red and volume was above the line in red. Perfect short entry. You would enter here, set your stop loss above the middle line, and take profit here for another winning trade. By combining this strategy with basic support and resistance analysis, you dramatically increase

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:12:54 - 00:13:29]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> your win rate. So now you understand how both strategies work manually and this is exactly where Claude comes in. Instead of watching charts all day doing this yourself, I handed both of these strategies to Claude and asked it to write me full pine scripts so TradingView can automatically detect every signal for me no manual watching no missed entries let me show you the prompts I use I am going to put them on screen right now so you can copy them exactly prompt one is for the Bollinger Band and RSI strategy and here is prompt two for the three indicator strategy

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:13:29 - 00:13:51]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> that is it you paste either of those prompts into Claude I am using Claude code here and within seconds it spits out a complete work in pine script in a notepad file. Open that file, press ctrl a to select all of the code, then ctrl c to copy it. Now let's get it into trading view. Now this exact prompt along with the pine script used in this video is available in my private group.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:13:51 - 00:14:24]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> You can find the link down below. Open trading view and go to any chart. I'll use bitcoin again. At the bottom right of the screen click on the pine script editor tab, the one that looks like a pine tree once the editors open you'll see some default code in there just select all of it and delete it then paste in the code that Claude just gave you now click add to chart that's the button at the top right of the pine script editor trading view will compile the script and apply it directly to your chart and there it is you can see the Bollinger bands on the chart the rsi panel below

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:14:24 - 00:14:49]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> in the buy and sell signals automatically plotted green arrows for longs red arrows for shorts the the high confidence divergence signals are labeled separately, so you know which setups are the strongest. To set up alerts, click the alarm clock icon at the top of TradingView, select Create Alert, and in the Condition drop-down, you'll see the alert conditions that Claude added, long signal and short signal.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:14:49 - 00:15:10]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Set those up, and TradingView will notify you the moment a signal fires. So now, instead of watching the chart manually, TradingView is doing all the work for you. the moment the Bollinger Band and RSI conditions line up, especially on a divergence. You get an alert straight to your phone. And the exact same process works for the three indicator strategy.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:15:11 - 00:15:44]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Paste the second PineScript into the editor, click Add to Chart, and you will see the Duncan channels, the LWTI panel, the volume indicator, and the buy and sell arrows all firing automatically, exactly the way we set it up manually. But now it is doing it for you. set up your alerts the same way, long signal and short signal. And the moment all three conditions line up on that five minute chart, you get a notification straight to your phone. You check it, you execute, and you are done. Now here's where it gets really interesting. Most people just take a

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:15:44 - 00:16:05]` | Segment #32

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> PineScript, drop it into TradingView, and hope for the best. But what I do is I go back to Claude and I ask it to analyze the results and tell me what is wrong. So once you have run the backtest on TradingView, you will see a strategy performance panel at the bottom of the screen. It shows you your total P&L, your win rate, your max drawdown, and your number of trades.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:16:06 - 00:16:40]` | Segment #33

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Click on that little grid icon in the strategy tester panel and download the CSV file of all the trades. Then go back into Claude, drop that file in, and ask it this. And what Claude does is genuinely impressive. It does not just give you generic advice. It reads the actual trade data and identifies the specific leaks for the Bollinger Band and RSI strategy. When I ran this, Claude came back and told me the biggest issue was false signals during sideways markets, which is exactly what we talked about earlier on the chart. It suggested adding a volatility filter.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:16:41 - 00:17:14]` | Segment #34

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> So the strategy only fires signals when the Bollinger Bands are wide enough to confirm the market is actually trending or making a real move, not just chopping around. So I asked it to rewrite the pine script with that fix included and this is the prompt i use and within seconds claude outputs a revised script you paste it back into trading view the same way run the backtest again and compare the results now keep in mind sometimes the tweak makes things better sometimes it actually makes things worse and that is not a failure that is the process and this is the real power of claude

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:17:14 - 00:17:50]` | Segment #35

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> it is not just a code generator it is a strategic thinking partner you go back and forth you test You compare, you refine. And over time, you are building something that is genuinely yours, not just a strategy you copied from the internet. The models are getting so good these days that if you are not using AI to refine your strategies, you are already falling behind. The top traders, the top quants, they're all doing this. And the good news is most retail traders have no idea this workflow even exists. So right now, you have a real edge just by doing what I'm showing you in

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:17:50 - 00:18:23]` | Segment #36

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> this video. Now, if you want to take this even further and have it trade open automatically on your exchange the moment a signal fires, I've got you covered. I put together a private group where I share all of my use cases for Claude Code from integrating it with Telegram, TradingView, and searching for whales on Hyperliquid. All automatically. Everything I showed you today, it's all inside the group. And I'm constantly adding new stuff, new strategies, new prompts, new integrations every time i build something new it goes straight in there the price is 79.99 a

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:18:23 - 00:18:50]` | Segment #37

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> month and honestly when you think about what this actually is the most cutting edge ai trading setup available to retail traders right now constantly updated with everything included inside there is also a full agentic trading course 2.5 hours beginner to expert no coding background needed By the end of it, you will have your own AI trading system running live, something most retail traders do not even know is possible right now.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:18:50 - 00:19:09]` | Segment #38

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> $79.99 a month. One good trade covers it. And the first 100 members lock in that rate permanently. After that, the price goes up. The link is in the description. You genuinely cannot afford to miss this. And that is it, guys. Two strategies, two clawed prompts, two pine scripts fully automated on TradingView.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

### ⏱️ `[00:19:09 - 00:19:32]` | Segment #39

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> No coding, no manual chart watching, no missed signals. If you want to see a full demo of how I trade using only my telegram and the full demo of all use case on TradingView, click the video popping on screen right now. If you found this useful, leave a thumbs up. It really does help the channel. Subscribe if you haven't already and I'll see you in the next one.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation ou face-caméra explicatif du trader sans interface logicielle partagée.

**Contenu textuel & Code** : Explications orales des stratégies et mise en contexte méthodologique du marché.

**Action / Démonstration** : Explications face caméra et analyse conceptuelle des marchés.

---

