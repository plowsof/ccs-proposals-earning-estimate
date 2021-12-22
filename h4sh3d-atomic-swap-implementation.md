---
layout: wip
title: Monero Atomic Swaps implementation funding
author: h4sh3d et al.
date: September, 2020
amount: 2727
milestones:
  - name: M1.A.1 User-facing
    funds: 7% (190.89 XMR)
    done: 31 March 2021
    status: finished
  - name: M1.A.2 Service internals
    funds: 3.25% (88.6275 XMR)
    done: 31 March 2021
    status: finished
  - name: M1.B.1 External specification of swap-lib
    funds: 3.25% (88.6275 XMR)
    done: 31 March 2021
    status: finished
  - name: M1.B.2 Internal specification of swap-lib
    funds: 3.25% (88.6275 XMR)
    done: 31 March 2021
    status: finished
  - name: M1.C Specification of chain-syncer
    funds: 3.25% (88.6275 XMR)
    done: 31 March 2021
    status: finished
  - name: M2.A. Cryptographic libraries
    funds: 3.375% (92.03625 XMR)
    done: 15 December 2021
    status: finished
  - name: M2.B. swap-lib
    funds: 11.25% (306.7875 XMR)
    done: 15 December 2021
    status: finished
  - name: M2.C. swap-client
    funds: 5.625% (153.39375 XMR)
    done: 15 December 2021
    status: finished
  - name: M2.D. swap-daemon
    funds: 13.5% (368.145 XMR)
    done: 15 December 2021
    status: finished
  - name: M2.E. chain-syncers
    funds: 11.25% (306.7875 XMR)
    done: 15 December 2021
    status: finished
  - name: M3.A.1 xgroup-dleq-lib
    funds: 8.75% (238.6125 XMR)
    done:
    status: unfinished
  - name: M3.A.2 ecdsa-adaptor-sig
    funds: 8.75% (238.6125 XMR)
    done:
    status: unfinished
  - name: M3.B. chain-syncer
    funds: 5.25% (143.1675 XMR)
    done:
    status: unfinished
  - name: M3.C.1 swap-cli
    funds: 3.5% (95.445 XMR)
    done:
    status: unfinished
  - name: M3.C.2 swap-gui
    funds: 5.25% (143.1675 XMR)
    done:
    status: unfinished
  - name: M3.D. swap-daemon
    funds: 3.5% (95.445 XMR)
    done:
    status: unfinished
payouts:
  - date: 23 April 2021
    amount: 190.89
  - date: 25 April 2021
    amount: 354.51
  - date: 22 December 2021
    amount: 1227.15
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
---

:warning: *DIFFERENT CCS RULES ARE IN PLACE FOR THIS PROPOSAL! PLEASE READ THE FOLLOWING!* :warning:

```
As a trial, this CCS proposal is going to operate on slightly different rules
given the unprecedented scope and duration of this proposal. For this proposal
ONLY, refunds will be issued in the event that the funding is not satisfactory
or the milestones are not completed. This differs from the standard of excess or
unused funds going to the general fund.

To qualify for a refund, the donator must send their tx ID, amount, and return
XMR address to luigi1111@getmonero.org (PGP fingerprint:
FE6D D72A 19CD C5FC 6CB9  1696 BA18 1389 4EDD 58B9, full PGP key at
github.com/monero-project/monero/blob/master/utils/gpg_keys/luigi1111.asc) NO
LATER than ONE WEEK after their donation is made. Any remaining unclaimed funds
(in the event that the proposal is not completed) will be sent to the general
fund as usual. If refunds are to be issued, the funds will be returned via the
provided XMR address.

In summary, the funds can be either:

Unclaimed, leading to the general fund receiving them in the case of a failed
proposal.

Claimed within one week of the donation, leading to a refund in the case of a
failed proposal.

Note: The hope is that the refunds will not be needed, and the proposal will get
funded and completed. In the event of proposal completion, refunds will NOT be
issued. It is only if the proposal is not completed or funded to satisfaction,
and ONLY for this proposal.
```

# Monero Atomic Swap implementation funding

