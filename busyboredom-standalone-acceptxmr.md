---
layout: wip
title: Standalone AcceptXMR
author: busyboredom
date: February 31, 2023
amount: 14
milestones:
  - name: Dockerize AcceptXMR
    funds: 14
    done: 5 July 2024
    status: finished
  - name: Wordpress Plugin
    funds: 10
    done:
    status: unfinished
  - name: Maintenance 1 year
    funds: 20
    done:
    status: unfinished
payouts:
  - date: 19 July 2024
    amount: 14
---

# Standalone AcceptXMR
Another payment gateway CCS proposal.

## Summary
I would like to create a standalone, dockerized, AcceptXMR-based payment gateway with wordpress
support.

AcceptXMR ([demo](https://busyboredom.com/projects/acceptxmr),
[docs](https://docs.rs/acceptxmr/latest/acceptxmr/),
[repo](https://github.com/busyboredom/acceptxmr/)) is a payment gateway library (or crate, in rust
lingo) I wrote as a hobby project and have made available to the community. While my library serves
its purpose well, I understand that most merchants are not programmers therefor cannot use
AcceptXMR.

This proposal aims to make AcceptXMR usable for anyone capable running a docker container and
installing a wordpress plugin.

## Why AcceptXMR
Lots of reasons!
* View pair only, no hot wallet.
* Subaddress based (as opposed to the older integrated addresses).
* Pending invoices can be stored persistently, enabling recovery from power loss.
* Ignores transactions with non-zero timelocks.
* Zero-conf works out of the box.
* No local node, wallet RPC, or block explorer needed. Just pick a public remote node.

And of course, I am already intimately familiar with it.

## How It'll Happen
I will dedicate a portion of my weekends (you can expect about 10 hours a week on average) to
completing the following milestones. There will be some weeks with more progress and others with
less, but that's the average I'll be aiming for.

### Dockerize AcceptXMR
_14 XMR from xmrSale's abandoned funding._

This is the largest milestone. I'll be taking the webserver and frontend work you see in my demo,
cleaning it up significantly to bring it up to production standards and dockerizing it for easy
setup. I will also provide documentation on how to perform that setup.

### Wordpress Plugin
_10 XMR from xmrSale's abandoned funding._

Wordpress is popular, and it has a plugin system that supports custom payment gateways. I will write
a wordpress plugin for the freshly dockerized AcceptXMR implementation. I will also provide
documentation on how to use the plugin.

### Maintenance for 1 Year
_20 XMR total, with 6 XMR coming from xmrSale's abandoned funding and the remaining 14 XMR coming
from this CCS proposal._

Both rust and monero have rapidly changing ecosystems. Left alone, my work would likely be out of
date by the end of the year due to breaking changes in my library's dependencies if nothing else.
Keeping AcceptXMR up-to-date and functional is something I currently do for free, but building out a
full standalone gateway adds overhead. For this reason, I've bookmarked 20 XMR for maintenance for 1
year from the funding date.

I am hesitant to provide target dates for first  two milestones above, but I have been maintaining
AcceptXMR for over a year now and I don't plan on ghosting on it now.

## Stretch Goals / Future work
I'm not promising any of the following happens, but I'm putting it here to let the community know
it's on my radar and I want to do it if I get the opportunity:
* TOR support for the daemon RPC connection.
* A no-JS frontend. I have an example with this implemented on github, but I'll have to clean it up
a bit and integrate it into the new dockerized setup.
* ZMQ support as a more performant alternative to polling the remote node.

## Prerequisites
Before I start work on this CCS, I'll need to wrap up changes I'm making with v0.12.0 of AcceptXMR.
I'm not charging for that work, I'm just disclosing here that I need to resolve the issues in that
milestone before I start work on this CCS.

## License
AcceptXMR is dual-licensed under the MIT and Apache 2.0 licenses. I am not planning on changing the
license. It will always be under a permissive license.

## About Me
Busyboredom is _not_ an anonymous alias, you can see my minimally-redacted resume on my personal
website [busyboredom.com](https://busyboredom.com).

Proposal Expiration: January 1st, 2025.

Note: This CCS was originally intended to be funded entirely by the 30 XMR leftover from the abanoned
xmrSale project. At the request of the community, I have extended my maintenance commitment and
increased the maintenance budget by 14 XMR. This change allows CCS donors to act as a final check on
whether this proposal goes forward.
