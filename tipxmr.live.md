---
layout: wip
title: "tipxmr.live - a non-custodial livestream donation service for OBS"
author: AlexAnarcho and hundehausen
date: September 16, 2020
amount: 72
milestones:
  - name: Milestone 1 - Basic setup of webpack with monero javascript and react
    funds: 2% (1.44 XMR)
    done:
    status: unfinished
  - name: Milestone 2 - Working Prototype with implemented WASM wallet and front-end mockups
    funds: 48% (34.56 XMR)
    done:
    status: unfinished
  - name: Milestone 3 - Finished product and launch of serivce
    funds: 50% (36 XMR)
    done:
    status: unfinished
payouts:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
---

# CCS Proposal: tipxmr.live - a non-custodial livestream donation service for OBS


## Exec Summary

[Tipxmr.live](https://github.com/hundehausen/tipxmr) aims to be a non-custodial service for streamers to accept and display Monero donations in their livestreams.

Much like the existing solutions, this allows for an interactive experience for viewers and an easy way to monetize for the streamer.

For this we use a browser based Monero WASM wallet and OBS.


## The Problem we want to solve

Censorship on the internet is an ongoing issue. Big platforms like YouTube and Twitch wield godlike power when it comes to their users. Not only do they impose barriers to entry, they also deplatform at whim and destroy years of work take away steady income streams. Content creators either have to conform and self censor or change their occupation.

Furthermore, streaming platforms take big chunks of the streamers income, for example Twitch Bits. Some platforms take as much as 40% of the streamers donations (Chaturbate).

Tipxmr.live fixes this.

### Advantages of our solution

With tipxmr.live we enable streamers to recieve income independent of a given platform. For this we employ Monero natively in the browser. Donors send XMR directly to the streamer without tipxmr.live as a custodian.

Being build upon the Monero project, we inherit many benefits of the privacy coin we all love.

Streamers are not required to have access to the banking system, all they need is provided for free on the internet (i.e. Monero and OBS).

Moreover, streamers do not have to hand over personal information such as location, real identity and more. This opens the door for marginalized groups to recieve income, even if the doors to the tradional system is barred.


## Who we are

We are two Monero enthusiasts that have been following the project since the beginning of 2017. Our values are privacy, sound money and individual souvereignty. Crypto in general and Monero in particular fulfill these values and are the tool of the future.

In the beginning of 2018 we created the [MoneroMumble Podcast](https://moneromumble.de/), a german-speaking, monthly podcast/roundtable to inform and engage the German community about developments concerning Monero. The roundtables take place on the second Sunday of every month on Jitsi and are livestreamed to YouTube.

It was in this setting that the idea of a livestream donation program based on Monero was born. Tipxmr.live is therefore aiming to fulfill our need and we are our own customers.

Grischa, aka hundehausen, has contributed many times to the Monero community, most recently with an [infographic about the workings of a Monero wallet](https://reddit.com/r/Monero/comments/gy0m1u/i_made_an_infographic_on_how_a_monero_wallet_is/). Grischa also wrote his bachelor thesis on the thought of "Monero as a currency for the masses" (thesis in German).

Alex, aka AlexAnarcho, has been involved in the early days of the Monero Outreach and is a well-known outspoken advocate for Monero in the German community. Alex has been working for various cryptocurrency magazines such as the BeInCrypto and BTC-ECHO. In August he quit his full-time job at BeInCrypto to dedicate himself to tipxmr.live.

[mghny](https://github.com/mghny) - who chooses to remain pseudonymous - has been a professional software-engineer for 5 years and has been coding for 8 years. They have been involved with tipxmr.live since the very beginning and keeps an eye on architecture, code and many more technical aspects. It cannot be overstated how beneficial an experienced engineer is in a project like ours, since it reduces complexity and makes the code easily reusable by other developers.


## What is your project

Since our [original idea and prototype](https://github.com/hundehausen/obs-monero-donations), the implementation has significantly evolved. The most obvious issue with the prototype was that it required a broad technical understanding. You can try it out by cloning the repo and seeing first-hand how cumbersome this process is. After cloning the repo you have to set up either a VPS or self-host and use portforwarding. Then you have to install monero, run an RPC, buy a domain, issue a SSL-certificate and so forth. In short, a process that no ordinary person would go through.

But we don't want to be the only people enjoying the benefits of Monero. We want to make it accessible to _everybody_ - even non techy people. Therefore we went back to the drawing board and came up with a way that is intuitive yet non-custodial and as safe as possible.

The current vision only requires [OBS](https://obsproject.com/), which is not only the biggest streaming software but also open source. In this we are platform agnostic and our users can use YouTube, Twitch, any other streaming platform or even host the stream themselves.


### How it works

The biggest issue in the beginning was how to make this whole thing non-custodial AND easy to use. Thanks to the awesome [monero-javascript library of woodser](https://github.com/monero-ecosystem/monero-javascript) that now includes a Monero WASM wallet, we are able to offer just that. WASM or WebAssembly basically means that you are running a full Monero wallet _in your browser_. You are the only one controlling the keys, they never leave your system. _But_ we are able to create a nice userinterface, a dashboard with settings, and much more.

Of course the details are of no concern to the normal user. The streamer simply navigates to tipxmr.live, clicks to create a new account and the WASM wallet will generate a XMR seed on the clients machine. The streamer writes down the seed and chooses a username.

Then the streamer can log in using only their seed. We have a small database running on our server that checks the hash of the seed and logs the user in if it checks out. The streamer is then shown a dashboard where they have an overview of their usage. The dashboard also includes a wallet section where they can send/recieve XMR (for instance if they want to withdraw to a cold storage). Last but not least the streamer can change some settings, i.e. how donations should be displayed etc.

Every steamer has their own animation URL that they can point an OBS browser source to. Donation messages are displayed there, so if the browser source in OBS is active, they will overlay over the stream.

For donors the whole process is very easy as well: The streamer simply displays his donation URL (tipxmr.live/$username). Depending on the streamers configuration a donor can enter a message and their name. Once they hit "submit" the donors browser will query the streamers browser over our backend for a subaddress. Once the subaddress is payed the animation site of the streamer is refreshed and the message is displayed.

Donors are shown the subaddress with XMR URI and the corresponding QR code to pay either via desktop or mobile wallet.

Donations are accepted on a 0-conf basis, meaning they will be queued up to display once they are seen in the mempool.

It is surprising _how easy paying with Monero actually is_. Much easier than paying with PayPal or a bank. Also, _way more private_ and cheaper.



### Other awesome stuff

Since monero is an internet-based technology, there are many cool things we can do. Here is a few thoughts:

-   allow the streamer to specify a "second price". I.e. if the second costs 0.00043 XMR the donor can select how many seconds he wants his message to stay visible and then will be given a specific amount of XMR to donate
-   allow the streamer to set a cost per character in the message, same procedure as with the second price for the donor
-   upload custom sounds to be played when recieving a message
-   allow donors to send gifs with their message, and demand a minimum amount for this feature from the donor
-   have a funding goal that gets added to with every donation
-   and much more...


## How our projects benefits the Monero community

-   Tipxmr.live strives to give one more usecase to Monero and do so natively without having to use another cryptocurrency.
-   We enable streamers to _earn_ XMR - the best way to aquire Monero. Furthermore, like Dr. Daniel Kim always talks about tipxmr.live is a usecase for the squeaqy clean guy. In short a way to use Monero that has nothing to do with illegal activity. This lends legitimacy to Monero as a medium of exchange and gives one more example in the narrative for our fight to privacy.
-   Community led streams such as Monero Coffee Chat, Monero Space, Monero Mumble and many more will have an easy way to monitize to cover costs and increase enagement from the community.
-   Monero has low fees and pretty good privacy. However, the privacy increases with every transaction on the blockchain and makes a blackball attack much harder. Since all our donations are on-chain, we increase the number of decoys for everybody. Notice that we as a service do not store any on-chain information such as TX-Id. Don't believe us? Check the code.
-   We are one of the first, if not the first project to make use of the Monero javascript WASM wallet, as such we serve as an example project for implementation that many others can copy and look to. This is actually a big deal for everybody that knows some webdevelopment but is not savy enough to configure Webpack with monero javascript and say, Reactjs. Been there, done that - you are welcome!
-   All of our code is open source, of course. This means that you do not have to use tipxmr.live, you can fork the repo and setup your own service. We also encourage everybody to look through the codebase and raise issues when needed.
- We aim for a high developer friendlyness so others can take our implementation and change it to their needs. The implementation of the WASM Wallet should be a good example for others.
-   To sum it up, we increase the possiblities in the Monero universe for streamers, average users and developers.


## What has been done so far

Since we are very passionate about Monero and the idea, we already have a GitHub repo with some code in it. We started on this late August 2020 and have been working on it full time (70-80 hours per week in total). We can see that there is still much work to be done and in order to get some feedback and support ourselves we turn to the Community Crowdfunding System.


## What we ask for

We ask for 72 XMR (approx. 5400 EUR) in total. So far we have invested more than 250 hours and will take another 150 hours to complete the minimum viable product.

The cost for this project is considerabely lower than it would be if we were not bleeding heart fans of Monero and our idea. We want to see the Monero Project grow and enable more usecases.

The first two milestones will cover the work we have already done. Which is mainly setting up the Webpack configuration for Monero javascript and React. And then implementing functions of Monero javascript with the WASM wallet, backend to allow communication between streamer and client (using socket.io) and writing of wallet functions (i.e. sync, getSubaddress etc.).

The third milestone is when the project is finished and the service will officially launch. This will happen within the year 2020.

We will also provide a server to host the website, our own full node and proxy to solve to [CORS issue](https://github.com/monero-project/monero/issues/5172). 

We also contemplate expanding on tipxmr.live and generating income that way. But please keep in mind that we are 100% open source and anybody can copy our idea and hard work.


## Future Plans

To be absolutely clear: Tipxmr.live will be a paid service!

We host the website and allow streamers to have a comfortable experience in recieving live donations. To cover costs and to protect against spam of accounts, we will charge a small, flat fee (probably 1 USD worth of XMR per month) for our base model. From our experience with livestream donations this fee is negleable, since most streams will earn far more than the fee.

We are also thinking of a higher fee for premium tier that allows for more customizations. The premium account will hopefully make our innovative business model sustainable and keep us improving the project.

