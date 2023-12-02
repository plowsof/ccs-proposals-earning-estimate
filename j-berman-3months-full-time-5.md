---
layout: cp
title: j-berman full-time development (3 months)
author: j-berman
date: July 26, 2023
amount: 216 Monero
milestones:
  - name: Month 1
    funds: 33% (72 Monero)
    done: 21 September 2023
    status: finished
  - name: Month 2
    funds: 33% (72 Monero)
    done: 19 October 2023
    status: finished
  - name: Month 3
    funds: 33% (72 Monero)
    done: 18 November 2023
    status: finished
payouts:
  - date: 8 November 2023
    amount: 72
  - date: 2 December 2023
    amount: 144
---

## What

Work full-time 3 months on:

- Continuing Seraphis wallet library work.
  - My next task is to complete an async wallet scanner implementation using the Seraphis wallet lib that points to `monerod`.
    - I have a working implementation that can be tested as described [here](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/359#note_21276).
    - When I point this async scanner on my local machine to a remote `monerod` instance @selsta spun up, I observe a **~40% speed-up in scanning** over the current wallet2 scanner.
    - The bulk of the remaining work to get it to PR-ready includes:
      - Explore replacing the existing epee http client lib with a widely used http client lib like libcurl. This avoids needing to rewrite the epee http client lib to safely handle concurrent network requests.
      - Code cleaning/factoring.
      - Unit tests.
  - Once I complete the async scanner, I plan to collaborate with @dangerousfreedom @rbrunner7 and the no-wallet-left-behind working group to work on whatever is next highest priority to get the Seraphis wallet lib ready for production.
- Integrating [full chain membership proofs](https://github.com/kayabaNerve/full-chain-membership-proofs/) into the Seraphis library (and therefore demonstrate how to integrate them into the core Monero repo). The goal is to construct and verify Seraphis transactions using full chain membership proofs, including a suite of unit tests and benchmarks.
  - In my view, before Monero could actually consider accepting a PR for full chain membership proofs, there is a large amount of work still needed to prove its security and to land on a ready-for-production design. That work is currently proceeding in parallel. I would personally like to proceed with the above implementation work to maximize certainty that the Seraphis upgrade path is compatible with reasonably efficient full chain membership proofs.
- Miscellaneous Monero work, debug issues, review PR's.

## Who

j-berman on github / jberman on matrix

Past CCS's:
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-4.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-3.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-2.html
- https://ccs.getmonero.org/proposals/j-berman-3-months-full-time.html

## Proposal

216 XMR

480 hours, 0.16 XMR/hr + $48/hr, $166/XMR from coingecko
