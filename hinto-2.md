---
layout: cp
title: hinto-janai full-time work on Cuprate (3 months)
author: hinto-janai
date: May 5, 2024
amount: 264
milestones:
  - name: RPC server design
    funds: 20% (52.8)
    done: 5 June 2024
    status: finished
  - name: JSON RPC interface
    funds: 40% (105.6)
    done: 9 August 2024
    status: finished
  - name: Binary/other RPC interface + other work
    funds: 40% (105.6)
    done: 9 August 2024
    status: finished
payouts:
  - date: 18 June 2024
    amount: 52.8
  - date: 12 August 2024
    amount: 211.2
---

## What
[Cuprate](https://github.com/Cuprate/cuprate) is an alternative Monero node implementation, currently worked on by me and [Boog900](https://github.com/boog900).

The next large section that needs work is the RPC server. Another contributor, [yamabiiko](https://github.com/yamabiiko), is also interested in working on the RPC server, although they currently have limited time, so I'll be starting on it alone for now (with much help from Boog900).

## Who
I'm [hinto-janai](https://github.com/hinto-janai).

Past CCS: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/422.

## RPC server
yamabiiko has started a discussion on the design for the RPC server [here](https://github.com/Cuprate/cuprate/issues/106), and Boog900 has suggested some changes.

The first milestone's time will be spent on:
- Fleshing out the current proposal or potentially finding better alternatives
- Preparing an initial design document, similar to [`database/`](https://github.com/Cuprate/cuprate/pull/35)

The current design for the database was spread out across several months, although, the design for the RPC server should take much less time.

After a design is set, the second/third milestone will start on the RPC interface library - the timeline for this is by the end of this CCS. This includes testing, documentation, etc. The current plan is to separate the interface from the inner RPC handler. After the interface is finished, the internal handler(s) will be finished in another CCS (potentially split between contributors).

By the end of this CCS, the initial design document will be polished to reflect the implementation, similar to [here](https://github.com/Cuprate/cuprate/blob/main/database/README.md), and user documentation will also be finished (again, like `database/`).

The resulting design document will be added to [Cuprate's architecture book](#cuprates-architecture-book) (see below).

## Other work
There's also other work that I believe would be beneficial to start on earlier rather than later.

These will be started on during this CCS:

- Cuprate's architecture book
- Persistent transaction pool
- `monero-core` RPC PRs
- Benchmarking suite
- Project lints

The persistent transaction pool will be finished within this CCS, the rest will grow alongside the project.

### Cuprate's architecture book
This is a book similar to [Cuprate's protocol book](https://monero-book.cuprate.org), although it will be for Cuprate's implementation. The RPC design will be documented in this book (along with every other component) as they are implemented. The current [database document](https://github.com/Cuprate/cuprate/blob/main/database/README.md) will be ported to the book as well.

Current rough draft: https://hinto-janai.github.io/cuprate-architecture

Expected included items are:
- Relational map of components (RPC, DB, block downloader, verifier, etc)
- Component designs
- Thread model (when/where/how many threads get spawned? for what purpose?)
- Resource model (files, sockets, memory usage)
- Instrumentation (logging, data collection methods)
- Known inefficiencies/tradeoffs, their reasoning

### Persistent transaction pool
Considering RPC implementation will take a while, implementing a persistent transaction pool sooner rather than later would be preferred; another option Cuprate has is to create an in-memory only transaction pool, although this would only be a stop-gap and would take more work in the long run, thus this work will be done now.

### `monero-core` RPC PRs
As I'll be going through all of `monerod`'s RPC methods/objects and [`getmonero.org`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html) documentation, I will open PRs to `monero-core` or create an issue if I notice any discrepancies.

### Benchmarking suite
Creating a benchmarking suite for Cuprate's components would allow for collecting and storing information on code execution time. This data can be used later on to detect performance regressions as well as measuring optimizations.

Creating a bespoke benchmarking tool would be a project of its own, so Cuprate is planning to use the [Criterion](https://bheisler.github.io/criterion.rs/book/criterion_rs.html) project.

### Project lints
Lints cause compiler warnings to become hard errors, blocking compilation. An example: [`serai-dex`](https://github.com/serai-dex/serai/blob/21123590bb600323aa424f64ffaa5d321b1b22ed/Cargo.toml#L135-L184).

Cuprate's CI already fails on warnings (among other pedantic things), although there are many additional lints we could add. Selecting the lints that make sense for Cuprate sets higher code standards for the project. Setting this up and fixing current code should not take too much effort, but it will be drawn out over time.

## Funding
I am asking for a rate closer to market rates, please read [here](https://gist.github.com/hinto-janai/8ce1d4847f51304aa4d71c3614408d7f).

I am asking for $65 + 0.05 XMR per hour for 480 hours at $130/XMR. This gives 264 XMR.

Recent activity has shown that `monerod` does not handle load well. Furthermore, there is little system-level documentation; changes needed to fix issues like this are more difficult than necessary. I do not believe this has to be repeated.

I believe this is a fair rate for creating well documented and maintainable infrastructure. I am also asking for less hours than before as I don't believe I can continue at my current pace long-term.