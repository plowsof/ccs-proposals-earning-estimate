---
layout: fr
title: Deploy and maintain Monero Casino.
author: M0n3r0d1c3
date: April 4, 2022
amount: 1
milestones:
  - name: Deployment
    funds: 100% (1 XMR)
    done:
    status: unfinished
payouts:
  - date:
    amount:
---

Hello! I'm M0n3r0D1c3, and I've created casino for Monero.
Yup already created, the code is written and it works pretty well. Hence - it was even deployed once but died because of lack of proper marketing and funding.

Here are some screenshots:
 - https://ibb.co/bPcpS4t
 - https://ibb.co/Gd2ygDG
 - https://ibb.co/7R9WvvZ

Here is an overview of features
 - Provably fair bets, casino can't fake the bet result.
 - No minimum bet, withdrawal and deposit amounts.
 - Community funded bankroll - If you don't feel like playing in casino you can always pick the other side. Be a investor and take adventage of the 1% house edge!
 - On-site chat bridged with telegram chatroom and tip command.
 - Referral system.
 - Deposits can be made using any of the currencies supported by majesticbank and will be exchanged onto xmr and deposited to the site.
 - Monero as accepted currency and Bitcoin as a tolerated currency (with an option to add other currencies, if community wants that).

Now here come few elephants in the room:
 - The casino was already started once - https://bitcointalk.org/index.php?topic=5383564 - but failed due to, lack of investments, lack of marketing, time and funds to promote the site.
 - I'm having extremely bad time with predicting monero transaction fee using the rpc wallet, so the fee amount is constant and the difference is being cashed back to the account (even if negative). But that's being worked on already.

That being said, I'm opening this CCS to get funding mainly for hosting the service, buying the domain ~~(and getting some more attention by the community)~~.

All I'm asking for is money for the VPS with following specs that will run a hidden service, xmr (full) and btc (pruned) node.

 - 2GB Memory 
 - 512 GB (mixed hdd and ssd)
 - Unmetered Bandwidth

For 10$/m.o. for one year, resulting in a 120.00$ yearly price

And another VPS, bought at another vendor that will be responsible for serving clearnet frontend (it will act as a proxy for the hidden service on clearnet.)

It's specs are similar, except for storage - only around 25GB. The offer that I found cost 6$/m.o. (72$/year) and will do the job.

Why two servers? Because one server will be easy to find in case the site will get reported. And at worst case scenario they will take down the clearnet service, but the hidden service will remain up and working - that will allow me to buy another server to serve clients (or at worst case scenario - allow people to withdraw their funds using hidden service).

Last expense is the domain. I think that domain name should be discussed as a part of this prospal. Njal.la will be a good choice for a provider, and their pricing is at 15eur - 70eur, but I think that the most interesting domain names are at 30eur - so domain name will cost us around 35$.

To sum everything up:
 - vps server 1: 120.00$
 - vps server 2: 72.00$
 - Domain: 35.00$
 - Total: 227$

According to `Market Rates: Apr 4, 2022 at 12:53 PM UTC` fetched from CoinMarketCap 227 USD is equal to `1.07187734` XMR (~1.08 XMR)

If you wish to discuss some things with me directly, please contact me using telegram - [@M0n3r0D1c3](https://t.me/M0n3r0D1c3). Or comment on this proposal, I'll be happy to explain everything.

P.S. After funding this proposal I'll be able to deploy the site within few days - including monero node sync time (bitcoin sync however will take somewhat longer amount of time). But the site will need investors that will provide bankroll, to become a investor all you need to do is deposit money on site and create a new investment on the bottom of it. I won't be able to provide any bankroll because my personal monero holding are relatively small (I wouldn't ask for 1XMR otherwise).
