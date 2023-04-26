---
layout: wip
title: dangerousfreedom - wallet development 2 
author: DangerousFreedom
date: February 26, 2022
amount: 31 
milestones:
  - name: deliver of proposed wallet functions
    funds: 31
    done:
    status: unfinished
payouts:
  - date:
    amount:
---

## What and Why ?

Transaction history component with knowledge proofs

The idea is to collect transaction records (both for legacy and seraphis) authored by the wallet in order to provide the user the information he wants to look back. This component should import or update authored txs by looking at their enote's key-image and spent status. 

The plan is to go in the direction of building a component to handle transactions by integrating the following non-comprehensive list of equivalent wallet2 methods into a component: get_transfers, get_payments, get_payments_out, get_unconfirmed_payments_out, get_unconfirmed_payments, export_outputs, import_outputs, import_outputs_from_str, export_payments, import_payments, import_payments_out, get_num_transfer_details, transfer_details, get_tx_proof, check_tx_proof, get_spend_proof, check_spend_proof, get_reserve_proof, check_reserve_proof.

An initial discussion about this topic can be found [here](https://github.com/seraphis-migration/wallet3/issues/49).

Since some of these functions are not purely wallet functions as they depend on a daemon, I expect to help and get help to properly interface them with a proto daemon.

All the efforts will be documented and unit_tests will be provided whenever possible.

## Who?

- I did [this](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/298) and [this](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/344) previous works and I believe I'm sharpening my skills and understanding of Jamtis and Seraphis to accomplish this work as described. 

I propose to work for 30 USD per hour, 20h per week, for 8 weeks (2 months). Which makes 31 XMR considering 155 USD/XMR.
