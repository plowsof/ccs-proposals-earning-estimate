---
layout: fr
title: hinto-janai full-time work on Cuprate (3 months)
author: hinto-janai
date: Nov 6, 2023
amount: 153
milestones:
  - name: Internals
    funds: 33% (51)
    done:
    status: unfinished
  - name: API
    funds: 33% (51)
    done:
    status: unfinished
  - name: Integration + 3 months of work
    funds: 33% (51)
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
[Cuprate](https://github.com/Cuprate/cuprate) is an alternative Monero node implementation, currently solely worked on by [Boog900](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/405).

I've been in contact with Boog and there are many sections within Cuprate that can be worked on in parallel, currently the most pressing section is the database. This work was left unfinished by SyntheticBird45 before they left the project. Boog is currently working on block downloading/verification/consensus with cobbled together database-like functions - this means an actual database layer can be worked on in parallel without any merge conflicts, and can be cleanly slotted in once complete.

This CCS is to support me working on full-time on Cuprate for the next 3 months, specifically on the database implementation.

## Benefitting Monero
This CCS will fund part of a larger effort to create an alternative Monero node implementation (among other things).

As such, things will initially be slow-going as groundwork is laid. This CCS specifically may not _directly_ benefit `monero-core` immediately, yet it's work that must be completed such that Cuprate _can_ benefit `monero-core` (and Monero) in the future.

## Who
I'm [hinto-janai](https://github.com/hinto-janai).

Past CCS: https://ccs.getmonero.org/proposals/gupax.html.

## Design
The design document and active PR is here: https://github.com/Cuprate/cuprate/pull/35 and will be updated as things change.

The main goal is to create a layer that separates the underlying database and the higher-level functions that are called by the other portions of Cuprate, e.g, `get_block()`. The aim here is to allow for easy hot-swapping of databases to test for the various operations Cuprate will be performing. In the end, a single database will be selected after testing, although the layer will continue to exist. 

The database implementations in mind (for now) include:
- LMDB (via [heed](https://github.com/meilisearch/heed))
- [sanakirja](https://docs.rs/sanakirja) (a database [similar and originally based off](https://pijul.org/posts/2021-02-06-rethinking-sanakirja) LMDB)

Both of these will be forked and maintained by Cuprate as there are `monerod`-specific things that must be added (e.g output lookup using [sub-keys](https://github.com/monero-project/monero/blob/ac02af92867590ca80b2779a7bbeafa99ff94dcb/src/blockchain_db/lmdb/db_lmdb.cpp#L3447C1-L3449C80)).

The overall design is mostly from Boog900 - I am simply implementing it.

## Future
There's plenty more work to be done after the database. Boog plans on handling P2P code after his current CCS, which means I could possibly work on these things in the future (in parallel with Boog's work):

- RPC server (e.g. `get_info`)
- Transaction-pool related (e.g. Dandelion++)
- Application interface linking everything together (e.g. `./cuprated --option`)

Most likely, the RPC server would be the next thing I would be working on.

And there are things that are planned, but for the very distant future:
- ZMQ support
- Tor/i2p support: [Tor is quite feasible today](https://blog.torproject.org/announcing-arti), i2p less so
- RandomX: Currently, there exists multiple (quite rough) `C/C++ <-> Rust` bindings but as RandomX is in active use (and will most likely be for the foreseeable future) another implementation or more realistically, a maintained "Rust"-like shim on-top would be nice
- CryptoNight: Same as RandomX but less important as this is only used for legacy purposes
- P2P encryption (preferably compatible with the proposal for [`monerod`](https://github.com/monero-project/monero/issues/7078))

These points are laid out to showcase what else must/could be done for Cuprate to reach some level of parity with `monerod`.

## Why
Cuprate has an advantage in that it has an [8+ year old codebase](https://github.com/monero-project/monero) as reference - although we are starting with a blank canvas, we have a finished painting next to us, displaying all the very good, okay, and not-so-good parts.

As such, we can focus on things other than making it work, notably: documentation, maintenance, and correctness.

Other than documenting the [Monero protocol itself](https://monero-book.cuprate.org), we plan to write documentation for internal subsystems such that future Cuprate contributors/maintainers will be able to pick up easily where we left off. What this means for me and this CCS is that I'll be documenting how this database "layer" fits in with the rest of Cuprate, and answer all the "what does this do?", "how does this work?", "why was it done like this?" questions. If I were to continue working on Cuprate past this CCS, i.e. the RPC server, all RPC types would also be documented (and the internals as well) - the same goes for any future subsystems.

Other notable projects following this pattern: [Tor](https://youtu.be/hdFL0kXu440?t=700), [Bitcoin](https://github.com/rust-bitcoin/rust-bitcoin), [Ethereum](https://github.com/rust-ethereum), [Zcash](https://github.com/ZcashFoundation/zebra).


## Proposal
I propose to work for 44 hours/week for 3 months.

By the end of this proposal, Cuprate will have a working database. I believe 3 months is enough time to create and refine an implementation enough for usage.

It is hard to separate large single implementations like this cleanly into goals/timeframes as usually many things get worked on at any given moment - although, there are 3 bigger milestones this CCS has:

1. Internals: implementing the database and functions themselves
2. API: cleanup of the interface and many other miscellaneous things for external usage
3. Integration: slotting the database into Cuprate, and at least 3 months of work

Milestone 3 is only to be paid out upon:
- A complete database has been integrated into Cuprate
- 3 months of work has been done

This means if the database takes 428~ hours to complete, I will continue to work for 100~ more hours (most likely on the things listed in `Future`) to complete milestone 3.

- Hours: 528
- Rate: $45 USD/hour
- XMR: $155 (20-day EMA, Kraken, 2024/01/15)
- Total: 153 XMR
