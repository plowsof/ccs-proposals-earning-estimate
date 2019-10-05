---
layout: cp
title: xiphon part time coding (3 months)
author: xiphon
date: 5 April 2019
amount: 111
milestones:
  - 1st-month:
    funds: 33% (37 XMR)
    done: 18 June 2019
    status: finished
  - 2nd-month:
    funds: 33% (37 XMR)
    done: 4 October 2019
    status: finished
  - 3rd-month:
    funds: 33% (37 XMR)
    done: 4 October 2019
    status: finished
payouts:
  - date: June 22, 2019
    amount: 37 XMR
  - date: 4 October 2019
    amount: 74
---

# What

Part time Monero coding for 3 months. Have a couple of distinct things i want to address and start working on first:

1. Decentralized remote node scanning/selection for both CLI and GUI wallets  
Provide an easy to use option for Monero remote node users. A feature to sync the wallet and send transactions without relying on any centralized service or specific remote node.

2. Improving GUI requests processing to prevent GUI unresponsiveness and lagging.  
Improve communication between GUI wallet and the daemon, hardware wallets.  
Is an important issue that affects UX and overall product quality.

3. Additionally will be working on the GUI and CLI code, submitting bug fixes and addressing the ongoing issues, putting my efforts where it is appropriate

# Who

I'm Xiphon, pretty familiar and contributed to Monero core and GUI codebase, helped to implement subaddress support and other missing parts in CCS backend.

Feel free to check the following links to inspect my Monero-related commits:  
- https://github.com/monero-project/monero/commits?author=xiphon  
- https://github.com/monero-project/monero-gui/commits?author=xiphon  
- https://repo.getmonero.org/monero-project/ccs-back/commits/master
- https://github.com/bisq-network/bisq/pull/2422 (Monero address validator for Bisq)

# Proposal

10 hours per week at 55 USD/hour rate for a total of 111 XMR. XMR/USD rate is based on the 14-day moving average exponential on Kraken from 5 April 2019, which is approximately 59.36 XMR/USD.

## Decentralized remote node scanning/selection for both CLI and GUI wallets  

As a part of this approach I've implemented `--public-node` (already merged) mode. Once it is enabled user's daemon starts to advertise its public RPC port to others through P2P.  
And also committed `--no-sync` cli switch that optionally prevents a daemon from downloading the blockchain.

Regarding the proposal I plan to introduce `--bootstrap-daemon auto` mode that will lookup for available public nodes (collect the list over P2P) and then proxify (utilizing current `--bootstrap-daemon` implementation) any incoming RPC request to automatically selected remote node.

Both used in conjunction `--no-sync --bootstrap-daemon auto` on the wallet side and having enough volunteers running their nodes in `--public-node` mode will achieve the specified goal (CLI wallet).

Finally, I will integrate it into GUI wallet to enhance the Simple Mode.

## Improving communication between local daemon and GUI wallet

Current GUI wallet lags and UI becomes unresponsive for quite a noticeable and annoying time during wallet operations. Hardware wallet communications (Ledger/Trezor) freeze the UI as well.

Will locate the code parts that block the UI in order to implement background and/or kind of async requests processing. Might involve some related optimizations and speedups.