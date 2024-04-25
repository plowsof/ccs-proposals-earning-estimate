---
layout: fr
title: "Full-Chain Membership Proofs + Spend Authorization + Linkability Research CCS"
author: kayabaNerve
date: April 13, 2024
amount: 2000
milestones:
  - name: Provide a soundness proof for the proof using Elliptic Curve Divisors
    funds: 0
    done:
    status: unfinished
  - name: Formally verify the gadgets
    funds: 0
    done:
    status: unfinished
  - name: Prove the composition to be unlinkable, unforgeable, and non-malleable
    funds: 0
    done:
    status: unfinished
  - name: Audit the Implementation of GBPs
    funds: 0
    done:
    status: unfinished
  - name: Audit the Elliptic Curve Divisors Library
    funds: 0
    done:
    status: unfinished
  - name: Audit the implementation of the gadgets
    funds: 0
    done:
    status: unfinished
  - name: Audit the implementation of the circuit
    funds: 0
    done:
    status: unfinished
  - name: Audit the implementation of the Towering Curve Cycle
    funds: 0
    done:
    status: unfinished
  - name: Audit the implementation of the Generalized Schnorr Protocol
    funds: 0
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
---

This CCS is to prove, review, and audit Full-Chain Membership Proofs (a trustless solution based on Generalized Bulletproofs) into Monero under RingCT, replacing the existing CLSAG. This is distinct from prior intents to integrate FCMPs into Monero with Seraphis, and was prior discussed in a MRL meeting with well reception. That same meeting organized the [funding of security proofs for Generalized Bulletproofs](https://ccs.getmonero.org/proposals/cypherstack-gbp-security-proofs.html), a critical component for FCMPs (under both this proposal and Seraphis). The review and audits here would also lay the ground work for FCMPs with Seraphis as well.

All of these milestones have "?" for their required funds. The goal of this CCS is to raise the funds necessary to contract various external parties. All XMR will be held per the usual CCS policy, by core, until the necessary agreements are made for each milestone. The intention of this is to prevent needing to file several CCSs (addng delays) and to minimize the amount of confusion re: funding efforts. I do not want to have to justify to the community, after 5 CCSs for audits, why a 6th one is still justified and FCMPs aren't a black hole of endless fundraises for audits.

Unfortunately, that last note cannot be completely unavoided. Since there are not auditors ready for each and every milestone, this CCS may run out of funds prior to completion of all milestones (requiring another CCS). The amount chosen (2000 XMR, roughly 230k USD) was chosen on the belief it's reasonable for the scope described. Due to the subject matter (ZK proofs and circuits) currently being one of the hottest fields in the cryptocurrency space at large, with both startups and VCs, I'm unable to provide any such guarantee.

With that note, it may sound optimal to do individualized CCSs. That'd not only add weeks/months to the process (as some of these audits are serialized, so a delay in one adds to the delay in the next), it'd risk being unable to contract certain auditors. In my experience, auditors schedule as long as months out *from time of agreement*. In the time it takes to discuss the proposal and raise the funds, auditors' availability schedules may shift dramatically, including in rates (shifting the amount necessary/adding a deadline for the discussion and fundraising). Hence this proposal.

kayabaNerve and jberman are the people primarily expected to find such parties, with the actual agreement on parties and amount to be by their endorsement, and a general agreement within MRL that the proposed expenditure is reasonable. The word choice of reasonable means that the proposed parties are reasonably trusted to be able to adequately perform the work proposed, the amount to be paid is understandable and amenable, and if there are other potential parties, none are clearly, completely, and definitively better choices. 

If the work within this CCS for any reason fails, or completes with a remaining balance, the funds raised and remaining (held by core, per the rules of the CCS) will roll over into a general MRL research fund to sponsor further research and development, such as proofs for and review of Seraphis. The direction of and process for this new fund will be decided and agreed upon such a roll over occurring by core and discussions within MRL. The idea for this was premised on the idea of hiring researchers, Cypher Stack specifically, on retainer with MRL having discretion over how those hours were spent. That was discussed at the same meeting as this proposal (proposal as in cryptographic idea, not proposal as in CCS proposal) with sufficiently well reception for me to propose it as the fallback here.
