---
layout: cp
title: "New Localization platform: Weblate"
author: ErCiccione
date: 22 August 2019
amount: 11
milestones:
  - name: Replace Pootle with Weblate
    funds: 7.5
    done: 13 October 2019
    status: finished
  - name: Update documentation, import terminology guides and translation memories
    funds: 3.2
    done: 13 October 2019
    status: finished
payouts:
  - date: 14 October 2019
    amount: 11
---

Hello everybody, as preannounced in past community meetings, in the [dedicated meeting of the localization workgroup](https://web.getmonero.org/2019/05/04/logs-for-the-localization-workgroup-meeting-held-on-2019-05-03.html) and in [this reddit post](https://old.reddit.com/r/Monero/comments/c06vuw/my_last_proposal_as_coordinator_of_the/), here is my CCS proposal for the integration of Weblate as new localization platform. I'll keep it as schematic and short as possible.

The first milestone is already ongoing and almost complete. This request of payment doesn't include the previous testing of weblate, which was included in my last CCS proposal, but only the actual installation/configuration on translate.getmonero.org (Where is already possible to see a read-only preview of the platform).

### What
This proposal is divided in 2 milestones:

1. *Install and configure Weblate*  
Which means:

- Complete, operative and configured Weblate instance
- Import unpushed contributions from Pootle
- Set up logging and backups
- Set up a review and submission process for translations

As said, this work has been ongoing for some time. To have a less problematic implementation than Pootle I asked moneromooo to add the possibility to activate and deactivate languages in the CLI. See the [related issue](https://github.com/monero-project/monero/issues/5753). The translations still on pootle [have been PRd](https://github.com/monero-project/monero/pull/5788) and they just got merged.

While configuring weblate I found some issues with their documentation, so i thought would have been nice to give a small contribution back to this open source project. I opened two issues suggesting changes: ([1](https://github.com/WeblateOrg/weblate/issues/2838), [2](https://github.com/WeblateOrg/weblate/issues/2854)).

Note: In this state of things Monerujo will not be added to Weblate. Please see [this issue](https://github.com/m2049r/xmrwallet/issues/521) for the reasons.

Estimated amount of time needed for this milestone: **18 hours**

2. *Update documentation, import terminology guides and translation memories*  
The Monero Localization Workgroup has terminology guides, translation memories and documentation created by members of the workgroup. Translation memories are easy to import/export, but the same cannot be said for the terminology guides. I will need to manually convert them to a format acceptable to Weblate and then import them on the platform.

Also, at the moment we have a guide for Pootle that I created when we started using it. I will replace this guide with one about Weblate, specific for Monero translators. All other documentation in [monero-translations](https://github.com/monero-ecosystem/monero-translations) and all references to Pootle in our ecosystem will be updated.

After weblate will be operative, I will maintain it as volunteer (no compensation)

I'm tracking most of the time spent working on Weblate with a time tracker, logs will be provided to the core team if requested.

Estimated amount of time needed for this milestone: **8 hours**

### Compensation
I always offered my work at a very low rate, $20/h, which translates in about €18/h (i'm based in europe). I think it's time to ask a "less political" price, especially since market volatility had a very heavy inpact on my income during the time I was community funded (about 1 1/2 year) and as some of you know, I fully lived on only Monero. For this proposal I'm asking **€30/h** (~$33/h), which will result in 7.5 XMR for the first milestone and 3.2 XMR for the second (considering the average of 1 XMR = €72) for a (rounded) total of *11 XMR*.
