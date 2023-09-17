---
layout: fr
title: dangerousfreedom - wallet work
author: DangerousFreedom
date: September 17, 2023
amount: 96 
milestones:
  - name: deliver of proposed demonstrator and wallet functions
    funds: 96 
    done:
    status: unfinished
payouts:
  - date:
    amount:
---

## What and Why ?

The end goal of this proposal is to be able to make a basic but broad demonstrator of the seraphis_wallet by opening a wallet, use @jberman scanner to load legacy enotes, make transactions, make transaction proofs, show enotes and balance, close wallet. A lot of work has been done in this direction but they are not yet fully organized. So the goal is to have this basic but organized demonstrator capable of doing that.

In order to do so, I would work on the following tasks:
- Create basic functions for wallet initialization, program flow and terminal handling.
- Create the basic components of a seraphis_wallet (basically the wallet needs to load/save the KeyContainer, EnoteStore and TransactionHistory components). 
- Create basic function to fill `EnoteStore` with jberman's scanner.
- Create functions similar to `create_transaction_2`, `create_transactions_from` on wallet2 and `construct_tx_for_mock_ledger_v1` in seraphis_mock to send a tx.
- Add entries to `TransactionHistory` when a transaction creation is attempted.
- Create terminal functions to show enotes and provide knowledge proofs.
- Use/review/integrate @ghostway's work and @shalit's work on the key_container and on the EnoteStore serialization 

All the efforts will be documented and made public on the seraphis_wallet group. Unit_tests will be provided whenever possible.


## Who?

- I did [this](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/298), [this](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/344) and [this](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/377) previous works.

I propose to work for 40 USD per hour, 30h per week, for 12 weeks (or until finish all the tasks), which makes 96 XMR considering 150 USD/XMR.
