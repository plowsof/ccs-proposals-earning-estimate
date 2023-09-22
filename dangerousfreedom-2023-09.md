---
layout: fr
title: dangerousfreedom - wallet work
author: DangerousFreedom
date: September 17, 2023
amount: 64 
milestones:
  - name: deliver of proposed demonstrator and wallet functions
    funds: 64 
    done:
    status: unfinished
payouts:
  - date:
    amount:
---

## What and Why ?

The end goal is twofold:

1) Get started with a basic variant to handle transactions both in legacy and seraphis: since a blockchain is made of blocks and blocks are made of transactions, we probably need a class to handle node queries smoothly between the classes `transaction` and `SpTxSquashedV1`. Hopefully this will generate discussions and start paving the way for future works about reading/writing data from/in the blockchain (1/4 of total time).

2) Make a basic but broad demonstrator of the seraphis_wallet by: opening a wallet, make mock transactions, make transaction proofs, show enotes and balance, close wallet. A lot of work has been done in this direction but they are not yet fully organized. So the goal is to have this basic but organized demonstrator capable of doing that (3/4 of total time).

I would work on the following tasks:
- Create the `TransactionVariant = tools::variant<transaction, SpTxSquashedV1>` to handle similar methods of these classes.
- Create unit_tests with legacy and seraphis transactions to test these methods.
- Create basic functions for wallet initialization, program flow and terminal handling.
- Create the basic components of a seraphis_wallet (basically the wallet needs to load/save the `KeyContainer`, `EnoteStore` and `TransactionHistory` components). 
- Create basic function to fill `EnoteStore`.
- Use mock transactions like `construct_tx_for_mock_ledger_v1` to create txs.
- Add entries to `TransactionHistory` when a transaction creation is attempted.
- Create terminal functions to show enotes and provide knowledge proofs.
- Close/save wallet and make sure it loads everything when reopened.

All the efforts will be documented and made public on the seraphis_wallet group. Unit_tests will be provided whenever possible.


## Who?

- I did [this](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/298), [this](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/344) and [this](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/377) previous works.

I propose to work for 40 USD per hour, 20h per week, for 12 weeks (or until I finish all the tasks), which makes 64 XMR considering 150 USD/XMR.
