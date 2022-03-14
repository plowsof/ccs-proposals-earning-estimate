---
layout: wip
title: j-berman full-time development (3 months)
author: j-berman
date: February 7, 2022
amount: 135
milestones:
  - name: Month 1
    funds: 33% (45 Monero)
    done:
    status: unfinished
  - name: Month 2
    funds: 33% (45 Monero)
    done:
    status: unfinished
  - name: Month 3
    funds: 33% (45 Monero)
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

Hi all, I love my new job and very much so hope that my performance has been satisfactory. I'm requesting 135 XMR to continue working on Monero full-time for the next 3 months (2/7/22 - 5/2/22).

On my immediate radar, I'd like to help ensure the upcoming fork goes smoothly. I can take on the following:

- help the ecosystem prepare for view tags:
	- [monero-lws](https://github.com/vtnerd/monero-lws)
	- [openmonero](https://github.com/moneroexamples/openmonero)
	- potentially others if needed
- help resolve merge conflicts between PR's
- bump the ring size from 11 to 16 (tiny bit more effort than changing a single constant) (edit: PR for this [here](https://github.com/monero-project/monero/pull/8178))
- whatever else I have the skills to help on

Beyond the fork, here are some concrete tasks I'd also like to work on:

### [Background wallet sync cache](https://github.com/monero-project/monero/issues/8082)

This is a great idea by @hyc for wallets to continuously scan for a user's transactions in the background. This should make scanning a more pleasurable experience on mobile. The key idea behind the proposal is keeping the view key "hot" on the device, but *not* the spend key. This way wallets can more safely do this background scanning without leaving a spend key exposed.

### Subaddresses in [`monero-lws`](https://github.com/vtnerd/monero-lws)

I proposed a way to implement subaddresses in light wallet servers in [this PR](https://github.com/monero-project/meta/pull/647). I'd like to see this through to completion. To me, completion == there is a well-tested client-server implementation (with tests), where a frontend can interact with your own running `monero-lws` server. Been in communication with various light wallet ecosystem folks to move forward to flesh out the details of the API spec (shoutout to @endogenic, @vtnerd, and @ndorf for their involvement) :)

### Complete monero-lws informal audit if there is demand

If there is demand, I'm happy to complete [this review of monero-lws](https://github.com/vtnerd/monero-lws/pull/29) I started as part of my prior CCS. To be clear, I've read through the whole code base, and stand firm behind my conclusion that it is great software with no obvious backdoors. There are a number of files I left as "TO-DO's" in the review since it was taking up a lot more time than anticipated. Happy to fill it out if people would like.

### Other tasks

I have a running list of stuff I'd like to get to (some rolled over from last CCS):

- complete [these issues](https://github.com/vtnerd/monero-lws/issues/created_by/j-berman) as needed in monero-lws + work through the suggestions shared in [my review](https://github.com/vtnerd/monero-lws/blob/16f1ceaa6a5eb4d9263863068bf57bc8e032a408/docs/review_02.03.22/review_02.03.22.md#suggestions)
- continue investigating ways to make wallet scanning faster
- pick up on research into [deterministic binning](https://github.com/monero-project/research-lab/issues/84)
- [thread safety in the daemon RPC](https://github.com/monero-project/monero/pull/7936)
- implement a rw lock for the Blockchain class
- encrypt the wallet cache

## Who

j-berman on github, jberman on Matrix/IRC, and here is my [last CCS](https://ccs.getmonero.org/proposals/j-berman-3-months-full-time.html).

Merged commits: [monero-project/monero](https://github.com/monero-project/monero/pulls?q=is%3Apr+author%3Aj-berman+is%3Aclosed), [openmonero](https://github.com/moneroexamples/openmonero/pulls?q=is%3Apr+author%3Aj-berman)

Open commits: [monero-project](https://github.com/monero-project/monero/pulls/j-berman)

## Proposal

Requesting 135 XMR, which is a 25% raise from last CCS proposal from (0.08 XMR + $24)/hr to (0.1 XMR + $30)/hr, for 480 hours (12 weeks), at $168 / XMR from coingecko. This hourly rate totals to 133.8 XMR for the period (0.1 XMR + $30/$168 XMR = 0.279 XMR/hr * 480 hrs = ~133.8 XMR), which divides into 3 payments of 44.6 XMR. I rounded 44.6 XMR up to 45 XMR to land on a total of 135 XMR (3 * 45 = 135 XMR).

My prior CCS, I ended up working about a month longer than expected without submitting another CCS, since I wanted to see things through to completion as best I could, and prioritize must-do work before spending time wrapping up the prior CCS, and writing this proposal. I'd like to have more flexibility and comfort in making a decision like that, which I feel a higher rate affords.

I will share monthly updates, and will keep track of my hours as before, but likely won't be submitting an hourly time tracking spreadsheet with each update (it feels a little invasive and no one seems to care about it anyway, I probably shouldn't have done it in the first place). I'll also continue attending every #monero-research-lab + #monero-dev meeting I can, and sharing what I work on there when applicable.

Final note: if I run into any bounties that I want to work on in the future (like [view tags](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero)), I'd like to work on them as part of my CCS, and pay the bounty out to PR reviewers (and in some cases, to original idea-havers too). I'd like to have flexibility to make decisions on what I think would be most valuable for me to work on, but will always welcome feedback :)
