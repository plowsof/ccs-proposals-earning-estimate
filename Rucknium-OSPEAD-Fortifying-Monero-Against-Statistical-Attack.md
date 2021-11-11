---
layout: fr
title: OSPEAD - Fortifying Monero Against Statistical Attack
author: Rucknium
date: September 25, 2021
amount: 171
milestones:
  - name: Milestone 1 - Deliver fully specified estimation plan to scientific review panel
    funds: 67
    done:
    status: unfinished
  - name: Milestone 2 - Deliver initial probability density function to scientific review panel
    funds: 74
    done:
    status: unfinished
  - name: Milestone 3 - Deliver final version of probability density function to Monero developers
    funds: 30
    done:
    status: unfinished
payouts:
  - date:
    amount:
  - date:
    amount:
  - date:
    amount:
---

# Abstract

The current decoy selection algorithm, developed by a group of non-statisticians in 2018, statistically leaks metadata about transactions on the Monero blockchain. This metadata, which comes in the form of the age of the outputs that are used as inputs for transactions, could be used by an adversary to probabilistically identify the "real spend" in Monero transactions and thus make Monero transactions somewhat traceable.

The current decoy selection algorithm (DSA) has been acknowledged as a weak point in Monero's privacy model, but to date no plan has emerged to improve it. Over the last three months I have developed an outline of a plan to overhaul the algorithm through a technique I have termed OSPEAD: Optimal Static Parametric Estimation of Arbitrary Distributions. The overhaul should substantially improve user privacy by reducing Monero's statistical attack surface. Given that Monero will likely come under increasingly sophisticated attack in the near future, carrying out this plan --- or one like it --- is critical for Monero user privacy and Monero's future as a whole.

