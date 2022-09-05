---
layout: wip
title: "koe: Seraphis Library Work"
author: koe
date: 18 Aug 2022
amount: 122
milestones:
  - name: PoC
    funds: 100% (122 XMR)
    done: 
    status: unfinished
payouts:
---

## Intro

Hi all, I [closed out](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/314#note_18262) my previous [Seraphis Wallet PoC CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/314) after consuming all the hours. There are additional tasks I would like to work on. For background on this CCS, please see the links in the previous sentence.

In the last CCS period I decided that an actual wallet proof-of-concept is too ambitious. My more modest/realistic goal is to complete the Seraphis library so wallets can be (relatively) easily built.


## Continuing work

Here are the tasks I hope to finish by the end of this CCS (a continuing refrain, maybe some day my list will have no more items). As before, these will be implemented in my [seraphis_lib](https://github.com/UkoeHB/monero/tree/seraphis_lib) branch.

- Legacy/Seraphis integration so old cryptonote-style enotes can be spent in Seraphis transactions.
- Seraphis-style coinbase transaction type.
- Test out tevador's [x25519 library](https://github.com/tevador/mx25519) for enote ECDH instead of ed25519, which may speed up enote scanning by a non-trivial amount (>10%). (big thanks to @tevador for putting that library together)
- Miscellaneous code cleanup (mostly update/add comments, cleanup TODOs).
- Update the [Seraphis draft](https://github.com/UkoeHB/Seraphis), which I have not touched for 6 months.

As usual, I will also lump all the miscellaneous Monero R&D tasks that I work on into this CCS (e.g. in the last period I did more review/work on multisig security patches, among other things).


## Funding

- Rate: 50 USD + 0.2 XMR
- Hours: 12 weeks @ 20hr/wk = 240hrs
- XMR equivalent: 48 + (50\*240)/USD\_EXCHANGE\_RATE XMR
- USD\_EXCHANGE\_RATE: set from 14-day EMA on a major exchange
  - 163 USD/XMR at 0045 UTC 08/18/2022 w/ 14-day EMA on Kraken -> 122 XMR total

If I require more time, and the community supports it, then I may make another proposal to extend the hours.
