---
layout: wip
title: j-berman full-time development (3 months)
author: j-berman
date: August 30, 2021
amount: 78
milestones:
  - name: Month 1
    funds: 33% (26 Monero)
    done: 29 September 2021
    status: finished
  - name: Month 2
    funds: 33% (26 Monero)
    done:
    status: unfinished
  - name: Month 3
    funds: 33% (26 Monero)
    done:
    status: unfinished
payouts:
  - date: 6 October 2021
    amount: 26
  - date:
    amount:
  - date:
    amount:
---

## What

### Improve the Decoy Selection Algorithm

When constructing a new transaction, your wallet references a past output you received in a prior transaction, and uses it as one of the inputs to your new transaction. The wallet hides this output among a set of decoy outputs from other people's transactions from across the blockchain, in order to sever the link from your newly constructed transaction to your prior transactions. That is what the decoy selection algorithm does in the wallet: it mixes your real outputs spent in a transaction among a set of decoy outputs. This algorithm has room for improvement to better protect users under a wider set of circumstances today, and I would like to focus on these areas. I found and patched a couple low-hanging fruit areas of improvement, and have written about 4 areas worth continuing to focus attention on today [here](https://github.com/monero-project/research-lab/issues/86):

1. Assess observed chain data and determine the relative safety of fully patching an [integer truncation issue](https://github.com/monero-project/monero/pull/7798#issuecomment-900728961).
2. Push forward a "binning" solution to bucket outputs into bins, in order to mitigate weaknesses in exclusively using past spending patterns to select decoy outputs.
3. Collaborate with community member @Rucknium on methods of improving the probability distribution used in the decoy selection algorithm, so that it would more accurately reflect true spending patterns (it currently uses a gamma distribution -- @Rucknium believes there are likely better distributions to use).
4. Work on a PoC that demonstrates how to simply enforce transaction uniformity in decoy selections via consensus.

### Informally audit [monero-lws](https://github.com/vtnerd/monero-lws) (light wallet server) for safety issues

The benefits of running a light wallet server alongside a node are significant. You could connect a light wallet compatible client to your server from anywhere, and your wallet would stay synced and ready to use at all times. This way you wouldn't have to wait for your wallet to sync when you load your wallet. The minor downside is that your address and view key would be "hot" on your server, meaning if someone gets access to your server, they get access to your address and view key and could therefore see all of your past and future outputs received. @vtnerd has evidently put a ton of effort into [monero-lws](https://github.com/vtnerd/monero-lws), it would be great to get it into more hands. @vtnerd mentioned in IRC that having someone look over the implementation for obvious privacy backdoors is one of the last steps needed to get it into the main repository. I'd love to spend 10-20 hours (or more?) on an informal audit. I'm decently familiar with the light wallet stack, since I worked on a fork of [openmonero](https://github.com/moneroexamples/openmonero) (and the MyMonero client libraries) in the past.

### Other one-off tasks I'd like to work on as well

- Update [openmonero's](https://github.com/moneroexamples/openmonero) decoy selection algorithm to use the latest version
- make the daemon RPC thread safe
	- I started on this [here](https://github.com/j-berman/monero/pull/1)
- make wallet cache an lmdb file
- authenticated encryption for wallet cache
- rw lock for the Blockchain class instead of mutex
- zeromq msgpack support (performance - discussed with vtnerd)
- json-schema support (ease of use for developers - discussed with vtnerd)
- [reduce # of requests to poll a daemon](https://github.com/monero-project/monero/issues/7571)
- [add wallet-dir flag for monero-wallet-cli](https://github.com/monero-project/monero/issues/7674)
- scan the wallet2 code for ways of providing stronger protection from malicious nodes

+ any other high value tasks that come along I can help out on, prioritizing safety issues above all else, then liveness issues, then performance/usability. I plan to help out where I can on PR reviews as well.


## Who

I'm Justin Berman (I go by jberman in IRC). This is my first CCS proposal. I've been working full-time on patches for (and analysis of) the decoy selection algorithm for close to 2 months. I have knowledge of the Monero code base from past work on a fork of Monero for 4.5 months (Haven). I decided I'd really like to work on Monero full-time if it's possible. I am very passionate about Monero and want to see the best sound, hard, private money used everywhere :) I have a bachelor's degree in Computer Science from the University of Texas at Austin.

My past contributions to Monero include:

- [Finding](https://github.com/monero-project/monero/issues/7807) and [patching](https://github.com/monero-project/monero/pull/7821) the issue where the core wallet code ignores very recent spendable outputs when selecting decoys.*
- [Finding](https://github.com/monero-project/monero/pull/7798) and [patching](https://github.com/monero-project/monero/pull/7845) an issue where the wallet truncates integers in the decoy selection algorithm, which would have eventually caused wallets to construct transactions that would reveal real spent outputs 95%+ of the time if left unchanged.
- Improving a protection measure [in the wallet](https://github.com/monero-project/monero/pull/7848).

Unfortunately the above are all small snippets of code, so it may not be the most useful means of gauging my abilities. If desired, I can point to larger swathes of changes I made on Haven to show I am comfortable working across the entire code base (from wallet to RPC interface to consensus rules to LMDB), though many of my contributions there are not shown to be authored by me on Github.

**Full disclosures**

- I received a job offer to join Cypher Stack doing research work. I personally would prefer the CCS route, though I may pick up contracting work if I feel that the work could strongly push Monero forward.

- I received a contracting offer from Cake Wallet to work on the Thorchain Monero integration. I haven't decided yet what I'd like to do on this.

- I'm a co-owner of [Userbase](https://userbase.com), which is a SaaS tool for web devs to make end-to-end encrypted apps. I spend ~5 hours a month on support, and in my free time would like to implement new features from time to time.

Final point on me: Justin Berman is my real name. I think anons are extremely important, and I debated using a nym myself. Ulimtately I feel having a balance of anons + non-anons is a good thing. Personally I want to show that sound, hard, private money should be a publicly acceptable, normal thing. I'm not a shadowy super coder, I'm just a normal dude who thinks normal people and businesses don't want to share all their financial information with the entire world :)

## Proposal

$24 + 0.08 Monero per hour for 40 hours a week, for 12 weeks starting August 30th, ending November 21st. At the current exchange rate of $290 / XMR from coingecko, this totals to [($24 / $290) XMR + 0.08 XMR] * 40 * 12 = [0.0828 XMR + 0.08 XMR] * 40 * 12 = ~78 Monero

To be clear, I am comfortable accepting the volatility, and am requesting a total of 78 Monero for this proposal. I figure $24 + 0.08 Monero per hour is a good price point for future CCS proposals as well.

As of right now, I'd like to work over 40 hours a week on this proposal and don't expect to be compensated for doing so, but if I do decide to take on contract work, I may end up working less than 40 hours a week on this proposal. My promise is to work a total of at least 40 * 12 hours = 480 hours, even if it extends past November 21st, though I anticipate working more than 480 hours over the period.

I'll keep track of my hours and provide bi-weekly updates for the first 2 months, then a single update for the final month.

**(*) Correction: previously stated that some recently spent outputs were definitively linkable as a result of the discovered bug, which [was not the case](https://www.getmonero.org/2021/09/20/post-mortem-of-decoy-selection-bugs.html).**
