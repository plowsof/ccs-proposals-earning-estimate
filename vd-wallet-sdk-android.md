---
layout: wip
title: Wallet SDK for Android
author: valldrac
date: May 17, 2023
amount: 295
milestones:
  - name: Development
    funds: 180 XMR
    done: 4 March 2024
    status: finished
  - name: Security Enhancements
    funds: 24 XMR
    done: 12 August 2024
    status: finished
  - name: Continuous Integration & Testing
    funds: 51 XMR
    done:
    status: unfinished
  - name: Maintenance (3 months)
    funds: 20 XMR
    done:
    status: unfinished
  - name: Maintenance (3 months)
    funds: 20 XMR
    done:
    status: unfinished
payouts:
  - date: 21 March 2024
    amount: 180
  - date: 14 August 2024
    amount: 24
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
---

### Summary

We propose supporting the development of the new Monero SDK for Android that the [Molly.im](https://molly.im) team is actively working on.

The goal of this SDK is to provide a solution for developers to integrate Monero into their apps by offering an Android wallet library and a sample app. The library will include advanced features such as support for multiple wallets, sandboxed C++ code, client-side load balancing and asynchronous API. It will be compatible with Android Studio and fully optimized for size and performance. The demo app will feature the capabilities of the library, using the best practices and tools.

The development of this SDK aims to resolve issues found in existing libraries during the integration of Monero into Molly. If you would like to know the rationale behind this SDK, and learn about the Molly project and background, we recommend checking out our CCS titled "Decentralizing Molly.im to support Monero payments" and the latest follow-up at the following links: [CCS proposal](https://ccs.getmonero.org/proposals/vd-molly-payments-stage1.html) and [update post](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/252#note_20900).

### SDK Overview

The Monero SDK consists of two components:

1. **Android Library**: A specialized library that allows developers to interact with the Monero network and perform wallet operations. This library is written in Kotlin and offers a reliable asynchronous API.

2. **Sample Wallet App**: An example app written in Kotlin that showcases the usage of the library for wallet app development. It serves as an integration guide for developers and facilitates the testing of new functionalities.

### Android Library

The Android library is the core component of the SDK. Internally it wraps and extends the wallet2 low-level API.

Key features and design decisions of the Android library include:

- **Kotlin Language**: The library is implemented in Kotlin, which is the preferred language for Android development. Kotlin's interoperability with Java ensures compatibility with existing apps.

- **Asynchronous API**: It leverages Kotlin's Coroutines support for asynchronous programming, providing a reliable and non-blocking API that seamlessly integrates with Android's event-driven development model.

- **Sandboxed Execution**: All non-memory-safe code (C++) runs within an isolated process with zero privileges and restricted access to the host app or system resources. Even if a remote execution exploit affects Monero, it becomes extremely difficult for an attacker to elevate privileges to the system or host app.

- **Modular Architecture**: The library is built as an Android service, using Android's AIDL interprocess communication (IPC) to connect the Kotlin layer with the sandboxed native code. This client-server architecture decouples the internal wallet2 implementation from the public API of the SDK, facilitating future swapping of the wallet2 module without major changes to the API. This enables smoother migration to Seraphis for developers using our SDK.

- **Storage Abstraction**: The library provides a storage abstraction layer, simplifying wallet persistence for developers. It allows the SDK to be agnostic about the underlying storage mechanism (files, database, cloud, etc.). This flexibility enables developers to improve data-at-rest encryption without modifying the SDK code.

- **Network Client Injection**: Instead of relying on the networking code of wallet2, the SDK allows the app to provide its own HTTP client. This gives the app the freedom to support any transport protocol, such as Tor, transparently to the SDK.

- **Custom Logging**: The library includes a logging adapter that developers can customize. It enables the host app to determine log storage and location, providing a way to encrypt or remove sensitive information from the logs if needed.

- **Client-side Load Balancing**: The library enables the host app to dynamically select the optimal remote node for RPC calls, ensuring efficient synchronization with the Monero blockchain. This can significantly reduce synchronization time by choosing the fastest node.

- **Android Studio Compatibility**: The SDK is fully compatible with Android Studio, supporting native debugging, code navigation, and linter capabilities, for both the SDK library and the Monero codebase.

- **Optimized Build System**: The  library has optimized CMake files that vendor all dependencies of wallet2, and applies Link-time optimizations (LTO) to remove all C++ code that is never called by the SDK. The result is a reproducible and lightweight library size of only 6 MB per arch, that can be built directly from Gradle.

### Sample Wallet App

The sample app is a fully functional multi-wallet app that serves as a reference for developers on integrating Monero into their apps. It is also a way to test if the library works well in a real-world application. Key features of the sample wallet app include:

- **Clean Architecture**: The sample app uses the latest Android libraries and follows the [official architecture guidance](https://developer.android.com/topic/architecture#recommended-app-arch).

- **Kotlin and Jetpack Compose**: The sample app is entirely written in Kotlin and uses Jetpack Compose for the UI, as well as many architecture components like Room, Lifecycle, and Navigation.

### Use Cases

The SDK is primarily designed to support two use cases: (i) local synchronized mobile wallets and (ii) Monero payments, with a focus on security, simplicity and performance. Although we are centered on these specific use cases, it would be beneficial to consider other potential applications where the SDK could be used in the future.

In the first stable release, it is planned to provide the following functionality:

1. Wallet Management
   1. Create and restore wallet from mnemonic seed (25-words standard) or secret key
   2. Export wallet seed and secret key
   3. Save and load wallet from the storage defined by the app
2. Account Generation and Subaddresses
   1. Derive account subaddresses and track their usage
   2. Parse base58 public addresses
3. Balance Inquiry
   1. Query locked/unlocked balance at a specific time
   2. Retrieve transaction history
   3. Listen to balance and transaction (ledger) updates
4. Transaction Handling
   1. Construct, sign, and broadcast single and multi-recipient TXs 
   2. Handle network fee automatically
   3. Create and verify payment proofs
5. Blockchain Synchronization
   1. Resume scanning or restart it from a specific height
   2. Load balance RPC calls and failover to multiple remote nodes
   3. Monitor remote node status and response time

The following features would be left out of the first release: fine-grained coin control, hardware wallets, manual transaction input, message signing, and multisig. There is no roadmap or timeline yet for when these additional features will be included in future releases.

### Code Example

This snippet of code is a basic example to show how to use the API: [wallet-sdk-android-example.kt](https://gist.github.com/valldrac/54ff6842e4cc6d624ab893f4e839b2ae)

### Limitations and Known Issues

The biggest issue we have come across is how wallet2 trusts the remote nodes for blockchain synchronization. While it is widely known that malicious nodes can manipulate the returned blocks to deceive clients, the current lack of validation in wallet2 makes it too easy to exploit. Unfortunately, wallet2 fails to verify if the returned blocks line up with the previous blocks in the chain. This vulnerability has already been described in a security advisory ([link](https://www.reddit.com/r/Monero/comments/134jbdt/security_advisory_new_attack_from_malicious/)).

To mitigate this problem, we suggest adding basic integrity checks into wallet2, but without validating PoW. These checks will help wallet2 to early detect the attack when connecting to an honest node.

Our plan is to address this issue for the initial release of the SDK, as well as upstream the fixes to wallet2.

### Comparative Analysis

The main difference, in addition to the aspects mentioned in the design section, is that the existing libraries are essentially "library wrappers". They consist of a thin layer of code that translates the wallet2 API into a compatible interface for Java while maintaining the same (and intricate) semantics. However, in our SDK we have tried to develop a simplified yet flexible API explicitly designed for Android that prevents common pitfalls associated with wallet2.

It is important to note that we have not conducted a comprehensive comparative analysis yet between our SDK and existing Java libraries like Monerujo's [xmrwallet](https://github.com/m2049r/xmrwallet) or woodser's [monero-java](https://github.com/monero-ecosystem/monero-java).

### Progress Report

The development progress of the library API at a high-level is as follows:

- Wallet Management: 90% complete.
- Account Generation and Subaddresses: 20% complete.
- Balance Inquiry: 70% complete.
- Transaction Handling: 0% complete.
- Blockchain Synchronization: 80% complete.

We have made significant progress in the demo wallet app as well, implementing key features such as multiple wallet creation, customizable settings, balance checking, and individual remote node configuration for each wallet. The demo includes a basic syncing service that automatically refreshes and saves the wallets. It also supports syncing over SOCKS proxies.

Based on the progress made so far, we have spent a total of 625 hours on development. Out of these, 550 hours until the end of April, and 75 hours from May until now.

The SDK, that includes the library and the demo, is available on GitHub: https://github.com/mollyim/monero-wallet-sdk

### Proposal & Milestones

By funding this project we aim to accelerate the adoption of Monero in the Android ecosystem, providing a reliable and flexible solution for developers to integrate Monero into their apps. This funding will also drive the integration of Monero into Molly.im.

The proposed milestones for this project are as follows:

1. Development

   - Complete the development of the library for the planned use cases.
   - Complete the implementation of the remaining features for the demo wallet app.

2. Security Enhancements

   - Implement and validate basic integrity checks in wallet2 to mitigate the risk of malicious nodes.
   - Upstream the improvements to the core library.

3. Continuous Integration & Testing:

   - Set up CI pipeline to automate builds, testing, and release processes.
   - Maintain a minimum unit test coverage of 70% for the library (excluding 3rd party and generated code).

4. Release Management

   - Iterate on the SDK based on community feedback, fixing issues, and reviewing pull-requests on GitHub.
   - Coordinate new releases, including versioning and release notes.

5. Documentation

   - Create a clear README that provides an overview of the project and build instructions.
   - Generate the API reference documentation.
   - Include code snippets and recipes to demonstrate how to solve common problems with the SDK.
   - Create a component diagram that illustrates the architecture and key components.
   - Comment the code of the wallet app to serve as an integration guide, explaining the implementation details.
   - Regularly update the documentation.

6. Community Engagement

   - Engage actively with the community on Matrix to understand their needs and include their suggestions into future updates.

7. Seraphis Migration Planning

   - Join the Seraphis Working Group to provide feedback, share design ideas, and review migrations plans for a smooth transition to Seraphis.

### Funding

We are requesting a total of $36,000 in funding to support this project, allocated in these milestones:

1. Development: $22,000
2. Security Enhancements: $3,000
3. Continuous Integration & Testing: $6,200

For the remaining milestones (4 to 7) we propose to allocate $4,800 for 6 months of maintenance, with payouts of $2,400 every 3 months.

Based on current rate of 1 XMR = $140 (as of June 10th 2023) with a 15% volatility buffer, the equivalent amount of $36,000 would be approximately 295 XMR.

### Expiration

If no milestones have been claimed within 9 months from the start of the project (since moved to work-in-progress) or latest payout, the CCS for the project shall be considered expired. In case of expiration, the remaining unclaimed funds will be donated to other CCS proposals.
