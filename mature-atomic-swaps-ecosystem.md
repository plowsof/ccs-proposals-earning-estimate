---
layout: fr
title: "From Prototype to Marketplace: Maturing the XMR-BTC Atomic Swaps Ecosystem"
author: "binarybaron and einliterflasche"
date: July 9, 2024
amount: 729
milestones:
  - name: 1st month
    funds: 121.5
    status: unfinished
    done:
  - name: 2nd month
    funds: 121.5
    status: unfinished
    done:
  - name: 3rd month
    funds: 121.5
    status: unfinished
    done:
  - name: 4th month
    funds: 121.5
    status: unfinished
    done:
  - name: 5th month
    funds: 121.5
    status: unfinished
    done:
  - name: 6th month
    funds: 121.5
    status: unfinished
    done:
payouts:
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

![https://i.ibb.co/3NvpYp2/upload-398781d371d354427bb455356731258c.png](https://i.ibb.co/3NvpYp2/upload-398781d371d354427bb455356731258c.png)
![https://i.ibb.co/wgYK9FF/generated-gif-2.gif](https://i.ibb.co/wgYK9FF/generated-gif-2.gif)

### Who

We (binarybaron and einliterflasche) are two Monero enthusiasts from Berlin and both computer science students. We have been excited about XMR<>BTC atomic swaps since the COMIT team started development of their prototype. binarybaron has contributed to the project since its early stages while einliterflasche joined later on.

### What is this project anyway?

The project mostly consists of four parts:

1. A command-line utility ([ASB](https://github.com/comit-network/xmr-btc-swap/blob/master/docs/asb/README.md)) that enables individuals to operate a 'swap provider' service. These swap providers offer to sell Monero in exchange for Bitcoin.
2. A command-line interface ([CLI](https://github.com/comit-network/xmr-btc-swap/blob/master/docs/cli/README.md)) that allows users to connect with swap providers and exchange their Bitcoin for Monero.
3. A graphical user interface ([GUI](https://github.com/UnstoppableSwap/unstoppableswap-gui/)) that utilizes the CLI behind the scenes, making the swap process way more user-friendly.
4. A command-line utility for hosting a [rendezvous point](https://github.com/comit-network/rendezvous-server) in the decentralized discovery network. Swap providers can register at these nodes to make themselves known to the network. CLI users can retrieve a list of swap providers.

### What we have been working on over the last 2 years:

- Developed an early web interface to simplify XMR<>BTC swaps. This project has since been deprecated and replaced with a desktop GUI. 
- Stepped in as maintainers for the [xmr-btc-swap](https://github.com/comit-network/xmr-btc-swap) project which includes the ASB and CLI applications. We have become the main developers fixing issues, implementing new features and pushing out releases.
- Developed the [GUI](https://github.com/UnstoppableSwap/unstoppableswap-gui/). Last year alone, more than 3,000 swaps were completed using our GUI. Since we completed our second CCS from May 2022, we worked on the project during our free time. This is also the reason we weren't able to dedicate as much time to the project as we'd like to and, frankly, as it deserves.
- Running a mainnet swap provider to kickstart adoption that has performed over a thousand swaps with users. This has been put on pause for now as more swap providers have emerged.
- We have also been hosting, and developing publicely accessible infrastructure
    - An API service that gathers a list of all known swap providers. This can be used in the GUI and also by others in the community (e.g [OrangeFren](https://orangefren.com/)) in addition to rendezvous points.
    - A reliable rendezvous point
- As part of our efforts to make atomic swaps accessible to the general public we have have been writing [documentation](https://docs.unstoppableswap.net/) for atomic swaps in general as well for the GUI and CLI applications.

### Proposal:

We're excited to keep working on atomic swaps. While swaps work realiably under optimal conditions, there are still many imperfections. We are confident that given a few months time to fully dedicate to the project, we can transform the ecosystem from more of a proof of concept into a mature marketplace.

We are asking the community for funding in order to be able to focus our efforts on improving the atomic swaps ecosystem.

We request 729 XMR for continued development for 6 months. At the end of each month 121.5 XMR will be paid out. We will dedicate 35 hours of focused work per week per person. Our hourly rate is 60 EUR. We're calcuating these amounts at a current average price of 138 EUR/XMR.

We will be providing monthly detailed updates in the comment section.

### What we will be working on

We will continue to maintain both the GUI and the underlying CLI/ASB by:
- Planning, coordinating and implementing new features and bug fixes,
- Coordinating releases,
- Keeping in touch with users and the community as a whole as well as offering a built-in feedback system in the GUI.

Furthermore, we will continue to manage some community infrastructure:
- We host a [webpage](https://unstoppableswap.net/) for the GUI as well as [documentation](https://docs.unstoppableswap.net/).
- We maintain both a public registry of swap providers as well as a reliable node in the decentralized discovery network.

For the CLI and ASB, which form the backbone of the GUI and swap provider infrastructure respectively, our focus will be to improve overall reliability. While swaps work consistently under optimal conditions, there are many moving parts, leading to various challenges in practice. These challenges include:
- Reliably staying in sync with both the Bitcoin and Monero blockchains,
- Completing swaps amid connectivity issues,
- Discovering peers in the network,
- Maintaining backwards compatability between peers (network protocols),
- Handling concurrent swaps,
- Accounting for blockchain congestion,
- Stringently enforcing protocol compliance,
- Ensure fail safety when swaps can't be completed,
- Minimizing the manual intervention required (e.g having to manually refund in some edge cases),
- ...

For the ASB daemon specifically, our focus will be on enhancing its ability to handle large amounts of liquidity reliably. We will also make it easier for a wider range of individuals to become a swap provider and sell their Bitcoin for Monero. This will improve competition and in turn lead to lower markup rates. Our work will include:
- Developing user-friendly tooling to simplify the setup and operation of the ASB and its accompanying services.
- Improving ASB extensibility and automatability by implementing an JSON-RPC server:
   - Swap providers can connect to their ASB using a standardized OpenRPC protocol
   - This will enable providers to:
     - Dynamically adjust their exchange rate based on current conditions and market assessment
     - Flexibly set maximum and minimum swap amounts according to their risk tolerance
     - Automate access to internal Bitcoin and Monero wallets for fund management
     - Listen for all kinds of events
- Enabling anyone to automate their ASB service to their liking by developing easy-to-use connector libraries for popular programming languages (e.g. Python, TypeScript, Rust, Java).

Integrating the RPC server and developing client libraries will take a lot of work and large refactors, but it will be worth the effort. It will enable the creation of custom applications and scripts built on top of the ASB. This will open basically unlimited possibilities but the most obvious use cases include:
   - Complete access to statistics and internal data and logging
   - Adjust exchange rate and minimum swap amount based on current Bitcoin transaction fees
   - Listening for specific events and executing custom actions e.g. sending notifications or replenishing funds by executing trades on other platforms
   - Integration of Bitcoin privacy protocols (e.g., CoinJoin, Whirlpool) for received funds

For the GUI itself our focus will be to:
- Make the GUI more accessible to non technical users (e.g. tooltips, explanations, ...),
- Provide documentation for end users as well as technical documentation to improve transparency and attract new developers,
- Work on migrating the GUI framework (from Electron to Tauri) to simplify the architechture,
- Release an Android (and possibly iOS) version of the GUI.
- _(We are also looking into a web version, powered by WebAssembly, which can run in browsers. This may not be possible and will require extensive refactors in the code base.)_
- Build a new UI for hosting and managing the ASB from inside the GUI. Thereby enabling selling Monero for Bitcoin.

### Why

We want to enable anyone to reliably acquire Monero by building an anonymized, decentralized and trustless market that is resiliant to censorship. We believe that by realizing the potential of this project we can bring this to reality.

A mature ecosystem will attract more users and swap providers. This will lead to increased liquidity and competition and thus make atomic swaps a viable alternative to centralized exchanges.
