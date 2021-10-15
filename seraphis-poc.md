---
layout: fr
title: "koe: Seraphis Proof-of-Concept"
author: koe
date: 1 October 2021
amount: 92.6
milestones:
  - name: PoC
    funds: 100% (92.6 XMR)
    done: 
    status: unfinished
payouts:
---

## Intro

Hi all, after some encouragement I decided to request funding for my ongoing work on Seraphis. Specifically, funding for future work on the Seraphis C++ proof-of-concept that I have been developing since the second week of September.

My goal is for this code to be 95% production-ready. It is appropriate to get large pieces of code funded if they have a strong potential to be merged into the master branch.



## What is Seraphis?

[Seraphis](https://github.com/UkoeHB/Seraphis) is a next-gen transaction protocol abstraction, which means it defines various high-level rules for a concrete transaction protocol. RingCT can be thought of as the current tx protocol abstraction, even though [the RingCT paper](https://web.getmonero.org/resources/research-lab/pubs/MRL-0005.pdf) specified concrete proving structures directly without abstraction.

The main innovation of Seraphis (and [Lelantus-Spark](https://eprint.iacr.org/2021/1173), a very similar protocol developed independently) is using _only_ simple commitments-to-zero for showing that a transaction input (an output being spent) exists in the ledger. This allows proofs about key images to be independent of membership proofs, which means one-time addresses and key images can be creatively designed. In particular, it is possible to avoid one of the main drawbacks of [Triptych](https://eprint.iacr.org/2020/018), namely a key image construction that makes multisig [much more complicated](https://github.com/cypherstack/triptych-multisig).

Seraphis has other potential benefits over RingCT and Triptych (depending on concrete design choices):
- membership proof delegation (allows transaction chaining, offloading proof construction to third parties, improved indistinguishability of multisig tx [construct membership proofs at the last minute to avoid leaking timing details], allows the 10-block lock time to be somewhat ignored when transacting with a trusted party)
- multi-tier wallet permissions (e.g. a view-only wallet that can detect spent outputs, a view-only wallet that can see received outputs but not their amounts)

The main costs of Seraphis compared to Triptych are:
- more implementation effort
- all users would have to generate new addresses from their private keys (don't need new private keys, seeds, or wallets); all old addresses would become unusable
    - **note**: Replacing old addresses is an opportunity to deprecate 'normal addresses' in favor of 'subaddresses' only. A uniform address format would simplify UX and various implementation details.



## PoC

**Scope**: I am working on a core component library for Seraphis, which includes proof structures, transaction structure and validation, core transaction building pieces (both normal and multisig transactions), unit tests, performance tests. The scope is similar to the `ringct/` subdirectory. I currently do not plan to touch the `wallet/` subdirectory.
- The scope also extends to my efforts to performance test different variants of Seraphis, and Lelantus Spark. However, only the main parts of Seraphis will get high-quality attention until performance results are available.

Building a new transaction-builder component library is a good opportunity to both re-imagine how to architect component versioning (i.e. instead of spaghetti conditionals, which are rampant in some parts of the codebase after 13 hard forks), and to add various things from my wishlist.

Ultimately, I want to include the following in my PoC (found in the MRL and Monero GitHub Issues linked below):
- reorganized tx semantics (`tx_supplement` takes some stuff out of the `tx_extra`)
- view tags
- enforce 1 tx pub key for 2-out tx, 1 key per output for >2-out tx
- enforce sorted-TLV in the extra field
- Janus mitigation (one way or another - depending on the address scheme chosen)


### PoC: current progress

The PoC currently has:

- mock-up of RingCT with CLSAG (for performance comparisons)
- mock-up of Triptych (for performance comparisons)
- concise Grootle proof (with 'aggregation coefficients', like found in Triptych)
- plain Grootle proof (without 'aggregation coefficients', like found in Lelantus-Spark)
    - **note**: The guys at Firo theorize this should have faster verification than concise Grootle proofs (using 'small scalar weighting'), but in my tests it is slower. This may be due to a limitation of Monero's crypto library, which contains no optimizations for small scalar EC multiplication, so future improvements may be possible.
- Seraphis composition proof
- unit tests for all of the above
- tx mock-up performance testing framework


### PoC: TODO

My immediate plans for the PoC include:

- core multisig functionality in Seraphis composition proof
- mock-up of 4 different Seraphis variants
- mock-up of Lelantus-Spark (probably... it turns out coding complex cryptographic algorithms like advanced signature schemes is a lot of work)
- unit tests for all of the above
- comprehensive performance testing of all tx protocol mock-ups

Once performance tests are complete, I will take a break of 1-4 weeks to finish the Seraphis paper. Then, after making various design decisions to narrow down the optimal tx protocol and address scheme (based on discussion in the Monero community - primarily IRC channels #monero-dev and #monero-research-lab), I want to add the following to the PoC (I will probably make a new branch for this, and cut out all the extra stuff from performance testing).

- mock-up of Seraphis addressing framework
- mock-up of Seraphis transaction builder framework (with multisig)
- the wishlist from [above](#PoC)



## Past and current Monero work

- [Seraphis paper](https://github.com/UkoeHB/Seraphis): in-progress
- [Seraphis PoC branch](https://github.com/UkoeHB/monero/tree/seraphis_perf): in-progress
- [ZtM2](https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf): complete
- [ZtM1](https://web.getmonero.org/library/Zero-to-Monero-1-0-0.pdf): complete
- [MRL issues](https://github.com/monero-project/research-lab/issues/created_by/UkoeHB): many are active/open (the fee issue is [close to merging on master](https://github.com/monero-project/monero/pull/7819))
- [Monero issues](https://github.com/monero-project/monero/issues/created_by/UkoeHB): tx semantics proposal is open
- [Monero PRs](https://github.com/monero-project/monero/pulls/UkoeHB): multisig address-generation rework is open



## Funding

- Rate: 50 USD + 0.2 XMR
- Hours: 6 weeks @ 40hr/wk = 240hrs
- XMR equivalent: 48 + (50\*240)/USD\_EXCHANGE\_RATE XMR
- USD\_EXCHANGE\_RATE: set from 14-day EMA on a major exchange when merging proposal
  - 269 USD/XMR at 1800 UTC 10/13/2021 w/ 14-day EMA on Kraken -> 92.6 XMR total

If it takes me fewer than 240hrs, then I will allocate the extra hours toward whatever future Monero work I end up doing (or pass the left-over funds into the general fund if necessary).

If I require more time, and the community supports it, then I may make another proposal to extend the hours.
