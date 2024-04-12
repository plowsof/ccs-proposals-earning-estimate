---
layout: wip
title: Rucknium Statistical Research
author: Rucknium
date: March 28, 2024
amount: 204
milestones:
  - name: Month 1
    funds: 33% (68 XMR)
    done:
    status: unfinished
  - name: Month 2
    funds: 33% (68 XMR)
    done:
    status: unfinished
  - name: Month 3
    funds: 33% (68 XMR)
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

## What

I propose to carry out statistical research to improve Monero's privacy, guide protocol decisions, and respond to Monero developer requests for statistical analysis of code changes where needed. In the short term I will complete in-progress analysis of the suspected transaction spam attack to provide a comprehensive view of the options to defeat this attack and possible future ones. This involves producing a Monero Research Lab research bulletin from the draft of ["March 2024 Suspected Black Marble Flooding Against Monero: Privacy, User Experience, and Countermeasures"](https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf). I will work with ArticMine to evaluate changes to ring size, fees, and block size scaling parameters to balance privacy, usability, and decentralization. Some items to complete the draft research bulletin:

- Derive the tradeoff function between ring size and transaction fees, i.e. how does a marginal increase in each variable affect the cost to a potential attacker?
- Simulate the combined black marble attack and Dulmage-Mendelsohn decomposition from Vijayakumaran (2023) to evaluate vulnerability to chain reaction analysis.
- Estimate any changes in the real spend age distribution during the spam incident using OSPEAD techniques. Movement toward more recent outputs suggests more evidence for the spam hypothesis.
- Create a node network crawler that seeks the source of large transaction volumes. Possibly combine the crawler with statistical analysis techniques of Sharma, Gosain, & Diaz (2023).
- Finish the research literature review.

Once the black marble flood analysis is completed, I would move to other research priorities:

- PocketChange privacy evaluation
- Ring member binning
- Fee discretization and fee prediction
- Safety of adjusting the 10 block lock
- Preparation of a paper describing OSPEAD for peer review and research journal publication
- EAE/EABE attack and churning
- Network privacy through steganography

I will not be able to complete all of these projects during this work period. Research priorities can be modified at Monero Research Lab meetings due to new events or findings.

I am nearing completion of [the OSPEAD improvement to Monero's decoy selection algorithm](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html). OSPEAD probably can only be safely implemented at a hard fork boundary because multiple decoy selection algorithms being used at the same time is [a potential threat to user privacy](https://github.com/Rucknium/misc-research/blob/main/Monero-Fungibility-Defect-Classifier/pdf). In the short them, analysis of the suspected flood attack is a higher priority. After, I will put hours into finishing the OSPEAD CCS proposal. Then after OSPEAD I will return to putting hours into this CCS proposal.

## Who

I am an empirical microeconomist. My recent contributions to Monero include:

- [Discovery of a mining pool misconfiguration. Sped up average time to first transaction confirmation by 60 seconds.](https://reddit.com/r/Monero/comments/11nu4aj/monero_transaction_confirmations_are_now_60/)

- [Privacy vulnerability report to Exodus Wallet about nonstandard fees. Successfully resolved.](https://reddit.com/r/Monero/comments/176e1zr/privacy_advisory_exodus_desktop_users_update_to/)

- ["Discussion Note: Formula for Accuracy of Guessing Monero Real Spends Using Fungibility Defects"](https://github.com/Rucknium/misc-research/blob/main/Monero-Fungibility-Defect-Classifier/pdf)

- [Identification of privacy-reducing nonstandard transaction fees](https://github.com/Rucknium/misc-research/tree/main/Monero-Nonstandard-Fees)

- [Analysis of the privacy impact of Mordinals (Monero NFTs)](https://reddit.com/r/Monero/comments/12kv5m0/empirical_privacy_impact_of_mordinals_monero_nfts/)

- [Monerotopia 2023 presentation: "A Statistical Research Agenda for Monero"](https://github.com/Rucknium/presentations/blob/main/Rucknium-Monerotopia-2023-Slides.pdf)

- [Statistical privacy analysis of P2Pool coinbase outputs in ring signatures](https://github.com/monero-project/research-lab/issues/109)

- ["Closed-form Expression of Monero's wallet2 Decoy Selection Algorithm"](https://github.com/Rucknium/misc-research/tree/main/Monero-Decoy-Selection-Closed-Form/pdf)

Pull requests reviewed for statistical issues:

- [wallet: mitigate statistical dependence for decoy selection within rings](https://github.com/monero-project/monero/pull/9023#issuecomment-1802593848)

- [wallet2: prevent duplicate outs](https://github.com/monero-project/monero/pull/8047#issuecomment-967113046)

- [monero-serai: fix decoy selection algo and add test for latest spendable](https://github.com/serai-dex/serai/pull/384#issuecomment-1870597406)

## Budget

I will work 20 hours/week for three months (13 weeks). My fiat-equivalent labour rate is the same as my previous proposal, adjusted for the lower purchasing power of the USD today: 110 USD/hour. The average daily opening USD/XMR exchange rate for the last 14 days (2024-03-15 to 2024-03-28) according to CoinGecko was 139.49.

The above numbers compute to `20 * 13 * (110/139.49) = 205.0326`. Rounding down to get whole numbers for the three milestones sets the total budget for this proposal to 204 XMR paid in three milestones of 68 XMR each. This proposal expires on January 1, 2025.

## References

Sharma, P. K., Gosain, D., & Diaz, C. (2023). "On the Anonymity of Peer-To-Peer Network Anonymity Schemes Used by Cryptocurrencies." Proceedings 2023 Network and Distributed System Security Symposium.

Vijayakumaran, S. (2023). "Analysis of CryptoNote Transaction Graphs using the Dulmage-Mendelsohn Decomposition." 5th Conference on Advances in Financial Technologies (AFT 2023), volume 282 of Leibniz International Proceedings in Informatics (LIPIcs).
