---
layout: cp
title: dangerousfreedom - more Seraphis development 
author: DangerousFreedom
date: September 20, 2022
amount: 120
milestones:
  - name: Audit framework Seraphis.
    funds: 20
    done: 9 February 2023
    status: finished
  - name: PoC CLI Wallet.
    funds: 100
    done: 9 February 2023
    status: finished
payouts:
  - date: 23 February 2023
    amount: 120
---

## TLDR
Hello, I would like your help to develop more features for Seraphis like the audit framework and a simple CLI wallet.

## What and Why ?
I will try to address the following issues:

1) Create the necessary functions and explanation for the audit framework in Seraphis, i.e., proofs of ownership, unspentness, tx in, tx out (InProof,UnspentProof,SpendProof, OutProof) and update the [legacy](https://github.com/monero-project/monero/issues/7353) protocol if necessary .

2) Help developing a wallet for Seraphis. My goal is to be able to create the necessary functions to open a wallet, perform a CLI 'transfer address amount' that would create a transaction in the Seraphis/Jamtis standards, close the wallet, re-open a new wallet where the transferred funds are, 'scan the blockchain' and transfer the funds back to the original wallet. I will closely work with koe, rbrunner and jberman to better elaborate the tasks and get feedbacks or follow-ups whenever possible. Initially, the simplest wallet would open/save/close a file, keep track of the transactions inputs and outputs, perform a transfer in the Seraphis standards and prepare everything for the serialization and storage in the blockchain. These are the minimum features I will implement. More about it [here](https://github.com/seraphis-migration/wallet3/issues/10).


## Who
- I created the website [www.moneroinflation.com](www.moneroinflation.com) where you can find some information to improve your odds of winning a debate about the inflation issue in Monero.
- I have spotted a [fungibility issue](https://github.com/monero-project/monero/issues/8351) (Monero allows the storage of non-canonical points which harms the fungibility of transactions). 
- I have spotted a [malleability issue](https://github.com/monero-project/monero/issues/8438) (Monero has wrong signatures - signatures that don't match the data stored in the blockchain according to the canonical standards, which came from a wrong operation of a function when certain conditions are not met). 
- AFAIK I was the first to make an implementation of the core functions of Monero in another language and (try to) scan the whole blockchain with them.

I propose to work for 40 EUR per hour, 25h per week, for 18 weeks. Which makes 120 XMR considering 150 EUR/XMR.

If everything goes well, I believe we could have a basic PoC CLI wallet by the end of January/23 and enough achievements to move to testnet. 
