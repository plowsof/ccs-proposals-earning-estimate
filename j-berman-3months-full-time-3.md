---
layout: fr
title: j-berman full-time development (3 months)
author: j-berman
date: July 18, 2022
amount: 187.5 Monero
milestones:
  - name: Month 1
    funds: 33% (62.5 Monero)
    done:
    status: unfinished
  - name: Month 2
    funds: 33% (62.5 Monero)
    done:
    status: unfinished
  - name: Month 3
    funds: 33% (62.5 Monero)
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

I'd like to continue full-time another 3 months in a similar capacity:

- Continue with PR review (especially on larger time-intensive PR's), including wrapping up [8076](https://github.com/monero-project/monero/pull/8076) (reduce wallet load and refresh time).
- Patch bugs.
- Finish the background sync mode that enables scanning for txs without a spend key. My code is [here](https://github.com/j-berman/monero/commit/238ea538f218ad447808c6806386a73bb1ab0fd5) and is functional as is. I approached it cautiously and thoughtfully to ensure it's safe as I went along. I still have some final touches on it + tests to add to wrap it up, [described here](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/285#note_15356).
- Potential tasks:
	- Start going deeply through Seraphis code, implementing Jamtis features, and working toward completing a handoff from UkoeHB -> core repo. [From @UkoeHB](https://libera.monerologs.net/monero-research-lab/20220713#c120001): "Todos after [he finishes his final poc tasks]: investigate/implement the wallet-side features of Jamtis (RIDs, Polyseed, address authentication), build wallets that use the seraphis library interface for building/handling txs and enotes (full wallet, view-only wallet, multisig full wallet, payment validator), integrate seraphis into the daemon/ledger, ...".
		- My own opinion on the state of Seraphis/Jamtis: both should undergo deeper review and round(s) of audits from independent parties and earn "rough consensus" before ultimately deployed. It would also be nice to see research into trustless zk-SNARKs move further along to have a better idea of how they could fit alongside Seraphis/Jamtis. Still, I think it would be valuable to start getting more finalized audit-able code prepared, especially code that likely wouldn't be impacted by the latter (such as RIDs, Polyseed, and address authentication).
	- Work together with @endogenic on factoring wallet2.
	- Implement subaddresses in `monero-lws` as per [this spec](https://github.com/monero-project/meta/pull/647). At this point, moving this forward feels dependent on others in the light wallet ecosystem and isn't fully in my hands (unless enough people want subaddress support in the server and don't need a client).
- Whatever seems highest priority to work on to me that I know can add value on that comes along. As of this moment, [PR 7999](https://github.com/monero-project/monero/pull/7999) (a serialization overhaul) is a leading candidate; however, with 7999, there is a chance I'm unable to provide an adequately deep review that the PR requires as my skill level may not be at that point yet. If I do decide to work on 7999, I wouldn't count my hours toward my CCS unless those hours lead to demonstrable value that pushes what the PR aims to solve forward.

## Who

I've identified and patched several privacy issues with varying severity in the Monero ecosystem:

1. The reference wallet's decoy selection algorithm didn't select very recent spendable outputs in some cases. ([source](https://www.getmonero.org/2021/09/20/post-mortem-of-decoy-selection-bugs.html))
2. The reference wallet truncated integers in the decoy selection algorithm, which would have borked the decoy selection algorithm entirely if tx volume were to increase; in the normal case, it marginally weakened the algorithm. ([source](https://www.getmonero.org/2021/09/20/post-mortem-of-decoy-selection-bugs.html))
3. `openmonero` was still using the old proven weak decoy selection algorithm, also leaving a fingerprintable trail by decoy selection algo. ([source](https://github.com/moneroexamples/openmonero/pull/177))
4. MyMonero doesn't use the updated CLSAG fee calculation which fingerprints MyMonero txs on chain by tx fee. ([source](https://github.com/mymonero/mymonero-core-cpp/pull/35))
5. MyMonero's fee calculation->input selection logic differs ever-so-slightly from the reference wallet, resulting in a fingerprintable tx fee. ([source](https://github.com/mymonero/mymonero-core-cpp/pull/36))
6. `monero-lws` fee masking on the server also caused ever-so-slightly different fee calculations from the reference wallet, resulting in a fee fingerprintable to `monero-lws` (a fingerprint that is distinct from MyMonero). ([source](https://github.com/vtnerd/monero-lws/pull/31))
7. In PR review on the upcoming hard fork's changes to the tx fee, identified the introduction of [slightly different fee calculation logic](https://github.com/monero-project/monero/pull/7819#discussion_r804404285) that would have caused tx fees to be fingerprintable to either old or new version until the hard fork.

Most of the above took a significant amount of time to investigate and in some of the cases, patch. Some were really simple to patch, some were difficult but only took a couple lines.

Some other contributions:

- implemented [view tags](https://github.com/monero-project/monero/pull/8061) to speed up wallet scanning.
- identified and patched daemon reliability issues, especially for users of tor/i2p daemons (moved forward solving long-standing issues [6631](https://github.com/monero-project/monero/issues/6631), [6929](https://github.com/monero-project/monero/issues/6929), and [6938](https://github.com/monero-project/monero/issues/6938)):
	- [Tor/i2p daemons periodically send a peer list that gets itself dropped](https://github.com/monero-project/monero/pull/8324).
	- [The daemon periodically drops outgoing tor/i2p connections](https://github.com/monero-project/monero/pull/8330).
	- [Tx re-relay math was off](https://github.com/monero-project/monero/pull/8326).
- since Ledger was fairly unresponsive, I implemented the changes for the upcoming hard fork needed to send and receive:
	- [monero repo](https://github.com/j-berman/monero/commit/cfbd590fd63ff9e0c5ec68c618e2f3fdaf24d241)
	- [ledger repo](https://github.com/j-berman/app-monero/commit/c1a6eb8bbbc1cc7974ce0938e9d8f920d0ad3ae9)
- patched a [cryptographic vulnerability in monero-python](https://github.com/monero-ecosystem/monero-python/commit/ece5b9d4cd929ced9539dca839d8a9fda4271663) (identified by kayabaNerve) where a malicious sender can get an honest recipient (who's using `monero-python` to scan for txs) to assume they received an arbitrary amount chosen by the sender (e.g. a 0.00000001 XMR tx could be made to look like 1000 XMR).
- [identified that the updated fee algorithm didn't implement the expected algorithmic block size increase at consensus](https://github.com/monero-project/monero/pull/7819#discussion_r799064615).
- implemented view tags in:
	- [the onion block explorer](https://github.com/moneroexamples/onion-monero-blockchain-explorer/pull/266)
	- [monero-lws](https://github.com/vtnerd/monero-lws/pull/33)
	- [openmonero](https://github.com/moneroexamples/openmonero/pull/181)

## Proposal

187.5 XMR. 480 hours, 0.12 XMR/hr + $36/hr, $133/XMR from coingecko.

I'm requesting a raise from my prior CCS because I feel I have demonstrated my contributions are worth a more competitive rate, and can continue to provide (increasing) value to Monero in a full-time capacity.