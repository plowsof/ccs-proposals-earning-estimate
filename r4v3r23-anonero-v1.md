---
layout: wip
title: ANONERO version 1.0
author: r4v3r23
date: April 12, 2024
amount: 199.265
milestones:
  - name: Inital payment
    funds: 20% (39.853 XMR)
    done: 29 April 2024
    status: finished
  - name: Payment for first test build
    funds: 40 % (79.706 XMR)
    done:
    status: unfinished
  - name: Payment for completion
    funds: 40 % (79.706 XMR)
    done:
    status: unfinished
payouts:
  - date: 29 April 2024
    amount: 39.853
  - date:
    amount:
---



# Who

ANONERO project, creators of the security & privacy focused Monero wallets ANON & NERO.

# What


Migrating our codebase to Android's native language Kotlin with Jetpack Compose UI. 

When we first started the project, we bootstrapped development by using a combination of xmrwallet's Java code and Flutter. This allowed for fast interations and great UI performance, but as the app grew with more advanced features, the Native <> Java <> Flutter layers proved to be a bottleneck.

Now that we have a working Proof of Concept alpha wallet, and are much more familiar with the Monero codebase, we've decided to move the app to a new framework that's better suited to our feature set. This will give us a solid, stable codebase and make future developement much easier.

As part of our commitment to privacy & security and using the latest features, ANONERO has contributed to Monero, directly and indirectly, in various ways:

 1) First fully airgapped DIY HWW cold storage solution: https://monero.town/post/223593
 
 2) First working implementation of background sync via view-keys

 3) Helped identify, debug, and fix issue where Polyseed was failing to build on 32-bit Android: https://github.com/tevador/polyseed/issues/5

 4) Helped identify, debug, and test fix for the DNS leak when using onion nodes: https://github.com/monero-project/monero/pull/8849
 
 5) Helped discover bug where key images weren't being passed by signed tx payload: https://github.com/monero-project/monero/pull/9049
 
 6) Discovered background sync bug which caused all cached blocks to be erased: https://github.com/monero-project/monero/pull/8619#issuecomment-1808920063
 
 7) Helped test tobtoht's upcoming [Polyseed](https://github.com/tevador/polyseed) patch to monero core
 
 8) Worked with tobtoht to improve offline-signing UX
 
We'll continue to adopt and test new features and upstream fixes to core if/when they arise during the CCS.

# Proposal

Instead of guesstimating work hours and giving an hourly rate, we are asking for an amount that will guarantee funding for the entire wallet rewrite. 

Monerujo's Sidekick project raised 181.15 XMR, and seeing as we addressed the community's concerns by shipping the feature fully airgapped using animated QR codes, we are asking the community to match that amount, plus 10% for misc things like hosting, documentation, website improvement etc for a total of 199.265 XMR.  

For the past year and a half we relied on our small community to help fund us, and now that we've proven we can deliver, we are requesting 20% upfront to start development:
 
- Milestone 1:  39.853 XMR (20%) paid upfront upon funding
  
- Milestone 2:  79.706 XMR (40%) paid upon release of first test build (corresponding to v0.5)

- Milestone 3:  79.706 XMR (40%) paid upon final feature-complete release

Progress will be posted on our repo http://git.anonero.io (onion redirect) and we will begin open testing as soon as we can.

CCS will expire one year from date of first payout and funds can be send to the General Fund.
