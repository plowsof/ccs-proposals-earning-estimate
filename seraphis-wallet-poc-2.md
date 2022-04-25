---
layout: fr
title: "koe: Seraphis Wallet Proof-of-Concept 2"
author: koe
date: 1 May 2022
amount: 155
milestones:
  - name: PoC
    funds: 100% (155 XMR)
    done: 
    status: unfinished
payouts:
---

## Intro

Hi all, I [closed out](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/290#note_16046) my previous [Seraphis Wallet PoC CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/290) after consuming all the hours. There are additional tasks I would like to work on. For background on this CCS, please see the links in the previous sentence.


## Continuing work

Here are the tasks I hope to finish by the end of this CCS. As before, these will be implemented in my [seraphis_lib](https://github.com/UkoeHB/monero/tree/seraphis_lib) branch.

- Add tx builder plumbing for _discretized_ tx fees (see the [04/20/22 MRL meeting](https://github.com/monero-project/meta/issues/691) for a discussion).
- Consider using 16-byte address indices (instead of 7), with 2-byte encoded address index MACs (instead of 1).
- Implement a robust 'input selection' solver that takes advantage of statically-determinable tx weights.
- Implement a maximally-efficient and generic enote-scanning workflow.
- Build a wallet proof-of-concept that demonstrates all the 'transaction engineering' capabilities and implementation modularity of Seraphis/Jamtis. My goal is to have unit tests representing all the main workflows possible with Seraphis, and all the main wallet implementations necessary (i.e. mock-ups of interfaces that could potentially be developed into full-fledged wallet software).
- Test out using x25519 for enote ECDH instead of ed25519, which may speed up enote scanning by a non-trivial amount (>10%).
- Miscellaneous code cleanup (mostly update/add comments, cleanup TODOs).

As usual, I will also lump all the miscellaneous Monero R&D tasks that I work on into this CCS (e.g. in the last period I did more review/work on multisig security patches, among other things).


## Funding

- Rate: 50 USD + 0.2 XMR
- Hours: 16 weeks @ 20hr/wk = 320hrs
- XMR equivalent: 64 + (50\*320)/USD\_EXCHANGE\_RATE XMR
- USD\_EXCHANGE\_RATE: set from 14-day EMA on a major exchange
  - 175 USD/XMR at 0100 UTC 05/16/2022 w/ 14-day EMA on Kraken -> 155 XMR total

If I require more time, and the community supports it, then I may make another proposal to extend the hours.
