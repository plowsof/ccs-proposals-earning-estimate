---
layout: wip
title: "Decentralizing Molly.im to support Monero payments"
author: valldrac
date: Sep 27, 2021
amount: 177
milestones:
  - name: Signal server deployment
    funds: 12.5% (22 XMR)
    done:
    status: unfinished
  - name: Monero payments
    funds: 70.0% (124 XMR)
    done:
    status: unfinished
  - name: E2E testing
    funds: 17.5% (31 XMR)
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

### Summary

The goal is to build a secure messaging app with integrated support for Monero payments and a decentralized backend.

The application will be based on the Signal fork [Molly.im](https://molly.im) (henceforth 'Molly') but with a privacy-focused backend that allows the user to sign up anonymously (without phone number), encrypt their local database with passphrase encryption, RAM shredding, and more.

Monero features will include the ability to set up a XMR wallet, send and receive funds, keep track of the balance, and review the transaction history.

### About Molly

Molly is a fork of Signal for Android which began in 2019. Molly connects to the Signal servers and adheres to the Signal protocol, so Molly users can chat with their Signal contacts seamlessly. Over the last two years it has become a popular alternative to the official Signal and Signal FOSS clients for its improved security features, open source friendly approach, and growing community of contributors of all kinds.

As we rely on the Signal for the server infrastructure we must adhere to Signal rules and limitations. All Molly features are improvements of the standard Signal client.

Officially Signal takes the stance that they do not allow forks to connect to their servers. This has not always applied in practice since many projects exist that use their infrastructure. There is the risk, however, that Signal could at any time decide to enforce this policy in the future. While Signal could make the decision to disable forks, it is believed is not technically feasible to ban Molly from the Signal servers without banning also all devices without Google GMS services. This is due to the fact that the Molly app is identical to Signal from the server side.

At present we want to decentralize the Molly backend. Signal currently offers no protection against traffic analysis and metadata harvesting in the server side. Molly can offer this improvement with a properly implemented decentralized backend.

Links:
- Website: [molly.im](https://molly.im)
- GitHub: [mollyim/mollyim-android](https://github.com/mollyim/mollyim-android)
- OpenCollective: [mollyim](https://opencollective.com/mollyim)
- Twitter: [@mollyimapp](https://twitter.com/mollyimapp)

### MobileCoin Status

MobileCoin payments in Signal are enabled only in a few countries: UK, Germany, France, and Switzerland. This restriction is enforced by the server. Recently the MobileCoin Foundation launched an [airdrop campaign](https://mobilecoinfoundation.medium.com/test-your-mobilecoin-wallet-through-a-beta-air-drop-7096b9dd9153) on Signal.

MobileCoin has been disabled in Molly since the beginning of MobileCoin release.

### Proposal & Milestones

Showcase in-app payments with minimal setup. It includes the following phases:
1. Deploying a minimal Signal compliant server
2. Build a flavor of Molly that replaces MobileCoin with Monero and connects to this server
3. Add automated end-to-end (E2E) testing to support further development

High-level functionalities to be developed for payments:
- Activate and deactivate payments
- View transaction history and details
- Change currency conversion for displayed balance (tentative)
- Send a payment in-chat
- Request a payment in-chat
- Restore wallet from mnemonic seed
- View wallet mnemonic seed and keys
- Transfer in
- Transfer out

The server, for this stage, will be a monolithic instance of [Signal server](https://github.com/signalapp/Signal-Server) deployed in AWS. It will support basic messaging features but will not support audio/video calls, SGX dependent services like: PIN cloud backups, contact discovery, or multi-device support. There will not be phone number validation, it will be replaced with random virtual number generation to emulate the use of a validated phone number for the user at registration.

This environment is not expected to scale to more than 10K simultaneous users and will not provide a production-ready or reliable service for end users. For the purpose of this stage this server could be considered "pre-production/staging server".

The Molly app will continue to be updated in its current form in the interim. In order to integrate the new Monero payment feature while preserving the Signal based functions a welcome screen will be implemented with the following two choices:

1. Sign up to the Signal Network: MobileCoin disabled, all other features functional.
2. Sign up to the Molly Network: Native Monero payments and no phone number required to register.

The Signal network will not support native Monero payments. There will, however, be a button to share the Monero address manually and request the recipient to initiate a payment.

We estimate to complete this stage in approximately 20 weeks time by executing the following three steps: (i) Signal server deployment ~2.5 weeks. (ii) Monero payment functionality development ~14 weeks, (iii) E2E testing ~3.5 weeks.

### Goals

- Provide an experimental but fully functional messaging app with XMR payments to the Monero community
- Identify pain points with Monero SDK early in the development cycle
- Evaluate the security of the integration and ensure it meets Molly's security requirements for data-at-rest
- Learn about Signal server and further our understanding of the codebase
- Continue to grow the Molly userbase 
- Prepare the framework for stage 2

### Funding

We are at this time requesting funding of 177 XMR (equivalent of $38,150) as per 14-day EMA (1 XMR = \$248.05) on Kraken for 2021/09/26 with a 15% volatility buffer. This is based on the previous outline which we anticipate will take a total of 650 hours of development to bring to fruition across our 20 weeks timeline. Below is a high level overview of where the exact funding will go:

- Development cost: \$55 x 650 hours (total of \$35,750)
- Hosting expenses (AWS) until Q2 2022: \$2,400

### Next Steps

With the action taken in stage 1 we are effectively deploying the framework on which the Molly app can forge itself.

Once stage 1 is complete, we will be in a position to further our research on mixnets and other possible backend solutions. Through this process we maintain the deployed Signal server for additional use cases that may arise during the development period.

A security audit would be the logical follow up to the implementation of Monero payments. This audit would encompass distinct Molly functions over Signal as well. Once audit findings are resolved, we will be able to ensure that we are meeting the security standards expected by privacy-focused communities. We expect our development will onboard new collaborators of all kinds to the project. Peer-reviewers will likely increase in number as a result of the audit as well.

Additionally, we would design and deploy a website with robust Molly documentation, news, and more.

### About Me

Currently I am the lead developer of Molly. 

I am a security engineer specializing in offensive security and cryptography, and a former forensic analyst. I began learning Android app development 2 years ago for Molly specifically. Recently my career became completely focused on mobile security.
