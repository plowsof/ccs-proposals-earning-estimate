---
layout: wip
title: ETH-XMR Atomic Swap Development
author: noot
date: Dec 4 2021
amount: 56 XMR
milestones:
  - name: Maintainence of existing codebase
    funds: 5 XMR
    done: 5 February 2022
    status: finished
  - name: Contract improvements
    funds: 8 XMR
    done: 27 January 2022
    status: finished
  - name: DLEq integration
    funds: 12 XMR
    done:
    status: unfinished
  - name: Integration testing
    funds: 8 XMR
    done: 21 March 2022
    status: finished
  - name: Network testing 
    funds: 8 XMR
    done:
    status: unfinished
  - name: Pre-print paper and additional research
    funds: 5 XMR
    done:
    status: unfinished
  - name: UI
    funds: 10 XMR
    done:
    status: unfinished
payouts:
  - date: 28 January 2022
    amount: 8
  - date: 8 February 2022
    amount: 5
  - date: 22 March 2022
    amount: 8
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
---

# Summary

This proposal is for the continued development of ETH-XMR atomic swaps. The milestones include continued maintence and testing of the current codebase, gas improvements, network and integration testing, and documentation. At the completion of this proposal, there will be an audit-ready pre-production release of the ETH-XMR atomic swap software, as well as a pre-print paper outlining future improvements to the protocol. The total estimated duration of this proposal is 16 weeks.

# Team

