---
layout: cp
title: "MoneroSigner. Fork of seedsigner for Monero."
author: Monero-HackerIndustrial
date: June 08, 2022
amount: 55.38
milestones:
  - name: seedsigner emulator audit
    funds: 0 
    done:
    status: Finished
  - name: moneroSignerLibraries
    funds: 0 
    done:
    status: inprogress
  - name: PortableMoneroQR research and standard creation
    funds: 14.2 
    done:
    status: unfinished
  - name: Monerosigner Beta Build
    funds: 28.4 
    done:
    status: unfinished
  - name: Companion Application
    funds: 7.1
    done:
    status: unfinished
  - name: DIY scripts & docs
    funds: 5.68
    done:
    status: unfinished
payouts:
  - date:
    amount:
  - date:
    amount:
---

----
### Proposal Closure/Transferral 17th June 2024

All remaining funds (55.38 XMR) have been transferred to/repurposed for: [MoneroSigner Resurrection](https://ccs.getmonero.org/proposals/%20MoneroSignerResurrection.html)

Effective immediately:

- HackerIndustrial is hereby terminated from this project and relinquishes any claim to the remaining CCS funds.
- The project will now proceed under vthor, who has already achieved significant progress in a matter of weeks, demonstrating the competence and dedication required.

----

The Monero community could benefit from a fork of [seedsigner](https://seedsigner.com/) to supports Monero. Seedsigner uses an air-gapped Raspberry Pi Zero to sign for Bitcoin transactions. The project aims to make it easy for anybody to make a dedicated offline signing device out of low-cost commodity computer components (raspberry pi zero). This helps in reducing the need to trust hardware verndors. The most private hardware wallet, is the only only **you** know about.  

Seedsigner is focused only on Bitcoin, because of this, the UI/UX and features are not very helpful to Monero users.

### Why?

Supplychain poses a significant attack vector to hardware manufacturers, this threat is exacerbated when dealing with cryptocurrency devices. Monerosigner offers a DIY hardware wallet built out of easy* to source over the counter general hobbyist parts. This makes it easier for users to self custody their keys on their own devices. 

### Proposal 

I plan on creating a Monero specific fork of seedsigner called Monerosigner. Monerosigner is an offline signing hardware wallet built around the raspberry pi zero SBC. The hardware comes with a companion desktop application called Monerosigner Companion. With the companion application users are able to send unsigned transactions via QR codes to Monerosigner. 

### Who:
HackerIndustrial, I recently created some Monero themed decorative circuit board meant to be hung as [Christmas ornaments](https://genesisboards.com/crypto-circuit-ornaments/4-monero-light-up-circuit-board.html). I have done work in the web3 space and noticed a lack of self custody hardware devices. 

### What:

A Monero centric version of "seedsigner". I am forking the codebase and removing the bitcoin compnents and replacing them with Monero/Privacy specific features. 

Monerosigner features:
- Generate seed from dice rolls
- Generate seed from mnemonic phrase
- Import seed from QR code 
- Generate Addresses from accounts 
- Load unsigned transactions via QR 
- Sign unsigned transactions 
- Upload signed transactions to companion app via QR codes 
- Generate view only wallet & Export 
~~- GPG key generate ~~
~~- GPG PUBkey share ~~

Monerosigner companion application (Desktop):
- Transfer unsigned transactions via QR code 
- Transfer signed transactions and upload to network 

Monerosigner self custody Documentations:
- Help users built their own images 
- Help users build their own devices
- Help users with opsec/security best practices 

PortableMoneroQR:
- Data transfer standard for QR codes with a focus on lower end cameras and screens
- Variable data sizes with different frame rates 
- Application agnostic


### Milestones 

#### Milestone (-1)- monerosigner-emulator

I forked the seedsigner emulator from https://github.com/enteropositivo/seedsigner-emulator. I did a simple audit of the code and hosted my version at following location: https://github.com/Monero-HackerIndustrial/monerosigner-emulator

The emulator should help development and testers be able to use monerosigner without needing hardware. 

#### Milestone 0 - moneroSignerLibraries

I created a monerosigner core libraries. These libraries are then used on the device for all monero related function. Having the libraries as a separate project helps with portability of the code base. Many of the functions on the library will be used for the companion application

#### Milestone 1 - PortableMoneroQR 

https://github.com/Monero-HackerIndustrial/PortableMoneroQR
The portable QR standard is a compression/pagination standard for data frames for offline data transfer. There has been a lot of different projects through the years but they didn't deal with the smaller device constraints. (Smaller devices contain smaller screens and cheap/lowres cameras). 
This is a research project with 2 deliverables after research:
1. Standard definition 
2. Sample library in python. 


#### Milestone 2 - Monerosigner Alpha Release  

I will have created a beta version with all the Monerosigner features listed above. This version can be made available as an image build for flashing to sd cards. The source code will be available on github but requires some technical knowledge to setup and troubleshoot. This is considered an early alpha build for testing. 


#### Milestone 3 - Monerosigner Companion Application 

I will create a very barebone desktop application that allows the generating of unsinged transactions into QR codes. The application will also be able to get signed transactions from the Monerosigner device via QR codes and a webcam. 


#### Milestone 4 - Monerosigner DIY scripts and documentation

I will create scripts to make it easier for less technical users to be able to build their own images without having to rely on my prebuilt images. The scripts come with documentation for helping users get started. 


~~~~#### Milestone 4 - USB gadgetmode
I will integrate usb gadgetmode which will help signing of large messages and will not require a webcam.~~~~
I am saving the usb gadget mode for future proposals. This is not included in this proposal



Code will be published on github. Any of the code I contribute can be of the preferred community license. Any code forked will be a fork of the original license. (Someone more experienced with different license types can chime in).
