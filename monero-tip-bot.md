---
layout: wip
title: A Monero Tip Bot for Telegram
author: HAH! Sun (omani)
date: July 10, 2019
amount: 13
milestones:
  - name: Collect Feature Requests and Prototype the Telegram bot
    funds: 1
    done: 1 October 2019
    status: finished
  - name: Implement Features
    funds: 5
    done: 1 October 2019
    status: finished
  - name: Intensive Testing of Bot on Stagenet Within Monero Telegram Groups / Bug Fixing
    funds: 4
    done: 1 October 2019
    status: finished
  - name: Delivering Bot to Monero Project Team
    funds: 0
    done: 1 October 2019
    status: finished
  - name: Maintenance and Support
    funds: 3
    done:
    status: unfinished
payouts:
  - date:
    amount:
  - date:
    amount:
---

# Monero Tipping Bot

I would like to put forward a proposal for the development of a Monero tipping bot. I am a code contributor to the Monero Project and author of the [Go Monero RPC Client](https://github.com/monero-ecosystem/go-monero-rpc-client) and a member of the [Monero Ecosystem](https://moneroecosystem.org/) and I believe that I have all the necessary skills to complete this development.

Like many others, I enjoy using Telegram on a daily basis. I am an active member in various monero groups on Telegram and I have noticed the huge interest in a Monero tip bot. So here I am, putting myself forward with a proposal to develop, and deliver, the first ever Monero tip bot for Telegram.

## The Proposal and Milestones
I aim to combine my Monero RPC Client and the Monero Wallet RPC with the official Telegram Bot API.
The Bot will be written in Golang, as is the above mentioned Monero RPC Client of mine that I will be using.
The Bot will be group-enabled, publicly available and accessable in Telegram. Users can use the bot to tip each other from within or outside a group. Users will be able to receive a notification upon sending or receiving a tip when they have started the bot (in a PM, which is standard practice in Telegram). 

### What can this bot do?
This bot is the first of its kind and effectively a Monero wallet for telegram. A telegram user can receive and send Moneros from this wallet using this bot.
Nothing will be stored on the server (where the bot is running), except the wallet, of course. Other than that, no user data, personal information or any other personal data will be stored. Everything happens on-chain and thus no backend database is required. You can tip other users, friends and people in groups, set up giveaways and do lots of other cool things, like sending monero to regular wallet addresses!

The bot is group-friendly, meaning it won't spam the group with messages. Most of the wallet relevant information will be sent to the user via PM.

## Milestones
### 1. Collect Feature Requests and Prototype the Telegram bot
Gather feature requests from telegram users in various Monero groups and decide on a final specification for the bot. Put together the base, boilerplate and structure of the code and make it ready to implement the requested features.

Estimated time: 1 week

### 2. Implement Features
Develop the bot and roll out a test version with the essential and some of the desirable features, in order of priority. Initial focus will be on security and interoperability with the Monero Wallet RPC. Enhanced functionality will be rolled out in regular future updates.

Estimated time: 2 weeks (for core release)

### 3. Intensive Testing of Bot on Stagenet Within Monero Telegram Groups
At this point the bot will need extensive testing to ensure robustness and verify the security features. I propose to test it on stagenet by adding the bot into various groups and let people tip each other with stagenet coins. Every user who is interested to test the bot will be tipped with a certain amount of stagenet coins, big enough to complete a standardised testing script followed by some ‘real life’ use. Stagenet coins will be provided by myself and/or other stagenet coin owners who would like to be involved with this project. I expect a minimum of 50 people to test this bot depending on the degree of engagement from the Monero community. Bug reports from the community and testers will be collected and fixes will be deployed accordingly. Once testing is complete, the operator will switch from stagenet to mainnet by connecting to a daemon running on mainnet.

Estimated time: 4 weeks.

### 4. Delivering Bot to Monero Project Team
Ownership of the bot can be transferred to the official Monero Project Team (Core Team) at any point during the development, should they wish to do so. This official ‘Monero Team’ branding has the obvious advantage of increasing trust in the product, which should drive adoption on Telegram. The bot requires a Monero Wallet RPC Daemon running on a wallet that is also hosted on the node (meaning the operator holds the private keys and seed). All one needs to operate the bot on Telegram is a server (eg. Virtual Private Server or Virtual Machine) and a running Monero Wallet RPC (holding the wallet) that is connected to a remote node. Any chosen individual ‘of trust’ can host the wallet on any server of choice.
  
### 5. Maintenance and Support
As long as I am the author/maintainer of the repository, I will provide support for the code. Eg: Updates on the code when a new version of the Monero Wallet RPC is released, bug fixes, implementation of new features, maintaining Telegram API compatibility etc.

## Cost
* Collect Feature Requests and Prototype the Telegram bot: 1 XMR
* Implement Features: 5 XMR
* Intensive Testing of Bot on Stagenet Within one or more Monero Telegram groups / Bug Fixing: 4 XMR
* Maintenance and Support: 3 XMR (one time fee) 

__Total: 13 XMR__

## Notes
*Authors wish*: I really hope that the Monero Team considers my proposal, and my track record, and takes up this offer. I am genuinely motivated by a desire to contribute towards the growth of the Monero community and the entire Monero ecosytem. 
Should the Monero core team prefer to host the bot themselves after this is coded, this can be easily arranged and the transfer will be fully supported by myself.

The Code will be open source and licensed under the MIT License and will be under the umbrella of the the Monero Ecosystem by transfering the repository to the [monero-ecosystem organization](https://github.com/monero-ecosystem) on Github, like I did with the mentioned Go Monero RPC Client.

## Who?
Sun (also known as `@tombish` on Telegram and `omani` on Github).
