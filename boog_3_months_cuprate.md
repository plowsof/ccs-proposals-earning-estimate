---
layout: fr
title:  Boog900 full time work on Cuprate (3 months)
author: Boog900
date: January 27, 2024
amount: 190
milestones:
  - name: The PeerSet + Routing methods excluding D++
    funds: 54 XMR
    done:
    status: unfinished
  - name: D++ Routing method + Network Initialisation
    funds: 54 XMR
    done:
    status: unfinished
  - name: The Block Downloader + Syncer
    funds: 54 XMR
    done:
    status: unfinished
  - name: P2P Documentation
    funds: 28 XMR
    done:
    status: unfinished
payouts:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
---

This proposal is to continue my work on [Cuprate](https://github.com/Cuprate/cuprate), specifically I will be working on
Cuprate's P2P layer and syncing. While doing this I will also expand [monero-book](https://monero-book.cuprate.org), which I created during my last CCS, 
with the P2P types, message encoding and message flows (handshakes etc).

# Who

I am [Boog900](https://github.com/Boog900), you can see my last CCS [here](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/405).

# What

As well as continuing to lead coordination of Cuprate, I will also be an active maintainer for monero-rs, during the past few months
I have been reviewing and merging PRs and have released a new version: [ v0.20.0 ](https://github.com/monero-rs/monero-rs/releases/tag/v0.20.0)

For this CCS I will be working on getting Cuprate's P2P layer into a working state.

Currently Cuprate's P2P has:

- Levin header decoding/ encoding
- Every P2P message decoding/ encoding
- Handshakes.
- Rough individual peer message routing.
- A P2P address book.

What I will be doing:

## Hardening Individual Peer Message Routing

Individual peer message routing needs to be hardened, currently we don't do any checks the data received is the data we
asked for, we should be doing these checks in the connection task before handing the message to the rest of Cuprate.

## The PeerSet

The `PeerSet` is the structure that holds all currently connect peers on a certain network, it will have methods to get
peers by direction (Inbound, Outbound) or by a custom strategy, e.g a load balancing algorithm. This structure is then
used by the different routing methods.

## All The Routing Methods

The routing methods are how the rest of Cuprates interact with the P2P network. The goal is to have there be one end point
that the rest of Cuprate can send requests to. This end point will need to be made up of multiple `tower::Services` for the different
routing methods (broadcast to all, etc).

I will also be creating the Dandelion++ routing method, which will handle keeping the current d++ state, selecting out peers to route to and
keeping track of stem routes. It won't handle all of D++ as that requires knowledge of the tx-pool, but it will handle all the routing
side.

## Network Initialisation

I will make the network initialisation code, to start the network and return the end point that requests can be sent to.

## The Block Downloader

The block downloader will be a `futures::Stream` that will handle finding the chain with the most PoW from the `PeerSet` and will download
this chain from the peer(s), giving the downloaded blocks back to the caller to then verify and add to our chain.

## The Syncer 

The syncer will handle synchronisation after falling behind, it will use [the block downloader](#the-block-downloader) and
the consensus service I created for my last CCS. It will get the blocks from the downloader, verify them and then
giving them to the database*.

*the database will not be worked on for this CCS, see [hinto's CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/422).

If this CCS and [hinto's CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/422) are accepted then when both are complete Cuprate will
be able to sync, verify and store the blockchain.

## Documentation

There are already documents describing the [levin header format](https://github.com/monero-project/monero/blob/master/docs/LEVIN_PROTOCOL.md) and [epee binary format](https://github.com/monero-project/monero/blob/master/docs/PORTABLE_STORAGE.md).
I will be documenting the format of each P2P message (how they are encoded, the fields) and successful message flows: handshakes, syncing etc. 

# Why

I believe that having an alternative node is needed to help to protect against implementation issues like [this one](https://github.com/monero-project/monero/pull/9013) I found during my
last CCS.

Having an accessible P2P library and documentation will make it easier for devs to build software that needs to interact with the P2P network.

# Milestones

1. The PeerSet + Routing methods excluding D++
2. D++ Routing method + Network Initialisation
3. The Block Downloader + Syncer
4. Documentation

# Funding

I am asking for $45/hr for 50hrs/week for 3 months at $142/XMR this gives 190 XMR
