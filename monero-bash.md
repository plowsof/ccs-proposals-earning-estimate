---
layout: cp
title: monero-bash, a wrapper for monero written in bash, for Linux
author: hinto-janaiyo
date: March 24, 2022
amount: 10.0 XMR
milestones: 
  - name: Integrated P2Pool Mining
    funds: 5 XMR
    done: 30 April 2022
    status: finished
  - name: RPC/Daemon API integration
    funds: 3.5 XMR
    done: 30 April 2022
    status: finished
  - name: Mining quickstart commands
    funds: 1 XMR
    done: 30 April 2022
    status: finished
  - name: Automated encrypted wallet backup
    funds: 0.25 XMR
    done: 30 April 2022
    status: finished
  - name: Auto GPG key verification for binaries
    funds: 0.25 XMR
    done: 30 April 2022
    status: finished
payouts:
  - date: 30 April 2022
    amount: 10
---

# Intro

Hi everyone, I'm hinto. This is my first CCS Proposal.

I would like to develop directly for Monero, but unfortunately: I cannot code. With that said, I've setup Monero nodes and miners on many machines for others and myself, and after a while, ended up making tons of Bash scripts to automate these processes.

I rewrote a couple scripts to make them usable by anyone and put them in the public:
- [XMRig-Auto-Build, for downloading/building everything needed to build XMRig](https://github.com/hinto-janaiyo/XMRig-Auto-Build)
- [monero-toolchain, a link filterer that always downloads the latest releases of monero-related software](https://github.com/hinto-janaiyo/monero-toolchain)

I'd like to receive support through this CCS to continue on a more ambitious project: `monero-bash`

## What

[monero-bash](https://github.com/hinto-janaiyo/monero-bash) is a wrapper for monero written in bash, for Linux.

monero-bash does what bash normally does:
**it glues together multiple programs in a more automatic fashion, in this case:**
- monerod
- monero-wallet-cli
- monero-rpc
- (p2pool planned...)

monero-bash abstracts `monero-cli` commands into interactive prompts and `linux-like` syntax

while monero-bash is helpful for people who want everything automated, it's also just as powerful as monero-cli because:
~~~
it is essentially a bunch of bash scripts invoking monero-cli
~~~
and so, any `monerod.conf` or `monero-wallet-cli.conf` that may be in your `.bitmonero` folder, can be used by monero-bash

## Features
**currently implemented:**
- Automatic `monero` release upgrades, verified with SHA256SUMS
- Software and wallet management
- Easy wallet/daemon control
- Price stats from API

**to be added:**
- Automatic P2Pool mining
- RPC/Daemon API integration
- Mining quickstart commands
- Encrypted wallet backups
- GPG key verification for binaries

## Issues
`monero-bash` runs into problems much like [systemd](https://en.wikipedia.org/wiki/Systemd):
There are massive conveniences to having a single program manage and abstract everything for an end user, however, that funnels all the trust onto that single program. Although... `systemd` is a highly adopted system-manager on Linux, `monero-bash` is a niche script-system for Monero *from some random person.* So, the question might be asked:

## But, Why?
I think something like `monero-bash` would give a nice and easy bootstrap to people who normally wouldn't have manually setup a node or setup P2P mining. Another (maybe selfish) reason is that I'm making this to actually use it myself! Running `monerod`, `monero-wallet-cli`, `monero-rpc`, `XMRig` and `P2Pool` on multiple headless machines makes me wish there were a more central program to manage it all.

## Security
As the person who will be making this, I obviously have no problems using it, however, even I would be wary of using other's supposedly "safe" scripts to manage sensitive things like Monero. Thankfully since it's just Bash, anyone that uses Linux (or macOS,BSD) will most likely be able to audit everything. If there are `spooky` looking functions or variables, I'd be happy to explain its purpose and what it does. If something looks over-complicated, it's not on purpose, I'm just bad at bash.

## End-Game & Proposal
I'd like for:
- Running a Monero Node
- Managing Wallets
- Upgrading and Verifying Monero-CLI Binaries
- Mining on P2Pool as the Default

to be as simple as running a couple commands.

I'll be working for however long it takes to satisfy these milestones:
- 5.0 XMR: Integrated P2Pool Mining
- 3.5 XMR: RPC/Daemon API integration
- 1.0 XMR: Mining quickstart commands
- 0.25 XMR: Automated encrypted wallet backup
- 0.25 XMR: Auto GPG key verification for binaries

for a total of 10XMR, regardless of fiat pricing.

[For full details of the current version, here is the GitHub.](https://github.com/hinto-janaiyo/monero-bash)
Feedback would be appreciated.
