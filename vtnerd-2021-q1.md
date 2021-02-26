---
layout: fr
title: vtnerd Full-Time 2021 Q1
author: Lee Clagett (vtnerd)
date: February 17, 2021
amount: 133.4 XMR
milestones:
  - name: Month 1 (160 hours)
    funds: 44 XMR
    done:
    status: unfinished
  - name: Month 2 (320 hours)
    funds: 44 XMR
    done:
    status: unfinished
  - name: Month 3 (480 hours)
    funds: 45.4 XMR
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

3-Months full-time software development on monero "core" components in 2021 q1 (through early q2).

## What
Work primarily on the `monerod`, `wallet2`, and `monero-lws` (pending feedback in comments). Some of the work to be attempted or investigated:

  - Complete work necessary to merge [DANE/TLSA in wallet2/epee](https://github.com/vtnerd/monero/tree/improve/dane_tlsa).
  - Adding trust-on-first-use support to wallet2 (already work in progress)
  - Progress on [my proposal to add encryption to p2p protocol](https://github.com/monero-project/monero/issues/7078) has been slow, but it looks like the consensus is FOR encryption, just no clear consensus on TLS 1.3 vs Noise protocol. Continued work would be design+implementation for the selected encryption technique.
  - Potential performance improvements:
    - Improve "cryptonote" read-serialization performance - helps with p2p block responses, RPC responses, among other things. Profiling suggests this could have big improvement on efficiency.
    - Determine a technique for safely returning `std::weak_ptr`/`std::shared_ptr` of p2p connections - this can help with efficiency in a few areas:
      - Remove lock acquire to send dandelion++ fluffs and I2P/Tor white noise
      - Remove lock acquire and atomic increment per connection when relaying bocks (a list is already obtained)
      - Others? Any `foreach_connection` call that can be safely done concurrently can use this technique
    - Various epee/p2p serialization (output) routines (carryover from q4, this is difficult to update)
  - Potential compilation improvements (carryover from q4 since mj-xmr has focused on this more):
    - Moving serialization code to cpp (although this could be spurious in updates which is frowned upon)
    - Dropping the templated nature of the epee TCP server would yield best improvement, but might be cause too much "pain" in the review
  - `monero-lws` work (assuming no complaints in comments):
    - Provide pre-built binaries
    - Add support for immediate mempool scanning (via ZMQ-PUB)
    - (Unlikely this quarter) - reproducible builds so community members can verify+sign the binary hashes

More than 3 months listed there, priorities may change as community requests or issues arise.

## Who

Lee Clagett (vtnerd). I've had [two](https://ccs.getmonero.org/proposals/vtnerd-tor-tx-broadcasting.html) [CCS](https://ccs.getmonero.org/proposals/vtnerd-2020-q4.html) proposals. The [full list of my PRs for last quarter CCS](https://github.com/monero-project/monero/pulls?q=is%3Apr+author%3Avtnerd+created%3A%3E2020-10-27). There's also some investigation/writeup for encrypted p2p, and investigations to improve efficiency (logging in particular) that aren't in that list since any code is still a crude mashup for quick testing. A working, but still in progress [DANE/TLSA wallet implementation](https://github.com/vtnerd/monero/tree/improve/dane_tlsa) also exists.

Bigger higlights: [improved serialization performance to epee binary](https://github.com/monero-project/monero/pull/7009), [removed copy of all outgoing p2p messages and duplicate copies of p2p block notify messages (not merged)](https://github.com/monero-project/monero/pull/7136), [changed p2p connection list to `std::weak_ptr` for small efficiency improvement and code clarity (not merged)](https://github.com/monero-project/monero/pull/7345), [improved `byte_stream` alllocation efficiency](https://github.com/monero-project/monero/pull/7003), [added `byte_stream` realloc to reduce memory usage after new reallocation strategy (not merged)](https://github.com/monero-project/monero/pull/7005), and [fixed timeout bug in Dandelion++](https://github.com/monero-project/monero/pull/7021).

## Proposal

Work on the various tasks outlined above for 40 hours/week over the next 3 months after potential funding. I already use time-tracking software for work; if the hours dip in a given month unexpectedly, the update/milestone will be at the completion of the hours listed above.

The funds were calculated with 55 USD/hour with ~197.85 USD/XMR which is the 14-day exponential moving average on Kraken through 2021/02/16.
