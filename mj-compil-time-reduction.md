---
layout: fr
title: Compilation time reduction and housekeeping
author: mj
date: April 15, 2020
amount: 52.9
milestones:
  - name: ccache for CMake (demo)
    funds: 0 XMR
    done:
    status: finished
  - name: Dynamic linkage
    funds: 2% (0.9 XMR)
    done:
    status: unfinished
  - name: Automated reports of ClangBuildAnalyser and iwyy
    funds: 4% (2 XMR)
    done:
    status: unfinished
  - name: Automated reports of Valgrind (test bottlenecks)
    funds: 2% (1 XMR)
    done:
    status: unfinished  
  - name: Optional precompiled headers for CMake 3.16
    funds: 4% (2 XMR)
    done:
    status: unfinished
  - name: Moving boost headers out of own headers 1/3
    funds: 9% (5 XMR)
    done:
    status: unfinished
  - name: Moving boost headers out of own headers 2/3
    funds: 19% (10 XMR)
    done:
    status: unfinished
  - name: Moving boost headers out of own headers 3/3
    funds: 19% (10 XMR)
    done:
    status: unfinished
  - name: Forward declarations of own classes + interfaces
    funds: 15% (8 XMR)
    done:
    status: unfinished
  - name: One class per header
    funds: 4% (2 XMR)
    done:
    status: unfinished
  - name: Parallel tests (ctest -jN)
    funds: 9% (5 XMR)
    done:
    status: unfinished
  - name: Static methods of the wallet2
    funds: 8% (4 XMR)
    done:
    status: unfinished
  - name: Proper ordering of headers (general last)
    funds: 6% (3 XMR)
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
---

# What
The proposal is about minimizing the compilation time of the project. 

