---
layout: wip
title: "XMR BTC Atomic Swaps Desktop GUI"
author: binarybaron
date: October 1, 2021
amount: 52
milestones:
  - name: "Working Prototype of GUI"
    funds: 45
    done: 6 February 2022
    status: finished
  - name: "Tor & Rendezvous Protocol Integration"
    funds: 4
    done:
    status: unfinished
  - name: "Infrastructure maintenance (October - November)"
    funds: 1
    done: 30 November 2021
    status: finished
  - name: "Infrastructure maintenance (December - January)"
    funds: 1
    done: 31 January 2022
    status: finished
  - name: "Infrastructure maintenance (February - March)"
    funds: 1
    done: 31 March 2022
    status: finished
payouts:
  - date: 6 December 2021
    amount: 1
  - date: 3 February 2022
    amount: 1
  - date: 8 February 2022
    amount: 45
  - date: 2 April 2022
    amount: 1
  - date:
    amount:
---

# What
## GUI for BTC<>XMR Atomic Swaps
Atomic swaps between BTC and XMR have been one of the most discussed and anticipated developments in the space for quite some time. While Farcaster is still working on the implementation of their protocol, the COMIT team has already delivered an MVP. There are several swap providers active on the mainnet right now. Trustless cross-chain trades are becoming a reality.
While the swap-cli developed as part of the MVP is usable and indeed works, it is not suitable for use by non-technical people who don't have experience navigating the command line.

For trustless atomic swaps to become widely adopted, the user experience must be dramatically improved. One should not have to manually type commands into a terminal or understand the protocol on a technical level to have the ability to take part.
For this reason, I would like to spend my time working on a FOSS GUI for BTC<>XMR atomic swaps. The GUI will be built around the swap cli and will empower even non-technical people to swap their BTC for XMR.

# Who
I binarybaron, the creator of [unstoppableswap.net](https://unstoppableswap.net) ([proof](https://unstoppableswap.net/proof.txt)) and Monero enthusiast. I was excited about Atomic Swaps from the beginning, tested the first versions and even contributed to the project (e.g. https://github.com/comit-network/xmr-btc-swap/pull/585). When the first testnet asb went online, I realized that we would need a better user interface and a platform to compare the different swap providers. I decided to start building [unstoppableswap.net](https://unstoppableswap.net). The interest has been much greater than I could have ever predicted. In the last week alone, the site has been visited more than 150,000 times. The website has become an important entry point for new users.

# Proposal
I am asking for 45 XMR to develop and deliver the first working prototype of a graphical user interface that will allow users to perform an Atomic Swap, withdraw funds from the internal wallet, compare swap providers, and view their past swap history all without having to use the terminal. I estimate that it will take 3-4 months to complete.

Once this groundwork is in place and the basic functionality is reasonably stable, I will start working on the Rendezvous protocol and Tor integration. I'll require 4 XMR for this to be completed.

In addition, I need 0.5 XMR per month (for 6 months) to operate and maintain the infrastructure of unstoppableswap.net. This includes a rendezvous server where swap providers can register using the libp2p rendezvous protocol. The backend, which indexes the swap providers, provides additional information such as uptime and age about providers, and makes this information available via a publicly available API (http and websocket). And the frontend which will serve as a directory for releases of the GUI and a stripped-down web version of the tool.

# What I want to focus on
### Port the existing UI of unstoppableswap.net to an Electron app
I'll use Electron with React and TypeScript as a software stack for developing the frontend as well as the 'backend' (meaning the code that controls the swap-cli).
- Setup Electron and convert the existing codebase to TypeScript
- Setup Ci for testing, compilation, and publication of artifacts

### Spawn swap-cli as child process
- Automatically download the latest version of swap-cli from GitHub and validate checksums
- Potentially also verify signatures if COMIT decides to sign their releases

### Derive swap state from swap-cli logs
In order to display instructions and details about the current state of the swap to the user, I need to derive the internal swap state from the log output and from internal database of the of the cli.
- Decide on the best data structure to represent the state of a running swap
- Implement using a state management system like redux
- Potentially open PR upstream to add additional logging statements to cli
- Requires https://github.com/comit-network/xmr-btc-swap/pull/780
- Detect updates to the SQLite database and reflect those in the GUI

### Happy-Path
I will start developing the interface that will navigate the user through the swap procedure. I will initially be focusing on the "happy path", i.e. a scenario where both Alice and Bob follow the defined rules and the swap is completed successfully.


### View, resume, cancel swaps
I will enable users to view, resume and cancel swaps. A user will be able to check the amounts swapped in a particular swap and additional information such as the transactions involved will be displayed.
- Requires https://github.com/comit-network/xmr-btc-swap/issues/766
- Requires https://github.com/comit-network/xmr-btc-swap/issues/133
- Potentially open PR upstream to add additional logging statements to cli

### Refund and punish path
Will add logic to state management system to derive the state for the refund and punish paths.
- Consider all the different scenarios and inform the user at all times what is happening

### View balance of internal wallet and allow withdrawal of funds
Enable end-user to view the balance of the internal bitcoin wallet of the swap-cli and withdraw funds at will.
- Requires https://github.com/comit-network/xmr-btc-swap/issues/766
- Enable user to import the keys of the internal wallet into another wallet by computing the seedphrase and displaying it to the user

### Use rendezvous server(s) for asb discovery
At the very beginning we will use the API of unstoppableswap.net for the asb discovery. It would be ideal if the GUI could also use public [rendezvous](https://github.com/libp2p/specs/blob/master/rendezvous/README.md) servers (like the one from COMIT) for looking up publicly accessible swap providers.
- Reimplement rendezvous protocol using js-libp2p
- Or use swap-cli to connect to a rendezvous server and retrieve the swap providers that have registered with them

### Support for onion routing (rendezvous server, asb connection)
To not expose the users IP-address to the maker and to improve privacy, all traffic should be routed through tor.
- Automatically download the latest tor binary official sources
- Start in the background
- Validate checksums and possibly signature
- Configure swap-cli to use tor socks5 proxy

### Education
We need to educate users on the specific rules they need to follow to avoid losing funds (e.g., not going offline for more than 12 hours after starting a swap).
- Quiz at first start-up to make sure user understands what rules he needs to follow
- Link to educational material
- Documentation

### Release
- Compile binary for Windows, Linux and macOS
- Provide download on unstoppableswap.net

Expiration date: November 30, 2021
