---
layout: wip
title: xiphon part-time coding (3 months)
author: xiphon
date: 20 Jul 2020
amount: 215
milestones:
  - name: Sep
    funds: 33% (71 XMR)
    done: 30 September 2020
    status: finished
  - name: Oct
    funds: 33% (71 XMR)
    done:
    status: unfinished
  - name: Nov
    funds: 33% (73 XMR)
    done:
    status: unfinished
payouts:
  - date: 15 October 2020
    amount: 71
  - date:
    amount:
  - date:
    amount:
---

# What

Would love to prolong my part time Monero coding for another 3 months.  

There are some specific tasks i would like to work on first.

* Monero GUI Windows static build.  
  Plan to utilize cross-compilation using recently implemented Docker Monero GUI Linux static build environment.  
  If there will be any unresolvable issue, we can use Windows native Docker container (based on Windows Server image), but the approach will require using Windows as a host system.  
* Investigate (and implement if possible) Monero GUI MacOS bundle build environment.  
* Reproducible Monero GUI Linux build.  
  Depending on the first task, might also implement Windows reproducible builds, this is unclear at the moment.  
* Explore Windows GUI binaries signing with a Microsoft certificate.  
  Could help us to mitigate AV related issues on Windows.  
  Figure out the procedure and the requirements.  
  Signing doesn't play well with reproducibility. Think this could be resolved by using/implementing some custom software or a script that will verify signed binary contents skipping the signature. Want to investigate this.

As usual will be working on Monero Core and Monero GUI code:
* Inspecting and implementing ongoing feature requests
* Submitting bug fixes
* New functionality
* Code review
* Putting my efforts where it is appropriate

# Who

I'm Xiphon, active contributor to Monero Core and Monero GUI since July 2018.  

My previous CCS proposals: 
* https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/99
* https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/55
* https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/122
* https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/139

During the recent 30h/week proposal i implemented:
* Docker Monero GUI Linux static build. CMake integration.  
  `release` build target support (Linux, Windows, MacOS).  
  `release-static` build target support (Linux and Windows).  
  CMake continuous integration (Github Workflows) support on Linux, Windows, MacOS hosts.  
  A user can now run just a couple of commands to build Monero GUI Linux static binary:  
  https://github.com/monero-project/monero-gui/#building-linux-static-binaries-with-docker-any-os  
* Socks5 support in Monero GUI Advanced mode (remote node only) *(Work in progress)*  
  Runtime proxy configuration support in Monero Core Wallet API.  
  Integrating Socks5 proxy support into the GUI right now.  
* Portable mode for Monero GUI  
  https://github.com/monero-project/monero-gui/pull/3026

in order to not clutter the proposal i'm not listing all the related pull requests this time. I strongly encourage you to visit the following Github links to see the amount of work done by me, its quality and importance for the Monero Project.

Please check the following links to inspect my Monero-related activity:  
- Monero Core - https://github.com/monero-project/monero/pulls?q=is%3Apr+author%3Axiphon
- Monero GUI - https://github.com/monero-project/monero-gui/pulls?q=is%3Apr+author%3Axiphon

# Proposal

Looking forward to coding and accomplishing mentioned and ongoing tasks and issues. Implementing new code/functionality that will be needed. Investigating bug reports and submitting bug fixes, fixing build and compilations errors/warnings/etc. Would like to inspect and complete/fix/address issues and feature requests that are reasonably desired and/or worth to spend time on. Improving GUI, fixing UI/UX issues, implementing design changes.

Dedicate 30 hours per week to Monero Project, at 55 USD/hour rate for a total of 215 XMR. XMR/USD rate is based on the 14-day moving average exponential on Kraken from 20 Aug 2020, which is approximately 92.16 XMR/USD.