[noot](github.com/noot) will be completing milestones 1-6. Milestone 7 will be completed by [Tbaut](https://github.com/Tbaut).

### About me (noot)

Since I'm quite new to the Monero space, I figured I'd post a little bit about me here. I've been working as a professional blockchain protocol engineer for nearly 4 years (will be 4 years in March 2022). I also have a Bachelor's of Applied Science specializing in Computer Engineering from the University of Toronto. For my undergraduate thesis project, I explored adding privacy to Ethereum, which ended up with me writing a Go implementation of RingCT. Although the project didn't really go anywhere, it was my introduction to real-life cryptography and of course Monero. Since then I've been casually following Monero. I've always loved the tech and the ethos and I'm glad to finally be able to contribute to it! 

I'm passionate about privacy-preserving technologies and I think Monero really is the best and only (afaik) cryptocurrency that's truly private. I hope this project will bring more users to Monero by reducing the onboarding overhead, specifically by not needing to rely on a centralized exchange. I hope this work, along with the current inspiring XMR-BTC swap work being done, will help bring in fully decentralized, peer-to-peer exchanges.

Most of my past work is focused on alternative blockchain protocol implementations, including implementations for Polkadot and Filecoin. I've also worked on Ethermint (EVM Cosmos module), a *little* bit on some ETH2 libraries, and written/tested various smart contracts in my day, which consists of most of my Ethereum experience. I've also worked on go-libp2p-noise (a handshake protocol for the p2p library libp2p) and go-schorrkel (schnorr signatures over ristretto255, used in Polkadot), both of which are now in production! The language I've used the most is Go (namely why this project is in Go), but I've also used Rust, JS, and Solidity.

Since I'll be continuing to work full-time, this project will be done on a part-time basis. As of writing I'm the only person who will be working on this. I estimate I'll be able to put in ~15 hours per week, which might vary week-to-week depending on how busy I am.

# Motivation

Atomic swaps are a method for trustlessly exchanging funds across blockchains. An ETH-XMR atomic swap will allow for users to, in a trustless and completely decentralized manner, exchange Ether for Monero. This connects the leading smart contract blockchain (and the home of defi) with the leading privacy-preserving blockchain. Along with the BTC-XMR atomic swaps, this will allow for completely decentralized cross-chain exchanges to be built that allow for XMR swaps. 

# Milestones

## 1. Maintenance of existing codebase (estimated 2 weeks)
This includes:
- improved unit tests, >70% test coverage for whole repo
- inline documentation (ie. code-level docs)
- JSON-RPC API documentation
- general code cleanup

## 2. Swap contract improvements (estimated 2 weeks)
There is already a smart contract (Swap.sol) that implements the Ethereum on-chain side of the protocol. However, to reduce gas costs, this can be turned into a "factory" style contract that allows users to create swap instances without having to re-deploy a contract, thus allowing for gas savings. 

This milestone includes:
- Creation of swap factory contract
- Testing and integration of contract with codebase
- Documentation on how to deploy the swap contract ot any EVM-based chain and interact with it 

## 3. DLEq integration (estimated 2-4 weeks)
For background, monero uses the ed25519 elliptic curve and ethereum uses the secp256k1 elliptic curve. The current implementation of the protocol verifies that a secret corresponds to a valid public key on the ed25519 curve by performing an elliptic curve multiplication (ECMUL). There is a version of the protocol that allows for massive gas savings (~30x improvement on Claim/Refund calls) by moving some of the computation off-chain. This is achieved by allowing secp256k1 keys to be verified on-chain (instead of ed25519), while off-chain, a DLEq proof is passed by each party to the counterparty that proves that their secret corresponds to public keys on both the secp256k1 curve and the ed25519 curve.

This milestone includes:
- Completion of the DLEq version of the swap contract, which performs a secp256k1 ECMUL as the verification step
- Testing of the contract
- DLEq proof generation and verification
  - either using an existing Rust library, potentially using CGO to create language bindings from Rust->Go
  - or, creating a Go implementation of DLEq proof and verification
- Integration with the codebase (updates of network messages and handling of protocol steps)

A potential alternative to using an existing Rust library is to write a DLEq implementation in Go. This would be preferred in the long run as it will be easier for users to build (as they would only been one language installed) and usage of CGO can cause linking issues during build on different platforms. As well as a developer, it's easier to maintain. I would prefer to create a Go implementation for the aforementioned reasons, although it would take longer than using an existing library. However, in the long run, I believe it would save developer hours.

## 4. Integration testing (estimated 2 weeks)
This includes:
- End-to-end testing of the swap from both parties's point of view and for all possible claim/refund cases.
- Will be in the form of Go test cases.

## 5. Network testing and infrastructure (estimated 3 weeks)
This includes:
- setting up infrastructure (servers) to host swap nodes 
- testing of a larger network of swap nodes (10+ nodes) that has many swap providers
- testing of node discovery, messaging, and swap initiation
- testing script to allow for the above cases to be run against a network 

As there will likely be issues that are uncovered while testing, this milestone is assumed to include fixes for those issues.

## 6. Additional research and pre-print paper (estimated 2-4 weeks)
I would like to formalize the existing swap protocol and its variations, and as well to conduct additional research into improvements to the protocol. 

This includes:
- a pre-print paper that describes the current ETH-XMR atomic swap protocol and its security guarantees
- a new version of the protocol that allows the XMR-holding party to move first, as the current protocol is limited by the ETH party needing to lock their funds first
- potential optimizations to the protocol, focusing on ethereum gas costs
- discussion of privacy implications on both the ethereum and monero sides

## 7. UI
This milestone includes an in-browser UI for interacting with the swap network. 

This includes:
- displaying the current swap offers available on the network
- ability for a user to log in with a browser-based Ethereum wallet (Metamask) and take a swap offer

## In case of extra funds

If there are extra funds/time left over, this will be used to investigate the following:
- ERC20 support; ie. ability to directly swap XMR for an ERC20 token
- privacy improvements on the ethereum side
- tor support

## Licensing

The codebase is currently licensed as GPLv3 due to usage of a library that is licensed GPLv3. However, this license can be changed after the DLEq integration (milestone 3) is complete. My preference is for GPL but I will also relicense as LGPL if needed. I would like to stick with GPL or LGPL as it prevents the code from being relicensed and used in closed-source software.

## At completion

At completion of this proposal, there will be a pre-production release of the software that includes binaries for Linux, MacOS and Windows.

# Expiration date

This CCS will expire on February 4 2022.
