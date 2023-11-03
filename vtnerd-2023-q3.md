---
layout: wip
title: vtnerd Full-Time 2023 Q3
author: Lee Clagett (vtnerd)
date: June 11, 2023
amount: 166.95 XMR
milestones:
  - name: Month 1 (160 hours)
    funds: 55 XMR
    done: 20 September 2023
    status: finished
  - name: Month 2 (320 hours)
    funds: 55 XMR
    done:
    status: unfinished
  - name: Month 3 (480 hours)
    funds: 56.95 XMR
    done:
    status: unfinished
payouts:
  - date: 3 November 2023
    amount: 55
  - date:
    amount:
  - date:
    amount:
---

3-Months full-time software development on monero "core" components in 2023 q3.

## What
Work primarily on the `monerod`, `wallet`, and `monero-lws`. Some of the work to be attempted or investigated:
  - Complete p2p Noise encryption (already in-progress)
  - Get new serialization routine merged (work on piecemeal PRs for reviewers sake)
  - Complete work necessary to merge [DANE/TLSA in wallet2/epee](https://github.com/vtnerd/monero/tree/improve/dane_tlsa).
  - Adding trust-on-first-use support to wallet2
  - Add msgpack support to monerod-ZMQ (requires merging of new serialization system)
  - `monero-lws` work:
    - Optional full chain verification for malicious daemon attack
    - Subaddresses
    - A accept-all-new-accounts mode similar to MyMonero behavior (instead of manually callback)
    - Webhook for new account creation (prevents polling for new accounts)
    - ZMQ pub support for incoming transactions and blocks (notifies of _any_ new transaction or block)
    - Create Github Actions that run unit-tests and provide binaries
    - Provide official LWS docker-image
    - Provide official snap/flatpak/appimge (tbd one or all of those)
    - Provide pre-built binaries
    - (Unlikely) - reproducible builds so community members can verify+sign the binary hashes

More than 3 months listed there, priorities may change as community requests or issues arise.

## Who

Lee Clagett (vtnerd). I've had [three](https://ccs.getmonero.org/proposals/vtnerd-tor-tx-broadcasting.html) [CCS](https://ccs.getmonero.org/proposals/vtnerd-2020-q4.html) [proposals](https://ccs.getmonero.org/proposals/vtnerd-2021-q1.html). The [full list of my monero PRs since last CCS](https://github.com/monero-project/monero/pulls?q=is%3Apr+author%3Avtnerd+created%3A%3E2021-02-17). I've also written a [msgpack implementation](https://github.com/vtnerd/monero-lws/pull/63) for the new serialization system (in Monero-LWS), an [admin REST](https://github.com/vtnerd/monero-lws/pull/62) api to Monero-LWS, as well as [webhooks for incoming transactions](https://github.com/vtnerd/monero-lws/pull/66) (including a [zero-confirmation](https://github.com/vtnerd/monero-lws/pull/72) for webhooks) (instead of the previously proposed ZMQ-PUB). [Unit tests](https://github.com/vtnerd/monero-lws/pull/53) were also finally added to Monero-LWS.

## Proposal

Work on the various tasks outlined above for 40 hours/week over the next 3 months after potential funding. I already use time-tracking software for work; if the hours dip in a given month unexpectedly, the update/milestone will be at the completion of the hours listed above.

The funds were calculated with 55 USD/hour with ~158.13 USD/XMR which is the 14-day exponential moving average on Kraken through 2023/07/02.
