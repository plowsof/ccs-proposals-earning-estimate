---
layout: wip
title: "ofrnxmr feat BasicSwapDEX - take over the world pt 2"
author: ofrnxmr
date: 12 August 2024
amount: 1685
milestones: 
  - name: M0-O (ofnxmr, 1st month)
    funds: 20 XMR
    done:
    status: unfinished
  - name: M0-Y (80xmr bounties, 3 months)
    funds: 80 XMR
    done:
    status: unfinished
  - name: M0-F (~0-160hrs, 1st month)
    funds: 40 XMR
    done:
    status: unfinished
  - name: M0-B (~0-160hrs, 1st month)
    funds: 55 XMR
    done:
    status: unfinished
  - name: M1-O (ofrnxmr, 2nd month)
    funds: 20 XMR
    done:
    status: unfinished
  - name: M1-F (~160-320hrs, 2nd month)
    funds: 40 XMR
    done:
    status: unfinished
  - name: M1-B (~160-320hrs, 2nd month)
    funds: 55 XMR
    done:
    status: unfinished
  - name: M2-O (ofrnxmr, 3rd month)
    funds: 20 XMR
    done:
    status: unfinished
  - name: M2-F (~320-480hrs, 3rd month)
    funds: 40 XMR
    done:
    status: unfinished
  - name: M2-B (~320-480hrs, 3rd month)
    funds: 55 XMR
    done:
    status: unfinished
  - name: M3-O (ofrnxmr, til completion)
    funds: 100 XMR
    done:
    status: unfinished
  - name: M3-F - Frontend GUI v3.0.0 - v5.0.0+ (prepaid, ~6 months)
    funds: 320 XMR
    done:
    status: unfinished
  - name: M3-B - Backend v0.13 - v0.15+ (prepaid, ~6 months)
    funds: 410 XMR
    done:
    status: unfinished
  - name: M4 - Delivery of 1.0 (postpaid, ~3 months)
    funds: 190 XMR
    done:
    status: unfinished
    milestones: 
  - name: M5 - 1yr maintenance (ongoing)
    funds: 240 XMR
    done:
    status: unfinished
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
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
---

Welcome ladies and gentleman, kids and pets.

Lets skip the intro.

  BasicSwapDEX is, as far as I know, Monero's only Bidirectional Atomic swap service, and the only one that allows swapping monero with coins not named Bitcoin (such as Litecoin). 

  BasicSwapDEX has been mainnet for a while now, but is a beta / POC. With this CCS I hope empower and steward BasicSwapDex to production quality software within ~1 year. Some milestones are to be paid to ofrnxmr in advance. I'm also requesting that some funds be escrowed by the CCS Coordinator.
	 
##### M0/M1/M2 = accelerate work / probation.
- M0 paid at funding. To be paid to ofrnxmr to distribute as follows:
  - M0 = 80xmr to ofrnxmr to pay for bounties / extra help, and/or bonuses to backend/frontend devs
  - M0/M1/M2 = 20xmr/month (60xmr/3months) to ofrnxmr
  - M0/M1/M2 = 40xmr/160hrs (120xmr/3mths) to BasicSwap Team - Frontend
  - M0/M1/M2 = 55xmr/160hrs (165xmr/3mths) to BasicSwap Team - Backend

##### M3-O - Paid end of month 4
  - 100xmr
    
##### M3-F - Frontend GUI v3.0.0 - v5.0.0+
- Paid start of month 4
  - 240xmr earmarked for frontend development (paid out by ofrnxmr as work is completed, 40xmr/160hr)
  - 80xmr to ofrnxmr to pay for bounties / extra help, and/or bonuses to frontend devs

##### M3-B - Backend v0.13 - v0.15+
- Paid start of month 4
  - 330xmr earmarked for backend development (paid out by ofrnxmr as work is completed: 55xmr/160hr)
  - 80xmr to ofrnxmr to pay for bounties / extra help, and/or bonuses to backend devs

##### M4 - Delivery of 1.0
- Paid after M3 is completed to satisfaction, and 1.0 is shipped 
  - 80xmr for frontend dev(s)
  - 110xmr for backend dev(s)

##### M5 = Maintenance
- Payout in Month 13 at the earliest, to be redistributed on a monthly basis 
  - 8xmr to backend devs
  - 8xmr to frontend devs
  - 4xmr to ofrnxmr

#### Scope (wherever technically possibly)
- **_M0/M1/M2 = Catchup work. Begin preparing for M3 milestones._**
  - [Some things yet to be completed](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/457#note_24394)
- **_M3-F - Frontend GUI v3.0.0 - v5.0.0+_**
  - CEX-like UI and UX (aside from speed)
    - Orderbook
    - Market depth
    - Order types ie. Market, limit, stop, trailing, profit taker
  - Private orderbook UI
  - Overall UI and UX updates
    - Mobile friendly
    - Better notifications
    - Improve / simplify in progress and historical bid details
  - Historical swap exports
  - Drop _reliance_ on centralized price APIs
  - Add wallet (rpc) functionality to the wallets themselves
  - Ability to use external wallets to take offers
  - Include new GUI interfaces to match new backend functionalities
- **_M3-B - Backend v0.13 - v0.15+_**
  - Secure the backend
  - Better code reviews
  - Fix and enhance user APIs
  - Add provider / swapper APIs
  - Web frontend APIs
  - Enable swaps between incompatible coins. [Example: XMR <> FIRO]
  - Integrations of atomic protocals such as those from BCH and ETH
  - Disconnect SMSG from Particl blockchain
  - Create and use a local price oracle
  - Bridge orderbooks from other services such as Samourai 
  - EVM wallet compatibility
  - Necessary changes to enable frontend features
- **_M4 - Delivery of 1.0_**
  - M3-X Completed to satisfaction
  - Ship 1.0 installation packages as (example), a Flatpak, appimage
- **_M5 - 1yr Maintenance_**
  - Addressing concerns in an efficient manner
  - Continued improvement of the codebase

The scope of work is quite large. You can follow Particl dev report (going back to January) for current, ongoing and planned work, which is ever evolving.

Should any part of this CCS fail, I may choose to redirect remaining funds to fork the project or to acquire devs willing/able to complete it.

In the event of total failure, all unused funds will be donated to a 2/3 multisig (The elusive "jetfund") with the COMMUNITY Coordinator and 1 other [TBD] party, to be used **as the community decides**....Though, im ofrnxmr. I'm not _fill in name of scammer_. I will see this through to completion.

##### Coverage
- M0/M1/M2 = Month 0-3
- M3-O = Month 4-12
- M3-X = Month 4 'til Completion of M3-X milestones (target = ~6 months)
- M4 = Completion of M3-X milestones til the later of completion of M4 or Month 13
- M5 = 12 Months. Earliest payouts may begin is the later of completion of M4 or Month 13

**This CCS allows the Monero Community to lead the space to a goal of having a FOSS, trustless, unregulatable, P2P, decentralized, liquid economy, with _0 platform fees, 0 dev taxes_ and _0 targets_.**

**I would hope (and assume) that non-monero communities who are under constant threat for having cypherpunk ideals (_cough_ BTC, BCH, ETH, and whoever else shares our ideals) will also support and donate to this endeavor.**
