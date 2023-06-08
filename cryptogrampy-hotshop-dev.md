---
layout: cp
title: HotShop Point of Sale
author: cryptogrampy
date: April 7, 2022
amount: 18
milestones:
  - name: Milestone 1 - Create and publish payment code, perform basic payment generation and verification on deployed webapp
    funds: 0
    done: 29 May 2022
    status: finished
  - name: Milestone 2 - Create and publish draft Point of Sale user interface for feedback
    funds: 8
    done: 29 May 2022
    status: finished
  - name: Milestone 3 - Create finalized Point of Sale interface, create install and deployment instructions, publish freely available version
    funds: 10
    done: 27 May 2023
    status: finished
payouts:
  - date: 1 June 2022
    amount: 8
  - date: 7 June 2023
    amount: 10
---

HotShop - a browser-based, ephemeral, no-server point of sale

**who**
Hello, it's me, your great-grandfather CryptoGrampy.  You might know me on Twitter as @CryptoGrampy or from my work on the Monerod-on-Termux Android script, the Android PocketNode(tm), the Monero Drag n' Drop Electron app or from Friday morning bridge club in the cafeteria.

**what is this**
Monero is really lacking in the physical Point of Sale department. Let's fix that. 

The HotShop will be a simple to use webapp with a simple aesthetic and UI similar to Kasisto (RIP) and POS.cash that can be accessed from just about any web browser (on mobile or desktop) with a slight amount of user customization (company name/image, etc). 

You will be able to hit HotShop.cryptogrampy.com, enter your payment details, type in the desired XMR (optionally USD if you allow that API request) amount... a QR code and address will display, and the UI will update (payment confirmation progress as well) immediately when someone has paid the correct amount. 

No hosting, private spend keys, personal servers/VPS's or payment gateways will be required. The app will be able to be added to any free web host- Github pages, etc and available for anyone to use because the magic happens in your browser (you'll be able to self-host it if you want) Users will need provide the app with their primary and view keys (no spend key involved!) on the client side (this info does NOT get sent to the server) and they will specify a remote Monero node of their choice.

The tech stack will be something like: Monero-Javascript, Vue3, and Typescript.

You'll be able to set this up at a garage sale, coffee shop, with your friends, etc and generate fresh/unused payment addresses displayed as QR codes.  In the settings, you'll set your desired number of confirmations (or do zero conf!), point it at a remote Monero node of your choice, and be able to collect payments and immediately validate that they were received/watch them as they get confirmed.  

You'll be able to bookmark a link on your phone/browsers that contain all of the credentials necessary to start up the POS or have a QR code on a card containing a special link in your wallet... Just scan it with any device- your friend's phone, the library computer, the ipad at your store, and Boom! you have an instant Point of Sale.

**Who does this benefit? Why do I need this when I can just use a mobile wallet?**
- I think the physical Point of Sale situation is still pretty lacking in Monero
- No existing wallets have good Point of Sale tech or UI
- Perhaps you're in a situation where you can't have a wallet app on your phone/desktop but want to receive/validate payment
- Perhaps you're in a situation where you want to be able to accept payments, but are worried about someone stealing your device or spend key wallet
- An ephemeral point of sale that sort of lives on a QR code or bookmark in your phone sounds really cool
- Maybe your mobile wallet is 1000000 blocks behind and want to IMMEDIATELY accept and verify a payment
- Don't you want to make 100% sure your buddy at the bar *actually* sent those funds?  It's better than a static payment address.

Also... Need yet another payment gateway?  The code for this will be written in a clean way that could be used in a NodeJS server or as a different front end implementation via simple exposed methods for instantiating the gateway, creating new payment requests and verifying payments.  If I have enough time, I will publish this portion of the code separately, and ideally as an npm library.  

**what does this not do**
- It's not going to keep track of payments that occurred before you hit the website (it's not going to be a full wallet).  It will sync at the latest block height to have the ability to immediately begin accepting payments
- It's not going to keep track of prices, photos and items you have for sale in your store

**potential reach ideas**
- CSV export of tx's that occur in a session
- Vending machine exploration
- Pin code lock/unlock
- Display past tx's within the session in a pleasant way
- Local browser storage of user data
- Importing prices/items via github repo json files
- TOR support
- Payment completion callback (provide a POST endpoint to receive completed payment data)

**milestones**
1st milestone - Coding up the basic payment portion in a nice/clean way, publishing a mostly bug-free, minimal version for testing user setting import and payments
2nd milestone - Publish first draft of the POS interface (will be responsive), getting feedback from testers
3rd milestone - Publish functioning POS to Github pages, etc, create documentation/video demo for use and self-hosting  

**amount**
I estimate that this will take about 4 to 5 weeks of mostly full time work and I am asking for 18 XMR. 

**expiration**
I will be working on this in the evenings and weekends but expect to have this complete within 4-8 months.
