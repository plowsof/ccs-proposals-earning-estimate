---
layout: wip
title:  Boog900 full time work on Cuprate (3 months)
author: Boog900
date: June 28, 2024
amount: 215
milestones:
  - name: Month 1
    funds: 71 XMR
    done:
    status: unfinished
  - name: Month 2
    funds: 72 XMR
    done:
    status: unfinished
  - name: Month 3
    funds: 72 XMR
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

This proposal is to continue my work on [Cuprate](https://github.com/Cuprate/cuprate).

# Who

I am [Boog900](https://github.com/Boog900), you can see my last CCS [here](https://ccs.getmonero.org/proposals/boog_3_months_cuprate.html).

# What

Cuprate is very close to having an alpha binary ready. During my last CCS I created a test binary with the components
we currently have to test a full sync, a full sync with this binary wasn't achieved due to a few issues discovered, which have since
been fixed, however timings up to the height (~2,300,000) we did reach are promising for Cuprate's performance.

This proposal will be for 3 months work on Cuprate while continuing coordination of the Cuprate project and also being an active maintainer
for monero-rs.

My main plan is to work towards what is needed to achieve a working alpha binary that can sync, stay synchronized, handle reorgs and
participate in transaction propagation. 

This will include:

### Blockchain service

The blockchain service is what will keep the blockchain's state, handle incoming blocks, decide when to re-org, etc. It will use
the consensus and database services created in previous CCS proposals (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/405 & https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/422).

### Tx Pool

The transactions in the txpool will be stored in a separate database from where the blockchain is stored, using the same database abstraction. 
I will work on the txpool tables and the service that will handle txpool requests from other parts of Cuprate.

Hinto, as apart of their CCS, has already began work here. Although Hinto's CCS includes a small note about completing the persistent transaction 
pool: `The persistent transaction pool will be finished within this CCS`, I will be taking over from where hinto has left off as the exact 
transactions pool tables are yet to be decided and the transaction pool service is heavily tied in to other areas I will be working on. 

### Peer Protocol Request Handler

The peer protocol request handler is what is given to `cuprate-p2p`, it is used to handle requests for blocks/transactions and other chain data.
In our test binary I created a mock request handler that just doesn't respond to requests, this lead to pretty unstable connections, with the other
components here though I will be able to create a working request handler.

### Other Tasks

There are other smaller things that need to be worked on for Cuprate to be ready for an alpha binary, mainly bug fixes and leftover TODOs.

# Milestones

Unlike my previous CCS proposals, I am basing milestones on hours worked instead of completed work. 

There are a few reasons for this. The exact work needed is likely to change as we get closer to an alpha binary, for example, bugs that need
fixing may come up. It also brings the proposal closer to the average full-time developer proposal.

Although doing milestones based on time requires more trust, we are doing weekly [Cuprate meetings](https://github.com/monero-project/meta/issues/1028) 
where I am, and will be reporting progress.

# Funding

I am asking for $55/hr for 50 hrs/week for 3 months at $166/XMR. This gives 215 XMR.

This is a raise over my last CCS ($45 -> $55), I believe this is justified given my past work.  
