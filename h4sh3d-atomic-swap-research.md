---
layout: fr
title: "Monero Atomic Swaps research funding"
author: h4sh3d
date: May 19, 2020
amount: 18
milestones:
  - name: Work is done
    funds: 100% (18 XMR)
    done:
    status: unfinished
payouts:
  - date:
    amount:
---

# Monero Atomic Swaps research funding

From [https://github.com/h4sh3d/xmr-btc-atomic-swap](https://github.com/h4sh3d/xmr-btc-atomic-swap):

> In blockchains where hashed timelock contracts are doable atomic swaps are already deployed, but when one blockchain doesn't have this capability it becomes a challenge. This protocol describes how to achieve atomic swaps between Bitcoin and Monero with two transactions per chain without trusting any central authority, servers, nor the other swap participant.

## Motivation:

Two years ago (Dec 2017), I published a draft to swap between Bitcoin and Monero.

In March 2019 I rewrote the protocol in more details, specifying what kind of zero-knowledge proofs were needed to guarantee the "trustlessness" of the protocol and the known limitations of the scheme, funded by my previous employer.

zkao and I presented the protocol at 36C3 in December 2019 ([link here](https://www.youtube.com/watch?v=G-v6hDnzpds)). After discussing it during March and April on #monero-research-lab IRC, andytoshi's idea of using "discrete logarithm equality across groups" that sarang has a write-up [here](https://web.getmonero.org/resources/research-lab/pubs/MRL-0010.pdf), I changed the zero-knowledge requirements by adapting the protocol, but the protocol, thus on-paper complete, was still not implementable as it used an inactive bitcoin op-code: `OP_AND`.

Recently I learned some new cryptographic tricks with ECDSA that should make the protocol complete and implementable with today's tools without requiring hash pre-image zero knowledge proofs.

**This research will update the draft protocol to completely remove hash pre-image zero-knowledge proof requirement.**

So far, I've carried out the latest research on my spare time. I can now use part of my working time to continue. My company has an internal budget for doing research, and because it's my first funding request, it will match the raised funds. Thus I will request 1/2 week of funding from the community, and will spend 1 week working on this project.

## Overview:

R & D Institution: Cryp GmbH (I work and own part of the company)

Funding: Monero CCS

Duration: 40 hours of research (of which 20h paid by community)

Job completion: Within 2 months after successful funding

Contributors:

 * Principal researcher: h4sh3d
 * Supervisor: zkao

Licences: All work will released under CC-BY-4.0

Expiration date: If not funded or completed until July 31, 2020 funds can be released

## Project Roadmap:

One week of research and writing.

### Deliverable:

 * **Revised version of "Bitcoin--Monero Cross-chain Atomic Swap":** new version with updated cryptographic primitives and protocol variation

## Cost

I ask for the equivalent of 1200 USD from CCS.

Therefore, using a 7-day EMA of 66.21 USD/XMR from Kraken the request total is __18.~~12~~ XMR__.

## Feedback

First CCS, so questions, comments, and feedback regarding this request are very welcome.
