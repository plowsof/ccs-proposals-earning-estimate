---
layout: cp
title: "jeffro256: part-time dev work 2022Q3"
author: jeffro256
date: 17 May 2022
amount: 60
milestones:
  - name: Month 1
    funds: 33% (20 XMR)
    done: 23 September 2022
    status: finished
  - name: Month 2
    funds: 33% (20 XMR)
    done: 19 November 2022
    status: finished
  - name: Month 3
    funds: 34% (20 XMR)
    done: 4 April 2023
    status: finished
payouts:
  - date: 24 October 2022
    amount: 20
  - date: 29 December 2022
    amount: 20
  - date: 11 May 2023
    amount: 20
---


## What

I propose to spend 20 hours a week for 3 months working on Monero Core and the Monero GUI. Here are some areas, in tentative order of descending importance/specificity, that I'd work on:

1. Work with @selsta to protect GUI users in "simple mode" by implementing a trusted community node system
2. Create a RPC SSL connection integrity indicator for the CLI and GUI wallets
3. Allow GUI users more fine-grained control of their SSL connections
4. Create a more thorough UI for warning users of GUI mode of high fees
5. Draft a formal Levin/Cryptonote protocol specification
6. Revamp Doxygen documentation
7. Do other general documentation of the codebase
8. Transition legacy OpenSSL code to comply with OpenSSL 3.0 (already started)
9. Explore using faster & smaller EC OpenSSL certificates in place of traditional RSA certificates
10. Continue to remove dead code, and simplify codebase, especially the (epee module)[https://github.com/monero-project/monero/pull/8211]
12. Misc developing / reviews

## Who

My name is Jeffrey; I am currently working on completing a computer science major with a minor in both cybersecurity and mathematics. I have always been fascinated with cryptography and digital privacy, so learning about Monero during the altcoin boom of 2017 was eye-opening and exciting. Soon enough, supporting Monero became a no-brainer for someone who is passionate about digital privacy.

I got my first PR merged on March 18th, and you can see the rest of them here: <https://github.com/monero-project/monero/pulls?q=is%3Apr+is%3Amerged+author%3Ajeffro256>. So far I have been doing it as a hobby, but I would love to spend more time on this project than I currently am, as I am rather busy with schoolwork and my job. As this is my first CCS proposal, I am very open to criticism and questions, so don't be afraid to ask! I will do my best to respond in the comments below.

## Why

### Trusted community node system and high fees (1 & 4)

As can be seen in [this issue](https://github.com/monero-project/monero/issues/8298), among others, there appear to be malicious node(s) which advertise themselves as public nodes, allow users using the GUI wallet in "simple node" to connect, and respond with insanely high fees. This issue runs even deeper, and this exploit can be used to deanonymize GUI users to a certain degree in simple mode when they send transactions. There's no replacement for running your own node (and double-checking your fee amounts), but for those who choose not to, they should be able to expect at a minimum to not have their funds stolen from them.

### RPC connection integrity indicator and fine-grained SSL control (2 & 3)

Getting SSL right is difficult and nuanced. You can verify with system certificates, user-supplied certificates, accept any connection as long as it is secured, or any combination of these options. You can have certificates which sign other certificates. As it stands, the way the GUI wallet secures connections is not ideal. It more or less accepts any connection, using SSL if its available, but for no specific ccertificate, and there is not a way to specify how to connect with SSL (unlike in the CLI wallet). I want to afford the users two things: the ability to quickly asses the quality of their connections to their nodes via an elegant UI element, and the ability to tweak their SSL settings if so desired.

### Levin/Cryptonote Specification (5)

Unclear protocols cause bugs and choke out emerging projects which wish to incorporate into the ecosystem. Here are a couple recent PRs to fix bugs with the p2p/relay code:

* <https://github.com/monero-project/monero/pull/8330>
* <https://github.com/monero-project/monero/pull/8326>
* <https://github.com/monero-project/monero/pull/8324>

While it would be quite a feat to document ALL of the cryptonote protocol, it could be helpful to more thoroughly document the Levin protocol commands and the expectations surrounding the calls (interface, relay rules, ban criteria, etc). The p2p protocol of Monero is useful not only for nodes, but also for wallets and light wallet servers, especially when using untrusted connections. This was already started in [this document](https://github.com/monero-project/monero/blob/master/docs/LEVIN_PROTOCOL.md), but could certainly be fleshed out.

### OpenSSL 3.0 Compatibility (8)

It's always a nice thing to have your code compile on all your targets. In newer versions of OpenSSL, they have deprecated a large portion of the API, much of which we rely on to secure connections in Monero, particularly RPC.

### EC OpenSSL certificates (9)

Currently, we use RSA certificates for RPC SSL, but EC certificates are smaller and thus faster. This could offer speed improvements while syncing, etc. @HYC suggested the idea while I was working on moving certain parts of the codebase to OpenSSL 3.0: <https://github.com/monero-project/monero/pull/8335>.

### Nice-to-haves (6, 7, 10, 11)

All of these points do not directly affect the end-user experience but will ultimately improve the developer experience, reducing friction in the future, contributing to the long-term health of the codebase.

## Funding
* Wage: 30 USD/hr
* Hours: 12 weeks x 20 hours/week = 240 hours
* Total pay in USD: 240 hours x 30 USD/hr = $7200 USD
* Exchange rate: $116.41 USD/XMR. Calculated from one week simple average of closing prices on coinmarketcap.com
  * 24 June: $126.47
  * 23 June: $122.70
  * 22 June: $111.18
  * 21 June: $118.80
  * 20 June: $117.30
  * 19 June: $114.22
  * 18 June: $104.18
* Total pay in XMR: $7200 USD / $116.41 USD/XMR = 61.85 XMR

Expiration Date
1 August, 2022

