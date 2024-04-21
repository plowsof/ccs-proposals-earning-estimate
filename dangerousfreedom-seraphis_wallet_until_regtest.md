---
layout: fr
title: dangerousfreedom - seraphis wallet work until regtest
author: DangerousFreedom
date: March 30, 2024
amount: 80.64
milestones:
  - name: deliver of proposed demonstrator of a wallet in a regtest
    funds: 80.64
    done:
    status: unfinished
payouts:
  - date:
    amount:
---

## What and Why ?

Since we have now a basic demonstrator of a wallet using a mock ledger, my next goal is to have it on a real ledger. Many components are well developed for that goal like the enote_scanner from @jberman with @SNeedlewoods modifications and the serialization functions from @jeffro256 to enable write/reading transactions into a block in a blockchain file. So the idea is to put all the components together and finish developing the remaining ones in order to have a functional (local) regtest.

The tasks I can foresee for that goal are:

- Review @ghostway's KeyContainer to get it into its final form
- Have a working MockLedger that correctly handles legacy and seraphis enotes.
- Have a prototype of a wallet that loads a legacy wallet, derive a seraphis wallet from that and create seraphis transactions (both using Grootle proofs and FCMP) using legacy enotes.
- Create the basic functions to mine blocks and send enotes to an user.
- Save/Load the blocks into the blockchain using a LMDB database. 
- Make sure to have a basic wallet working on a LMDB regtest database capable of doing basic functions like loading the wallet keys and its enote/history, transferring, visualizing and making knowledge proofs on enotes.

There are many intermediary tasks that would be necessary to do that I am not fully aware of now.

## Who?

- I did [this](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/298), [this](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/344), [this](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/377) and [this](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/409) previous works.

I propose to work for 42 USD per hour, 20h per week, for 12 weeks (or until we have a functional seraphis wallet in regtest), which makes 80.64 XMR considering 125 USD/XMR.
