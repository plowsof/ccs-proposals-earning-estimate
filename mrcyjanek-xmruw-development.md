---
layout: wip
title: xmruw - development of cross platform wallet
author: mrcyjanek
date: February 29, 2024
amount: 76.68
milestones:
  - name: Month 1
    funds: 25.56
    done:
    status: unfinished
  - name: Month 2
    funds: 25.56
    done:
    status: unfinished
  - name: Month 3
    funds: 25.56
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

Hello! I'm mrcyjanek and I'm currently working on the Unnamed Monero Wallet (short: xmruw) that aims to be as portable as possible and as close to `wallet2_api.h` as it is reasonably possible.

However, this project got much bigger than I initially expected and resulted in a project that is huge in size, but also has really large portability capabilities, after fighting for a couple days with Wayland implementation on SailfishOS I (with the help from Mister_Magister and NotKit) managed to run the first cryptocurrency wallet natively on SFOS ([that is available on the app store of that os](https://openrepos.net/content/mrcyjanek/unnamed-monero-wallet-xmruw)). More details and the origin story can be found in a [blog post announcing the wallet](https://www.mrcyjanek.net/p/xmruw-monero-wallet/).

I'm developing `xmruw` with a few critical points in mind:
- There should be no database responsible for any of the monero-releated functions - so I won't accidentally do something that shouldn't be done.
- The app should be as close to `wallet2_api.h` as possible to eliminate things like overly complex state management as something that causes issues.
- Privacy should be prioritized - no external services are contacted in the app, and if there ever happens to be some external feature it will be opt-in in settings with an option to route entire traffic through Tor.
- Security is also prioritized - not only by minimizing the attack surface but also by providing features such as stealth mode (inspired by Samourai wallet)
- UX is the most critical of them all in my opinion - without the right UX, not many users are going to use a wallet, so it is my responsibility as a developer to make the wallet available on all platforms and to be appealing to users.
- As a mobile Linux enthusiast I'll also do my best to offer secure monero wallet solutions for owners of non-Android and non-iOS mobile devices

# About

I've decided to take the simplest path from `wallet2_api.h` to the actual wallet UI, so instead of forking m2049r/cake implementation I've decided to use `dart:ffi` to call the native functions - this made a lot of code unnecessary, and the part that was still required was mostly generated - so I call that a huge win. But not without it's own cost - I had to write a wrapper for `wallet2_api.h` that would provide C headers instead of C++ - which meant [writing a bunch of boilerplate code](https://git.mrcyjanek.net/mrcyjanek/monero_c/src/commit/abaa3a2d165577a79ce0c3fe5382b68fa260ecc1/libbridge/src/main/cpp/wallet2_api_c.cpp#L1549) and implementing a couple of dart/flutter libraries, that gave birth to the foundation of the wallet

## Unnamed Monero Wallet (xmruw)

[Website](https://xmruw.net), [Gitea](https://git.mrcyjanek.net/mrcyjanek/unnamed_monero_wallet), [GitHub](https://github.com/mrcyjanek/unnamed_monero_wallet), [Downloads](https://download.xmruw.net/)

Features of the wallet include:
- Sending/Receiving monero
- Online/Offline wallet modes
  - With URQR and file exports for Android/iOS
  - With clipboard-based exports for QubesOS
- Embedded Tor support
- (soon) Embedded i2p support [^1]
- Stealth mode (fake calculator app that opens wallet if the correct pin is provided)
- Multiple account support
- Coin control
- Signing / Verifying of messages
- Custom themes
- Advanced settings
  - Performance analysis tool for the `wallet2_api.h` functions called
  - Debug information that makes development easier
  - Configuration options to opt-in to experimental features (such as [background sync](https://github.com/monero-project/monero/pull/8619))
- OpenAlias resolving
- Backup/Restore
- Historically accurate currency conversion done fully offline
- And all of the "obvious" features such as transaction list, subaddress list, wallet locking, QR code scanning, etc.

## Scope of work

While working on Unamed Monero Wallet, here is a non-comprehensive list of the things I want to accomplish in no particular order, as it doesn't make sense to separate some things.

- Expanding compatibility of `monero_c` to all platforms that I have access to (Linux (glibc+musl), FreeBSD, iOS, MacOS, Windows) in an easily-reproducible way (single script and a docker environment)
- Making `xmruw` available for all platforms (and I do mean all platforms) and in app stores (including play store, self-hosted f-droid repository, apple app store, .deb, and .rpm repository).
- Implementing features desired by users, currently this includes
  - periodic sync (via [background-sync](https://github.com/monero-project/monero/pull/8617)) to provide seamless experience, no matter how frequently the app is actually opened
  - merchant mode
  - many UI/UX improvements/changes (some of more important ones: make seed offset and its role more obvious, better backup mechanism, time-lock warn, automatic node selection)
- Work on documentation (this will be a significant task on its own, but the goal is to allow anybody to integrate monero no matter what language/framework they are using by using monero_c/monero.dart).
- Fix issues that were made along the way
  - Bytewords entering an infinite loop when incorrect text is passed in
  - No compatibility with Feather / ANONERO in offline mode due to lack of CBOR encoding
  - Not cross-platform QR scanner [^2]
  - Bad UI on desktop (not that it's bad, it is just mobile-first)
  - and more, if found when developing
  - sending fixes to relevant peers and upstream

## Milestones

Given the nebulous nature of development, I would prefer my milestones to be time-based. I prpose a milestone completion and subsequent payout once every month (after services rendered).

In addition to the above features mentioned in the scope of work, I propose an additional deliverable of a weekly report so my progress can be verified.

# Payment

I'm proposing to work for 20 hours/week for `40$/hour` at a rate of `~125,14$/XMR` (according to open prices between 2024-02-17 and 2024-03-01 (date of writing) via [CoinGecko](https://www.coingecko.com/en/coins/monero/historical_data)) for 12 weeks, summing up to a total of `~76,68` XMR split into 3 payments of `25,56` XMR every 4 weeks.
At the end of each week, I'll comment a summary of what happened along the way and what tasks were done.

[^1]: The library is there, it needs some love to be usable, cross platform and built in a reproducible fashion.

[^2]: Camera isn't fun, especially when being cross-platform is a goal, but supporting it is critical for URQRs. This isn't a milestone on it's own, but a topic that I'll research, do some PoC and come up with a solution, especially because getting camera to work is one task, then we need to scan qr the codes (and be **very** fast at it), so this milestone is more of "explore the possibilities" and come up with a reasonable plan for future regarding cross-platform camera support.
