---
layout: fr
title: j-berman full-time development (3 months)
author: j-berman
date: August 26, 2024
amount:  317 Monero
milestones:
  - name: Month 1
    funds: 33% (105 Monero)
    done:
    status: unfinished
  - name: Month 2
    funds: 33% (106 Monero)
    done:
    status: unfinished
  - name: Month 3
    funds: 33% (106 Monero)
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

- Integrating full-chain membership proofs++ into Monero under RingCT.
  - As part of this CCS, I will prioritize and guarantee completion of the following in this PR: https://github.com/monero-project/monero/pull/9436
    1. Trim the tree on reorgs and when popping blocks.
    2. Key image migration.
    3. Optimize tree building where possible.
        - Multithreaded output conversion to leaves.
        - Multithreaded hashing.
        - Batched inversion.
    4. Construct fcmp++ transactions.
        - I anticipate updating `cryptonote::construct_tx_and_get_tx_key` for this, and not touching wallet2 in this proposal.
        - By the end of this proposal, there will be a modular function wallets can use to construct fcmp++ txs, but I may not have an end-to-end functioning wallet that can construct fcmp++ txs implemented by the end of this proposal.
    5. Verify fcmp++ transactions.
    6. Consensus changes for fcmp++.
        - New unlock time logic.
        - Allowing new fcmp++ RCT type.
        - Implement a grace period for current tx types in the pool at the fork to make it into the chain.
        - Misc. necessary changes.
  - Work together with @dangerousfreedom on full wallet scanning.
  - The remaining integration tasks that I would also work on if time permits and someone else doesn't:
    - Construct fcmp++ transactions in a fully functional wallet.
      - Pre-requisites: modular function to construct fcmp++ transactions and full wallet scanning.
    - Implement the RPC route for light wallets to query for paths in the curve trees tree.
    - Wallet changes for background syncing.
    - Multisig.
- Continuing Seraphis wallet library work.
  - Making it clear up front: I anticipate not making much progress on the Seraphis wallet library work in this CCS. I plan to prioritize fcmp++. If time permits, I would work on bringing the Seraphis wallet library to production.
  - To be clear, working on the Seraphis wallet library is not implementing the Seraphis upgrade; it is bringing the Seraphis wallet library, which supports scanning today's blockchain, into the core Monero repository. This would speed up wallet scanning today, and is part of an effort to deprecate wallet2 and its technical debt, and replace it with the Seraphis lib ([source](https://github.com/seraphis-migration/wallet3/issues/64#issuecomment-2067030930)).
  - Next I plan to resolve merge conflicts in the current open PR's, and open all piecemeal PR's to the core Monero release branch to prepare Monero daemons/wallets and reduce the size and scope of the async scanner PR.
- Misc. review, debugging, etc.

## Who

j-berman on github / jberman on matrix / IRC

Past CCS's:
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-7.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-6.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-5.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-4.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-3.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-2.html
- https://ccs.getmonero.org/proposals/j-berman-3-months-full-time.html

## Proposal

317 XMR

480 hours, 0.25 XMR/hr + $65/hr, $158/XMR from coingecko
