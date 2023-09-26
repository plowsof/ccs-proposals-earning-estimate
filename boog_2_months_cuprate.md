---
layout: wip
title: Boog900 full time work on Cuprate, the Rust Monero node (2 months)   
author: Boog900
date: August 03, 2023
amount: 130
milestones:
  - name: Consensus rules up to RingCT
    funds: 53 XMR
    done:
    status: unfinished
  - name: All Consensus rules up to present
    funds: 53 XMR
    done:
    status: unfinished
  - name: Consensus Rules document
    funds: 24 XMR
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

Cuprate is a WIP Rust Monero node that SyntheticBird45 started back in Feburary, I joined the project not 
long after that, but sadly me and SyntheticBird have not been able to spend much time on it. Even more sad 
is that recently SyntheticBird decided to stop working on Cuprate for personal reasons that I will not get 
into here.

This CCS is to support me working on Cuprate full time for the next 2 months, In this time I will complete 
the transaction/ block verification. While doing this, I will also create a `consensus rules` document, which 
will document all of Moneros consensus rules from genesis to the current rules.

# Why

Currently, Monero only has one node written in C/C++, many would see this as an issue.
Having only one implementation makes us more vulnerable to implementation bugs, having
another node will help us to spot and fix these issues.

monerods code is also a bit of a mess, as many devs who have worked on it would agree. Cuprate
is a fresh start and is built with modularity in mind which will lead to a cleaner and easier
to understand codebase.

Having a `consensus rules` document will make it easier for developers to build software to interact
with Monero. It will also make it easier to spot potential issues with consensus rules.

# Who

I am [Boog900](https://github.com/boog900), the current, and now solo, maintainer of Cuprate.

# Design

For an overview of the design see [here](https://github.com/Cuprate/cuprate/blob/main/misc/DESIGN.md)

# What Has Been Done

## P2P

The peer-to-peer code is mostly complete; I have implemented levin headers, the epee binary format and all p2p messages.
I have also done the p2p address book, individual peer request routing, handshakes and pruning calculations.

## Blockchain Data

I made a PR to monero-serai adding decoding/encoding/hashing of legacy transactions and blocks so this is complete.

## Consensus Checks

There is still a lot to do here, but monero-serai has already done verifying for bulletproofs(+) and CLSAG.
My PR to monero-serai also contained an unverified MLSAG verify function and a WIP Borromean range proofs
function.

## Database

The initial database abstraction is complete, and we have defined the tables (we have copied monerod for
the moment). We have also created the methods to add and get blocks and transactions from the database.

Still to-do: We need to investigate the database schema for optimizations.

# Tasks

We need to implement/ get ready for production verifying for MLSAG, borromean range proofs and V1 ring signatures, there are other 
checks we need to do, but these are the big ones. As Monero does not have a protocol document, we will have to go through monerod 
to find every check it performs and do them in Cuprate.

Cuprates consensus checks will be grouped together in a single location, so they are clear and not spread around the codebase,
they will also reference the `consensus rules` document at every check. If some checks are done elsewhere, for example some are done at
deserialization, we will either duplicate the check or, if its expensive, we will put a comment referencing the check and the
`consensus rules` in the single location.

We also need to create bindings for Moneros legacy CryptoNight POW algorithms and select a Random-X binding. There is a Rust 
Random-X implementation, which we plan to implement as an option, but we won't enforce it as it lacks review/ usage.

As our P2P/ database code still needs some work, we will be using monerods RPC interface to test the code.

*All code produced for this CCS will be licensed under MIT.*

### Milestones

1. ###### All Consensus rules up to RCT
   Implement verification for transactions and blocks before RCT.
2. ###### All Consensus rules up to present
   Implement verification for all transactions and blocks.
3. ###### Creation of the `consensus rules` document


# Funding

I am asking for $45/hr for 50hrs/week for 2 months at $148/XMR this gives 130 XMR
