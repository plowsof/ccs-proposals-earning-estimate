---
layout: wip
title: mj part time coding Q2 2022
author: mj
date: Mar 01, 2022
amount: 102.0 XMR
milestones:
  - name: Month 1
    funds: 34.0 XMR
    done: 30 March 2022
    status: finished
  - name: Month 2
    funds: 34.0 XMR
    done:
    status: unfinished
  - name: Month 3
    funds: 34.0 XMR
    done:
    status: unfinished
payouts:
  - date: 2 April 2022
    amount: 34
  - date:
    amount:
  - date:
    amount:
---


# What

I propose to work for 3 months, spending 30 hours a week on Monero Core and Monero GUI, specifically on topics such as (in this order):
- reviewing the Monero Core and GUI code
- enabling and helping new developers
- providing more documentation for new devs
- CI fixes
- addressing user issues (whenever I can help)
- benchmarking [tsqsim](https://github.com/mj-xmr/tsqsim) (although this one is arguable)
- regenerating and extending my [Monero health report](http://cryptog.hopto.org/monero/health/)
- adding Monero-GUI to the health report
- general firefighting, whatever problems we face in near future

# Why

Over the last 3 month period, I've been fully focused on developing my [tsqsim](https://github.com/mj-xmr/tsqsim) tool for Monero Research Lab's [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) project. Even though I did occasionally review new code in Monero Core and GUI, a few members noted that since I was being focused on the tool so much, they felt developer resources being dragged away from Core/GUI. I'd gladly take it as a compliment :>

The current state of tsqsim is "usable", but not yet perfect. To unleash its full potential, some more work has to be put in: I estimate ~2-4 months. However this can be scheduled for later (and half-time) as well, while the OSPEAD research could already start, based on the current state of tsqsim.

Therefore in the next 3 months, I'd like to catch up with the usual maintenance. Additionally, I'd like to continue enabling new devs, by pointing them to documentation, explaining and extending it. Previously, I was helping new devs in the #monero-dev channel. Just recently I noticed, that there's quite a crowd awaiting directions in the Recruitment Matrix Channel, formed at the end of last year by @Rucknium (correct me if I'm wrong). I promised them, that I'd be available from March for either 1-on-1 sessions or to answer general questions in the channel.

## Benchmarking tsqsim

A special sub-task of the quarter would be benchmarking the tsqsim, requested by @selsta and @bigbklynballs. Even though C and C++ remain the fastest languages (yielding only to Assembler), I'm of the opinion, that the USP of tsqsim is the ability of setting up controlled experiments, without the need of them to be coded by the Researcher. This fact will be reflected by the benchmark, or more generally then: a comparison. While the user @bigbklynballs suggested benchmarking tsqsim against [all of his proposed 10 alternatives](https://libera.ems.host/_matrix/media/r0/download/libera.chat/ffa8bb5c2f97fd1ff5b9990a70f139ad96586270), which were:

- https://github.com/statsmodels/statsmodels
- https://github.com/rapidsai/cuml
- https://github.com/h2oai/h2o4gpu
- https://github.com/alkaline-ml/pmdarima
- https://github.com/timeseriesAI/tsai
- https://github.com/facebookresearch/Kats
- https://github.com/unit8co/darts
- https://github.com/winedarksea/AutoTS
- https://github.com/alan-turing-institute/sktime
- https://github.com/linkedin/greykite

, I'll spare the Community's funds by restricting the benchmarking process to 1 or 2 of the above tools and then ask for further wishes.

# Who

mj, I have been contributing to Monero-core since 2020. Here is a [list of my previous work](https://github.com/pulls?q=is%3Apr+author%3Amj-xmr+archived%3Afalse+is%3Amerged+), all related to Monero, even if it got upstreamed.


## Previous reports
Here is a list of the previous reports, that describe my completed or started tasks in more detail:
- [Report 01](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/200#note_10764)
- [Report 02](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/200#note_10860)
- [Report 03](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/200#note_10954)
- [Report 04](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/231#note_11248)
- [Report 05](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/231#note_11421)
- [Report 06](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/231#note_11662)
- [Report 07](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/266#note_14040)
- [Report 08](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/266#note_14436)
- [Report 09](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/266#note_14671)

[Previous CCS Proposal](https://ccs.getmonero.org/proposals/mj-part-time-2021-q4.html)
[Postponed CCS Proposal (tsqsim)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/283)

# Proposal

I will spend 30 hours a week on Monero for the next 3 month period, starting from 1st March.

I propose a wage of 45 €/h for 3 months. As of 01.03.2022 the average between the opening and closing price of XMR/EUR was at (159.850 + 151.990)/2 = 155.92 € [according to investing.com](https://www.investing.com/crypto/monero/xmr-eur-historical-data). This would make a total of:
45 €/h * 30 h/week * 4 weeks * 3 months / 155.92 XMR/EUR = 103.899 XMR. Rounded down to be divisible by 3 -> 102 XMR.

Cheers!



# Expiration date
30 Jun, 2022
