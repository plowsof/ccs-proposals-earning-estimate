---
layout: fr
title: j-berman full-time development (3 months)
author: j-berman
date: November 21, 2022
amount: 253 Monero
milestones:
  - name: Month 1
    funds: 33% (84.3 Monero)
    done:
    status: unfinished
  - name: Month 2
    funds: 33% (84.3 Monero)
    done:
    status: unfinished
  - name: Month 3
    funds: 33% (84.3 Monero)
    done:
    status: unfinished
payouts:
  - date:
    amount:
---

## What

Continue full-time another 3 months in a similar capacity:

- Prioritize debugging any significant issues that arise, such as [daemon connection issues](https://github.com/monero-project/monero/issues/8520#issuecomment-1310975634), [zmq missing publishing txs submitted to the daemon](https://github.com/monero-project/monero/pull/8427), [recovering multisig wallets from seed](https://github.com/monero-project/monero/issues/8537#issuecomment-1233946415), etc.
- Complete work stress testing how daemons handle a transaction pool under heavy load to both gauge daemon performance, and to help get [PR 8076 - reduce wallet round trips to the daemon](https://github.com/monero-project/monero/pull/8076) across the finish line after gauging its impact on pool processing performance.
  - The day leading up to the hard fork this summer, the transaction pool experienced heavier load than usual. Daemons that saw heavy traffic reported issues serving RPC requests. I would like to dig deeper into this.
- Start working through Seraphis and Jamtis wallet tasks piecemeal, picking up collaboration with @koe, @rbrunner7, and @dangerousfreedom. The first task I've gotten a handle on and have a decently fleshed out view of what work is needed is input selection. I intend to get @koe's naive input selection implementation to production-ready, ensuring it functions as close to the wallet does today. From @koe [here](https://github.com/seraphis-migration/wallet3/issues/8#issue-1368934355): "a real implementation needs many more mechanisms and heuristics (e.g. filter for dust threshold to ignore, filter for origin statuses to permit, randomization and spread to mitigate timing analysis)"
  - The general plan with Seraphis/Jamtis is to start fresh with new wallet code that avoids the complexity and pitfalls of `wallet2.cpp`, which at the moment is a source of growing technical debt (discussed a bit [here](https://github.com/monero-project/monero/issues/8157)). Considering Seraphis and Jamtis would bring a number of changes to core wallet features (a new address scheme, new balance recovery algorithm, new fee calculation, etc.), the proposed plan currently on the table is to start fresh rather than factor the existing `wallet2.cpp`. Many of the features that users already expect (such as sweeps, tx key recovery, watch-only wallets, etc.) would be maintained, or improved where possible. The implementation of some existing features is still up for discussion, such as [accounts](https://github.com/seraphis-migration/wallet3/issues/21).
  - I'd like to reiterate this point: Seraphis and Jamtis still need to undergo stringent review both from the community and by independent 3rd parties. At this time, @koe is still working on the technical paper describing the protocol in its current iteration, which will need to undergo review in the future. Further, feedback on the core feature changes is still strongly encouraged and desired.
- Review PR's.

## Who

I've identified and patched several privacy issues with varying severity in the Monero ecosystem:

1. The reference wallet's decoy selection algorithm didn't select very recent spendable outputs in some cases. ([source](https://www.getmonero.org/2021/09/20/post-mortem-of-decoy-selection-bugs.html))
2. The reference wallet truncated integers in the decoy selection algorithm, which would have borked the decoy selection algorithm entirely if tx volume were to increase; in the normal case, it marginally weakened the algorithm. ([source](https://www.getmonero.org/2021/09/20/post-mortem-of-decoy-selection-bugs.html))
3. `openmonero` was still using the old proven weak decoy selection algorithm, also leaving a fingerprintable trail by decoy selection algo. ([source](https://github.com/moneroexamples/openmonero/pull/177))
4. MyMonero didn't use the updated CLSAG fee calculation which fingerprinted MyMonero txs on chain by tx fee. ([source](https://github.com/mymonero/mymonero-core-cpp/pull/35))
5. MyMonero's fee calculation->input selection logic differed ever-so-slightly from the reference wallet, resulting in a fingerprintable tx fee. ([source](https://github.com/mymonero/mymonero-core-cpp/pull/36))
6. `monero-lws` fee masking on the server caused ever-so-slightly different fee calculations from the reference wallet, resulting in a fee fingerprintable to `monero-lws` (a fingerprint distinct from MyMonero). ([source](https://github.com/vtnerd/monero-lws/pull/31))
7. In PR review on the latest hard fork's changes to the tx fee, identified the introduction of [slightly different fee calculation logic](https://github.com/monero-project/monero/pull/7819#discussion_r804404285) that would have caused tx fees to be fingerprintable to either old or new version until the hard fork.

Other contributions:

- Implemented [view tags](https://github.com/monero-project/monero/pull/8061) to speed up wallet scanning.
- Implemented [background sync](https://github.com/monero-project/monero/pull/8619) initially proposed by @hyc so that wallets can scan for transactions in the background when the user is not active, without the spend key loaded in memory.
- Identified and patched daemon reliability issues (moved forward solving issues [8520](https://github.com/monero-project/monero/issues/8520), [6631](https://github.com/monero-project/monero/issues/6631), [6929](https://github.com/monero-project/monero/issues/6929), and [6938](https://github.com/monero-project/monero/issues/6938)):
	- [Tor/i2p daemons periodically send a peer list that gets itself dropped](https://github.com/monero-project/monero/pull/8324).
	- [The daemon periodically drops outgoing tor/i2p connections](https://github.com/monero-project/monero/pull/8330).
	- [Tx re-relay math was off](https://github.com/monero-project/monero/pull/8326).
- Implemented the changes needed for Ledgers to function for the latest hard fork:
	- [monero repo](https://github.com/j-berman/monero/commit/cfbd590fd63ff9e0c5ec68c618e2f3fdaf24d241)
	- [ledger repo](https://github.com/j-berman/app-monero/commit/c1a6eb8bbbc1cc7974ce0938e9d8f920d0ad3ae9)

Prior CCS proposals:
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-3.html
- https://ccs.getmonero.org/proposals/j-berman-3months-full-time-2.html
- https://ccs.getmonero.org/proposals/j-berman-3-months-full-time.html

## Proposal

253 XMR. 480 hours, 0.16 XMR/hr + $48/hr, $131/XMR from coingecko.

I'm requesting a raise from my prior CCS because I feel I have continued to demonstrate my work is worth a competitive market rate.
