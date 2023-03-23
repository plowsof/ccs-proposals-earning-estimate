---
layout: fr
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

A full peer review of the eprint version [[link]](https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=83&browserTabID=) of the paper. Note that at the time of writing this proposal, the paper is not yet published in a peer-reviewed conference/journal.

The deliverable is a write-up which will include recommendations, notes, weaknesses, and issues (if any) of the BP++ paper touching on:
- The soundness, completeness, and zero knowledge portions of the paper.
- Efficiency. Aggregation. Batching. MPC compatibility.
- Making sure it fits neatly and completely into the place that BP+ currently sits by checking the correctness of proofs.

## Funding

- $16,500 + 20% buffer = $19800 gives 130XMR @ 152.30USD
- Funds are released by Core to a third party and converted. 
- $16,500 will be paid directly to [CypherStack](https://cypherstack.com/).
- Excess XMR after conversion will be donated to the next Bp++ CCS.
- Any shortfalls from volatility will be paid by the Monero General Fund.
