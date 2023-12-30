---
layout: wip
title: Bulletproofs++ Peer Review
author: Monero Research Lab
date: March 22, 2023
amount: 130
milestones:
  - name: Bp++ eprint peer review
    funds: 130
    done:
    status: unfinished
payouts:
  - date:
    amount:
---
## Bulletproofs++ Peer Review

This CCS will provide funding for the first step towards Bulletproofs++ implementation in Monero. (and also the planned Seraphis upgrade). Bulletproofs+ were added in the latest [Network Upgrade](https://www.getmonero.org/2022/04/20/network-upgrade-july-2022.html). They reduce the typical transaction size by ~5-7% and improve typical verification performance by ~5-7%, making every transaction lighter and faster. Bulletproofs++ claims to significantly improve upon this (e.g. ~27% smaller than Bp+).

## Scope / Deliverables

A full peer review of the eprint version [[link]](https://eprint.iacr.org/archive/2022/510/20230717:163509)  of the paper. Note that at the time of writing this proposal, the paper is not yet published in a peer-reviewed conference/journal.

The deliverable is a write-up which will include recommendations, notes, weaknesses, and issues (if any) of the BP++ paper touching on:
- The soundness, completeness, and zero knowledge portions of the paper.
- Efficiency* Aggregation. ~~Batching. MPC compatibility.~~ 
- Making sure it fits neatly and completely into the place that BP+ currently sits by checking the correctness of proofs.

## Out of scope

- Multiparty computation. There are no specific protocols presented for this, and no corresponding security model of proofs of security.
- Batch verification. While the preprint mentions that BP++ supports batch verification, it provides no details on the corresponding algebra.
- Multi-asset transactions. The preprint discusses multi-asset transactions in the context of its protocols, but these are not required for range proofs.
- Optimized binary range proofs. The protocol proposed for optimized binary range proofs has only an informal and vague security proof that is insufficient to assert the claims of the corresponding theorem.

## Funding

The latest version of the paper is now greatly expanded. CypherStack has given a new quote for this paper of $32,000. Core will decide how the shortfall is handled.

- Funds are released by Core to a third party and converted. 
- $32,000 will be paid directly to [CypherStack](https://cypherstack.com/).
- Excess XMR after conversion will be donated to the next Bp++ CCS.
- Any shortfalls from volatility will be paid by the Monero General Fund.
