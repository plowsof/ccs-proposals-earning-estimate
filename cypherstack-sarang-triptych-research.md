---
layout: wip
title: Triptych research and optimizations
author: Cypher Stack
date: April 8, 2021
amount: 22.86
milestones:
  - name: First 20 hours complete
    funds: 6.325
    done:
    status: unfinished
  - name: Second 20 hours complete
    funds: 6.325
    done:
    status: unfinished
  - name: Third 20 hours complete
    funds: 6.325
    done:
    status: unfinished
  - name: Fourth 20 hours complete
    funds: 6.325
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
---

THIS PROPOSAL HAS BEEN CHANGED FROM TRIPTYCH RESEARCH OPTIMIZATIONS TO TRIPTYCH MULTISIG RESEARCH AFTER A MEETING WITH THE MONERO DEVS ON APRIL 21, 2021.

## Brief Intro

As of April 12th, 2021, Aaron "Sarang Noether" Feickert has joined Cypher Stack LLC as a resident researcher.

Cypher Stack is a for-profit LLC owned by Diego "rehrar" Salazar. It started as a design firm but has since expanded to include blockchain consultancy and digital utilities and infrastructure hosting. They already donate to the Monero Project in the form of employing Dan "pigeons" Miller as a system administrator, who is responsible for running and securing much of Monero's infrastructure including Taiga, Matrix, and other key infrastructure in conjunction with the core team.

Sarang himself needs no introduction. A previous full-time researcher of MRL paid for by the CCS, he wants to continue doing research into next-gen privacy with Monero (particularly in Triptych), hence this proposal.

## The scope

Sarang Noether and collaborators created the Triptych and Arcturus privacy protocols, which, if implemented in Monero, could allow ring sizes of greater than 100 with similar size transactions to present ones (though verification times would increase linearly).

Work is already underway to include Triptych into Monero's codebase, but one of the big question marks shrouding the new protocol is multisig. The Monero ecosystem is maturing in such a way that Monero's multisig feature is being used in more and more applications, and moving to Triptych would break the current implementation. This could potentially stop Triptych's implementation in its tracks.

The goal of this proposal would be to do further research into Triptych's multisig options. Some research has already been done, and a path forward is already known, but the details and specifics need to be ironed out. Sarang would conduct this research to see if multisig is possible, and how a migration from the old to the new might be conducted in a way that is safe, private, and efficient.

## The structure, milestones, and price.

This proposal is structured to be paid out along time-based milestones, but the time will not be consecutive. Each milestone will be paid out at intervals of 20 hours.

In other words, after 20 hours-worth of work is complete, a payout will be made to the completed milestone, but it may take one month or more to complete this 20 hours depending on time, availability, and other concurrent projects.

We are putting in a request for 80 hours (one cumulative month worth) of work. We are requesting $100/hour for this highly specialized work, which comes out to $8,000. At the exchange rate of $350/XMR we reach 22.86 XMR. We round it up to 23 and add a 10% buffer, which brings us to 25.3 requested XMR.

## The Deliverables

Deliverables to the community: Sarang will give an update every calendar month on his progress to the Monero community in the form of a Reddit post in the Monero subreddit. Other update platforms can be explored as well. Keep in mind, because of the structure of the proposal, some updates may have little to no progress as a result of other work. These reports would say as much.

Deliverables to the devs: Sarang will provide write-ups, documentation, or proof-of-concept code to the developers as applicable based on research progress and results, toward the goal of a potential future Triptych release that meets the needs of the community.

## Risks

A risk of this research is that multisig may not be possible with Triptych after all. If this is ascertained early on, further research on Triptych may be unnecessary as it will not be fit for our use given the importance of multisig in the Monero ecosystem. This means the research will stop immediately, and any partially completed milestones will be paid out to the extent of hours fulfilled. Remaining funds can be dispersed amongst other active fundraising proposals or however Core sees fit. The funds should NOT be rolled into the general fund as usual due to a conflict of interest, which is outlined below.

It is also possible that the work is finished early. If this occurs, the remaining funds from milestones will be utilized in the same manner as previously stated in the event that Triptych multisig can not be used.

## Conflict of interest

After some discussion on IRC I have added this section at the end to clarify that I, Diego Salazar, owner of Cypher Stack and employer of Sarang Noether, am also paid by the general fund to work for the Core Team. I have powers to merge in the CCS but only do so with permission from luigi1111, who oversees the whole CCS system. I recuse myself from any sort of merging or moving processes with this CCS proposal due to the conflict of interest.

Cypher Stack also has another active research contract with privacy coin Firo, and Sarang works on this project.
