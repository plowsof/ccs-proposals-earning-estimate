---
layout: wip
title: j-berman full-time development (3 months)
author: j-berman
date: May 2, 2024
amount:  376 Monero
milestones:
  - name: Month 1
    funds: 33% (125.3 Monero)
    done:
    status: unfinished
  - name: Month 2
    funds: 33% (125.3 Monero)
    done:
    status: unfinished
  - name: Month 3
    funds: 33% (125.4 Monero)
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

Work full-time 3 months on:

- Integrating [full-chain-membership proofs](https://ccs.getmonero.org/proposals/fcmp++-development.html) into Monero under RingCT.
  - As part of this CCS, I will submit PR's to the core Monero repository that do the following:
    - Implements the tree in C++ described in section 6.1 ([paper](https://github.com/kayabaNerve/fcmp-ringct/blob/develop/fcmp%2B%2B.pdf), [reference commit](https://github.com/kayabaNerve/fcmp-ringct/blob/221e8c0e155d5fe526080c6e56c6418e0433177d/fcmp%2B%2B.pdf))
      - Implements the `grow` and `trim` algorithms (sections 6.1.1 and 6.1.2)
    - Implements tree initialization with existing cryptonote outputs on boot (section 6.2.1)
    - Implements growing the tree as the node syncs (section 6.2.2 and 6.2.3)
    - Implements the transaction class containing FCMP's (part of sections 6.3 - 6.6)
      - I will probably extend `cryptonote::transaction` to do this.
  - The following tasks from the rest of section 6 are necessary to complete the integration; I'm happy to divide and conquer if someone wants to work on this as well:
    - Implement transaction construction with FCMP's (sections 6.3 - 6.6)
      - A pre-requisite for this is implementing the transaction class above.
    - Implement transaction verification (section 6.7)
    - Implement RPC route to return a path for outputs (section 6.9)
    - Implement unifying the distribution of {coinbase, pre-RCT, RCT} outputs and use it to select decoys paths (section 6.10)
    - Implement changes for multisig (section 6.11)
- Continuing Seraphis wallet library work.
  - My next task on this front is to bring the Serpahis lib async scanner into the current wallet API.
    - To be clear, this is not implementing the Seraphis upgrade; it is bringing the Seraphis wallet **library**, which supports scanning today's blockchain, into the core Monero repository. This would speed up wallet scanning **today**, and is part of an effort to deprecate wallet2 and its technical debt, and replace it with the Seraphis lib ([source](https://github.com/seraphis-migration/wallet3/issues/64#issuecomment-2067030930)).
    - The async scanner is currently under review ([source](https://github.com/UkoeHB/monero/pull/23))
    - In the latest round of benchmarks, I observed scanning speed-ups of 50-60% with a clearnet remote node, 40-45% with a tor node, 25-35% with a local node, all running the **current chain** (not Seraphis).
    - To be usable in the wallet API today, the following still needs to be implemented (I'm also happy to divide and conquer here):
      - Pre-RCT index handling (needs [source](https://github.com/UkoeHB/monero/pull/23))
      - A mutable subaddress lookahead ([source](https://github.com/UkoeHB/monero/pull/23#issuecomment-2036086371))
      - Pool scanning ([source](https://github.com/UkoeHB/monero/issues/41))
      - A clean way to save tx metadata ([source](https://github.com/UkoeHB/monero/issues/48))
- Complete p2p SSL review ([source](https://github.com/monero-project/monero/pull/8996)).
- Misc. review, debugging, etc.

## Who

j-berman on github / jberman on matrix / IRC

Past CCS's:
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-6.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-5.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-4.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-3.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-2.html
- https://ccs.getmonero.org/proposals/j-berman-3-months-full-time.html

## Proposal

376 XMR

480 hours, 0.25 XMR/hr + $65/hr, $122/XMR from coingecko

I'm requesting a siginificant raise from my past CCS (0.16 XMR/hr -> 0.25 XMR/hr, $48/hr -> $65/hr) because I believe I have demonstrated improved performance, and believe the recent donations to CCS proposals demonstrate the community is capable of paying strong Monero contributors market / above-market rates. I believe paying market / above-market rates for strong contributors is a stronger strategy for Monero to attract and retain strong talent.
