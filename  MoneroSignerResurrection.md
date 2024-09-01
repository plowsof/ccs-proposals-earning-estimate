---
layout: wip
title: "Monero Signer Resurrection: Reviving and Enhancing the Monero Signing Project"
author: Thor a.k.a vthor a.k.a DiosDelRayo
date: May 24, 2024
amount: 55.38
milestones:
  - name: Monero Signer basics on emulator
    funds: 5.38 XMR
    done: 19 June 2024
    status: finished
  - name: Monero Signer working with companion Application
    funds: 5 XMR
    done: 28 July 2024
    status: finished
  - name: Cleanup and production ready
    funds: 35 XMR
    done: 12 August 2024
    status: finished
  - name: Monero-GUI integration
    funds: 10 XMR
    done:
    status: unfinished
payouts:
  - date: 20 June 2024
    amount: 5.38
  - date: 29 July 2024
    amount: 5
  - date: 13 August 2024
    amount: 35
  - date:
    amount:
---
# Monero Signer Resurrection: Reviving and Enhancing the Monero Signing Project

## Proposal
This project has been stagnant since [December 28th, 2023](https://github.com/Monero-HackerIndustrial/polyseed.py/commit/2887588a1ebb6ccc6a48772595891175b5ce3c25). In taking over, I have updated the original proposal to include essential features for the current Monero ecosystem, such as:

Adding UR (Unified Resource) support
Integrating with [polyseed](https://github.com/DiosDelRayo/polyseed-python')
Interfacing with the Monero GUI
I have already made progress on some of these components, visible in my GitHub repositories, listed at the end of the proposal.

I propose to take over and finish the Monero Signer project, which was funded but never really started. After learning about Monero Signer and researching the existing work, I found it to be a stale project that was never truly initiated. I aim to complete the project by delivering what was originally promised, with some modifications to make it more useful and avoid wasting time on potentially unnecessary features.

I will complete all the work myself, as I prefer to move quickly, keep things streamlined, and discard unnecessary elements. Security and usability are my top priorities, followed by features and fancy extras. This approach leads to more secure and maintainable code, better user experience, and reduced documentation needs.


## Features
### Monero Signer
- [x] Monero seed generation by dice rolls (without password)
- [x] Monero seed generation  camera (without password)
- [x] Monero seed generation by picking 24 words (without password)
- [x] Polyseed generation by dice rolls
- [x] Polyseed generation by camera
- [ ] Full Polyseed support
- [ ] Wallet import with seed words (Monero/Polyseed)
- [ ] Wallet import with QR code
- [ ] Wallet export via Seed~~/hex~~/QR code
- [ ] View key only wallet export
- [ ] Receive via QR code unsigned transactions
- [ ] Sign transaction
- [ ] Send via QR code signed transaction

Reasoning why this is proposal is without password encryption for monero seeds:
```
On using monero-python there is no password protection implemented and after investigating a little bit,
the reason behind is probably, that the encryption/decryption is not really mad in a "standard" way.
So to be compatible with Monero-CLI and Monero-GUI the encryption must be implemented in CryptoNight and
another propiatary way to add and substract the mask of the CryptoNight password hash.
This will be a rabbit hole I can estimate.

Why not another encryption instead? I dislike to have various standards until nobody knows anymore what and where to use.
A temporary password encryption would in my opinion also only make the things worse on reaching compatibility with the
original implementation. Because now, what to do, support two different standards? Remove the way, people protected the
password of there seeds before?

If there is interest, and somehow funding for it I will implement it later in the monero-python fork (the original was archived) for MoneroSigner. But until then password encryption for seed will only supported for Polyseed.
```

### Monerosigner companion application (Desktop):
- [ ] Prepare unsigned transaction
- [ ] Send unsigned transaction via QR code
- [ ] Receive unsigned transaction via QR code
- [ ] Publish signed transaction

### Monero-GUI integration (Optional)
- [ ] Send unsigned transaction via QR code (hidden but accessible)
- [ ] Receive signed transaction via QR code (hidden but accessible)
- [ ] Check transaction and publish to network
- [ ] Process flow in `Send` for view key only wallet, to make the workflow natural as possible

### Documentation:
- [ ] Short and simple step-by-step guide
- [ ] README on how to use the automatic build process, including `git clone`, `make`, `make install`, and troubleshooting

### Tools and Scripts:
- [ ] Build image for target device
- [ ] Build emulator

I want to express that I will try to minimize the need for documentation by making the process easier to build and use. Nobody wants to read a book to get something done.

### ~~PortableMoneroQR:~~ dropped in favor of UR's
- [ ] ~~Well-defined data protocol~~
- [ ] ~~Targeting low-end cameras and screens~~
- [ ] ~~Targeting high speed~~
- [ ] ~~Application agnostic~~
- [ ] ~~Library Python~~
- [ ] ~~Library Java/Kotlin~~

There is no need for that, I was not aware of Blockchain Commons’ Uniform Resources (URs), but that is the way to go. Sending and receiving data will be implemented using URs.

## Milestones and Timeline
### Monero Signer basics on emulator (5.38 XMR) (10 days from now)
- [x] Emulator easy start
- [x] implement Polyseed in (pure) Python
- [x] Monero seed generation by camera
- [x] Monero seed generation on dice rolls
- [x] Polyseed generation by camera
- [x] Polyseed generation by dice rolls
- [x] Wallet export Seed~~/hex~~/QR code
- [x] Build script to generate executable (For macOS only Docker provided and I have no way to verify)

### Monero Signer working with companion Application (5 XMR) (25 days from now)
- [ ] Monero signer companion Application finished
- [ ] All missing Monero signer functionality
- [ ] ~~PortableMoneroQR stable~~
- [ ] UR's implemented

### Cleanup and production ready (35 XMR) (45 days from now)
- [ ] Tools
- [ ] Scripts
- [ ] Documentation final version
- [ ] Final cleanup Monero Signer
- [ ] Final cleanup companion Application
- [ ] ~~Final cleanup PortableMoneroQR~~

### Monero-GUI integration (10 XMR) (60 days from now from, until PR)
- [ ] Fork
- [ ] Modify
- [ ] PR

The given timeline reflects the upper bounds, but I target myself:
- Milestone 1: 7 days from now, June 1, 2024
- Milestone 2: 14 days from now, June 8, 2024
- Milestone 3: 30 days from now, June 24, 2024
- Milestone 4: 45 days from now, July 9, 2024

I kindly request that the payouts be made promptly upon completion of each milestone to allow me to concentrate fully on delivering Monero Signer successfully.

An expiration date for the proposal is set for 70 days from now, August 3, 2024.
- Milestone 4: 45 days from now, July 9, 2024

I kindly request that the payouts be made promptly upon completion of each milestone to allow me to concentrate fully on delivering Monero Signer successfully.

An expiration date for the proposal is set for 70 days from now, August 3, 2024.# Monero Signer Resurrection: Reviving and Enhancing the Monero Signing Project

Progress can be watched at:
[MoneroSigner](https://github.com/DiosDelRayo/MoneroSigner)
[Emulator](https://github.com/DiosDelRayo/monerosigner-emulator)
[polyseed python](https://github.com/DiosDelRayo/polyseed-python)
[monero python Todo, where is no work at the moment, but tracked about password encryption](https://github.com/DiosDelRayo/polyseed-python/Todo.md)

(will add with time other repositories, as soon there is code to see)