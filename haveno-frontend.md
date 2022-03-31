---
layout: fr
title: Haveno frontend development
author: Haveno
date: Mar 16, 2022
amount: 755 XMR
milestones:
  - name: Month 0
    funds: 151 XMR
    done:
    status: unfinished
  - name: Month 1
    funds: 151 XMR
    done:
    status: unfinished
  - name: Month 2
    funds: 151 XMR
    done:
    status: unfinished
  - name: Month 3
    funds: 151 XMR
    done:
    status: unfinished
  - name: Month 4
    funds: 151 XMR
    done:
    status: unfinished
  
payouts:
  - date:
    amount:
---

Hello again everyone. As promised, after improving Haveno's structure, we come back with a new (much cheaper) CCS proposal.

For a complete picture and all details, [see our initial proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/284), which assumed the old structure with centralized operators.

This is the blog post announcing Haveno's improved structure: https://haveno.exchange/2022/02/02/haveno-structure.html.

## The new structure

For details about Haveno's structure, please read carefully the blog post linked above. For convenience, here is a short summary:

- No more third party entity that will run the exchange. Everything will be managed by non-legal entity for more robustness and decentralization

- All fees paid on Haveno will be sent to 'Engine', a CCS-like structure that will fund Haveno and Monero development. It will work similarly to the CCS managed by the Monero Core Team (MCT), but instead of generous donors, the funds will be provided by the fees sent to Engine by Haveno.

- The funds of Engine will be managed by an entity called 'Engine Council', formed by 5 trusted long term contributors of the dev community, including one member appointed by the Haveno Core Team (HCT) and one member of the MCT[1]. The remaining 3 members will be chosen from a pull of candidates by the Haveno and Monero communities.

- The HCT will request monthly 50% of the funds sent to Engine.

- To avoid liabilities and legal structures, the members of Council will vote anonymously [using ring signatures](https://github.com/monero-project/urs) to ensure plausible deniability.

- Arbitrators will be chosen using Engine and will not be picked by the HCT. This allows to open a market of arbitrators, where Monero and Haveno community members can propose themselves for the role. There will be security mechanisms in place to avoid arbitrators colluding with traders, but that's out of scope for this CCS.

[1] We already contacted the Monero Core Team about this structure and they say they are happy with Haveno's model and are willing to have one of their members join the Engine Council. They point out that this individual should not be interpreted as representing the views of the Core Team directly and if direct MCT input is required, they will discuss internally.

## How much and for what

We are asking for **154k USD in XMR**. The money will be used **entirely to pay for the frontend development of Haveno**. This is the estimated cost to complete the frontend. We are already in contact with a team of three devs, which will start working on Haveno as soon as this CCS is accepted.

The cost is lower than in the past proposal, because the team will develop only the frontend as requested, so extra work (in case of changed or additional requirements) is not included. The HCT will be deeply involved, trying to keep costs as low as possible, but the support of our dev community will be greatly appreciated.

## Milestones and terms

Payments to the frontend team will be every completed sprint. Every sprint will be a task that will take about 2 weeks to complete. For simplicity, we ask the funds to be sent to us every month for 4 months, with the first reward being sent as soon as our proposal is funded. The community will be able to follow the development in the public GitHub repository and on the community channels.

To recap:

- 1st payment: As soon as the proposal is moved to the "In progress" phase.
- 2nd payment: 1 month after the first payment
- 3rd payment: 1 month after the second payment
- 4th payment: 1 month after the third payment
- 5th payment: 1 month after the 4th payment. Last payment.

The community will be able to follow progresses on Github and on our matrix/irc chatrooms. We hope the development of the frontend will be finished within 4-6 months.

Haveno Core Team  
[haveno.exchange](https://haveno.exchange)