![Statistical Monero Logo](https://github.com/Rucknium/misc-research/raw/main/Statistical-Monero-Logo/Statistical-Monero-Logo.gif)

# The status quo

The current decoy selection algorithm (DSA) is based on work in [Moser et al. (2018) "An Empirical Analysis of Traceability in the Monero Blockchain"](https://www.sciendo.com/article/10.1515/popets-2018-0025). They suggested a gamma distribution with [some fitted shape and scale parameters](https://github.com/monero-project/monero/blob/de3456e1275836725291ba71036b7ef0e2cda91f/src/wallet/wallet2.cpp#L137-L138) that ideally would have closely matched the true underlying real spend age distribution, thus concealing the real spends and substantially improving user privacy.

However, according to my research into the backgrounds of the 11 authors of the paper, none of them are statisticians. Their suggestion was a decent first draft, but in my view it never should have been implemented in production code due to several flaws. (To be fair and clear, it may have represented the best available DSA at the time, and I cannot find any fault with Monero researchers and developers for choosing to implement it since it represented a huge improvement over the status quo ante.) Another applied statistician within the Monero community has now reviewed the suggestion in Moser et al. (2018) and agreed with me that it has substantial shortcomings.

As far as I have been able to tell, no qualified statistician has reviewed Monero's privacy model, despite the fact that it clearly relies upon resistance to statistical attack to prevent traceability of transactions. Or, to word it more alarmingly, no qualified statistician *whose goal is to protect the privacy of Monero users* has reviewed Monero's privacy model. As an empirical microeconomist, I consider myself roughly equivalent to an applied statistician within this context, particularly since transactions are a key object of study within my discipline --- and therefore I may have special subject matter insight into the issue.

Much [academic](https://doi.org/10.1145/3448016.3452825) ink [has](https://www.mdpi.com/2624-800X/1/1/9) already [been](https://eprint.iacr.org/2020/593) spilled [regarding](https://www.sciendo.com/article/10.1515/popets-2018-0025) the [importance](https://www.sciendo.com/article/10.2478/popets-2021-0047) of [having](https://doi.org/10.1007/978-3-030-14234-6_5) a [good](https://link.springer.com/chapter/10.1007%2F978-3-319-66399-9_9) DSA. However, the clearest statement on the issue may be from @moneromooo-monero, who is responsible for [a greater number of commits to the Monero codebase](https://github.com/monero-project/monero/graphs/contributors) than any other developer. Recently [he stated](https://libera.monerologs.net/monero-dev/20210925#c31927):

> **\[Fixing the decoy selection algorithm\] is important. It's the weakest part of monero.**

@selsta, another key Monero developer, [has stated](https://www.reddit.com/r/Monero/comments/pz9gbm/comment/hezuw2p/):

>It has always been known that statistical attacks are possible on ring signatures in Monero, see for example the Moser et al. (2018) paper....I personally welcome research into the decoy selection algorithm, it is known to be one of the weakest spots in monero that isn't yet well researched.

# Proposed fix

On September 16, I submitted a 28-page encrypted document to Monero's Vulnerability Response Process (VRP). It contained a practical statistical attack on user privacy as well as an outline of a plan to overhaul the DSA to (1) reduce the potency of the attack in the medium term through a novel technique I have named Optimal Static Parametric Estimation of Arbitrary Distributions (OSPEAD); and to (2) eventually render the attack completely inert through a nonparametric and possibly dynamic approach. Dr. Mitchell P. Krawiec-Thayer (a.k.a. [isthmus](https://github.com/mitchellpkt/)), longtime Monero Research Lab researcher, has called my work "a fundamental breakthrough in analyzing Monero-style ledgers."

A key difficulty with writing this CCS proposal is that the attack and the plan to overhaul the DSA have some indirect links. Let me be clear about risks and transparency. The actual change to the DSA, in terms of the probability distribution that decoys are drawn from, will be open source and plainly visible in the Monero code in all circumstances. There seems to be a consensus forming that full disclosure of my attack should occur eventually, perhaps after the OSPEAD research plan is carried out but before it is implemented in a release of a new version of the Monero reference wallet. It does not make much sense to release the attack before an adequate defense has been developed. My sense is that a final decision on disclosure will be made once the problem is better understood as my research progresses.

According to my intuition, I expect that future transactions that use the overhauled DSA determined by OSPEAD will be 70-90% less vulnerable to statistical attack than transactions that use the current DSA. In addition, a "perfectly" implemented nonparametric approach, which will take much more time to develop, would completely eliminate this particular statistical attack vulnerability.

Increasing the ring size is part of Monero's long-term development roadmap. However, I have produced evidence that the statistical vulnerability would still remain with larger ring sizes. Raising the ring size from 11 to, say, 16 would barely dent the potency of my attack. Raising the ring size to 256 would mitigate the attack to a substantial degree, but user privacy might still be at some risk. In other words, we cannot get ourselves out of this problem by simply raising the ring size.

To use a metaphor, the decoys are like camouflage. In order for the camouflage to protect user privacy, merely having lots camouflage is not enough. We must also ensure that the camouflage is placed in the right locations. My overhaul to the DSA is intended to place the camouflage where it is needed.

# Timeline

By now it is well-established that Monero adversaries are pouring resources into efforts to attack user privacy. The most recent evidence is a [revelation](https://www.coindesk.com/business/2021/09/21/leaked-slides-show-how-chainalysis-flags-crypto-suspects-for-cops/) that Chainalysis is privately claiming to produce useful leads to law enforcement based on Monero transactions. A [healthy](https://www.reddit.com/r/btc/comments/psos06/comment/hdshs84) [skepticism](https://www.reddit.com/r/btc/comments/psos06/comment/hds2zkj) of these claims is, of course, warranted. However, given that I have now proven that it is possible to develop a practical statistical attack on Monero user privacy, *the fuse is lit*, so to speak. Monero adversaries may be able to develop a statistical attack -- or they may have already done so. An overhaul to the DSA should be developed and deployed as quickly as possible.

The upcoming hard fork, which does not yet have a fixed date, will include an increase in the ring size. The discontinuity that the hard fork creates can be leveraged to better understand how ring signatures work in pratcice on the Monero blockchain. Therefore, some of the research work will occur after the hard fork.

I will work with @j-berman and @mj to develop and implement OSPEAD, as they outlined in [their own](https://ccs.getmonero.org/proposals/j-berman-3-months-full-time.html) [CSS proposals](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/266). In order to ensure a degree of peer review of OSPEAD, I am in the process of establishing a scientific review panel of key Monero community members. In the event that the review panel cannot be established for some reason, I will submit Milestone 1 (the fully specified estimation plan) to @luigi1111 to simply verify that it exists, and then combine Milestones 2 and 3.

I estimate that development and implementation of OSPEAD will take 11.5 weeks of full time equivalent (FTE) labor, i.e. 460 hours. I expect the milestone breakdown, in terms of FTE weeks, will look like this:

### Milestone 1: Deliver fully specified estimation plan to the scientific review panel (4.5 weeks FTE)

My submission to the Monero Vulnerability Response Process contains an outline of the plan to implement OSPEAD, but I left it vague in several places due to time constraints. This milestone will involve a full consideration of all potential obstacles and how to surmount them. I will also spend 1.5 FTE weeks researching alternatives to OSPEAD. The review panel will have an opportunity to suggest alterations in the plan at this point in the process.

### Milestone 2: Deliver initial probability density function to the scientific review panel (5 weeks FTE)

This milestone involves implementation of the plan developed for Milestone 1. I will write a full report and submit it to the scientific review panel.

### Milestone 3: Deliver final version of probability density function to Monero developers (2 weeks FTE)

After the scientific review panel examines the report and suggests improvements, a final version of the probability density function for the DSA will be produced. There could be several rounds of review and re-submission depending on circumstances. This finalized probability density function will be delivered to Monero developers for consideration to be included in a subsequent release of the Monero reference wallet. Note that implementation of a new DSA does not require a hard fork of the network (at least for the time being) since Monero's blockchain consensus rules do not require any particular probability density function to be used in the construction of transactions.

The 11.5 FTE weeks of work will not be completely contiguous, but I expect Milestone 3 to be reached by February or March 2022. The timeline is somewhat dependent upon the hard fork schedule. I will set the final expiration date for the proposal, for the purposes of the CCS proposal process, to August 2022.

# Budget

My rate for this work is the XMR equivalent of 100USD/hour, which exactly matches the labor rate of the [Cypher Stack proposal to research Triptych multisig](https://ccs.getmonero.org/proposals/cypherstack-sarang-triptych-research.html). Implementing Triptych in Monero would allow ring sizes of over 100 inputs without a huge increase in transaction sizes.

As I stated above, there is evidence that merely increasing the ring size does not eliminate the statistical vulnerability. In my view, an overhaul to the DSA and an increase in the ring size are of similar importance to protecting Monero user privacy. Therefore, I believe it is appropriate to match the labor rate of the Triptych multisig research effort.

100USD/hour is also consistent with compensation for statistical consulting in the competitive labor market. According to the [American Statistical Association 2020 Work and Salary Survey,](https://www.amstat.org/asa/files/pdfs/YCR-2020WorkandSalarySurvey.pdf) statisticians at the median earn 186,750USD/year and 175,000USD/year in consulting or private industry roles, respectively, which translates to 97USD/hour and 91USD/hour.

Note that if this CCS proposal is not funded, I will have to halt virtually all of my Monero work due to incurring high opportunity costs. I will need to shift my attention back to BCH and accelerate my work on analyzing the CashFusion CoinJoin protocol, since the BCH community has already demonstrated willingness to fund that work.

The median daily closing exchange rate for USD/XMR over the last 30 days was 269USD/XMR. Therefore, the total cost of this CCS proposal is 171 XMR, with milestones 1, 2, and 3 corresponding to 67 XMR, 74 XMR, and 30 XMR, respectively.

# About me

I am an empirical microeconomist trained in the neoclassical tradition. That means that I primarily use real-world data, rather than mathematical theory, to investigate economic questions at the level of consumers, businesses, and industries. I have chosen to remain pseudonymous, and therefore my training and extant body of work are neither identified nor verifiable. However, I do have some publicly-available work associated with this Rucknium identity, which was created in June 2021:

1.  Statistical contributions to [the analysis of the mid-2021 Monero transaction volume anomaly](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/), particularly on the subject of [ring member age](https://github.com/Rucknium/xmr_volume_anomaly/blob/main/Noise-reduced-measure-of-youngest-ring-member.R).
2.  Development of [a sketch of a plan to recruit technical talent for the Monero Project](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/).
3.  4,000 lines of code contributed to [TownforgeR](https://github.com/Rucknium/TownforgeR), an alternative user interface for [Townforge](https://townforge.net/), which is a blockchain-based game primarily coded by @moneromooo-monero that is a heavily modified fork of Monero. I introduced wallet operations, a web-based custodial wallet option, an order book visualizer, a map of buildings, an inter-building influence map, and a land plot chooser based on a modified grid search optimizer. [Live version](https://townforger.net/).
4.  [An automated market maker bot for Townforge's commodity order books](https://github.com/Rucknium/TownforgeMMbot) that accepts investments of commodities and currency and issues in-game shares that will be used to pay dividends to player-investors.
5.  [A Townforge invitation faucet webapp](https://github.com/Rucknium/townforgefaucet) with a Beowulf-based CAPTCHA. The webapp also accepts contributions of invitation codes from any Townforge players, validating all submissions against a Townforge node running on a VPS. [Live version](https://townforgefaucet.net).
6.  Initiation of [the CashFusion Red Team](https://flipstarter.redteam.cash/) research project, including the [fusionstats.redteam.cash](http://fusionstats.redteam.cash/) web app.
7.  Article: [An Empirical Analysis of Satoshi Pyramid](https://read.cash/@Rucknium/scheme-or-scam-an-empirical-analysis-of-satoshi-pyramid-d3c79192).
8.  [Preliminary analysis of Monero cryptography benchmark data](https://github.com/Rucknium/misc-research/tree/main/Monero-Cryptography-Benchmarks).

# Disclosures

I am involved in a few cryptocurrency initiatives that involve or may involve monetary compensation. I believe that none of them give rise to any conflicts of interest with the objectives of this CCS proposal:

**CashFusion Red Team**. I am conducting an analysis of the strength of the privacy guarantees of CashFusion, an implementation of the CoinJoin protocol on the BCH blockchain. I have been paid 18 BCH through a [Flipstarter crowdfunding campaign](https://flipstarter.redteam.cash/) to carry out the first phase of this research project.

**Work on the Townforge ecosystem**. I receive no direct compensation for any of this work, since Townforge is a proof-of-work blockchain with no ICO nor pre-mine. However, via CPU mining and playing the game well, my involvement in Townforge may lead to some level of monetary earnings, assuming the in-game currency attains some nonzero market exchange rate with another cryptocurrency like XMR.
