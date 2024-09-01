---
layout: wip
title: vtnerd full-time 2024 q3
author: Lee Clagett (vtnerd)
date: July 11, 2024
amount: 208.12 XMR
milestones:
  - name: Month 1 (160 hours)
    funds: 69 XMR
    done: 24 August 2024
    status: finished
  - name: Month 2 (320 hours)
    funds: 69 XMR
    done:
    status: unfinished
  - name: Month 3 (480 hours)
    funds: 70.12
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

3-Months full-time software development on monero "core" components in 2024 q3.

## What
Work primarily on the `monerod`, `wallet`, and `monero-lws`. Some of the work to be attempted or investigated:
  - Code reviews of monero core PRs
  - Optimization work in monero core (work with the new stressnet team)
  - Add socks5 support to wallet and monerod (which adds IPv6 support to proxies)
  - Add support for [torspec/control-spec](https://github.com/torproject/torspec/blob/main/control-spec.txt). This is similar to the SAM proposal for I2P
  - Get new serialization routine merged (continue work on piecemeal PRs for reviewers sake)
  - Complete work necessary to merge [DANE/TLSA in wallet2/epee](https://github.com/vtnerd/monero/tree/improve/dane_tlsa).
  - Adding trust-on-first-use support to wallet2
  - Add msgpack support to monerod-ZMQ (requires merging of new serialization system)
  - `monero-lws` work:
    - Complete LWS frontend (using `wallet_api.h` as interface) so that wallets can begin using LWS API easily. This is separate from woodser et al working on LWS API within `wallet2` which may be deprecated.
    - Perform apache-benchmark test on REST api to determine effects of blocking ZMQ calls
    - Cache some ZMQ calls performed during REST api responses to reduce burden on `monerod` and improve REST throughput
    - Add concurrency to REST API responses - remove blocking ZMQ calls which starve valuable REST thread resources
      - A switchover to boost asio/beast/azmq from epee/zmq to handle async http responses will be needed
      - `get_random_outs` endpoint has blocking ZMQ calls that cannot be cached, thus the potential need for async-zmq
    - Add a "scale" factor to remote scanning load balancing - send more accounts to systems with faster single thread performance 
    - Add 64-bit ed25519 code for faster arm64 scanning
    - Provide official LWS docker-image
    - Provide pre-built binaries
    - (Unlikely) - reproducible builds so community members can verify+sign the binary hashes

There is intentionally more work than time allows - to ensure there is always something to work on in the proposal.

## Who

Lee Clagett (vtnerd). I've had [four](https://ccs.getmonero.org/proposals/vtnerd-tor-tx-broadcasting.html) [CCS](https://ccs.getmonero.org/proposals/vtnerd-2020-q4.html) [proposals](https://ccs.getmonero.org/proposals/vtnerd-2021-q1.html) ([last one](https://ccs.getmonero.org/proposals/vtnerd-2023-q3.html)), and [one Magic Grant](https://monerofund.org/projects/Q1Q2_2024_dev_vtnerd).

Some of my biggest features in monero core repo are [Dandelion++](https://github.com/monero-project/monero/pull/6314), [adding supercop ASM speedups to wallet code](https://github.com/monero-project/monero/pull/6337), [ZeroMQ Pub Support for new blocks and transactions](https://github.com/monero-project/monero/pull/6418), and [SSL support to p2p](https://github.com/monero-project/monero/pull/8996).

I've also made a functional LWS wallet scanner under CCS/Magic - which now has a MyMonero compatible REST API, admin REST API, LMDB storage, subaddress support, webhook/zmq/rmq publishing (new receives, spends, and accounts), multi-machine scanning with (primitive) load-balancing, and an untrusted daemon mode that verifies PoW is valid (whereas normal wallets trust `monerod` responses entirely).

## Proposal

Work on the various tasks outlined above for 40 hours/week over the next 3 months after potential funding. I already use time-tracking software for work; if the hours dip in a given month unexpectedly, the update/milestone will be at the completion of the hours listed above.

The funds were calculated with 65 USD/hour with ~157.41 USD/XMR which is the 9-day exponential moving average on Kraken through 2024/07/11. The rate is up a bit: (1) inflation, (2) volatility protection, and (3) closer in hourly compensation to 2 other contributors.