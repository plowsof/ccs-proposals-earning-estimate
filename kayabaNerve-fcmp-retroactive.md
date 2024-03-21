---
layout: cp
title: Retroactive funding for work on full-chain membership proofs
author: Luke Parker (kayabaNerve)
date: July 24, 2023
amount: 310 XMR
milestones:
  - name: Implementation of Bulletproofs+
    funds: 150 XMR
    done: 23 June 2023
    status: finished
  - name: Implementation of Curve Trees
    funds: 100 XMR
    done: 23 June 2023
    status: finished
  - name: Application of elliptic curve divisors for multiple times faster proofs
    funds: 50 XMR
    done: 23 June 2023
    status: finished
  - name: Implementation of COPZ's efficient cross-group discrete log equality proof
    funds: 10 XMR
    done: 23 June 2023
    status: finished
payouts:
  - date: 21 March 2024
    amount: 310
---

Prior to Monerokon, I spent a month and a half working on full chain membership proofs for Monero. This is the product of

- Discussions from https://github.com/monero-project/research-lab/issues/100
- Curve trees, as the fundamental idea https://eprint.iacr.org/2022/756
- Eagen's application of Elliptic Curve divisors https://eprint.iacr.org/2022/596
- COPZ's discrete log equality proof, letting us move to a curve cycle https://eprint.iacr.org/2022/1593

Having finished the work, which was considerable, I would like to fundraise for retroactive funding given the expenses occurred to me. Not only did I put off my own work for the significant amount of time spent on this, I made the decision to bring j-berman in at a rate we had prior established for their work on my own project.

To explain the work, it's an implementation of a membership proof _compatible with Seraphis_ which is efficient enough to feasibly support up to 777 million outputs. For more than 777 million outputs, proof time would increase ~50%, yet the chain would continue.

While this work isn't complete, it has asserted its existence as a viable path to proceed down.

# What Has Been Done

- An implementation of Bulletproofs+, designed to be clearly understandable and efficient.

A new implementation was written despite Monero already having a deployed implementation. This was due to Monero's implementation only supporting aggregate range proofs and being so tailored for them, it being infeasible to expand to include support for arithmetic circuits (the proof Curve Trees uses).

It is not yet ready for production for a few reasons.

1) It panics on invalid inputs, instead of returning errors.
2) It hasn't been externally reviewed/audited.
3) A design criteria to support curve trees is a vector commitment scheme (VCS). Bulletproofs+ does not support vector commitments, and I had to shim in my own scheme to compensate which is not viable for production.

This will be discussed below.

- An implementation of Curve Trees, or at least, the idea of Curve Trees.

Curve Trees describes a n-ary Merkle Tree where the hash function is a Pedersen hash. Since a Pedersen hash hashes from scalars to a group element, and the variables in an arithmetic circuit are scalars, Curve Trees uses a pair of Bulletproofs over a curve cycle, each layer of the tree represented by the complimentary proof. This ensures the output of the hash is always a native variable. My implementation is similar, yet instead of using the scalar multiplication algorithm provided in its paper, Eagen's application of Elliptic Curve divisors is used. This is multiple times more performant.

Additionally, my work was done over Bulletproofs+, not Bulletproofs, for minor efficiency gains. Post-deciding which arithmetic circuit proof to use, it was learned Curve Trees requires a VCS. Bulletproofs+ does not have a VCS posited, while Bulletproofs has one posited yet not proven. While work could be done to prove the VCS posited for BPs instead of developing a new scheme for BPs+, this would be detrimental in the long term.

To explain why, BPs defines a "inner-product" argument. BPs+, "weighted inner-product". BPs++, "norm". BPs++ argues its "norm" argument can be equivalent to BPs+'s "weighted inner-product", implying future development of a VCS around BPs++ would be best done from a VCS around BPs+. Since it is a goal to move to BPs++ for efficiency, not just for arithmetic circuits (this work) yet also Monero's range proofs (which BPs++ already has funding to be reviewed for), this was kept in mind.

As part of my work, I reached out to Firo, with researcher Aram Jivanyan and contracting researcher Aaron Feickert (sarangnoether) from Cypher Stack. I requested their collaboration in this effort, with current discussions being around them working on developing and proving a VCS. While no guarantees have been made, the answer to if a scheme for BPs+'s WIP argument is possible was estimated to be on the scale of weeks, not months. Accordingly, I'd personally evaluate it within timelines _and long-term fruitful_ to continue with BPs+ and not revert to BPs. If a BPs+ VCS is infeasible, then the work falls back to proving the VCS posited for BPs, which has passed first glances.

- An implementation of Elliptic Curve divisor calculation and checks

