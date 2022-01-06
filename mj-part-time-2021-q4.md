---
layout: wip
title: mj part time coding Q4 2021
author: mj
date: Oct 20, 2021
amount: 72.0 XMR
milestones:
  - name: Month 1
    funds: 24.0 XMR
    done: 30 November 2021
    status: finished
  - name: Month 2
    funds: 24.0 XMR
    done: 31 December 2021
    status: finished
  - name: Month 3
    funds: 24.0 XMR
    done:
    status: unfinished
payouts:
  - date: 4 December 2021
    amount: 24
  - date: 5 Jan 2021
    amount: 24
  - date:
    amount:
---


# What

In the same way as previously, I propose to work for 3 months, spending 30 hours a week on Monero Core, specifically on topics such as (in this order):
- statistical simulation (see [Proposal](#Proposal))
- addressing user issues (whenever I can help)
- enabling and helping new developers
- code reviews
- CI fixes
- extending my [Monero health report](http://cryptog.hopto.org/monero/health/)
- adding Monero-GUI to the health report
- general firefighting, whatever problems we face in near future

# Why

I need to raise the stakes unfortunately, since I'm strongly considering ditching my job, which became a pain in my back. This means, that I will be more dependent on the XMR money. Also, since I live in Western Europe, I pay my bills in EUR, which is seemingly going down against USD in a long term trend.
I normally hate hearing from people, who I have to hire to do things, which they can do better than me, that "they Have to earn more". I prefer saying first what additional stuff I'll deliver. Since my job will not get into the way as it did before, I will have more mental capacity to learn and read about the internals of Monero (outside of the proposed 30h/w). So far I've been doing (and gaining experience in) a lot of support tasks and I'm happy with the results as far as they can be reviewed and merged by the Maintainers. However there are now also some new challenges in Monero, which deal with statistics. I have some self-taught knowledge the field and I could provide some time series simulations, that would help in verifying if a given statistician's (or my) solution is able to yield the expected results in multiple alternative scenarios, as opposed to relying on a fixed history, which always leads to [overfitting](https://en.wikipedia.org/wiki/Overfitting). Please refer to the wonderful work of [Nassim Nicholas Taleb](https://en.wikipedia.org/wiki/Nassim_Nicholas_Taleb), especially [Fooled by Randomness](https://en.wikipedia.org/wiki/Fooled_by_Randomness) for more background. I already have a working software for such simulations, but it has to be adapted to fit Monero. I'd gladly reuse it for you guys, while you'd only pay for the adaptation itself. I think it's a good deal. I've been working on this software for many years for the purpose of statistical analysis of financial data, and a huge amount of them.


Some more details and summaries of other work packages are below:

## Statistical simulator

Here are the most relevant features of the simulator, that I'd adapt for Monero:

- Parallel Monte-Carlo simulation of alternative scenarios. The result of such a simulation are median and standard deviation of all experiments (in other words: the expected value as well as best and worst case scenario)
- The resulting value(s) are of a unit, defined by whatever objective function that is being fed into the simulator. In my current case of the financial simulation, it's the trading profitability.
- Smooth interfacing with Python (either via Boost or TCP), as Python is the (reasonable) language of choice for Statisticians. This means, that the Statisticians will not have to immediately rewrite their code to C++, if they want to have them checked by a very fast C++ simulator, compared to an analogous task, performed by Python code.
- Very fast loading of serialized data

The current visuals of my simulator can be seen below:

### Visualization

The visualization allows to take a closer look at what happens on the lowest level:

![QT](http://cryptog.hopto.org/monero/sim/sim-qt.png)

### Configuration

The current configuration UI, which produces serializable configuration files:

![Cfg](http://cryptog.hopto.org/monero/sim/sim-config.png)

### Evaluation

A console program, which performs the evaluation on larger data in parallel and joins them, plotting the result in the console:

![Test](http://cryptog.hopto.org/monero/sim/sim-test.png)

### Reporting

An HTML report is being generated after each evaluation. Here's how it currently looks:

A compound report, like in the console evaluation:
![Rep1](http://cryptog.hopto.org/monero/sim/sim-report-whole.png)

An individual report for each component:
![Rep2](http://cryptog.hopto.org/monero/sim/sim-report-indiv.png)

## CI
Me and the team were able to fix the prevailing [FreeBSD ccache issue](https://github.com/monero-project/monero/pull/7832). I also [separated the caches](https://github.com/monero-project/monero/pull/7780) based on how often they have to be recreated, which in turn saved space, so that GitHub doesn't have to purge them as often as before. All this together lead to a lot quicker reactions.
I don't see a potential for improvements of the CI anymore, which makes me happy. We can work relatively efficiently now, offsetting a lot of testing onto the CI without having to wait for a long time, nor having a bad feeling about abusing the service.
However, as soon as an unpredictable problem appears on the CI, I'm ready to address it.

## Enabling new devs
I helped in adaptation of Monero for RPi4 in the last month. I found it encouraging to work with people, who know what they want and are able to react lively. I spent some time on introducing new devs into the project, but somehow they gave up. OTOH, many new Monero devs, who didn't give up, to say the least, often message me privately with C++ questions, that I'm always happy to answer. I'd bet a lot of XMR, that it saves them a lot of frustration and time of own research. I'll happily keep doing it all.

## Health report
- I extended my [Monero health report](http://enjo.hopto.org/pub/monero/) with the Memory consumption (for compilation) report lately uncovering a huge RAM consumption of source files like `wallet2.cpp`. [See here](http://cryptog.hopto.org/monero/health/data/753dc901a/753dc901a-mem-usage-prod.txt).
- The report will be extended to cover Monero-GUI
- I will keep adding next tools into Monero codebase itself, whenever I decide, that they will have reached a production-ready state

# Who

mj, I have been contributing to Monero-core since 2020 with 73 merged commits. Here is a list of my previous work:

CLI contributions: https://github.com/pulls?q=is%3Apr+author%3Amj-xmr+archived%3Afalse+is%3Amerged+

## Previous reports
Here is a list of the previous reports, that describe my completed or started tasks in more detail:
- [Report 01](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/200#note_10764)
- [Report 02](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/200#note_10860)
- [Report 03](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/200#note_10954)
- [Report 05](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/231#note_11248)
- [Report 06](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/231#note_11421)
- [Report 07](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/231#note_11662)

Previous CCS: https://ccs.getmonero.org/proposals/mj-part-time-2021-q3.html


# Proposal

In Q4, I am able to realistically spend 30 hours a week on Monero. I arranged everything so, that the Q4 and January will be easy on me, so I won't have to prolong the work (and payment) like I had to do it in Q3. I'd like to start in November.

I propose a wage of 45 €/h for 3 months. As of 20.10.2021 the XMR/EUR is at around 220 €. This would make a total of:
45 €/h * 30 h/week * 4 weeks * 3 months / 220 XMR/EUR = 73.6 XMR, rounded down to be divisible = 72 XMR

Cheers!


# Expiration date
31 Jan, 2022