# Who
I have 12 years of object oriented programming experience, mostly in C++. I'm a passionate programmer, not only somebody who does this for money. I hold a M.Sc. degree in Computer Science.
Although I'd prefer staying anonymous, what I can tell about myself, is that I used to actively develop a couple of space flight navigation instruments in C++ for a realistic freeware space flight simulator. 
Nowadays I work on an automated trading and backtesting platform, also in C++, where speed matters.
Being able to see the code in a hierarchical order, both projects allowed me to create an extensive library, ready to be reused in a project like Monero, with serialization being my first low hanging fruit.
To pay the rent, I've worked in various fields, from automatic control, GIS apps, navigation systems, visual driving assistance and recently in autonomous driving.
My contributions to Monero so far are the following:
- I was able to bring ccache to the project. The amount of code committed is not large, but the effect size is. The Travis CI compilation time went from 22 minutes down to [2 minutes for each build](https://github.com/monero-project/monero/pull/6452#issuecomment-615024910).
- afterwards, selsta picked it up and [brought ccache to the CI "workflows"](https://github.com/monero-project/monero/pull/6495), achieving similar results.
- upon a request by vtnerd, [I made the ccache optional](https://github.com/monero-project/monero/pull/6501).

# Why
During all these years I have noticed how important it is to have a quickly compilable code base, which would otherwise put a negative psychological pressure on developers, making them refrain from changing anything for the better, not to mention the obvious reduction of required computational resources.
For Monero specifically, I have set up the following experiment:
I have calculated the sizes of header files, summing up the sub headers included by each of them (column 3). Then I have calculated how many times a given header is included by .cpp files (column 4), thus indicating both the approximate compilation time of the header and how many .cpp files would be affected by the change if the header (column 2) and sorted ascending by this value. Below is the list of the greatest 90% of the headers, using this convention:

```
11% = 10495 = 2099 * 5:	cryptonote_boost_serialization.h	
12% = 11907 = 1323 * 9:	wallet2_api.h	
13% = 12393 = 4131 * 3:	cryptonote_core.h	
13% = 12924 = 718 * 18:	crypto.h	
16% = 14856 = 4952 * 3:	core_rpc_server.h	
17% = 15990 = 1599 * 10: rctTypes.h	
17% = 16500 = 3300 * 5:	blockchain_db.h	
26% = 24225 = 8075 * 3:	blockchain.h	
30% = 27979 = 3997 * 7:	core_rpc_server_commands_defs.h	
61% = 56616 = 2696 * 21: cryptonote_basic.h	
100% = 92620 = 9262 * 10: wallet2.h
```

It becomes obvious, that the wallet2.h is the largest "hot spot" of the whole project. While compilation of the project took 30 minutes, touching the wallet2.h and recompiling took entire 6 minutes = one fifth.

# Milestones
What can be done with this is creating as many wrappers of the boost library as possible and putting as much as implementation code into .cpp files, instead of insisting on writing them inline, when these spots aren't bottlenecks. Putting a trivial method as inline may help, but only when it's called very very frequently, and only if that improvement is a large percentage of other parts of the software, which it usually isn't. Inlining has to be proven by profiling the software, and not being a default policy, since it brings nothing, while costing a lot, not only because multiple recompiles of the code in .cpp files in one session, but recompiles upon changes of the inlined implementation.

I'd like to earn something like 40$/h. It's hard now to assess how much time it will take, so I'm not strict on the concrete values. If I happen to finish ahead of time, thus becoming overpaid, I will admit it. I will be writing the time of work in each of my PRs.
By assessing the payments, I will now assume a price of XMR of 125$. 


## Milestone 1: ccache for CMake (demo)
Done with quite a success. The Travis CI was relieved and you, as a developer benefit each time you switch a branch.
Previous text:
"I'd like the CMake script to automatically pick ccache and clcache, when it can find them in the PATH. This piece of software helps in reducing the compilation time of compilation units (.cpp files and all their included headers), when their content hasn't changed. This means, that the more forward declarations and fewer included headers your headers have, the more the ccache will be able to leverage your discipline. This is especially useful when switching between branches."

## Milestone 2: Dynamic linkage
Static libraries tend to grow in sizes exponentially and slow down the generation of the final binaries. I would like to enable (opt-in) dynamic linkage in CMake for development purposes. Also whenever you are done writing a new test and would like to just modify the production code and just execute the test, the test binary can be made so, that it doesn't have to relink upon change of the production code's resulting shared library.
This is quite a low hanging fruit. There are 70 CMakeLists.txt, so multiplying each one by 2 minutes gives 2.33h plus 0.30h for creating some framework for further such changes gives 2.83h, and that equals to 0.9 XMR.

## Milestone 3: Automated reports of ClangBuildAnalyser and iwyy
Some advanced tools can be employed, that help in dynamic assessment of the quality of the code from many perspectives. For my purpose, I could use (ClangBuildAnalyzer)[https://github.com/aras-p/ClangBuildAnalyzer], which gives an objective truth about which parts of the code take longest time to compile. There's also CLang-based (Include What You Use)[https://include-what-you-use.org/] tool, which not only gives advice how to optimize the bottlenecks, but also tries to do it automatically (however it's better to use it just as a hint).
And last but not least, there exist tools, which help finding dangerous constructs in the code, which could lead to segmentation faults at runtime.
I'd like to use my low powered PCs to generate a daily report of the CLang tools and publish them to a dedicated webpage, that I'd manage. I will of course contribute the scripts, that generate the reports into the Monero source tree. Setting up the tools will take some time.

## Milestone 4: Automated reports of Valgrind (test bottlenecks)
Similar as above, however done weekly, since this will take more time. The context is somewhat different here however. Valgrind is able to perform performance tests, able to catch new bottlenecks by executing the tests. I think it would be benefitial, if such reports were available for the public, since their generation costs plenty of time.
This task is somewhat easier, but I'd just like to get compensated for the power costs on this one, so I think that 1 XMR should be fair.

## Milestone 5: Optional precompiled headers for latest cmake
There will surely occur a situation, when a boost header cannot be reasonably wrapped, because it is used in a template code. Such headers are best handled by precompiled headers, reducing the compilation time by up to 50% per precompiled headed. CMake 3.16 is able to generate them natively. Since some users will still be using older versions of CMake, this has to remain optional. I will start with this one before moving the headers away, as this is a low hanging fruit, delivered by CMake devs.

## Milestone 6: Moving boost headers out of own headers 1/3
If the compilation is to be done faster, all of the 3rd party large headers have to be moved outside from our headers, thus preventing them to be propagated into files, that don't need them and waste time on parsing them. This can be done via forward declarations and careful analysis of the dependency tree.
My such header analysis shows, that there are currently 369 occurrences of boost headers. Since each compilation costs 8.5 minutes and each change 2.5 minutes, we are at 11/60 * 369 = 67.65h of active work, excluding time of testing and verifying the speed improvement (passive work). This leaves us with 21.6 XMR for the active work. Let's round it up to 25 because of uncertainty and required passive work, as well as power costs. This forces me to split the task into 3 parts for simplicity. But as before, if I'm done earlier that I calculated, I will admit this and will report the work time for each PR.

## Milestone 7: Moving boost headers out of own headers 2/3
See milestone 6.

## Milestone 8: Moving boost headers out of own headers 3/3
See milestone 6.

## Milestone 9: Forward declarations of own classes + interfaces
It will be of a lot help, if abstractions (interfaces) were used instead of concrete implementations. Then you can easily share just the forward declarations of the unused parts of the interface for the client using the i-face, and include only these parts, which are needed. It can be achieved quite easily by creating and returning a unique pointer to an object of an implementation within a static function of the interface.
There are 358 .cpp files, and definitely more classes than that. If I were to start from the "hottest" 50 classes first, to achieve largest results at the beggining, I'd need 20 hours, assuming 15 minutes of active work on a class and 8.5 minutes of compilation time ((8.5+15)/60 * 50 = 19.58). This would equate to 6.26 XMR. Rounding up for the power costs, let's say 7 XMR.

## Milestone 10: One class per header
It also helps reducing the probability of having to recompile a large chunk of sources, if the classes are declared one per header. Better segmentation also helps ccache reuse its cache, if there's better granularity.
Since this is quite a mechanical work, not needing ANY analysis, I'd say 2 XMR would be enough.

## Milestone 11: Parallel tests (ctest -jN)
Did you know, that ctest allows for running the tests in parallel, just like make does? The problem is, that if they use the same resources during execution, they might (and in our case they do) affect each other. The task here would be to group the tests, which use the same resources and run them sequentially, while running other similar groups in parallel.
I honestly haven't done any analysis on this one yet (other than proving that it doesn't work yet), as there are other things to do, that's why I'll just shoot in the dark here with 5 XMR, or could leave it for somebody else to do.

## Milestone 12: Static methods of the wallet2
I'd like to address here the problems mentioned by Endogenic (highlighted at Konferenco)[https://www.youtube.com/watch?v=AsJaMw-3gGE&feature=youtu.be&t=25614] (thanks, Scott Anecito!), namely making the wallet2 as stateless as possible. I propose here 4 XMR, as this is one of the largest classes in the whole project (if not the largest).

## Milestone 13: Proper ordering of headers (general last)
The order of writing header files is not just a matter of taste. The proper order is local first, and more generic at the bottom, because only this way you could discover hidden dependencies, that you force the client to include manually. This is nicely described (here)[https://blog.knatten.org/2010/07/01/the-order-of-include-directives-matter/] and (here)[https://stackoverflow.com/questions/2762568/c-c-include-header-file-order/2762596#2762596]
With 358 .cpp files, this will take some time and is so mechanical, that I'd gladly leave it to an undegrad, but there were no takers for this yet.
Shall we make it 3 XMR?


# Expiration date
1 Jan, 2025
