---
layout: cp
title: Feather wallet GUI development
author: Feather team
date: 1 September 2020
amount: 188
milestones:
  - name: 1st milestone
    funds: 94
    done: 3 September 2020
    status: finished
  - name: Alpha release
    funds: 94
    done: 20 October 2020
    status: finished
payouts:
  - date: 3 September 2020
    amount: 94
  - date: 23 October 2020
    amount: 94
---

# What

Feather is an [upcoming open-source desktop Monero wallet](https://www.youtube.com/watch?v=tylbteVtwrw) with some interesting features. It has been in development for over a year. Community reception thus far has been quite positive.

- [/r/Monero/comments/idujx0/feather_free_opensource_monero_desktop_wallet/](https://www.reddit.com/r/Monero/comments/idujx0/feather_free_opensource_monero_desktop_wallet/)
- https://twitter.com/xmrdsc/status/1297275505704685568
- https://twitter.com/xmrdsc/status/1297620436184899585
- https://twitter.com/xmrdsc/status/1297906498899775490

A lot of work has gone into the project. The Feather team is excited about what has been developed and could use funding to support the cause of releasing this FOSS application, as there is still a couple of months left to bridge before release.

## TO-DO

We have most functionality working, the challenges ahead are:

1. Static builds for Windows and Mac OS
2. Upstreaming various patches to `src/wallet/api/wallet2_api.h` (CLI - that libwalletqt (GUI) can use, mostly additions).
3. Creating and hosting a dedicated static website.
4. Hosting both high performance clearnet and Tor remote nodes.
5. Hooking up buildbots to our git for nightly builds
6. Node switching inside the application.
7. Testing to ensure the wallet is stable and robust
8. Fixing platform-specific bugs

## CCS

Previously, dsc_ made [a proposal](https://ccs.getmonero.org/proposals/dsc-2019-q2.html) for Monero GUI development for which he has completed 1 out of 3 milestones. We believe it would be beneficial if those funds could be used to support finishing our Feather wallet project instead, as both proposals are regarding GUI work, we feel Feather is more important/impactful to the community.

We would like to use the remainder of the 2 milestones, the first being distributed **now**, to support ourselves while working on Feather, and the second milestone will be reached in (hopefully) October, when we go into alpha. 

Feather will:

- Release code under the Monero License.
- Self-host the website/issue-tracker/git-repositories (and also make it available through Tor).
- [dsc__](https://www.reddit.com/user/dsc__) and [tobtoht](https://www.reddit.com/user/tobtoht) will maintain future releases.
- Upstream wallet2 changes so that the Official GUI may borrow functionality.
- Deliver something great to the Monero community.

## What can we expect during alpha relase?

It will include most functionality - Linux and Mac OS.

1. Our repositories (Feather, websocket back-end (Python)) will be opened to the public
2. The community has the ability to test and give suggestions, create PRs
3. Static Linux builds via Docker (Qt 5.15.0) on an Ubuntu 18 base image
4. Self compilation required (we will not distribute static binaries)

We are targetting October.

The alpha version takes place on stagenet and it'll be an opportunity to test integration with various Linux distros. Bugs can be reported and managed on our self-hosted issue tracker. People running Mac OS are free to participate in the testing, but our focus will largely be on Linux.

## What can we expect on release?

1. Linux / Mac OS static binaries
2. A website with pgp signed binaries and documentation
3. Upstreaming of wallet2 changes
4. The features described in our [announcement post](https://www.reddit.com/r/Monero/comments/idujx0/feather_free_opensource_monero_desktop_wallet/) and [video](https://www.youtube.com/watch?v=tylbteVtwrw)
5. A robust/fast Linux/Mac OS Monero wallet.

We believe a full release in December is realistic.

## What can we expect after release?

- Windows support (Q1 or Q2 2021, [cross compilation attempts here](https://git.wownero.com/feather/mxe/commit/a6ed6f3c323c301dcdeed3fc685fce4b993d8900))
- Multi-sig (Still exploring the various options, [more info here](https://www.reddit.com/r/Monero/comments/ikiv8t/what_we_need_for_adoption_is_trivial_multisig/g3l7os6/))
- Debian package
- Wallet refresh over clearnet, transaction submission over Tor
- Feather as a websocket server (to be announced)

We will continue to maintain Feather after release, however any **significant** feature updates (such as multisig) may require additional funding through a separate CCS depending on the time and effort required to implement them.

## Ending note

We have been careful to make certain promises on timelines and features in this CCS proposal - mostly due to the complexity of the project. We target deadlines but delays may occur. However, we've already got a lot finished (as can be seen in [our video](https://www.youtube.com/watch?v=tylbteVtwrw)).

If we are not able to raise funding, it will be delayed notably as we will have to find ways to support ourselves. In that case the application will of course still *eventually* release under an open-source license, somewhere in 2021.


