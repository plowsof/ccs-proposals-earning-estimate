---
layout: wip
title: "TheCharlatan: VPS funding for reproducible gui builds"
author: TheCharlatan
date: 22 January 2020
amount: 14
milestones:
  - name: VPS
    funds: 15.01 XMR (actual amount raised)
    done:
    status: unfinished
payouts:
  - date:
    amount:
---
### What are Reproducible builds and why do we need it?

[Reproducible builds](https://reproducible-builds.org/) (aka "Deterministic Builds") are a set of software development practices that create an independently-verifiable path from source code to the binary code used by computers. 
See this [reddit post](https://www.reddit.com/r/Monero/comments/9wojxi/the_watering_hole_attack_and_some_points_on/) I wrote some time ago explaining some of the reasons we need this. 

### Why you should fund me:

About two years ago I started my journey to support a cross-platform reproducible way to compile the monero cli binaries. After creating the first funding request at the end of last year (again to fund renting a VPS) I began developing the tools and documentation needed for Reproducible Builds (old tracking issue [here](https://github.com/monero-project/monero/issues/2641) and already merged code [here](https://github.com/monero-project/monero/commits?author=TheCharlatan)). 

My work culminated into the [Boron Butterfly, Major Point Release 1](https://github.com/monero-project/monero/releases/tag/v0.14.1.0), which was the first monero release that was reproducibly built. I was glad to see the community [enthusiastically embrace](https://www.reddit.com/r/Monero/comments/c0l7tj/cli_v01410_has_been_tagged/) this new tool with many contributing their signatures of the release binary hashes to the [gitian.sigs](https://github.com/monero-project/gitian.sigs) repository, which I now maintain. It also has to be noted that other developers, chiefly amongst them Howard Chu and Jonathan Cross, expanded on my contributions, cleaning them up and adding further build targets, like freebsd (many thanks to them!).

The obvious step now is to add reproducible builds to the monero-gui. A first step in this direction was made by adopting my rough cmake recipe in this [pull request](https://github.com/monero-project/monero-gui/pull/2404). To get this far was a lot of work. Now, I am again asking for the tools to continue my work. The main bottleneck I face is access to modern, fast hardware to test these resource intensive build system changes.

I am therefore asking the community to help fund access to fast hardware to improve my efficiency.

### Funding details:

I currently work on a VPS / cloud server and I will apply whatever funds I receive from the community towards it, as my current contract will expire next month and I don’t have excess funds to renew it.

12  [month development workstation VPS](https://www.worldstream.nl/en/dedicated/custom/order/HP_ProLiant_DL360_2x_Intel_Xeon_E5620_2_40GHz?config_token=42d84460e0f0af36d72fb0e07ba5b181) 
€ 64 / month × 12 months = € 786 approx. 14 XMR (rounded up to account for fluctuations)

If I find a better fitting VPS host for the same cost, I reserve myself the right to use it instead.

NOTE: If some generous souls end up donating more than the amount requested, I will gladly apply that towards faster hardware, more RAM, etc.  The project (and my productivity) would benefit greatly from a more powerful computer than the one I am requesting (I could easily make use of 16 or even 32 cores, 64GB DDR4 RAM, etc).

## What I will do with the VPS

On the monero cli side I would like to finish the following over the next year:
* Support compiling the tests in the strict gitian environment
* Build and verify release binaries from other gitian builders

For the gui my work will mainly include:

* Writing build recipes to cross-compile qt with opengl support
* Improving the cmake recipe
* Lots of small iterative changes to get the hairy bits like device support and better native performance working
* Finally releasing gitian build scripts for the gui builds

### About me

I'm a physics and computer science student studying at the University of Zurich and I do part time work as a developer at a hardware wallet manufacturer: https://github.com/digitalbitbox . My contributions so far to Monero are found [here](https://github.com/monero-project/monero/commits?author=TheCharlatan) and [here](https://github.com/monero-project/monero-gui/commits?author=TheCharlatan). I currently still view working on Monero as a hobby, so I am not looking for hourly compensation, however the hardware costs are a problem for me and I do not want this to restrict my contribution to the project. I have already implemented reproducible builds for the cli and for other gui based projects, so I am reasonably confident that I will be able to complete them for the gui as well, despite the significant challenges it presents.

Next to the reproducible builds I have also started tinkering into the direction of writing a flexible monero transaction library in Rust that can be used in both on-system and embedded contexts.

If you have any questions or concerns about this funding request, please don’t hesitate to reach out to me.
