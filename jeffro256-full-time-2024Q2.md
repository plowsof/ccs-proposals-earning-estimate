---
layout: cp
title: jeffro256 full-time development 2024Q2
author: jeffro256
date: Feb 27, 2024
amount: 171
milestones:
  - name: Month 1
    funds: 33% (57.0)
    done: 7 April 2024
    status: finished
  - name: Month 2
    funds: 33% (57.0)
    done: 12 May 2024
    status: finished
  - name: Month 3
    funds: 33% (57.0)
    done: 13 June 2024
    status: finished
payouts:
  - date: 9 April 2024
    amount: 57
  - date: 18 May 2024
    amount: 57
  - date: 18 June 2024
    amount: 57
---

## What

I plan to continue work full-time moving towards a Seraphis testnet (and wallet if I have time). These next dev cycles will likely be spent on writing production-ready serialization code, adding support for validating Seraphis transactions to the Cryptonote core, adding database backing support for these transactions, etc (generally weaving the Seraphis library into the core codebase in a way that makes it active). I have already began expanding Seraphis transaction support by beginning work on a transaction class and paired serialization code which will let us capture all possible Monero-compatible transaction forms and handle them in the codebase (expanded on below). 

## Who

I have been contributing to the Monero core repository for [just over two years](https://github.com/monero-project/monero/pulls?page=2&q=is%3Apr+author%3Ajeffro256) with a total of [57 merged commits to master](https://github.com/monero-project/monero/commits?author=jeffro256) thus far. I also began working on the Seraphis migration project, so you can see some of my contributions [here](https://github.com/seraphis-migration/monero/pulls?q=is%3Apr+author%3Ajeffro256) and [here](https://github.com/UkoeHB/monero/pulls?q=is%3Apr+author%3Ajeffro256). Some more notable contributions from this last quarter:

- Polished [Jamtis changes draft PR](https://github.com/UkoeHB/monero/pull/26) and wrote up changes to the "Implementing Seraphis" paper, which were [approved by @UkoeHB](https://github.com/UkoeHB/Seraphis/pull/6).
- Began work on creating a [transaction type](https://github.com/jeffro256/monero/tree/monero_tx_variant) that encapsulates all past and Seraphis future transaction forms: cryptonote v1, v2, coinbase, Seraphis squashed, coinbase, with serialization that is backwards compatible. Along this same line, I wrote a [PR](https://github.com/monero-project/monero/pull/9174) that would help the LMDB backend code transition to Seraphis transactions.
- Wrote a [PR](https://github.com/monero-project/monero/pull/9135) that reduces hard disk usage for nodes.
- Reviewed @j-berman's [background sync PR](https://github.com/monero-project/monero/pull/8619).

Previous Proposals:
- https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/319
- https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/390
- https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/421

## Payment

I propose to work 40 hours/week for 3 months so `40 (hours/week) * 3 (months) * weeks_per_month = 40 (hours/week) * 3 (months) * (365 / 12 / 7) (weeks/month) = 521` hours total on-paper, though I usually work more than that. The proposal is broken into 3 milestones, one for each month. I am setting my hourly rate at 45 USD/hour (+1 USD/hour higher than last quarter), and at a market price of 136.88 USD/XMR, that makes for a total of 171 XMR. Price was calculated as 14-day simple average of opening prices on [CoinGecko](https://www.coingecko.com/en/coins/monero/historical_data) from 2024-02-23 to 2024-03-07 (day of writing).
