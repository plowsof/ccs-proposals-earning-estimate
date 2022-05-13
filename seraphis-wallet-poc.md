---
layout: cp
title: "koe: Seraphis Wallet Proof-of-Concept"
author: koe
date: 23 February 2022
amount: 81.4
milestones:
  - name: PoC
    funds: 100% (81.4 XMR)
    done: 25 April 2022
    status: finished
payouts:
  - date: 12 May 2022
    amount: 81.4
---

## Intro

Hi all, after the [completion](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256#note_15087) of my previous [Seraphis PoC CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), there are additional tasks I would like to work on. For background on this CCS, please see the links in the previous sentence.


## New tasks

These tasks will be implemented in my [seraphis_lib](https://github.com/UkoeHB/monero/tree/seraphis_lib) branch. My ultimate goal is that, once this CCS is complete, I can hand off seraphis_lib to other Monero developers who can start working on/thinking about how to get Seraphis actually used in Monero.

- Build a wallet proof-of-concept that demonstrates all the 'transaction engineering' capabilities and implementation modularity of Seraphis/Jamtis. My goal is to have unit tests representing all the main workflows possible with Seraphis, and all the main wallet implementations necessary (i.e. mock-ups of interfaces that could potentially be developed into full-fledged wallet software).
- Test out using x25519 for enote ECDH instead of ed25519, which may speed up enote scanning by a non-trivial amount (>10%).
- Add validation code and plumbing for `tx_extra` fields.
- Add tx builder plumbing for tx fees.
- Add multisig tx builders for Seraphis (with unit tests) after the master branch is updated with PR #7877.
- Miscellaneous code cleanup (mostly update/add comments, cleanup TODOs).

I will also lump all the miscellaneous Monero R&D tasks that I work on into this CCS (e.g. in the last period I did a bunch of review/work on multisig security patches, among other things).


## Funding

- Rate: 50 USD + 0.2 XMR
- Hours: 8 weeks @ 20hr/wk = 160hrs
- XMR equivalent: 32 + (50\*160)/USD\_EXCHANGE\_RATE XMR
- USD\_EXCHANGE\_RATE: set from 14-day EMA on a major exchange when merging proposal
  - 162 USD/XMR at 2100 UTC 02/23/2022 w/ 14-day EMA on Kraken -> 81.4 XMR total

If I require more time, and the community supports it, then I may make another proposal to extend the hours.
