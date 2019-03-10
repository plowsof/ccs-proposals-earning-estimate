---
layout: wip
title: Broadcast Transactions over Tor Hidden Service
author: Lee Clagett (vtnerd)
date: November 13, 2018
amount: 142.00 XMR
milestones:
  - name: Socks v4a
    funds: 60.00 XMR
    done: January 28, 2019
    status: finished
  - name: Timing Analysis Mitigations
    funds: 80.00 XMR
    done:
    status: unfinished
  - name: Tor Hidden Service Seed Nodes
    funds: 2.00 XMR
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

## What
Add support to Monero daemon for broadcasting new transactions received over RPC to privacy preserving p2p connections to conceal origin IP. This proposal will use Tor hidden services, but the implementation will be written such that additional anonymity networks (Kovri?) can be added in the future.

### Hidden Service Rationale
Tor can be used today via exit nodes. The issue is the potential for MitM attacks on the data, and blacklisting of the exiting nodes (to help facilitate surrounding node attacks). The recommendation is to use hidden service nodes, like Bitcoin. Users can already force traffic to Tor exit nodes through other techniques.

## Who
Lee Clagett (vtnerd) will be the sole implementer. I have experience contributing code to the Monero daemon, contributing to wallet implementions (simplewallet, mymonero), and vast protocol experience. I am also familiar with some of the literature on privacy networks (this should be obvious in the proposal section).

## Why
Sending transactions can be traced to their origin by ISPs, or other institutions that connect to many peers to trace the first appearance of a transaction. An entire project, Kovri, has been funded to help mitigate this issue. There are things to implement on the Monero side to make use of an anonymity network as well which will be completed with the Tor integration.

## Proposal / Milestones
The proposed rate is 50 USD/hour @ 100 XMR/USD for a total of 142 XMR. The proposal will be implemented in three stages:

### Milestone 1 - Socks v4a
Provide a sock 4a client implementation. A standard library is less desirable - Tor has some extensions for DNS lookup that will be useful in the future. The delivery for this milestone will _not_ be the ability to force all connections to a specific proxy (that is possibly left for a future FFS). The added functionality of this milestone:

- Socks v4a client with Tor extensions.
- Command line switch `--anonymizing-proxy tor,ip:port` which is **only** used for outbound Tor addresses.
- Any `--add-peer` in onion address format will only be used by the `--anonymizing-proxy` connection.
- `--add-exclusive-node` will work with onion addresses. Users could create a private testnet over Tor or a private mixed testnet.
- Command line switch `--anonymous-inbound tor,ip:port` which should only be used by advanced users. This unique ip/port will let the Monero daemon know what connections are coming _in_ from a Tor hidden service setup.
- Connections into `--anonymous-inbound` will have a restricted command set that can be expanded in the future. Most likely only control commands and broadcast transaction. Preventing spamming over Tor is a bit harder since public keys are cheaper to create than IP addresses.
- Network isolation, so that peerlist sharing is only done within the same network type. IPv4/IPv6 peerlists are never shared over Tor and vice-versa. Any future anonymity networks (Kovri) will be isolated from all other networks too. In other words, peerlists through `--anonymizing-proxy tor,...` and `--anonymous-inbound tor,...` will be considered isolated from the others.

After milestone 1, users can test broadcasting over Tor by creating a Tor hidden service manually. It is not recommending at this stage on livenet, because timing analysis is a real threat with Monero transaction volume. **Expected time:** 120 hours (60 XMR).

### Milestone 2 - Timing Analysis Mitigations
A well-known weakness of Tor is the lack of delay in data transmits. This has the side effect of leaking the timing of data transmits through the Tor network, and sometimes the size of a message being sent (if the link is often idle). This timing issue can result in the leaking of transaction origin purely by watching the timing and volume of traffic being sent over Tor. This is particularly problematic with Monero having a lower transaction volume than Bitcoin. This milestone will implement the following:

- "Whitening" of p2p connections through anonymity networks. Try to make data send in constant fixed chunked intervals. This will likely slow-down sending of transactions, but greatly increase privacy. A heavy amount of research will be required - communication via socks connection makes it difficult to control rate.
- Broadcast new transactions over anonymity networks first:
  1. If Monero daemon has at least one p2p connection through an anonymity network:
      1. Send transaction to all p2p connections through anonymity networks. The send rate will not exceed the whitening of the connection.
      2. When transaction is received over non-privacy preserving connection, re-broadcast transaction to all other non-privacy preserving connections. Whitening prevents packet/size/timing analysis and not re-broadcasting over privacy leaks prevents leakage of source (through anonymity connection ... but still).
  2. If no p2p connections through anonymity networks, broadcast to all p2p connections as usual.
- A transaction will not appear in mempool RPC calls until the node receives the transaction over the IP network. This will prevent leaks for users that connect to public nodes (there is no guarantee that the public nodes honor this, obviously).
- Transactions received over p2p links will be immediately forwarded to all p2p connections of the same "zone" (i.e. transaction first received over Tor is immediately sent to all Tor connections)
- Transactions received over p2p links will be randomly delayed (0-30 seconds) before forwarding to other p2p connection zones.

After this milestone, people could use Tor to broadcast transactions safely. **Expected Time:** 160 hours (80 XMR). A considerable amount of time may be necessary for research, and not leaking transactions across these zones.

### Milestone 3 - Tor Hidden Service Seed Nodes
I will have to work with the Monero core team to set this up. This will be similar to the hard-coded seed/bootstrap nodes used for connecting to the Monero network for this first time. These will most likely not be operated by me. This will allow `--anonymizing-proxy` to work without specifying a Tor `--add-peer`.

**Expected time:** 4 hours (2 XMR). Will need additional resources from the community to run the hidden service.

### Errata
Setting up a Tor hidden service will require manual configuration of Tor. A future FFS proposal can implement the Tor control connection protocol (like with Bitcoin). Additionally, this proposal will not provide support for completely hiding the usage of a Monero daemon, because that requires significant additional work to never make a connection outside of Tor.