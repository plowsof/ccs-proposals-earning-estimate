---
layout: wip
title: "Continued Feather Wallet development (3 months)"
author: tobtoht
date: 12 May 2021
amount: 91.5
milestones:
  - name: First month 
    funds: 33% (30.5 XMR)
    done: 16 June 2021
    status: finished
  - name: Second month
    funds: 33% (30.5 XMR)
    done: 11 July 2021
    status: finished
  - name: Third month
    funds: 33% (30.5 XMR)
    done: 
    status: unfinished
payouts:
  - date: 21 June 2021
    amount: 30.5
  - date: 11 July 2021
    amount: 30.5
  - date:
    amount:
---

### What

This CCS proposal is for 3 months of full time Feather Wallet development.

The goal for this proposal is to get Feather out of Beta and release the 1.0 version.

### Background

See the previous [CCS proposal](https://ccs.getmonero.org/proposals/tobtoht_feather_dev_q1_2021.html).

### What I want to work on

To ensure the first major release is as stable, robust, and reliable as possible I will be mainly focussing my efforts on polishing the existing feature set (and extending it where needed).

- Fix bugs and issues as they arrise
- Further improve the UI/UX (layout, actionable error messages, etc)
- Improve documentation and user guides
- Add more compile flags for minimal/alternative builds: (no-Tor, no-Websocket, etc)
- Refactor parts of the codebase
- Allow compiling on more architectures
- Extensive QA testing on all supported platforms
- Commission a redesigned logo
- Upstream changes to libwalletqt / wallet_api
- Improve the setup procedure (Windows installer, Debian package on PPA, mac DMG)
- More advanced coin control: manual input selection and individual output labeling
- Extend hardware wallet support to include Trezor devices
- Allow opening multiple wallets at once

Once the is more clarity surrounding Triptych-compatible multisig (see [1](https://repo.getmonero.org/monero-project/ccs-proposals/-/blob/master/cypherstack-sarang-triptych-research.md), [2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/225#note_10903)) I will continue working on integrating multisig into Feather.

As always I will rely heavily on user feedback to determine where to put my focus.

### Who

Hi, I'm tobtoht. Creator of xmrguide and maintainer of Feather Wallet.
I have been an active contributor to the Monero ecosystem since April 2018.

Some of the things I have worked on are:

- Created and maintained guides to set up Monero on Tails and Whonix ([xmrguide](http://xmrguide42y34onq.onion/), [reddit](https://old.reddit.com/r/Monero/comments/h8pbc2/))
- Made miscellaneous contributors to the GUI (most notably Tails support)
- Maintained a [list](http://xmrguide42y34onq.onion/remote_nodes) of .onion remote nodes with their status
- Co-created Feather Wallet with dsc

### Proposal

40 hours per week at 45 USD/hour for 3 months (mid May to mid August) for a total of 91.5 XMR. At a rate of $236/XMR.

Progress will be reported in #feather on OFTC. Monthly updates will be posted to /r/FeatherWallet in the form on release changelogs.

Feedback and comments are welcome.

**To donators**: In the week since I made this proposal there has been some very significant volatility, making it difficult to establish a "fair" XMR/USD price. As such I had to adjust the quoted price down several times because the difference had grown larger than my risk tolerance. I have currently settled on ${current_price} + 20%, in the expectation that the price will recover a bit after such a steep decline.

To ensure I can sustain myself in the coming months AND the community gets its money's worth, I will extend the time spent on this proposal in case there is significant price appreciation over the next three months, like I did with my previous CCS (1.5 months overtime).
