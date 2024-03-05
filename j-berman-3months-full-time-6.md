---
layout: wip
title: j-berman full-time development (3 months)
author: j-berman
date: December 18, 2023
amount:  211 Monero
milestones:
  - name: Month 1
    funds: 33% (70.3 Monero)
    done: 23 February 2024
    status: finished
  - name: Month 2
    funds: 33% (70.3 Monero)
    done:
    status: unfinished
  - name: Month 3
    funds: 33% (70.4 Monero)
    done:
    status: unfinished
payouts:
  - date: 4 March 2024
    amount: 70.3
  - date:
    amount:
  - date:
    amount:
---

## What

Work full-time 3 months on:

- Continuing Seraphis wallet library work.
  - Complete the async wallet scanner implementation using the Seraphis wallet lib.
    - When I pointed this async scanner on my local machine to a remote `monerod` instance @selsta spun up, I observed a **~40% speed-up in scanning** over the current wallet2 scanner.
    - Link to the draft PR that details all remaining TODO's in the PR description: https://github.com/UkoeHB/monero/pull/23
    - This CCS proposal will not be complete until I complete all major TODO's from the PR linked above, and deliver a final version of the async scanner PR for review.
  - Once I complete the async scanner, I plan to collaborate further with @jeffro256 @rbrunner7 @dangerousfreedom and the no-wallet-left-behind working group to work on whatever is next highest priority to get the Seraphis wallet lib ready for production.
- Continue work integrating [full chain membership proofs](https://github.com/kayabaNerve/full-chain-membership-proofs/) into the Seraphis library (and therefore demonstrate how to integrate them into the core Monero repo). The goal is to construct and verify Seraphis transactions using full chain membership proofs, including a suite of unit tests and benchmarks.
  - In my last CCS, I got an initial setup working to call full chain membership proof code written in Rust from a Monero repo C++ performance test. This was step 1-of-many toward the goal of constructing a full chain membership proof in a transaction using the Seraphis wallet lib.
- Miscellaneous Monero work, debug issues, review PR's.
  - Highest on my list right now is to review @vtnerd's p2p encryption implementation (source: https://github.com/monero-project/monero/pull/8996).

## Who

j-berman on github / jberman on matrix

Past CCS's:
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-5.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-4.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-3.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-2.html
- https://ccs.getmonero.org/proposals/j-berman-3-months-full-time.html

## Proposal

211 XMR

480 hours, 0.16 XMR/hr + $48/hr, $172/XMR from coingecko