Elliptic curve divisors can be used to offer proof-of-knowledge of discrete logarithms which are several times more efficient than in-circuit elliptic curve additions. I implemented the calculation of divisors, checks for them (in and out of circuit), achieving a roughly 3x reduction in DLog PoK circuit size than the Curve Trees DLog PoK circuit. This circuit is most of the overall circuit, and circuit size does directly relate to proof verification time.

- An implementation of COPZ's discrete logarithm equality proof

Since Curve Trees effectively requires a curve cycle, Monero would have to move to one. This proof lets Monero move to a curve cycle at a marginal cost (a one-time 160-byte proof per-output).

# What's Next

A series of tasks can be defined.

1) Proving and implementing a proper VCS scheme

This is currently in progress, and doesn't actively require the Monero project. In the future, it may require our involvement, and if so, we can discuss it then.

2) Proving/formally verifying Curve Trees

I agree more certainty behind Curve Trees is needed. I do not believe we should halt development efforts until we are fully certain, given the amount of evidence before us and alternative paths ahead of us for any road blocks we may face. Already happening is the development of a VCS scheme, with proofs. Once that happens, letting us formally define our Curve Trees instantiation, we can continue obtaining certainty. All of this can be done in parallel to this work's completion.

3) Polishing the above work

This will be tackled by future CCSs. I am planning one, and j-berman has already submitted a CCS which part of is experimentally integrating Curve Trees into Monero (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/401). I have also discussed with multiple developers in the ecosystem getting their involvement.

To be perfectly clear, in no uncertain terms, this CCS does not provide funding for nor guarantee any continued development. It is solely a representation of gratitude and acknowledgement for work already performed, and organization provided.

4) Auditing

Auditing can only occur once the academia, and the code, is completed.

5) The Monero project deciding whether or not to move to a curve cycle

I cannot truly comment here as I do not speak for the Monero community.

My personal thoughts on moving to a curve cycle can be found here: https://gist.github.com/kayabaNerve/97441ad851dc6e4d2a0b699f58a004f2

Relevant MRL issues are https://github.com/monero-project/research-lab/issues/100 and https://github.com/monero-project/research-lab/issues/110.

While this isn't the place to decide if a curve cycle is necessary, or if one will be adopted, it is important to note a curve cycle isn't technically required. It's optimal, and somewhat expected, yet we can hash Ed25519 points into a cycle (at additional cost). Accordingly, this work is relevant even if we don't move to a curve cycle.

6) The Monero project deciding whether or not to integrate this work

In order for the community to decide if this work should be integrated, it must be evaluated. Evaluation requires this work being viable for integration, which won't happen until it's complete. For now, I restate

> While this work isn't complete, it has asserted its existence as a viable path to proceed down.

And accordingly justify not only its historical funding, yet future funding.

# Why Historical Funding

The CCS has a distaste for historical/retroactive funding, which I understand. Personally, I do not accept payment for a job until it is done. While the milestone system offers that, I still must promise and obligate myself to doing the work by the fact I created a CCS and succesfully raised funds. I do not appreciate those obligations when I was unsure of my capabilities to produce not just a membership proof, yet a membership proof viable to continue with which was worth fundraising for. Before I wrote an implementation of BPs+, designed a higher-level arithmetic circuit framework, learned enough math to implement Elliptic Curve divisors, engaged with multiple other parties, and implemented Curve Trees, I was unsure this would become meaningful to Monero. It was on a scale I had never worked with before, and far too much work to ever be certain about before it is done and actual metrics can be assigned. Accordingly, I would never have felt comfortable with funding beforehand.

I also wished to avoid debate about the legitimacy of atttempting this work. This work, as currently implemented, with its current performance, commentary, and understandings, establishes itself as viable. Before it existed, it could not establish itself as viable. By waiting, I removed discussions about if it would be viable by now providing a proof it is.

While this work was done with limited visibility, I did contact parties as soon as they became relevant. Prior mentioned was a collaboration with Firo, yet I also reached out to Liam Eagen (author of BPs++ and a proof applying Elliptic Curve divisors), narodnik, and j-berman as beneficial.

# Funds Breakdown

The amount quoted is roughly 50,000 USD. Given the amount of work produced, and time spent, I believe this to be fair.

This is inclusive of my obligation to j-berman ($3,600) who:

- Reduced the multiplications performed, savings tens of percent off verification time
- Investigated a new algorithm for further reducing multiplicatios, which would also be applicable to Monero's current BP+ implementation

And my desire to thank Eagen for their contributions with $5,000. Eagen's application of divisors drastically increased the performance of this work. Also notable is narodnik who provided an initial Python reference for divisor construction and evaluation, yet they have declined to be so thanked.

With all of this in mind, and given the extended hours I generally work, my hourly rate would be roughly 100 USD.

# Resolution

If this proposal is not funded within two months, it will be closed regardless of status. All raised funds will be directed towards the already completed milestones, even if only partially funded. Whatever amount raised will close this CCS, and be considered as complete funding for these milestones.
