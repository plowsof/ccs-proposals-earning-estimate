---
layout: wip
title: jeffro256 full-time development 2023Q4
author: jeffro256
date: Oct 25, 2023
amount: 147
milestones:
  - name: Month 1
    funds: 33% (47.0)
    done: 28 December 2023
    status: finished
  - name: Month 2
    funds: 33% (47.0)
    done: 29 January 2024
    status: finished
  - name: Month 3
    funds: 33% (47.0)
    done:
    status: unfinished
payouts:
  - date: 6 January 2024
    amount: 47.8
  - date: 23 February 2024
    amount: 46.2
  - date:
    amount:
---

## What

I plan to work full-time to work towards implementing the Jamtis changes discussed by tevador, myself, and others, [here](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4665372#gistcomment-4665372), [here](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4692457#gistcomment-4692457), [here](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4706509#gistcomment-4706509), and [here](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4708912#gistcomment-4708912). In summary, I will work to implement flexible-sized view tags, light wallet privacy protections, the simplified key derivation structure, and auxiliary enote records, all together. I have already began work on this, which you can see on [this branch](https://github.com/jeffro256/monero/tree/jamtis_lw_take_2).

I also want to begin work on the new wallet after these Jamtis changes are implemented and reviewed. There are many new wallet types enabled by Jamtis, and much thought is needed to be put into the design so that the code stays easily maintainable and robust. I want to spend a lot of time in the design phase for the wallet so we end up in a better scenario than we are in with `wallet2`. 

## Who

I have been contributing to the Monero core repository for [over a year](https://github.com/monero-project/monero/pulls?page=2&q=is%3Apr+author%3Ajeffro256) with a total of [>=69 merged commits](https://github.com/monero-project/monero/graphs/contributors?from=2022-01-25&to=2023-05-30&type=c) thus far. I also began working on the Seraphis migration project, so you can see some of my contributions [here](https://github.com/seraphis-migration/monero/pulls?q=is%3Apr+author%3Ajeffro256) and [here](https://github.com/UkoeHB/monero/pulls?q=is%3Apr+author%3Ajeffro256). Some more notable contributions from this last quarter:

- I [wrote a library](https://github.com/seraphis-migration/monero/pull/4) that is able to load and store into the `wallet2` format without a dependency on `wallet2`. The way it is written allows for very robust conversion, even for hardware wallets, without the hardware being present. It is much more modular than the current `wallet` loading/storing code, and thus should be helpful in the Seraphis migration.
- I found a solution to some of the privacy problems with Jamtis light wallets and [opened a PR](https://github.com/UkoeHB/monero/pull/15) to fix those issues. I also discussed further changes on the linked Jamtis gist, and will continue to refine Jamtis.
- I [wrote documentation](https://github.com/monero-project/monero/pull/9024) for Monero decoy selection, as well as an easy-to-read, testable, modular Python script.

Previous Proposals:
- https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/319
- https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/390

## Payment

I propose to work 40 hours/week for 3 months so 480 hours total on-paper, though I usually work more than that. The proposal is broken into 3 milestones, one for each month. I am setting my hourly rate at $44/hr, and at a market price of 150 USD/XMR, that makes for a total of 141 XMR.
