---
layout: cp
title: xiphon part time coding (3 months)
author: xiphon
date: 15 Oct 2019
amount: 237
milestones:
  - 1st-month:
    funds: 33% (79 XMR)
    done: 11 November 2019
    status: finished
  - 2nd-month:
    funds: 33% (79 XMR)
    done: 31 December 2019
    status: finished
  - 3rd-month:
    funds: 33% (79 XMR)
    done: 31 January 2020
    status: finished
payouts:
  - date: 9 December 2019
    amount: 79
  - date: 3 February 2020
    amount: 158
---

# What

Would love to prolong my part time Monero coding for another 3 months.  
Will be working on Monero Core and Monero GUI code.  
* Inspecting and implementing outstanding feature requests
* Submitting bug fixes
* New functinality
* Addressing ongoing issues
* Code review
* Putting my efforts where it is appropriate

# Who

I'm Xiphon, active contributor to Monero Core and Monero GUI since July 2018.  

My previously completed CCS proposal: https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/55  

During that 10h/week proposal completed the following features.

**Monero GUI: async tasks processing, fixed UI freezing and lagging.**  
Introduced background tasks scheduling, moved time-consuming blocking code parts into background async logic implementing all the missing parts needed to accomplish this.  
Forthcoming Monero GUI v0.15 release will include the improvements, users will notice greatly improved UI response times, no lagging and smooth UX as a result of this work.  

**Implemented decentralized remote node scanning/selection for both CLI and GUI wallets.**  
Set `--public-node` daemon flag to voluntarily provide public access to your node and allow other Monero users to sync their wallets using it. The daemon will propagate its restricted public RPC port over P2P to other peers.  
Wallet users could now use `--bootstrap-daemon-address auto` command line daemon flag. The mode is extending `bootstrap-daemon` functionality. Allows to sync and use the wallet while the daemon is syncing with the network.  
While the daemon is syncing it will automatically select random public node (node that is running with `--public-node` mode enabled) to serve incoming requests (i.e. will use it as a remote node). If currently selected public node fails, the daemon will switch to another randomly chosen public node.  
Once the daemon is fully synced it will use the local blockchain to serve incoming requests, i.e. operating in normal mode.  
*Optionally* you can specify `--no-sync --bootstrap-daemon-address auto` daemon flags to force it to act like a proxy redirecting incoming requests to automatically selected public node.  
Integrated it into GUI Simple Mode, so that is what is used in Simple Mode under the hood now.  
Advanced GUI users to use this feature should enable local node mode, set `--no-sync` startup flag and set bootstrap daemon address to `auto` on the Node settings tab.

**Apart from the mentioned improvements, committed other changes and bug fixes**

Please check the following links to inspect my Monero-related activity:  
- Monero Core - https://github.com/monero-project/monero/pulls?q=is%3Apr+author%3Axiphon
- Monero GUI - https://github.com/monero-project/monero-gui/pulls?q=is%3Apr+author%3Axiphon

# Proposal

Monero is in active development. There is always a plenty of coding work to be done.

Core and GUI repos contain numerous feature requests and bug reports that might get implemented, some are small and some will take some time to implement.

Looking forward to coding and accomplishing ongoing tasks and issues. Implementing new code/functionality that will be needed. Investigating bug reports and submitting bug fixes, fixing build and compilations errors/warnings/etc. Would like to inspect and complete/fix/address issues and feature requests that are reasonably desired and/or worth to spend time on.  Improving GUI, fixing UI/UX issues, implementing design changes.

Dedicate 20 hours per week to Monero Project, at 55 USD/hour rate for a total of 237 XMR. XMR/USD rate is based on the 14-day moving average exponential on Kraken from 15 Oct 2019, which is approximately 55.59 XMR/USD.
