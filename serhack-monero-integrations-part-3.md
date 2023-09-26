---
layout: wip
title: Monero Payment gateways Gateways part 3
author: SerHack
date: March 2020
amount: 11
milestones:
  - name: Monero PHP library maintenance
    funds: 4
    done:
    status: unfinished
  - name: Monero Woocommerce payment gateway maintenance
    funds: 7
    done:
    status: unfinished
  - name: Others ideas
    funds:
    done:
    status: unfinished
payouts:
  - date:
    amount:
  - date:
    amount:
---

### What?

I am [SerHack](https://serhack.me), the author of [Mastering Monero](https://masteringmonero.com) and security engineer; I am one of the maintainers for [Monero integrations](https://monerointegrations.com) project. The project aims to provide a set of payment gateways and libraries (coded mainly in PHP, at the time of writing) for merchants and developers. As you might find on Github, the payment gateways are not in any third party companies, then no data is sent to any other website beside yours.

With this request, I would like to keep the two main repositories (PHP library and Woocommerce libraries) updated. I have set two main milestones.

#### Milestone 1: PHP library maintenance

I've listed all the possible issues I can fix or improve. Note that I would like to keep this library without any external dependencies (e.g. guzzle from composer) for security reasons. Honestly, I have some difficulties at trusting composer, but I'd like to discuss about this.

* [Enable SSL validation by default for non loopback connections](https://github.com/monero-integrations/monerophp/issues/11)
* [Daemon RPC Wrapper: "Other Methods"](https://github.com/monero-integrations/monerophp/issues/34)
* [Make stable version on packagist](https://github.com/monero-integrations/monerophp/issues/82)
* [Use code stype](https://github.com/monero-integrations/monerophp/issues/84)
* [Remove dead code](https://github.com/monero-integrations/monerophp/issues/85)
* [Library returns NULL when it receives a blank response or an error](https://github.com/monero-integrations/monerophp/issues/92)
* [PHP 7.2 - json_encode() breaks transfer submission of certain amounts](https://github.com/monero-integrations/monerophp/issues/100)
* [offline mnemonic support planned?](https://github.com/monero-integrations/monerophp/issues/103)
* [Make sure we support the latest PHP versions and do not support PHP < 7.2](https://github.com/monero-integrations/monerophp/issues/109)
* General improvement

If you have any additional idea, feature request, or issue, please let me know!

#### Milestone 2: Monero Woocommerce payment gateway maintenance

Monero Woocommerce Payment Gateway had only 40 installations from [Wordpress.org](https://wordpress.org/plugins/monero-woocommerce-gateway/#installation). This is partially my fault since the page was created to attract more merchants. As per Milestone 1, I have listed all the issues I would like to fix.

* [Switch to subaddresses](https://github.com/monero-integrations/monerowp/issues/56) – This has already been implemented, but in a cryptic way. It needs some review.
* [List of currencies vanishes](https://github.com/monero-integrations/monerowp/issues/67)
* [Improve the upcoming release 3.0](https://github.com/monero-integrations/monerowp/issues/74)
* [Decrypting payment id in Monero_Cryptonote results in infinite loop](https://github.com/monero-integrations/monerowp/issues/81)
* [Feature request: checkout shutdown on timeout](https://github.com/monero-integrations/monerowp/issues/83)
* [javascript disabled fall-back support](https://github.com/monero-integrations/monerowp/issues/84)
* [One payment will cause all pending orders with the same value to be marked as paid.](https://github.com/monero-integrations/monerowp/issues/85)

Any other idea is really appreciated!

### Why?

I would like to expand more this section since it is a subject close to my heart. Monero was created to be the most private cryptocurrency ever created; when I joined the Monero community, I had some difficulties at finding payment gateways that were private. Thus I've started this project.

### Costs

If milestones are not modified, I'll ask 11 XMR (~700 euros) - fixed price.  

### Proposal transfer

This proposal will be transferred to recanman who will enjoy an exclusivity period of 5 months to show reasonable progress in completing this proposal. They will receive payments for completed milestones directly.

SerHack: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/402#note_22039

>To consider the CCS completed, all the issues mentioned in the CCS must be completed: recanman will need to push changes to monero-integrations repositories and after reviewing the PRs, I'll close the issues.
