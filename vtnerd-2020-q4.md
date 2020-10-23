---
layout: fr
title: vtnerd Full-Time 2020 Q4
author: Lee Clagett (vtnerd)
date: October 15, 2020
amount: 224.6 XMR
milestones:
  - name: Month 1 (160 hours)
    funds: 74 XMR
    done:
    status: unfinished
  - name: Month 2 (320 hours)
    funds: 74 XMR
    done:
    status: unfinished
  - name: Month 3 (480 hours)
    funds: 76.6 XMR
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

3-Months full-time software development on monero "core" components in 2020 q4 (through early 2021).

## What
Work primarily on the `monerod` and `wallet2` base code (perhaps some `monero-lws` as well, provided supporters find this acceptable). Some of the work to be attempted or investigated:

  - Adding DANE support to wallet2/epee SSL (unbound->OpenSSL 1.1) to enhance wallet->monerod security. This allows for SSL without root certificate signing (relies on dnssec, which unfortunately has its own root+zone certificate chain). Also allows for "pinning" to a specific CA (so root CA + dnssec check).
  - Adding trust-on-first-use support to wallet2 if DANE and CA are unavailable
  - TLS certificate sharing for public RPC nodes. Possible to "piggy-back" on curve25519 keys for p2p stuff (see next point).
  - Adding encryption+authentication to p2p connections. I have a proposal written (separate CCS entirely?) for either TLS 1.3 or Noise_XK depending on community goals. The proposal is unique from prior attempts because it attempts to authenticate the connection.
  - Pontential performance improvements
    - Various epee/p2p serialization (output) routines (some examples, will need more profiling):
      - Improve container reading/writing in epee serialization
      - Switching from `std::ostringstream` in the binary output to direct byte slice output
      - Adding `byte_slice` internally so that binary values copy pointers instead of data
    - Improvements to "cryptonote" serialization - risky since its used by blocks+transactions internally, but theres much speed to be gained in that code
  - Potential compilation improvements:
    - Moving some epee stuff from headers into cpp to reduce includes as performance is being modified
    - Moving serialization code to cpp (although this could be spurious in updates which is frowned upon)
    - Dropping unnecessary includes from epee and few other core files. `boost::lexical_cast` is a top candidate for instance
    - Dropping the templated nature of the epee TCP server would yield best improvement, but might be cause too much "pain" in the review

There's quite a lot listed there, and its unlikely that all bulletpoints will be reached. There should be enough work in a 3month period though.

## Who

Lee Clagett (vtnerd). I have a prior [CCS](https://ccs.getmonero.org/proposals/vtnerd-tor-tx-broadcasting.html) for adding I2P/Tor support to the wallet and daemon which is completed, pending community members adding seed nodes for I2P/Tor. I also implemented Dandelion++, ZeroMQ Pub/Sub in daemon, various performance improvements to ZeroMQ JSON, [monero-lws](https://github.com/vtnerd/monero-lws), [x86-64 ASM speedups for wallet scanning](https://github.com/monero-project/supercop), and other assorted daemon bug fixes or changes.

## Proposal

Work on the various tasks outlined above for 40 hours/week over the next 3 months after potential funding. I already use time-tracking software for work; if the hours dip in a given month unexpectedly, the update/milestone will be at the completion of the hours listed above.

The funds were calculated with 55 USD/hour with ~117.55 USD/XMR which is the 14-day exponential moving average on Kraken through 2020/10/14.