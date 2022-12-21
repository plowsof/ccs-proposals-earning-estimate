---
layout: wip
title: "XMR BTC Atomic Swaps Desktop GUI - Continued development for 4 months"
author: binarybaron
date: 26 May, 2022
amount: 232
milestones:
  - name: July
    funds: 58
    done: 10 August 2022
    status: finished
  - name: August
    funds: 58
    done: 2 November 2022
    status: finished
  - name: September
    funds: 58
    done: 9 December 2022
    status: finished
  - name: October
    funds: 58
    done:
    status: unfinished
payouts:
  - date: 23 August 2022
    amount: 58
  - date: 4 November 2022
    amount: 58
  - date: 20 December 2022
    amount: 58
  - date:
    amount:
---

![](https://user-images.githubusercontent.com/86064887/152649852-4c8c6c3f-0568-4347-89d1-c291c17f2d30.png)
![](https://user-images.githubusercontent.com/86064887/152678743-b86f395e-01dc-43c5-ba71-b27962a4a6ba.png)
![](https://user-images.githubusercontent.com/86064887/152649633-9ae29f79-8041-476c-be45-ef3441f4dee1.png)

We've successfully completed all of the goals we set for ourselves in our [first CCS proposal](https://ccs.getmonero.org/proposals/binarybaron-unstoppableswap.html). The prototype of the GUI we wanted to develop is fully functional (on testnet) and it will soon replace the now obsolete web interface ([UnstoppableSwap.net](https://unstoppableswap.net)).
Based on the community response to both of our status updates ([reddit post 1](https://www.reddit.com/r/Monero/comments/slvy2a/making_atomic_swaps_accessible_to_all/), [reddit post 2](https://www.reddit.com/r/Monero/comments/uawipv/atomic_swap_gui_demo_on_mainnet_unstoppableswap/)), we felt that there is a strong desire in the community for us to continue development.

Over the course of 7 months we have:

- Made over **175 commits** to the [UnstoppableSwap GUI repository](https://github.com/UnstoppableSwap/unstoppableswap-gui/commits/main) and developed an initial working prototype.
    - [Demo video of mainnet swap](https://www.youtube.com/watch?v=8XLGSsggnP0)
    - [Demo video of decentralized peer discover](https://www.youtube.com/watch?v=MvUsjU67jf0)
- I’ve become one of the three unpaid volunteers maintaining the [xmr-btc-swap](https://github.com/comit-network/xmr-btc-swap/) repository after the comit guys (original developers who developed the first MVP) have moved on to other projects. I’ve submitted and merged [12 Pull Requests](https://github.com/comit-network/xmr-btc-swap/pulls?q=is%3Apr+is%3Amerged+author%3Abinarybaron+) over the last months and reviewed some more.

### Proposal:

We are excited to keep working on Atomic Swaps. There are still loads of things needed to make it accessible and easy to use for everyone. Therefore we'd like to continue spending our time working on the FOSS GUI for BTC<>XMR Atomic Swaps. It is being built around the *[swap-cli](https://github.com/comit-network/xmr-btc-swap/blob/master/docs/cli/README.md)* and will empower even non-technical people to swap their BTC for XMR in a safe, decentralized and trustless manner. We are asking for 232 XMR for continued development for 4 months. At the end of each month 37 XMR will be paid out. We will work approximately 25 hours per week for 4 months straight which amounts to 400 hours of labour. Our hourly rate is 66 USD which amounts to 232 XMR at a current price of 112 XMR/USD

### Who:
I am binarybaron, the creator of UnstoppableSwap.net and Monero enthusiast. I was excited about Atomic Swaps from the very beginning, tested the first versions (MVP developed by COMIT guys) and contributed to the project early on. When the first testnet swap provider came online, I realized that we would need a better user interface and a platform to compare different swap providers. I decided to start building UnstoppableSwap.net. To my surprise, the interest was much greater than I could have ever predicted. In the first week alone, the website was visited more than 150,000 times. 
Once I realized that a website was not enough due to the technical requirements, I started working on a desktop app. Soon after, I submitted my first CCS, which was quickly funded, and developed the first working prototype of the desktop user interface.

### **What:**

1. Development of the graphical user interface (*[GUI](https://github.com/UnstoppableSwap/unstoppableswap-gui)*)
    1. **Auto Update**. For this to work we’ll need to code sign the releases on Mac OS using a paid certificate. The *GUI* will download and install the new version on startup if a new release is available. 
    2. **Educate users on the rules of the swap protocol.** There are some simple but important rules all users need to follow to avoid loosing funds. Most importantly the functionality of the cancel and refund timelocks must be understood. If users are not fully aware on how to act in certain scenarios, **they risk loosing funds**. We’re not yet sure how to proceed on this. Some ideas are outlined below:
        1. Quiz at first start-up to make sure the user understands what rules he needs to follow
        2. Refer to official documentation of the *[swap-cli](https://github.com/comit-network/xmr-btc-swap/blob/master/docs/cli/README.md)* and the GUI
        3. Refer to blog posts, videos and other online resources by the community
    3. **Allow manual cancel & refund of swaps.** Although the *[swap-cli](https://github.com/comit-network/xmr-btc-swap/blob/master/docs/cli/README.md)* should refund swaps automatically in most cases, there are some edge cases where the user is required to cancel & refund manually. This is currently not possible in the GUI. Enabling the user to easily do this in the GUI is a must.
    4. **Unit and Integration tests.** Although the *GUI* is relatively stable, it has pretty low test coverage. We need to create a lot more unit and possibly integration tests to cover all edge cases. Especially critical code like the internal finite state machine needs extensive test coverage.
    5. **New Icon**. The current icon was only meant to be a placeholder and wasn’t intended to be final. We’ll either commision someone to make a new one or ask the community for input.
    6. **Performance improvements.** We need to investigate what the performance bottlenecks of the *GUI* are. The most obvious ones at the moment are:
        1. Inefficient SQL queries being used for querying the swap database
        2. Overly-cautious file reads of the swap database
        3. Unnecessary re-renders of React components
        4. Blocking code being run in the main thread leading to freezing of the whole application
    7. **General improvement of the GUI**. Fixing bugs, responding to issues, writing documentation and implementing new features as they come to mind.
    8. **Switch the GUI from Testnet to Mainnet.** The GUI is currently Testnet only. Once we feel it is stable enough overall we’ll switch it over to Mainnet.
2. **Development and maintenance of the API that enables clients to easily discover swap providers.** A swap provider is a peer you can connect with to exchange your BTC for XMR. ****Our API indexes them and provides additional data such as their uptime and their age. This API is publicly accessible and can be used by other services (e.g orangefren.com). We provide an HTTP(s) and a WebSocket (socket.io) endpoint which will be documented on UnstoppableSwap.net.
3. **Development and maintenance of the UnstoppableSwap.net site.** It was the first initial prototype for a user interface for Atomic Swaps. It used to be a very stripped down version of the GUI and allowed users to more easily initiate a swap using the *[swap-cli](https://github.com/comit-network/xmr-btc-swap/blob/master/docs/cli/README.md)* by displaying them with a command they could copy and paste. This was not ideal, as it gave the impression of being user-friendly, but could be quite confusing and risky to use. The site will be converted into a simple download page for the *GUI* (similar to bisq.network)
4. **Maintenance of rendezvous point.** There are currently three major ways for users to discover swap providers (peers they can swap their Bitcoin for Monero with). This proposal also includes the maintenance of the rendezvous point we run.
    1. Word-of-mouth: The community can share the address of swap providers online (e.g on Reddit, IRC, Matrix..)
    2. Centralized peer discovery via UnstoppableSwap API: We actively maintain a database of swap providers which can be used by anyone to retrieve a list of swap providers
    3. Rendezvous point: The [rendezvous](https://github.com/libp2p/specs/blob/master/rendezvous/README.md) protocol is a lightweight mechanism for generalized peer discovery. It allows for the discovery of peers in a decentralized fashion. We operate a community rendezvous point through which swap providers can make themselves known to users, and through which users can find swap providers with whom they want to swap.(`/dns4/discover.unstoppableswap.net/tcp/8888/p2p/12D3KooWA6cnqJpVnreBVnoro8midDL9Lpzmg8oJPoAGi7YYaamE`)
5. **Reviewing, merging and possibly submitting Pull Requests to the [xmr-btc-swap](https://github.com/comit-network/xmr-btc-swap/) repository.**
    1. This proposal is mainly for continued development of the GUI and not for maintenance of the xmr-btc-swap project. **Time spent on the [repository](https://github.com/comit-network/xmr-btc-swap/) will at most be 5% of the total time spent on this proposal.**
    2. Most of the Pull Requests we’ll submit will be related to making the *[swap-cli](https://github.com/comit-network/xmr-btc-swap/blob/master/docs/cli/README.md)* compatible with the *GUI*
    

If funded we'll provide monthly updates in the CCS comment section.
