---
layout: wip
title: "Continued Feather Wallet development (Q1 2021)"
author: tobtoht
date: 4 January 2021
amount: 150
milestones:
  - name: First month 
    funds: 33% (50 XMR)
    done: 8 February 2021
    status: finished
  - name: Second month
    funds: 33% (50 XMR)
    done: 
    status: unfinished
  - name: Third month
    funds: 33% (50 XMR)
    done: 
    status: unfinished
payouts:
  - date: 11 February 2021
    amount: 50
  - date:
    amount:
  - date:
    amount:
---

### What

This CCS proposal is for 3 months of full time Feather Wallet development.

The goal of this proposal is to:

- Reach feature-parity with the GUI (this mostly concerns hardware wallet support)
- Further advance the Monero desktop wallet space by implementing new (and experimental) features.

### Background

- Feather was [announced](https://old.reddit.com/r/Monero/comments/idujx0/feather_free_opensource_monero_desktop_wallet/) on Aug 21 2020. 
- A CCS [proposal](https://ccs.getmonero.org/proposals/feather-2020.html) funding the initial stages of development was accepted on September 1. 
- The first alpha builds became [available](https://old.reddit.com/r/Monero/comments/j8kn8e/feather_a_brand_new_monero_gui_desktop_wallet/) on Oct 10. 
- During the alpha time was spent on:
    - Troubleshooting teething problems
    - Bugfixes and performance improvements
    - Getting the websites and build infrastructure up and running
- The first beta builds were [announced](https://old.reddit.com/r/FeatherWallet/comments/kdmj3b/feather_beta2_released/) on Dec 15.
    - The beta introduced signed release binaries.
    - The focus for the beta was to fix the remaining UI/UX issues before adding new features. This is now mostly complete.
    - A total of 211 pull requests (171 made by me) were submitted to the repository since the alpha release.
- Some features that were added between the previous CCS proposal and now are: Windows support, view-only wallets, offline transaction signing, advanced transaction overview ([image](https://featherwallet.org/theme/img/feather_send_advanced.png)), transaction rebroadcasting, XMRig integration and reproducible Linux builds. Reproducible builds are mostly thanks to work done by Xiphon on the GUI.

### What I want to work on

- Hardware wallet support (most requested feature, so this is definitely happening now)
- More exchange integrations (among which LocalMonero)
- More advanced coin control features: manual input selection and individual output labeling
- An in-wallet troubleshooting wizard that detects and suggests fixes for common issues ([example](https://git.wownero.com/feather/feather/issues/144))
- Easy to use 2/2, 2/3 multisig (work on the message transportation layer and UI/UX design can commence before it is clear what changes Triptych/Arcturus will bring to multisig)
- Qr scanner (scan addresses with laptop camera/webcam)
- Multi destination transactions
- Debian package
- Sync over clearnet, construct & broadcast transactions over Tor
- Approach the Tails team to discuss potential inclusion of Feather Wallet by default
- Further UI/UX improvements (including more actionable error messages, better UI feedback)
- Upstreaming of changes to libwalletqt / wallet_api
- (Separate from Feather): Monero Daemon as a system service ([more info](https://git.wownero.com/feather/feather-meta/issues/3))

This is a non-exhaustive list of some of the things I want to work on during the proposal.
I expect the majority of the items on this list to be completed at the end of the 3-month period (with the exception of multisig, which will likely take longer).
As always I will rely heavily on user feedback to determine where to put my focus.

### Why contribute to Feather development?

- It is an excellent testing grounds for features that may later be implemented in the official GUI (14 word seeds, coin control, multisig, etc)
- There is more room to experiment with UI/UX and features and see what works before committing to it in a reference wallet.
- Some users cite its simplicity, focus on user experience, quick setup, addition of power user features and similarity to Electrum as reasons they prefer it over the GUI
- Feather will remain open source and licensed under BSD-3.

### Who

Hi, I'm tobtoht. Creator of xmrguide and maintainer of Feather Wallet.
I have been an active contributor to the Monero ecosystem since April 2018.

Some of the things I have worked on are:

- Created and maintained guides to set up Monero on Tails and Whonix ([xmrguide](http://xmrguide42y34onq.onion/), [reddit](https://old.reddit.com/r/Monero/comments/h8pbc2/))
- Made miscellaneous contributors to the GUI (most notably Tails support)
- Maintained a [list](http://xmrguide42y34onq.onion/remote_nodes) of .onion remote nodes with their status
- Created various Python [scripts](http://xmrguide42y34onq.onion/scripts) to convert from/to Monero using third party exchangers
- Co-created Feather Wallet with dsc

### Proposal

40 hours per week at 45 USD/hour for a total of 150 XMR. The XMR/USD rate is based on current exchange rate of $144 XMR/USD.

This will cover January/February/March. Any hours left over will bleed into April.

Progress will be reported in #feather on OFTC. Bi-monthly updates will be posted to /r/FeatherWallet in the form on release changelogs.

Feedback and comments are welcome.
