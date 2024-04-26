---
layout: wip
title: Full-Chain Membership Proofs + Spend Authorization + Linkability Development CCS
author: kayabaNerve
date: April 13, 2024
amount: 920 XMR
milestones:
  - name: Provide a specification of the circuit and high-level protocol
    funds: 80 XMR
    done:
    status: unfinished
  - name: Productionize the crate for the arithmetic circuit proof
    funds: 160 XMR
    done:
    status: unfinished
  - name: Productionize the crate for the Elliptic Curve Divisor Library
    funds: 80 XMR
    done:
    status: unfinished
  - name: Implement the gadgets
    funds: 320 XMR
    done:
    status: unfinished
  - name: Implement the circuit
    funds: 200 XMR
    done:
    status: unfinished
  - name: Implement the Generalized Schnorr Protocol
    funds: 40 XMR
    done:
    status: unfinished
  - name: Implement multisig for the Generalized Schnorr Protocol
    funds: 40 XMR
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
---

This CCS is to develop Full-Chain Membership Proofs (a trustless solution) into Monero under RingCT, replacing the existing CLSAG. This is distinct from prior intents to integrate FCMPs into Monero with Seraphis, and was prior discussed in a [MRL meeting](https://libera.monerologs.net/monero-research-lab/20240401) with well reception. That same meeting organized the [funding of security proofs for Generalized Bulletproofs](https://ccs.getmonero.org/proposals/cypherstack-gbp-security-proofs.html), a critical component for FCMPs (under both this proposal and Seraphis). This builds upon the [work prior done on FCMPs](https://ccs.getmonero.org/proposals/kayabaNerve-fcmp-retroactive.html), and does most of the ground work for FCMPs with Seraphis as well.

The exact deliverables will be:
- A document detailing the arithmetic circuit (a 'ZK program') and necessary integration work
- A ready-for-auditing Rust implementation of an amenable (trustless, formally proven, sufficiently performant) arithmetic circuit proof (currently expected to be Generalized Bulletproofs)
- A Rust library for calculating elliptic curve divisors
- The FCMP proof, as necessary for usage with RingCT
- The GSP (Generalized Schnorr Protocol) proof acting as the signature, with multisignature functionality

### Milestones

The milestones are unordered, barring the first to provide a specification. The gadgets will be specified as a series of constraints in a non-machine-interpretable manner intended to allow human understanding and review of the flow and composition. With the definition of the proofs (largely modelled as black boxes to the protocol), all of the supporting infrastructure will also be defined as necessary to comprehend the integration into Monero and new privacy protocol created.

"Productionize the crate for the arithmetic circuit proving system" means to develop the arithmetic circuit proof implementation to the point I endorse auditing it. With those audits, the crate would be eligible for usage in production. Any audits of the implementation would only be sane after the proof implemented is formalized, with security proofs. Currently, the proposed proof is GBPs, and security proofs for it are actively being worked on. If they fail to be proven, this milestone is worded in such a way an alternative proof (with acceptable properties, from being trustless to sufficiently performant to building upon sufficiently accepted academia) may also be accepted. If there are no alternative proofs acceptable, this milestone will be considered not possible at this time, and for the purposes of this CCS, 'failed'.

"Productionize the crate for the Elliptic Curve Divisor Library" means to develop the crate for calculation of divisors into a point it can be audited.

"Implement the gadgets" means to implement the prior-specified gadgets, and all supporting code for them, such that they are ready for soundness proofs, formal verification, auditing, and etc.

"Implement the circuit" means to implement the prior-specified circuit, and supporting high-level functions, to the degree described for the gadgets. This will also include an implementation of the towering curve cycle, Helios and Selene, though not one expected to be performant enough for deployment.

"Implement the Generalized Schnorr Protocol" means to implement the [Generalized Schnorr Protocol](https://eprint.iacr.org/2009/050.pdf) as needed for Monero's usage.

"Implement multisig for the Generalized Schnorr Protocol" means to implement a 2-round multisignature protocol, inspired by FROST, for the aforementioned Generalized Schnorr Protocol. This would have O(n) signing complexity and identifiable aborts.

All of these milestones will be done myself, kayabaNerve. Integration into Monero will be handled externally to this CCS, with jberman stating their intent to submit their own CCS. The steps for integration (regarding new protocol structures and how data such as the tree root will be specified/used when verifying transactions) will be part of the specification from the first milestone.

### Audits

https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/449 establishes an earmarked fund for paying for audits, as necessary for all of the work produced by this CCS. The justification for this structure is mainly provided within that CCS, and is considered out of scope to this CCS.

### Relation to Seraphis

GBPs, the Elliptic Curve Divisor library, the circuit specification (except the first layer), and the gadgets apply to a deployment of FCMPs with Seraphis (making this work largely reusable even if we don't move forward with FCMPs *before* Seraphis). The only part which wouldn't explicitly is the first layer of the circuit (which is currently expected to be composed of two distinct layers) and potentially the Generalized Schnorr Protocol work (as they are not currently used by Seraphis, yet I have proposed their use within Seraphis).

This work, if extended with the forward-secrecy discussions held *and all associated wallet code necessary*, would also be feature-complete with Seraphis. This would leave Seraphis, the protocol, a simpler/potentially more performant protocol, not an upgrade to privacy. This CCS, as currently specified, does not intend to detail all of the wallet upgrades which would be necessary (leaving that to future hard forks, keeping the scope of this concise and minimizing the timeline till deployment).

### Other Necessary Development

As aforementioned, integration must also be done, and development of a performant implementation of the towering curve cycle. While jberman has spoken up for the former, another party will need to be found for the latter (such as tevador, who found the cycle and has expressed domain expertise). Barring finding another party for the latter, I would have to personally learn how to implement efficient modulo arithmetic and step up (a problem left to the future).

### Failure

If the work within this CCS for any reason fails, the funds raised and remaining (held by core, per the rules of the CCS) will roll over into a general MRL research fund to sponsor further research and development, such as proofs for and review of Seraphis. The direction of and process for this new fund will be decided and agreed upon such a roll over occurring by core and discussions within MRL. The idea for this was premised on the idea of hiring researchers, Cypher Stack specifically, on retainer with the MRL having discretion over how those hours were spent. That was discussed at the same meeting as this proposal (proposal as in cryptographic idea, not proposal as in CCS proposal) with sufficiently well reception for me to propose it as the fallback here.