Previous CCS: [Monero Atomic Swaps research funding](https://ccs.getmonero.org/proposals/h4sh3d-atomic-swap-research.html)

Hi everyone,

Three months ago, I posted a CCS for continuing my research on Monero Atomic Swaps. That research is now complete and the results can be found [here](https://www.reddit.com/r/Monero/comments/i1fknt/ccs_results_monero_atomic_swaps_research/). The resulting protocol is implementable today; no more missing crypto! So much so that a PoC was implemented in no time; thank you, kayabaNerve and PlasmaPower! Thus I am reaching out to propose getting a team to work on implementing this protocol, with the end goal of creating a production-ready client/daemon for swapping Bitcoin and Monero. Our design enables to seamlessly extend support for more cryptocurrencies to swap with Monero. It would be very exciting to build that.

You can find the whitepaper that describes the full protocol [here](https://github.com/h4sh3d/xmr-btc-atomic-swap).

A ready-to-use implementation requires a lot of engineering work. Here, my colleagues and I attempt to break down the project into manageable parts, describing the dependencies that have to be fulfilled, and the general roadmap of the project.

## Motivation

Trustless technologies are now emerging, creating the option of refusing to accept counter-party risk. You can make trades with your enemy, as they can't cheat on you. If you don't have to trust, you don't have to know who they are, either.

It is very unlikely that Monero will get banned by all centralized exchanges, but by having an open source atomic swap implementation, such banning mechanism is inefective, as Monero would still be available to anyone who could acquire Bitcoin, which is ubiquitous, and swap the coins online anonymously, trustlessly, with a random peer. Monero will be more robust than ever.

Bitcoin is traceable. This is used to recognize dirty coins, but also for untargeted surveillance and censorship. Bitcoiners, in need of strong privacy, might recognize the utility of a trustless path with low resistance to convert their bitcoin into monero, and become Monero users. 

However, with power comes responsibility, atomic swaps enable users to exchange coins directly with each other. At the same time, if transacted value is significant, honest users MUST carry out their due diligence regarding the origin of the counterparty funds and possibly other anti-money laundering countermeasures, in order to comply with regulations. Trustlessness and no counter-party risk are narrowly defined terms of the atomic-swap literature, that ignores the context whereby the technology is deployed. Bitcoins accumulate dirt in their lifetimes, so swap your monero responsibly, because trustlessly receiving tainted bitcoins is a real counterparty-risk. The counterparties of a swap generate private and blockchain notarized cryptographic proofs of their private agreement, but the court of your jurisdiction might not like that explanation so much. 

The crypto-ecosystem is rapidly moving towards interoperability. Atomic swaps unleash interoperability between Monero and other blockchains. Whether a user needs to open a lighting channel from the monero-bitcoin swap or wants to fund an arbitrary bitcoin contract, the swap protocol exposes the interop socket.

This project will also, as a beneficial side-effect, extend the Monero ecosystem in Rust. Multiple libraries are needed to support the full protocol. Most of them are related to cryptography, for example the "Discrete logarithm equality across groups" algorithm described in the [MRL-0010](https://www.getmonero.org/resources/research-lab/pubs/MRL-0010.pdf) technical note by Sarang Noether (originally proposed by Andrew Poelstra), or directly at the Monero protocol level in the [Monero Rust Library](https://github.com/monero-rs/monero-rs).

Our motivation to build this software is to empower individuals and businesses, who *want* to or *need* to exchange within a strong security and privacy context using P2P, trustless technologies. 

This project has the potential of increasing Monero's liquidity and enabling Monero to get into the hands of more people.

We deem it critical to build this in a manner that fully aligns with the interests of the community. Thus we're reaching out to raise community money, to build this with the community, for the community, enabling the community to preserve its own interests.

### What are we building?
We aim to build a collection of programs---similar to programs you are familiar with, such as the Monero daemon, wallet CLI, or wallet GUI---that have limited functionality individually but as a collection, serve the functions an end-user requires. One can launch these swap programs to exchange coins with a counterparty. We call those programs: swap clients (CLI or GUI), the swap daemon (like the Monero daemon), and chain-syncers (connected to full nodes). In the default configuration, this will mean opening the swap client and letting it launch and manage all other programs involved.

For example, if you, as an end-user, want to acquire monero and have bitcoin, you'll launch a swap client that connects to a swap daemon, and connects to a counterparty that has monero and is looking to trade them for bitcoin at an agreed upon price. The swap client will give you an address where to move your bitcoin and, at the end of the swap, the swap client will display the monero key-pair to import into your wallet. You now own monero. If at some point the swap is canceled for any reason, your bitcoin will be refunded at the address you chose, making this exchange trustless.

Connecting to a counterparty will require knowledge of their daemon's address, and the amounts traded (i.e. the price and quantity). Creating a platform such as a DEX, allowing people to find each other and "auto" connect with the correct arguments or negotiate the price, is out-of-scope for this project. Industry standards for such interfaces are yet to emerge.

## Overview

R&D Institution: Cryp GmbH

Funding: Monero CCS

Duration: 7 months

Job completion: by Q2 2021

Contributors:

 * h4sh3d
 * kayabaNerve
 * lederstrumpf
 * the charlatan
 * zkao

Licenses: The license for the code will be decided based on community feedback. Our current preference is LGPL-3.0. The specification will be released under CC-BY-4.0. 

__Expiration date:__
Funding will remain open until __31.12.2020__. If materially underfunded until __31.12.2020__, we'll either (1) agree with the community to deliver a subset of the deliverables and collect the funds, or (2) discuss how to re-allocate the funds with the community.

## Architecture
The core project will be built in Rust. Rust's good coverage of cryptographic libraries and blockchain protocols, type safety, and language design makes it a very good candidate for such applications (and the prototype is also written in Rust, for the same reasons).

Here we present an overview of the project's architecture. More details of the individual components will be described in a forthcoming section under [Deliverables](#Libraries-and-Components).

#### The figure represents the general architecture of the swap components and their interactions.

![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_3d490af9aeffe7082babf7087ea404f5.png)


#### The following table summarizes different aspects of each component.

|                 | `swap-client`                    | `swap-daemon`                                        | `chain-syncer`     |
|-----------------|----------------------------------|------------------------------------------------------|--------------------|
| definition   | a program that controls the daemon and display the current state | a program that executes the core protocol in a state machine | a program that talks with a specific blockchain |
| cryptographic keys & secrets | private & public    | public only                                          | public only        |
| client/user  | end-user                         | `swap-client`, counterparty `swap-daemon`                | `swap-daemon`        |
| availability          | present at the start and to sign | mostly online, channel of communication between parties | always online      |
| communicates with | `swap-daemon`                      | `swap-client`, `chain-syncer`, counterparty `swap-daemon` | `swap-daemon`, blockchain |
| transactions    | signs                            | creates all transactions, verifies signatures        | listens for and publishes transactions  |
| protocol-state  | doesn't understand protocol, but can represent its state              | understands the protocol, but can't sign             | doesn't understand protocol |


### Client/daemon segregation rationale

The rationale behind segregating the client and the daemon is not for security reasons at the moment (the client signs the transactions received from the daemon blindly, implying full trust), but for the flexibility and extensibility added.

Other clients can be created: mobile applications (that also run the daemon in background), heavy or light desktop GUIs, or even scripted/automated backends (e.g. in a business environment).

### Future extensibility
The atomic swap protocol is just the first instantiation of a more generic interface to other systems---we aim to build this construction abstractly enough to allow clean extension [^1] to future protocols.

## Deliverables
Below is a complete list of our deliverables.

### Specifications
  * Specification of `swap-lib`:
Specify the interface and the requirements for adding support for a new chain, for one or both templates (Bitcoin-like and Monero-like).
  * Specification of `swap-daemon`:
Specify messages passed between `swap-daemon` and: `swap-client` and `swap-daemon`. These include protocol messages exchanged between swap participants, but also specify the medium of communication of `swap-daemon` and those components.
  * Specification of `chain-syncer`:
Specify the functionality and interface `chain-syncer` has to expose in order to permit the `swap-daemon` to carry out swaps. Specify the type of jobs a `chain-syncer` has to implement in order to support executing both templates.

### Libraries and Components
  * `swap-lib`: includes stateless libraries that implement the core protocol, without runtime, disk, nor network implementation. Knows how to create and verify all the transactions involved in the protocol: it understands and handles the crypto verification, including adaptor signatures and DLEQ proofs across groups, and contains two templates for the pair of exchanging chains (Bitcoin-like and Monero-like). The goal of `swap-lib` is to facilitate integration of the base protocol logic of all pairs of chains that implement the two templates, such that adding a new pair, e.g., Litecoin/Monero, only requires implementing Litecoin for the Bitcoin-like template and an `ltc-chain-syncer` (see below).
    * `btc-swap-lib`: an implementation for Bitcoin-like template exchanging bitcoin for monero.
    * `xmr-swap-lib`: an implementation for Monero-like template exchanging monero for bitcoin.

  * `swap-daemon`: implements a daemon, based on `swap-lib`, uses `chain-syncer` as interface to the blockchain world, has the full picture of the state of the cross-chain-swap, as it's aware of the events on both chains and of exchange counterparty protocol messages, it fully understands the protocol, and contains the state machine to execute its respective role in the protocol.

  * `swap-client`: used by the end-user to enter into the protocol, has access to secret keys, uses the `swap-daemon` to execute the protocol, and signs transactions when needed. `swap-client` trusts the daemon completely to execute the protocol on its behalf and to exchange protocol messages with the swap counterparty.
    * `swap-cli`: end-user CLI client that binds to the daemon for executing swaps and reporting the state of an ongoing swap.
    * `swap-gui`: minimal end-user GUI client that binds to the daemon for executing swaps and reporting the state of an ongoing swap.

  * `chain-syncer`: connects and synchronizes the protocol universe to the blockchain universe by following its client's commands (`swap-daemon`). `chain-syncer` knows the transactions of interest based on what its client subscribes to and informs the client in case one of its transactions gets reorged away from the main chain. `chain-syncer` must guarantee to be online during the entire execution of the protocol, and carry out actions on behalf of its clients. It has the ability to play a job and respond with events.
    * `btc-chain-syncer`: a `chain-syncer` connected to a Bitcoin full node, it takes jobs such as listening for transaction confirmation or event-driven transaction broadcast.
    * `xmr-chain-syncer`: a `chain-syncer` connected to a Monero full node, it takes jobs such as listening for transaction confirmation.

  * `xgroup-dleq-lib`: a cryptographic library implementing the [MRL-0010](https://www.getmonero.org/resources/research-lab/pubs/MRL-0010.pdf) technical note. This library must support at least `secp256k1` and `ed25519` curves. `secp256kfun` will be used at first to speed-up the development and will later be replaced by a fork of `libsecp256k1` and `rust-secp256k1`. `dalek-cryptography` will be used for `ed25519` cryptography.

  * `ecdsa-adaptor-sig`: a cryptographic library implementing ECDSA One-time VES over `secp256k1`. We are looking forward to how ["Add ecdsa_adaptor module"](https://github.com/jonasnick/secp256k1/pull/14) evolves and wait on this to add support in `rust-secp256k1`.

Disclaimer: those cryptographic libraries will require review for being considered as safe-to-use in production.

We're currently in discussions with potential academic collaborators to extend the formal coverage of the protocol and its publication. We're also in the process of publishing a preprint of the swap paper on the Cryptology ePrint Archive.

The code will be released mainly under the `monero-rs` and `swap-rs` Github organisations.

## Dependencies

We describe here a list of cryptographic and protocol dependencies likely needed for achieving a complete implementation (some dependencies are readily available, others will have to be extended or newly developed):

 * Monero library for block parsing and for transaction parsing, manipulation, and verification logic
 * Bitcoin library for block parsing and for transaction parsing, signing, manipulation and verification logic
 * RPC and ZMQ libraries for listening to bitcoin and monero nodes; allow reacting and broadcasting transactions depending on the protocol execution
 * Discrete logarithm equality across `secp256k1` and `ed25519` groups library, as described in [MRL-0010](https://www.getmonero.org/resources/research-lab/pubs/MRL-0010.pdf) technical note
 * ECDSA One-time VES over `secp256k1` library as described in [One-Time Verifiably Encrypted Signatures A.K.A. Adaptor Signatures](https://github.com/LLFourn/one-time-VES/blob/master/main.pdf), for signing some parts of the bitcoin transactions
 * ECDSA signing over `secp256k1` library, for signing bitcoin transactions

**Currently available Monero dependencies:**
  * monero (https://github.com/monero-project/monero)
  * monero-rs (https://github.com/monero-rs/monero-rs)
  * monero-rpc-rs (https://github.com/monero-ecosystem/monero-rpc-rs)

**Currently available Bitcoin dependencies:**
  * bitcoin-core (https://github.com/bitcoin/bitcoin)
  * rust-bitcoin (https://github.com/rust-bitcoin/rust-bitcoin)
  * rust-bitcoincore-rpc (https://github.com/rust-bitcoin/rust-bitcoincore-rpc)
  * libsecp256k1 (https://github.com/bitcoin-core/secp256k1)
  * rust-secp256k1 (https://github.com/rust-bitcoin/rust-secp256k1)
  * secp256kfun (https://github.com/LLFourn/secp256kfun); for ECDSA One-time VES over `secp256k1` signing implementation and prototyping DLEQ proofs

**Currently available general dependencies:**
  * rust-zmq (https://github.com/erickt/rust-zmq)
  * rust-libp2p (https://github.com/libp2p/rust-libp2p); as an option for daemon peer-to-peer communication
  * dalek-cryptography (https://github.com/dalek-cryptography); for `ed25519` arithmetic/curve operations

## Milestones

We split the principal milestones (1, 2, and 3) into unordered sub-milestones, each releasing a fraction of the total funds for their principal milestone.

The goal is to share the advance of each individual sub-milestones in biweekly progress reports.

![Milestone structure](https://codimd.s3.shivering-isles.com/demo/uploads/upload_7e18990edf9fa4fbf3ddbe0125e8d105.png)

### Milestone 1 (specs): 20% [6 weeks]

 * **Technical specifications:** a list of specifications that covers all aspects of the protocol, resembling specifications such as BOLT for Lightning network or Cryptonote.
 
The specifications will demarcate which functionality falls in scope of the implementation in Milestone 2, and which functionality will be postponed to Milestone 3.
 

#### A. Specification of `swap-daemon`
Detailed description and specification of the `swap-daemon`, internal and external.

#### A.1 User-facing [35% of M1] [2 weeks]
* Specify `swap-daemon`'s outer API layer of user interaction (`swap-client`s & counterparty `swap-daemon`) first to guide design of inner dependencies (`swap-lib` & `chain-syncer`) to match desired UX. This includes protocol messages exchanged between swap participants, that is: interactions with the counterparty `swap-daemon`.
* Specify the API that `swap-cli` and `swap-gui` consume from `swap-daemon`.
* Specify the networking stack between `swap-daemon` and: `swap-daemon` counterparty and `swap-client`s.

#### A.2 Service internals [16.25% of M1] [1 week]
Specify links between `swap-daemon` and the other deliverables it requires to facilitate a swap, but that are not user-facing, i.e. `swap-lib` and `chain-syncer`s:
* Specify the subset of `swap-lib`'s API strictly required for `swap-daemon`'s operation
* Specify API and network stack for `swap-daemon`'s required calls to `chain-syncer`s

#### B. Specification of `swap-lib` (core protocol)
Detailed description and specification of all the libraries that, in conjunction, form `swap-lib`, including stateless transaction construction libraries, crypto-libraries and their wrappers, and state-machine libraries for executing the protocol.

#### B.1 External specification of `swap-lib` [16.25% of M1] [1 week]
* Specify `swap-lib`'s public API to be consumed by `swap-daemon` only.
Preliminarily, covers `InitTx()`, `VrfyTx()`, `Vrfy()`, and `EncVrfy()` from the whitepaper.
* Specify `swap-lib`'s public API to be consumed by `swap-client`s only.
Preliminarily, covers `Sign()`, `EncSign()`, `DecSig()`, `RecKey()`, and `Rec()` from the whitepaper.
* Specify `swap-lib`'s public API to be consumed by both `swap-daemon` and `swap-client`s.

#### B.2 Internal specification of `swap-lib` [16.25% of M1] [1 week]
* Specify internal function calls of `swap-lib`.
* Specify a concrete implementation to support a chain, including all cryptographic primitives that must be supported.

#### C. Specification of `chain-syncer` [16.25% of M1] [1 week]
* Specify the functionality and interface `chain-syncer` has to expose in order to permit the `swap-daemon` to carry out swaps. Describe what jobs are, and what jobs must be supported.
* Specify the networking stack between `swap-daemon` and `chain-syncer`s.

A core goal of the spec-writing process is to ensure that the deliverables are compatible and functional in the sum of their parts. This process in Milestone 1 thus aims to identify limitations of the architecture presented in this proposal, which can impact the structure of Milestones 2 and 3. In case changes are consequently required, we will propose them to the community at the completion of Milestone 1, and we will ensure that the same final functionality as set out in this proposal will be delivered.

### Milestone 2 (implementation of core architecture): 45% [14 weeks]

 * **Minimal functionality:** at completion-time of milestone 2, all components for executing atomic swaps successfully are implemented using our libraries as proposed in the presented architecture.
 * **BETA STATE:** the software released is considered to be beta software and not ready for deployment.

This milestone achieves the initial implementation of all the components (without GUI client) interacting with each other. It implements only the minimally required functionalities specified in the specifications (Milestone 1).


#### A. Cryptographic libraries [7.5% of M2] [1 week]
For milestone 2 we intend to use Lloyd's experimental library for ECSA adaptor signatures (`ecdsa-adaptor-sig`) and DLEQ proofs (`xgroup-dleq-lib`).

We postpone the integration of a production-grade ECDSA adaptor signatures to the end of the project, namely milestone 3, as it is highly complex, and this gives tooling more time to mature. In case Bitcoin incorporates Schnorr signatures soon (BIP 340), ECDSA adaptor signatures may also not be needed and would then be replaced with Schnorr adaptor signatures.

At completion, we provide generic cryptographic libraries that expose a high level API, comparable to how `rust-secp256k1` exposes a high level API for ECDSA signatures over `secp256k1`.

#### A.1 `xgroup-dleq-lib`
Experimental discrete-log equality across groups library using secp256kfun. At completion, this library enables zk-proving discrete log equality across groups `secp256k1` and `ed25519` for arbitrary private keys.

#### A.2 `ecdsa-adaptor-sig`
Experimental ecdsa-adaptor signature library using secp256kfun. At completion, this library enables producing and verifying ecdsa-adaptor signatures, and extracting secrets from clear and encrypted signatures.

#### B. `swap-lib` [25% of M2] [4 weeks]
`swap-lib` is the core for adding support for a new chain, either via the Bitcoin-like template or the Monero-like template. At completion, this library is an interface for enforcing the requirements of `swap-daemon` and `swap-client` for a selected chain, and the requirements for each `chain-syncer` type.

#### B.1 `xmr-swap-lib`
A concrete implementation of `swap-lib` that allows the creation of a `swap-daemon` and a `swap-client` for exchanging monero for bitcoin.

#### B.2 `btc-swap-lib`
A concrete implementation of `swap-lib` that allows the creation of a `swap-daemon` and a `swap-client` for exchanging bitcoin for monero.

#### C. `swap-client`s [12.5% of M2] [2 weeks]
At completion of Milestone 2, we provide only the `swap-cli` client.

#### C.1 `swap-cli`
A CLI client utilizing `swap-daemon`'s API for executing swaps. At completion, a minimal CLI client for running Bitcoin and Monero swaps will be delivered.
* `swap-cli` can initialize a `swap-daemon` with parameters for a swap (swap-pair, swap-direction, counterparty daemon address, swap-amount, exchange-rate).
* `swap-cli` can sign transactions the `swap-daemon` provides.
* `swap-cli` sends signed transactions back to the `swap-daemon`.

#### D. `swap-daemon` [30% of M2] [4 weeks]
At completion, `swap-daemon` enables `swap-client` to successfully swap bitcoin for monero. 

It coordinates all aspects of the swap by communicating with `swap-client`, `chain-syncer`s and the counterparty's `swap-daemon`. It exposes an RPC server for client interaction. 

At this stage:
  - `swap-daemon` understands the semantics of all the public keys, unsigned, signed and partially-signed transactions, hash pre-images, and encrypted signatures involved in the protocol.
  - has the full picture of the state of the cross-chain-swap, as it's aware of the events on both chains; each `chain-syncer` only has a partial view. `swap-daemon` knows the off-chain events as well.
  - protocol implemented in 2 varieties: (1) one for executing btc-sender/xmr-receiver protocol (`btc->xmr`) and (2) another for xmr-sender/btc-receiver protocol (`xmr->btc`). In conjunction these 2 protocols cover the full protocol. 
  - at run-time, each `swap-daemon` instantiates a state-machine of only one of the varieties: either `xmr->btc` or `btc->xmr`.
  - at run-time, the daemon can start in a master or slave mode. In master mode, `swap-daemon` accepts entering connections, in slave mode `swap-daemon` tries to connect to a counterparty daemon.
  - reveals a high level API that lets `swap-client`s run the protocol.

#### E. `chain-syncer`s [25% of M2] [3 weeks]
At completion, `chain-syncer` exposes enough functionality to permit the `swap-daemon` to carry out swaps between Monero and Bitcoin. It does not publish transactions on behalf of its client yet (e.g. `do X once Y`), just listens to transactions of interest and blocks, process them and push events to the `swap-daemon` (i.e. `chain-syncer`'s client). It also exposes functionality for clients to publish transactions to the blockchain, if needed.

All `chain-syncer`s implement the base functionality:
* interface to `swap-daemon`
* read transactions (arriving in the mempool, or with a number of confirmations)
* read new blocks
* detect block re-orgs

#### E.1 `btc-chain-syncer`
A bitcoin concrete implementation of the `chain-syncer`.
In addition to the base functionality, `btc-chain-syncer`:
* connects to bitcoin full-node
* broadcasts transactions

#### E.2 `xmr-chain-syncer`
A monero concrete implementation of the `chain-syncer`.
In addition to the base functionality, `xmr-chain-syncer`:
* connects to monero full-node

### Milestone 3 (minimum viable product): 35% [12 weeks]

 * **Full integration of individual components:** the entire functionality as defined in the specs is now implemented.
 * **MVP STATE:** the software released is considered as stable for a minimum viable product.

At this stage, we replace/finish some components of Milestone 2 with MVP grade components, meaning all features specified in Milestone 1 are implemented.

#### A. Cryptographic libraries
At completion of this task, cryptographic libraries should benefit from more reviewed and more stable codebases.

#### A.1 `xgroup-dleq-lib` [25% of M3] [3 weeks]
We upgrade `xgroup-dleq-lib` to use `rust-secp256k1` (fork or mainstream) and dalek. The goal is to implement in C in `libsecp256k1` the high level API needed for cross group discrete logarithm equality proofs with `secp256k1` curve and update `rust-secp256k1` bindings (fork or mainstream).

#### A.2 `ecdsa-adaptor-sig` [25% of M3] [3 weeks]
We upgrade `ecdsa-adaptor-sig` to use `rust-secp256k1` (fork or mainstream), based of the C implementation in `libsecp256k1` currently in progress [here](https://github.com/jonasnick/secp256k1/pull/14).

#### B. `chain-syncer` [15% of M3] [2 week]
We upgrade the `chain-syncer`s to enable pattern such as: `do X if Y`. This allows other daemon requirements to be supported, i.e. a daemon can be written such that going offline for a small amount of time is not problematic, allowing e.g. mobile daemons.
* `swap-daemon` can queue tasks such as `execute refund path at block height X` with a `chain-syncer`.

#### C. `swap-client`s
We improve `swap-cli` and release a new web-based GUI client, `swap-gui`.

#### C.1 `swap-cli` [10% of M3] [1 week]
`swap-cli` exposes additional functionality and better UI/UX:
* during a swap, `swap-daemon` relays to `swap-cli` what actions are currently available to `swap-cli`, and future actions that will become available after `n` blocks.
* `swap-daemon` pushes updates to `swap-cli`, in lieu of the `swap-cli` pulling from the `swap-daemon`.
* `swap-cli` can schedule actions to be performed by `chain-syncer`s, as via the upgrade specified in M3.B.

#### C.2 `swap-gui` [15% of M3] [2 weeks]
A minimal web-based GUI client, `swap-gui`. Cryptographic requirements will be fulfilled with WASM or might be embedded as native libraries on an Electron webapp.
* `swap-gui` covers the functionality of `swap-cli` as implemented at the end of M2.
* web-based GUI that interacts with `swap-daemon` API.

#### D. `swap-daemon` [10% of M3] [1 weeks]
Implements all features defined in the specification for `swap-daemon`.

## Cost
We ask for 2727 XMR from CCS.

For further information on our crowdfunding, please visit https://cryp.ee/crowdfund or write to us at crowdfund@cryp.ee (PGP fingerprint `A873 CF81 AAFE C016 EC1A  14BB D889 86F7 A3F7 37C4`[^2]).

## Feedback
Due to the size of this project and the funding required for it, questions, comments, and feedback regarding this request are very welcome.

### Communication channel
Besides the MR comments on GitLab and the Monero IRC channels such as `#monero-community` and `#monero-research-lab`, we opened the `#monero-swap` IRC channel for crowdfunding questions, project updates, and work management during the development time-frame.

We commit to make ourselves highly available for the community of researchers and developers, such as participating in MRL meetings, sharing progress, incorporating/giving feedback from/to the community in general, and responding to general inquiries, if they fall under our expertise.

[^1]: A plausible extension path towards a generic interface is to initialize the daemon with a Petri net representation of a protocol, together with a set of places that the client is in control of - in lieu of them choosing a role from n-ary options.
[^2]: Full PGP key for crowdfund@cryp.ee:  
`-----BEGIN PGP PUBLIC KEY BLOCK-----`  
`Version: OpenPGP.js v4.10.8`  
`Comment: https://openpgpjs.org`  
`xjMEX4G6hRYJKwYBBAHaRw8BAQdAyb5mTWxnbmIqpRExJbZPg6McQK/nTFF0`  
`kgLd20WRMlbNJWNyb3dkZnVuZEBjcnlwLmVlIDxjcm93ZGZ1bmRAY3J5cC5l`  
`ZT7CjwQQFgoAIAUCX4G6hQYLCQcIAwIEFQgKAgQWAgEAAhkBAhsDAh4BACEJ`  
`EF+QaJfwBcaZFiEE55TK0pvlX5ijxFP+X5Bol/AFxpldtgEAlNrZjg5XRDdl`  
`SmPFZQWvCenIgRXnxe9G4BD529yz5zsA/0/xmq7N19VfpjOecoKl+vyxBBsq`  
`HiZ6zTNGzeBhr7gEzjgEX4G6hRIKKwYBBAGXVQEFAQEHQL5lk0xlsP59tESA`  
`h9L8GhCAt5xdOFbYLf7jGyUpjLp3AwEIB8J4BBgWCAAJBQJfgbqFAhsMACEJ`  
`EF+QaJfwBcaZFiEE55TK0pvlX5ijxFP+X5Bol/AFxpncCwEAm9hTDBjRgOIC`  
`nZs+2mgmDH0kCAsgwNCLmILfeZ1vbHwBAOwIZgrS74gFKsaeToDoizbF8ecW`  
`YqxRx7GzcX0NYoUK`  
`=oDUJ`  
`-----END PGP PUBLIC KEY BLOCK-----`
