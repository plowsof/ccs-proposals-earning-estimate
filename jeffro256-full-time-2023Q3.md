---
layout: cp
title: jeffro256 full-time development 2023Q3
author: jeffro256
date: May 30, 2023
amount: 147
milestones:
  - name: Month 1
    funds: 33% (49.0)
    done:
    status: unfinished
  - name: Month 2
    funds: 33% (49.0)
    done:
    status: unfinished
  - name: Month 3
    funds: 33% (49.0)
    done:
    status: unfinished
payouts:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
---

## What

I plan to work full-time to work towards accomplishing:
1. Implementing Seraphis wallet code with Ukoe, jberman, et al.
2. Drafting a formal specification for decoy selection and implementing it in a modular, robust, easily-testable way, and then creating a multitude of unit tests, integration tests, and statistical checks for this code.
3. Reviewing other Monero core PRs, especially those related to Seraphis or @vtnerd's serialization changes.

To expand on point 2, I think the decoy selection code is in need of a makeover. In light of recent, high-impact decoy selection bugs (more info [here](https://www.getmonero.org/2021/09/20/post-mortem-of-decoy-selection-bugs.html) and [here](https://github.com/monero-project/monero/issues/8872)), and whereas ring signatures are generally regarded as the weakest link in Monero's privacy model, I believe a new development initiative needs to take place to replace the decoy selection code. Typically I am against refactoring code "just because", but in this case it is warranted. All of the aforementioned bugs could have been spotted by statistical checks. However, currently, it is rather difficult to test the decoy selection in isolation due to the monolithic design of `wallet2`. In theory, decoy selection code could be written to be rather functional. To over-simplify, we take distribution of enotes on-chain usable for given for true spends, apply arbitrary picker distribution, then request information for selected decoys over RPC, retrying the process if enotes are blackballed or otherwise unsuitable. There are a lot of edge cases to consider, but there isn't any major reason why decoy selection can't be modularized and standarized apart from the rest of the wallet code. This goal also overlaps with point number 1, since this code can be used not only in `wallet2`, but in future versions of core wallets if written correctly.

## Who

I have been contributing to the Monero core repository for [over a year](https://github.com/monero-project/monero/pulls?page=2&q=is%3Apr+author%3Ajeffro256) with a total of [>=48 merged commits](https://github.com/monero-project/monero/graphs/contributors?from=2022-01-25&to=2023-05-30&type=c) thus far. Some more notable contributions:

* Implemented [research issue 109](https://github.com/monero-project/research-lab/issues/109) by [authoring a PR](https://github.com/monero-project/monero/pull/8815) that, when spending coinbase enotes, chooses coinbase enotes as decoys and vice versa.
* [Implemented](https://github.com/monero-project/monero/pull/8861) a requested wallet transfer feature that enables "fee-included" transactions
* [Found and fixed](https://github.com/monero-project/monero/pull/8707) an issue which nearly allowed a double spend bug, and could cause double spend bugs in the future if the code was not carefully inspected
* Helped review [patch](https://github.com/monero-project/monero/pull/8794) and write [disclosure report](https://github.com/monero-project/monero/issues/8872) on recent decoy selection bug.

Previous Proposals:
- https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/319

## Payment

I propose to work 40 hours/week for 3 months so 480 hours total. I'm setting my hourly rate at ~$43/hour, and at a price of $140/XMR (as of June 10th 2023), this makes for a total of 147.4 XMR. The proposal is broken into 3 milestones, one for each "month". These milestones may lag behind schedule if I do not complete 40 hours per calendar week, but in that event, I will not ask for payout until the hours are done.

