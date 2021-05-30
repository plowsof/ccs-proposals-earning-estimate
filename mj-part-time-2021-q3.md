---
layout: fr
title: mj part time coding Q3 2021
author: mj
date: Jun 30, 2021
amount: 45 XMR
milestones:
  - name: Month 1
    funds: 15 XMR
    done:
    status: unfinished
  - name: Month 2
    funds: 15 XMR
    done:
    status: unfinished
  - name: Month 3
    funds: 15 XMR
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


﻿# What

In the same way as previously, I propose to work for 3 months, spending additional 20 hours a week on Monero Core, specifically on topics such as:
- CI fixes
- code reviews
- addressing user issues (whenever I can help)
- enabling new developers to submit their patches quicker
- extending my [Monero health report](http://enjo.hopto.org/pub/monero/)
- general firefighting, whatever problems we face in near future

When there’s nothing left to extinguish, I'll be fixing compiler warnings and Clang-Tidy findings. Last time, there was so much other work, that I didn’t really even reach this topic, except for compiler warnings.

# Why

During preparation of my last such quarterly proposal, I noticed quite annoying nondeterministic CI failures, that I was able to fix, thanks to your funding and the Team's cooperation through reviews and integration. Please make your own opinion on how valuable my changes were. Due to the lack of a better measure, I propose comparing the number of pages of failed builds per month before and [after](https://github.com/monero-project/monero/actions?page=3&query=is%3Afailure) merging my change on the 30th March. In short, there are only 3 such pages in recent 2 months after, while the previous 2 months, before merging, marked a many as 7 such pages, until [here](https://github.com/monero-project/monero/actions?page=10&query=is%3Afailure)

The ability of improving this weak point of the development process gave me a lot of hope, that the somewhat disruptive, but positive changes are accepted, therefore the development will not come to a halt at some point. I'd like to continue working on such project and bring other similar improvements.


The details of the already identified work packages are the following:

## CI
- In the CI there's still an unresolved issue of FreeBSD not using ccache, thus taking unnecessary time for recompilations. This was left alone, due to the fact, that it's not a critical matter. However having this solved would be a cherry on top of the Monero's CI. I can't promise that it will be possible to fix and I haven't had time yet to look into it in detail, but I do know how to analyze such errors.
- Recently I noticed, that Unit Tests fail under Mac OSX. It wouldn't hurt to run only the UTs under OSX as one of the CI steps, as they cost only 10 minutes of processing time. Fixing the UTs would also be part of my job here.
- The CI could use a matrix of all the supported Boost library versions. As [discovered here](https://github.com/monero-project/monero/pull/7735), changes of the boost headers need to be handled with caution, in order not to introduce compilation regressions across still unchecked Boost versions. This is what a CI is for. 

## Enabling new devs
- The efficient compilation and debugging document, whose value you can measure via [this link](https://github.com/monero-project/monero/blob/master/docs/COMPILING_DEBUGGING_TESTING.md), is where the new developers could read, in order to learn faster how to integrate their patches, avoiding a steep learning curve and waiting times. This document will be continuously extended with setups for various IDEs and other such findings
- I need to continue the automation of adding all the headers to the IDEs' project files. Both the missing ones and those to be added in the future. The framework for this is already prepared. What's left is some monkey business of simply identifying the gaps and using the framework. Nothing hard, but time consuming. Having this level of order in the IDEs leads to a great reduction of confusion for developers while they change header files.

## Health report
- I extended my [Monero health report](http://enjo.hopto.org/pub/monero/) with the lcov report lately (Line coverage of tests), but didn't have the time to really integrate the report generation into Monero itself. I only do it locally. Therefore other devs can't generate such a report for themselves yet. The script would be a perfect fit to the collection of other health-related tools in Monero.
- I have some other handy source analysis tools, that go in the direction of Include What You use, but are not that dependency heavy and deliver less noise. This means, that everybody can run such an evaluation on almost no-time, while the other Clang-based tools take about 1,5 hour each, however complete they are.
- both of the above scripts, although serve their purpose, are not production ready from the code quality perspective, so I myself wouldn't want to merge this into the official repo in their current preliminary state. This needs some focused work now.

## Small issues
Some small things that I've flagged as reminders for now:
- [Adding regression tests](https://github.com/monero-project/monero/issues/7756)
- [Addressing previous PR comments for documentation](https://github.com/monero-project/monero/issues/7755)

# Previous reports
I'm sure you've either already read them or simply found them too long anyway, so I'll just link here the previous reports, that describe my completed or started tasks in more detail:
- [Report 01](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/200#note_10764)
- [Report 02](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/200#note_10860)
- [Report 03](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/200#note_10954)
 
# Proposal

I am able to realistically spend 20 hours a week more on Monero, additionally to my compilation time reduction efforts, which move at a slow pace. I will start not sooner than from the middle of June, due to current personal workload.

I propose a wage of 40 $/h for 3 months. As of 30.06.2021 (1 day before Q3) the XMR/USD is at around 217 $. This would make a total of:
40 $/h * 20 h/week * 4 weeks * 3 months / 217 XMR/USD ~ 45 XMR. (3 times 15 XMR)

Cheers!


# Expiration date
15 Sep, 2021
