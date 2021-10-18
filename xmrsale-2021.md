---
layout: wip
title: xmrSale Payment Processor Development
author: xmrsale
date: 10 August, 2021
amount: 85
milestones:
  - name: Functioning Monero payment processor with docker image install and woocommerce store
    funds: 25
    done: 2 October 2021
    status: finished
  - name: Text tutorial docs and website with woocommerce demo store
    funds: 10
    done:
    status: unfinished
  - name: Zeronode mode viewkeys
    funds: 20
    done:
    status: unfinished
  - name: RPC via tor hidden service
    funds: 10
    done:
    status: unfinished
  - name: Another webstore plugin
    funds: 20
    done:
    status: unfinished
payouts:
  - date: 18 October 2021
    amount: 25
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
[xmrSale](https://github.com/xmrsale/xmrSale) is a lightweight Monero payment processor that connects to your own Monero node, striving to be modular and lightweight. xmrSale has an accessible API written in python that talks to your own Monero node, uses RPC to generate new addresses, and monitors payment success with your own copy of the Monero blockchain.

xmrSale will make it easy to embed Monero donation buttons into your website with an HTML iframe tag, accepting donations from your supporters and community. Through an xmrSale Woocommerce plugin, we are going to allow anyone to self-host their own Monero accepting online store. Monero has been thriving in the "host your own tools" niche of the internet, and self-custody payments are crucial in this mission. Existing Monero eccommerce processors are custodial, sacrificing the privacy of you and your customers.

You can explore a demo of xmrSale here: [https://try.xmrsale.org](https://try.xmrsale.org)

** Please do not donate using the demo, please donate via the CCS **

# Who
As an anonymous developer, to prove my intention and dedication I have already put significant work into establishing the project to a working state (experimental!), and am somewhat close to achieving the first milestone.

# Milestones
With your support, I will continually work to ensure that xmrSale remains up-to-date with the SatSale project (from which we are based on), and also build above and beyond Monero specific features as listed below.

**Functioning Monero payment processor with node connection and docker image** (September)
* Get the project into a functioning state, where anyone running a Monero node could clone the repository, edit the config, and run xmrSale themself.
* Docker image installation option
* Instant payments
* Functioning xmrSale woocommerce plugin

**Text tutorial docs and website** (September)
* Write coherent and easy to follow installation instructions, aligned to various node configurations.
* Multiple example configs. Tor & HTTPS configurations. Nginx
* A functioning wordpress Monero store, with a demo store hosted 24/7
* Text tutorial
* Basic HTML and CSS website

**Zeronode mode viewkeys** (December)
* A mode that does not require a node to run, uses block explorers and viewkeys to check payments.

**RPC via tor hidden service** (December)
* Rather than use SSH to bridge to node, add option for Tor hidden services.

**Build a plugin for another ecommerce site** (Q1)
* Community can decide! Perhaps shopify? Let us know!

# Further development and research (not current milestones)
* Improved user interface
* More consistent price feeds (preload price too)
* Single click install container that deploys to a VPS with a node
* Any developments in the monero payment protocol. Including any layer 2.
* Security analysis
* Stress test under concurrent payments
* Improved user experience with payment timeouts
* Video installation tutorials

I will take community desire very seriously to guide this project, so if there is something you want but don't see here then please let us know! This proposal will expire 1 March, 2022.

cheers,

xmrsale dev

xmrsale@protonmail.com
