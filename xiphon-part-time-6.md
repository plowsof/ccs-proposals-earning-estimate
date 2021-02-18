---
layout: wip
title: xiphon part-time coding (3 months)
author: xiphon
date: 1 Nov 2020
amount: 162
milestones:
  - name: Dec
    funds: 33% (54 XMR)
    done: 31 December 2020
    status: finished
  - name: Jan
    funds: 33% (54 XMR)
    done: 31 January 2021
    status: finished
  - name: Feb
    funds: 33% (54 XMR)
    done:
    status: unfinished
payouts:
  - date: 25 January 2021
    amount: 54
  - date: 18 February 2021
    amount: 54
  - date:
    amount:
---

# What

Would love to prolong my part time Monero coding for another 3 months.  

There are some specific tasks i would like to work on first.

* CLI: Auto-updater. Updates downloading and verification functionality (will verify gitian signatures additionally to the GUI auto-updater features https://www.reddit.com/r/Monero/comments/jfanxi/gui_v01711_oxygen_orion_is_now_available_via_the/)
* GUI: Docker Windows static build: Qt 5.15 support
* GUI: Reproducible Windows builds (docker)
* GUI: Send to multiple addresses (related discussion https://github.com/monero-project/monero-gui/issues/740)

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
* https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/157

During the recent 30h/week proposal i implemented:
* Docker Monero GUI Windows static build.  
  A user can now run just a couple of commands to build Monero GUI Windows static binary:  
  https://github.com/monero-project/monero-gui/#building-windows-static-binaries-with-docker-any-os  
* Finished CMake integration: using CMake for all Monero GUI build targets now.  
* Docker Monero GUI Linux static builds - implemented Qt 5.15 support.  
* Docker Monero GUI Android build - updated to Qt 5.15, CMake support.  
  https://github.com/monero-project/monero-gui/#building-android-apk-with-docker-any-os-experimental  
* Reproducible Monero GUI Linux builds *Work In Progress*

in order to not clutter the proposal i'm not listing all the related pull requests. I strongly encourage you to visit the following Github links to see the amount of work done by me, its quality and importance for the Monero Project.

Please check the following links to inspect my Monero-related activity:  
- Monero Core - https://github.com/monero-project/monero/pulls?q=is%3Apr+author%3Axiphon
- Monero GUI - https://github.com/monero-project/monero-gui/pulls?q=is%3Apr+author%3Axiphon

# Proposal

Looking forward to coding and accomplishing mentioned and ongoing tasks and issues. Implementing new code/functionality that will be needed. Investigating bug reports and submitting bug fixes, fixing build and compilations errors/warnings/etc. Would like to inspect and complete/fix/address issues and feature requests that are reasonably desired and/or worth to spend time on. Improving GUI, fixing UI/UX issues, implementing design changes.

Dedicate 30 hours per week to Monero Project, at 55 USD/hour rate for a total of 164 XMR. XMR/USD rate is based on the 14-day moving average exponential on Kraken from 8 Nov 2020, which is approximately 120.95 XMR/USD.
