---
layout: fr
title: hinto-janai full-time work on Cuprate (3 months)
author: hinto-janai
date: August 9, 2024
amount: 221
milestones:
  - name: JSON RPC handlers
    funds: 40% (88.4)
    done:
    status: unfinished
  - name: Binary/other RPC handlers
    funds: 40% (88.4)
    done:
    status: unfinished
  - name: Other work
    funds: 20% (44.2)
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
[Cuprate](https://github.com/Cuprate/cuprate) is an alternative Monero node implementation.

The next section that needs work is the RPC handlers. The design, interface, routing, types, and (de)serialization were completed in my previous CCS, see here:
- Past CCS: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/456
- RPC interface tracking issue: https://github.com/Cuprate/cuprate/issues/183
- RPC book: https://architecture.cuprate.org/rpc/intro.html

This CCS is for the handlers, i.e. the functions that turn requests into responses.

Once the handlers are complete, Cuprate will have a working RPC stack that [mostly](https://architecture.cuprate.org/rpc/differences/intro.html) mirrors `monerod`.

## Who
I'm [hinto-janai](https://github.com/hinto-janai).

## RPC handlers
The 1st/2nd milestones are for the RPC handlers. This is the majority of the work.

This includes:
- JSON RPC handlers (methods behind `/json_rpc`)
- Binary RPC handlers (binary endpoints, e.g. `/get_blocks.bin`)
- Other handlers (other JSON endpoints, e.g. `/get_height`)

The RPC handlers will most likely be in its own library/section, built on-top of the RPC libraries Cuprate has so far. The current RPC interface library ([`cuprate-rpc-interface`](https://github.com/Cuprate/cuprate/tree/main/rpc/interface)) allows for custom handlers, as in, the mapping of `request` -> `response` can be customized. The handler created in this CCS will be a standard implementation that (mostly) follows `monerod`'s behavior, i.e. request comes in, get some data from the database and such, return a response. Although, other implementations are possible, such as an RPC handler that caches blocks, as mentioned in [this meeting](https://github.com/monero-project/meta/issues/996#issuecomment-2086710102).

Testing, [crate (library) documentation](https://doc.cuprate.org), and [architecture book](https://architecture.cuprate.org) sections will also be written.

### Binary strings
There are a few RPC methods that require further discussion before implementation in Cuprate, see the [binary strings proposal](https://github.com/monero-project/monero/issues/9422).

If the above proposal finds consensus on future `monerod` behavior, this CCS will implement that behavior.

If more time is required for the proposal, the related endpoints/methods will be left in a semi-unfinished state until behavior is agreed upon, where after Cuprate will implement that behavior.

If the proposal does not move forward, Cuprate is planning to fallback to implementing `monerod`'s current behavior.

## Other work
The 3rd milestone is for any miscellaneous work that needs to be done for Cuprate, but also, these 2 concrete things:
- Lints
- Benchmarking

I'd like to focus on these as:
- If they're always pushed to the side, they'll never get done
- I believe it's important to establish these early on in the project

I started integrating lints & benchmarks into Cuprate last CCS, this CCS will finish integrating them for all the libraries I've written so far, and [other libraries](https://architecture.cuprate.org/appendix/crates.html) if time allows.

The issues tracking the progress of these two can be found here:
- https://github.com/Cuprate/cuprate/issues/207 (lints)
- https://github.com/Cuprate/cuprate/issues/208 (benchmarks)

## Funding
I am asking for $65 + 0.05 XMR per hour for 480 hours at $158/XMR. This gives 221 XMR.
