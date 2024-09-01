---
layout: wip
title: jeffro256 full-time development 2024Q3
author: jeffro256
date: June 14, 2024
amount: 146
milestones:
  - name: Month 1
    funds: 33% (48.0)
    done: 16 July 2024
    status: finished
  - name: Month 2
    funds: 33% (49.0)
    done: 11 August 2024
    status: finished
  - name: Month 3
    funds: 33% (49.0)
    done:
    status: unfinished
payouts:
  - date: 17 July 2024
    amount: 48
  - date: 14 August 2024
    amount: 49
  - date:
    amount:
---

## What

In the last three months, the likely direction of the future of the Monero protocol changed
drastically with all the work done to bring FCMPs to RingCT. At my last CCS proposal, I
proposed that I would be working on the Seraphis wallet and consensus integrations. Then
I shifted gears to implementing [Jamtis-RCT](https://gist.github.com/tevador/d3656a217c0177c160b9b6219d9ebb96#).
I propose to refine this codebase and produce and LWS-client demo, in order to have these
set of features complete before the FCMP++ upgrade, assuming all goes well. This codebase
can currently construct `cryptonote::transaction`s with Jamtis info encode in the `extra` field,
and then successfully scan that data. Here is a non-exhaustive list of points that need
work with this library:

- Legacy address integration and testing
- Optimization: post-primary-view-tag scanning is about 20% slower than expected
- Testing against actual FCMP++ composition proofs
- Multi-threaded compute
- A live, over-the-wire LWS demo for evaluating the filter-assist/hidden enote trade-offs

I would also like to work on replacing `wallet2` internals with the Seraphis library 'legacy handling'
code, as discussed at this Github issue: https://github.com/seraphis-migration/wallet3/issues/64. A few people
are already working on it, but it will need a lot of manpower to bring it to fruition.


## Who

I have been contributing to the Monero core repository for [over two years](https://github.com/monero-project/monero/pulls?page=2&q=is%3Apr+author%3Ajeffro256) with a total of [68 merged commits to master](https://github.com/monero-project/monero/commits?author=jeffro256) thus far. I also began working on the Seraphis migration project, so you can see some of my contributions [here](https://github.com/seraphis-migration/monero/pulls?q=is%3Apr+author%3Ajeffro256) and [here](https://github.com/UkoeHB/monero/pulls?q=is%3Apr+author%3Ajeffro256). Some more notable contributions from this last quarter:

- Implemented [Jamtis-RCT](https://gist.github.com/tevador/d3656a217c0177c160b9b6219d9ebb96#) into the Seraphis library [here](https://github.com/jeffro256/monero/tree/jamtis_rct). This branch provides support for storing Jamtis scanning data into `tx_extra`, and performs a unit test where a pruned transaction is constructed addressed to Jamtis payment proposals, and then successfully scanned for both plain and self-send enote types. The way this branch was written merges the code paths for doing Jamtis on RingCT and Seraphis together. It could use some cleaning up, and the Seraphis multisig tests need to be updated, but otherwise all Seraphis tests are passing.
- Some other Seraphis stuff including a unified transaction format for Cryptonote, RingCT, and Squashed-Seraphis transactions.

Previous Proposals:
- https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/319
- https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/390
- https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/421
- https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/436

## Payment

I propose to work 40 hours/week for 3 months so `40 (hours/week) * 3 (months) * weeks_per_month = 40 (hours/week) * 3 (months) * (365 / 12 / 7) (weeks/month) = 521` hours total on-paper, though I usually work more than that. The proposal is broken into 3 milestones, one for each month. I am setting my hourly rate at 46 USD/hour (+1 USD/hour higher than last quarter), and at a market price of 163.97 USD/XMR, that makes for a total of 146.2 XMR. Price was calculated as 14-day simple average of opening prices on [CoinGecko](https://www.coingecko.com/en/coins/monero/historical_data) from 2024-06-01 to 2024-06-14 (day of writing), same as last quarter.
