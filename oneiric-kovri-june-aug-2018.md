---
layout: cp
title: "oneiric: June-August part-time Kovri junior developer"
author: oneiric
date: June 7, 2018
amount: 21
milestones:
  - name: Milestone 1 - 1st 16h
    funds: 13.33% (3.6 XMR)
    done:
    status: finished
  - name: Milestone 2 - 2nd 16h
    funds: 13.33% (3.6 XMR)
    done:
    status: finished
  - name: Milestone 3 - 3rd 16h
    funds: 13.33% (3.6 XMR)
    done:
    status: finished
  - name: Milestone 4 - 4th 16h (higher rate)
    funds: 30% (8.1 XMR)
    done:
    status: finished
  - name: Milestone 5 - 5th 16h (higher rate)
    funds: 30% (8.1 XMR)
    done:
    status: finished
payouts:
  - date: September 6, 2018
    amount: 10.8 XMR
  - date: December 7, 2018
    amount: 16.2 XMR
---
Who
Hello Monero community, I'm oneiric, and I've been working on Kovri since December 2017.

This is my first FFS proposal to the community, and I intend to make many more (if the community will have me). I'm in it for the long haul. Privacy is incredibly important to me, and I want to do everything I can to help Kovri and Monero. These projects are some of the strongest tools the common person will have in achieving freedom and financial privacy.

What
I am submitting this proposal to continue work with anonimal on bringing Kovri to release and integration, and to be funded as a part-time junior developer.

Contributions:

Over the past few months, I have collaborated with anonimal, rehrar, and others to make contributions to Kovri.

Identity: use Boost DateTime when creating router keys: replace sprintf and C date functions with Boost DateTime when creating router keys
Build: fix mingw warnings: resolve Windows compiler warnings
Configuration::ListParameter unit-tests: unit-tests for class used to parse Kovri configuration
SSU: support IP address size for peer test packets: get and set IP address size for SSU peertest packets
Build: fix Doxygen build: small CMake fix for building Doxygen documentation
AddressBook: Container for host-address entry: first attempt at a container class for an AddressBook hostname-address pair
AddressBook + HTTP Proxy: store only unique subscription addresses
AddressBook: add address to file I/O refactor + add exception handling: change how addresses are added to storage, and throw on filesystem errors
HTTPMessage: refactor jump service parser + add test-cases: change how the HTTP proxy handle jump service requests, and add unit-tests. One of my first contributions, and required a large amount of collaboration with anonimal (many thanks).
IdentityEx: lowerbounds check on buffer creation: bounds check on the supplied buffer, ensure it is large enough to hold a serialized IdentityEx class
Standing on the shoulders of giants:

Assistant for Kovri Project Management
Create End-User Kovri documentation
rehrar's 2018 Q1 Kovri proposal
anonimal's Kovri Full Time Development funding thread
Proposal for Kovri Dev
MILESTONES & PROPOSAL
Milestones
In collaboration with anonimal:

Create an enhanced form of the Kovri testnet
Integrate Kovri testnet with live tests
Write tests for 100% coverage on new and existing stable code
Remaining 0.1.0-alpha release milestones
Other tasks anonimal assigns
Compensation & Time Estimates
Amount: 27 XMR (0.225 XMR/hour * 40 hours + 0.45 XMR/hour * 40 hours)

The amount I am requesting is based on similar FFS proposals, and average base-pay for a junior developer.

In order for the community to get to know my work, I am willing to give a discounted (50%) rate for the first 40 hours (1 month @ 10 hours/week) of paid work.

The goal is to complete the milestones by DefCon 26, whatever it takes.

Any time more than 10 hours/week, I will volunteer to achieve the stated goals.

To get an idea of my dedication to accomplishing these goals, average time spent on Kovri in April-May was ~50-60 hours/week.

Let's Discuss
I am new to the project and community, and welcome feedback on this proposal.