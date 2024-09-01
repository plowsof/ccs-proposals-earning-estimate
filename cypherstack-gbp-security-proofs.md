---
layout: cp
title: Generalized Bulletproofs Security Proofs
author: Cypher Stack
date: April 4, 2024
amount: 200
milestones:
  - name: Funded
    funds: 200
    done: 11 April 2024
    status: finished
  - name: Completed
    funds: 0
    done: May 6th, 2024
    status: finished
payouts:
  - date: 11 April 2024
    amount: 200
---

Hello everyone, Diego "rehrar" Salazar here on behalf of [Cypher Stack](https://cypherstack.com/). We've recently [made a proposal to review the general Seraphis paper](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/441). After some discussion with MRL, including at an official MRL meeting, it was decided that while all parties do want this done eventually, there are perhaps some more immediate wins available for Monero's privacy tech, particularly in the form of Generalized Bulletproofs (GBP).

To summarize what it is, why it's important, and what work will be done, I post a blurb from Dr. Aaron Feickert, Cypher Stack's on-staff cryptographer:

```
"Full-chain membership proofs are a construction being proposed for future Monero protocol upgrades. These proofs can be used to replace ring signatures (used in the current Monero protocol) and membership proofs (used in the proposed Seraphis protocol) to improve privacy.

The proofs use a technique called curve trees that in turn rely on a Bulletproofs arithmetic circuit protocol. However, to meet technical requirements, the arithmetic circuit protocol needs to be modified to handle Pedersen vector commitments in a specific way. The modification, called generalized Bulletproofs, was informally described, but completely implemented, in a curve trees proof-of-concept implementation by one of its authors.

In collaboration with Firo and Luke Parker, we've already done a more thorough documentation of generalized Bulletproofs to aid future implementation. To our knowledge, however, the technique has never been proven secure.

Cypher Stack proposes to develop security proofs for generalized Bulletproofs. The goal is to produce a modified Bulletproofs arithmetic circuit protocol security proof that accommodates the generalized Bulletproofs technique and shows the required properties of perfect completeness, perfect special honest-verifier zero knowledge, and computational witness-extended emulation. This will mirror the existing proof of Theorem 4 in the Bulletproofs preprint.

We stress that it is not known if the generalized Bulletproofs technique readily admits such a security proof. As such, this is a research proposal that has a nontrivial risk of failure. Should the research be successful, Cypher Stack will produce a report containing the proof. Should it fail, Cypher Stack will produce a report containing any relevant information that may be useful for other researchers."
```

A few things I (rehrar) want to emphasize on this quote.

1. There is a non-negligible chance of failure to produce a satisfying proof. If this happens, the proposal is not considered a failure, and our deliverable changes to a report for future research.
2. Much of this work will be directly applicable and cross-over with Seraphis in the future. So it's not a distraction that will delay things, in that sense.

Cypher Stack asks for a total of 200 XMR to complete the review. We add a 10% volatility buffer, bringing the total up to 220 XMR. We aim to complete the review within 1.5 calendar (actual hours are not 1.5 months of man hours, but we have other work for other clients as well) months of the proposal being funded.

EDIT: We have been asked during the community and MRL meetings to remove the volatility buffer and receive the entirety of the money up front to simplify things and get this merged faster. The original proposal above remains in its original state for posterity purposes, but the proposal has changed to reflect the new terms. The new total is 200 XMR to be paid out as soon as the proposal is merged and fully funded.
