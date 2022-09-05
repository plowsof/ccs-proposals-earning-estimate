---
layout: wip
title: "Continued Feather Wallet development (3 months)"
author: tobtoht
date: 20 Jul 2022
amount: 162
milestones:
  - name: First month 
    funds: 33% (54 XMR)
    done: 
    status: unfinished
  - name: Second month
    funds: 33% (54 XMR)
    done: 
    status: unfinished
  - name: Third month
    funds: 33% (54 XMR)
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

### What

This CCS proposal is for 3 months of full time Feather Wallet development.

Non-exhaustive list of things I want to work on/towards or experiment with:

- Bootstrappable builds
  - Leverage [Guix](https://github.com/bitcoin/bitcoin/tree/master/contrib/guix) to produce cross-compiled, reproducible, [bootstrappable](https://bootstrappable.org/) builds for all target platforms and operating systems. Most of the work for this is already [done](https://github.com/feather-wallet/feather/pull/20). This has the added benefit of greatly speeding up release engineering, allowing for quicker release cycles.

- Offline transaction signing using animated QR codes
  - Export/import outputs, key images and transactions using animated QR Codes based on Blockchain Common's [Uniform Resources](https://github.com/BlockchainCommons/bc-ur).
  - Work with the [Keystone](https://keyst.one/) team to add support for Monero and integrate with Feather.

- Multi-node syncing (experiment)
  - Syncing a month worth of blocks now requires more than 300 MB of data. Wallet synchronization (when connected to a remote node) is often limited by one of two things: your download speed or a node's upload speed (for mobile devices your CPU might play a role too). Multi-node syncing will experimentally determine the fastest nodes from your node list and automatically gather blocks from the highest performing nodes to utilize as much of your available bandwidth as possible. If you are on a fast internet connection this can result in dramatically faster syncing.

- Allow skipping synchronization
  - POV: You just opened your wallet on Tails after leaving it unopened for 3 months. You proceed to wait an hour or more for your wallet to synchronize knowing that there has been no activity. An advanced option to skip synchronization will eliminate the wait and allow you to send transactions almost immediately.

- Improve Tor support and add support for more anonymity networks
  - Add support for Tor bridges and stream isolation
  - Switch the Tor client implementation to [Arti](https://blog.torproject.org/announcing-arti/) (when it is ready)
  - Remove the hard dependency on Tor and allow Feather to be used without anonymity networks
  - Modularize the anonymity network code to make it possible to integrate other networks like I2P and [Nym](https://github.com/nymtech/nym).

- Mining interface overhaul (+ P2Pool support)
  - The Mining tab is a bit crude. Mining is [not trivial](https://docs.featherwallet.org/guides/mining-setup) to set-up for new users, and it lacks configurability for advanced users. It's currently not possible to mine without having a wallet open. I want to move the Mining tab to a utility that can be accessed via the taskbar icon. Users should be able to quickly setup P2Pool, solo and pool mining. Feather will be able to run in the background and allow users configure scheduled mining, as well as provide a dashboard where users can check their mining stats and make changes to the configuration.

- Improve packaging for Linux distributions
  - Make Feather available as a Flatpak, Debian package, and maintain a working -bin package on the AUR. I also want to work on documentation that will help maintainers package Feather for their distribution.

- Support more ways of spending Monero
  - The libwallet interface lacks support for various advanced ways of spending Monero. The current Feather release added manual input selection. More is still desired, such as multi-destination sweeps or spends with an alternative change address.

- Improved documenatation
  - I'm already quite happy with the [documentation](https://docs.featherwallet.org/) in it's current state, but there is still room for improvement. A search feature is lacking and some parts could be improved with screenshots. Other parts can be rewritten to improve clarity and a glossary would be a welcome addition. I also want to add a section that goes in depth about threat-modeling to help users make more informed decisions about how they should use and configure the program to address their specific privacy or security concerns.

- Fix bugs and issues as they arise

I'll also work on reviewing contributions to CLI / GUI where I can and work on upstreaming patches to core.

As always I will heavily prioritize user feedback when deciding what to focus on.

### Who

Hi, I'm tobtoht. I am an active contributor to the Monero ecosystem since April 2018. Currently, I maintain Feather Wallet and contribute to the core codebase.

Previous CCS proposals:

- https://ccs.getmonero.org/proposals/tobtoht-feather-dev-2021-3.html
- https://ccs.getmonero.org/proposals/tobtoht-feather-dev-2021-2.html
- https://ccs.getmonero.org/proposals/tobtoht_feather_dev_q1_2021.html
- https://ccs.getmonero.org/proposals/feather-2020.html

### Proposal

Work 40 hours per week over the next 3 months at a rate of €45 / hour. At €133 / XMR (14 day EMA) this makes 162 XMR.
