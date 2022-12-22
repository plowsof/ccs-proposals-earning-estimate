---
layout: wip
title: "Gupax: GUI for P2Pool+XMRig"
author: hinto
date: 10 October 2022
amount: 100
milestones:
  - name: Working GUI + Documentation
    funds: 80% (80 XMR)
    done: 20 December 2022
    status: finished
  - name: 1 year of maintenance
    funds: 20% (20 XMR)
    done:
    status: unfinished
payouts:
  - date: 22 December 2022
    amount: 80
  - date:
    amount:
---

![banner.png](https://github.com/hinto-janaiyo/gupax/raw/main/images/png/banner.png)

## What
[Gupax](https://github.com/hinto-janaiyo/gupax) is a cross-platform GUI for [P2Pool](https://github.com/SChernykh/p2pool)+[XMRig](https://github.com/xmrig/xmrig). I was really happy when Monero GUI implemented P2Pool directly (many users seem to be using it) however, the embedded miner is slower than the dedicated XMRig miner. Unfortunately, integrating XMRig directly into Monero GUI is a no-go mainly due to [anti-virus issues.](https://github.com/monero-project/monero-gui/pull/3829#issuecomment-1018191461) Personally, I also think keeping Monero GUI's scope simple (monerod+wallet) is the way forward. Either that, or a properly implemented [plugin system.](https://github.com/monero-project/monero-gui/pull/3829#issuecomment-1018406709)

Gupax is a completely seperate GUI that can act as a companion alongside Monero GUI. One window with monerod+wallet, and another for P2Pool mining (with XMRig used for max hashrate!). It can act standalone as well, connecting to a remote node so no Monero node is needed.

## Why
There are a couple (abandoned) GUIs for XMRig, and 1 for P2Pool (Monero GUI). There are 0 for both combined. These two together are only accessible via the command line, which is not ideal. If you take a look at [/r/MoneroMining](https://www.reddit.com/r/MoneroMining) at any given moment, there will be threads where people are confused on how to set everything up. I'm 100% certain if there was a simple GUI solution people could point at ("just use Monero GUI + Gupax"), there would be many, many more miners on P2Pool. [On August 12th when MineXMR shutdown](https://www.reddit.com/r/Monero/comments/wb7a9s/minerxmr_is_shutting_down_august_12th_and), had a P2Pool+XMRig GUI existed, I'm certain it would have gained a much more significant chunk of the total hashrate. Instead, much of it went towards to the 2nd/3rd largest centralized pools.

I've been facinated with p2p mining even before SChernykh created Monero's P2Pool. Bitcoin's P2Pool was also seen in the same way as Monero's P2Pool is seen today, but the community neglected it, development stopped and it died off. The massive corporate ASIC farms popping up and making deals with centralized pools did not help either. [Here's an example thread from 2014](https://reddit.com/r/Bitcoin/comments/1uii40/p2pool_is_a_completely_decentralized_mining_pool). It is eerily similar to the Monero threads I read today.

I'd like P2Pool to live on and be accessible to as many people as possible. The current Monero GUI implementation is great, but I want everyone to have access to the ***full hashrate*** of what their machines are capable of.

## Implementation
- **OS:** Gupax will be tested for Windows, macOS, and Linux. Maybe the BSDs (see "Questions" below)
- **Docs:** All Gupax usage will have documentation on GitHub; General P2Pool/XMRig info will also be included
- **Packaging:** Gupax will be packaged in a bundled zip/tar that includes P2Pool/XMRig, and as a standalone binary that expects you to bring your own P2Pool/XMRig. Both will be the same binary, only difference being the first will include all necessary components. Maybe an installer as well (see "Questions" below)
- **Efficiency:** I don't normally care about resource usage too much because (although not ideal...) most computers can afford to run heavy programs. However, the context for Gupax is a ***mining*** machine, it would be too ironic if it impacted the hashrate performance, and so, Gupax uses the very lightweight [Rust egui library](https://github.com/emilk/egui). By default egui is an "immediate mode" GUI, meaning frames are rendered 60x/sec. This is turned off in Gupax so frames are only rendered upon user interaction. This allows for a fast and lightweight GUI. For context, it uses around 5x less CPU when switching around tabs compared to Monero GUI

## Planned
- **Community Node:** An option to use a trusted community Monero node instead of your own. At a small privacy cost, this allows users to immediately start mining on P2Pool without downloading the entire chain
- **Update:** Built-in update/upgrader for Gupax/P2Pool/XMRig and an (opt-in) auto-updater that runs at startup
- **Config:** All the basic configurations you would expect with P2Pool/XMRig (main, mini, peers, thread count, etc)
- **Status:** Status tab displaying mining statistics using P2Pool & XMRig's APIs

## Demo
Here's a demo of a working GUI prototype:

![](https://user-images.githubusercontent.com/101352116/194763334-d8e936c9-a71e-474e-ac65-3a339b96a9d2.mp4)

[More info and the source/binaries can be found here](https://github.com/hinto-janaiyo/gupax). Please give it a try and leave feedback.

## Who
I'm [hinto-janaiyo](https://github.com/hinto-janaiyo).

I created and maintain [monero-bash](https://github.com/hinto-janaiyo/monero-bash), which is also an effort to spread P2Pool usage. Frankly speaking, I think monero-bash is many more times more powerful than Gupax, more complex, more options, works better for me, etc. I use it daily, it's the sole way I interact with Monero/P2Pool/XMRig, but I realize it targets a niche group. Gupax is the GUI version with the goal that it's as accessible as possible, while still being powerful.

## Funding
**Timeframe:** 2 months (8 hours/day, 448 total hours)  
**Total:** 100 XMR ($14700 USD @ 1XMR/$147)  
**Rate:** $32.8/hour (14700 / 448)

The GUI is (mostly) already done, but it is still slightly buggy and fonts/sizing/style still need touchups. The internals will take the majority of the 2 months I think this will take to complete. There are two milestones for a total of 100XMR:
  1. v1.0.0 release + All documentation (80XMR)
  2. 1 year of maintenance (20XMR)

I'll likely be adding features on my own time afterwards as well (if they are useful to users). There will be documentation on everything, so even without my direct help, it will hopefully be easy for users to use and/or help each other out. I will most likely maintain this project for as long as I'm in this community and there are people using it.

## Questions
These are some design decisions that I think would be better decided as a community. If you have any opinions on the following, please leave feedback:
- **Q1. Auto-updater ON or OFF by default?** 
  - I think having up-to-date software is important but also, I do not like making connections unless users explicitly decide to
- **Q2. Which nodes should be included as "Trusted community nodes"?**
  - This is the list of nodes users can select to avoid running their own Monero node. Requirements are: good uptime, trusted by the community, ZMQ enabled. Current list: rino@node.community.rino.io, sethforprivacy@node.sethforprivacy.com, and selsta@selsta1.featherwallet.net 
- **Q3. Include an installer?**
  - I'm not familiar with Windows/macOS installers, but if having one would increase adoption, getting some help would be nice
- **Q4. Support the BSDs?**
  - I'm not familiar with the BSDs and testing releases on them will take away from development time
- **Q5. Which license?**
  - Normally I would have licensed this under MIT however P2Pool and XMRig are under GPLv3. Although I'm not directly using their code, I am planning to include their binaries so I feel it's appropriate to also use GPLv3. I do not mind using GPLv3, but feedback is welcome
- **Q6. Name/design change?**
  - Gupax is a stupid acronym for: GUI Uniting P2Pool And XMRig. The ugliness of both the name and logo have grown on me but I'm open to changes
