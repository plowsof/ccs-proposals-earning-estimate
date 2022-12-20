---
layout: wip
title: SolOptXMR - Solar Optimal mining of XMR
author: mj
date: Mar 26, 2022
amount: 110.55 XMR
milestones:
  - name: 1 Initial setup
    funds: 20.10 XMR
    done: 29 May 2022
    status: finished
  - name: 2 Profitability calculator
    funds: 16.75 XMR
    done:
    status: unfinished
  - name: 3.1 Measurements mj
    funds: 20.10 XMR
    done:
    status: unfinished
  - name: 3.2 Measurements Endor
    funds: 16.75 XMR
    done:
    status: unfinished
  - name: 4.1 Automation mj
    funds: 20.10 XMR
    done:
    status: unfinished
  - name: 4.2 Automation Endor
    funds: 16.75 XMR
    done:
    status: unfinished
payouts:
  - date: 2 July 2022
    amount: 20.1
  - date:
    amount:
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
The goal is to create open-source software that aids people mining Monero with excess solar power in the most profitable way. It will accommodate for issues such as:

- Time of day
- Weather fluctuations
- Avoiding depleting batteries below a threshold, that would damage them
- Avoiding overheating the mining rig
- Leaving enough power for your daily use

# Intro
I promised I'd help out in the [Monero Recruitment Matrix Room](https://matrix.to/#/#monero-recruitment:monero.social).
Although there was just one direct request to me so far, recently I've also pro-actively proposed cooperation to the chat room members. I presented there 2 projects, that are on my mind, and don't require extensive crypto knowledge, typically not available to students. Yet the projects are still useful for Monero specifically. One of the projects that I have on mind is optimization of mining performance on a solar farm, depending on varying inputs. The member Endor ([endorxmr](https://github.com/endorxmr) on GitHub and endor00 on Matrix) signed up for being the main contributor to the project, while I would serve as a mentor: namely coordinator, reviewer and designer. Such a setup will guarantee, that I won't get dragged away too much from the maintenance of Monero, that I signed up for, while at the same time, Endor will be able to continuously have access to my years of experience in automatic control and object oriented design. Endor on the other hand is heavily involved in everything, that’s connected to mining profitability.

Should Endor not make it until the deadline, I guarantee, that I will finalize the project by myself until the coming winter.

Introducing the project: SolOptXMR – Solar Optimal mining of XMR.

# Why
The following [YT video](https://www.youtube.com/watch?v=7OpM_zKGE4o) is able to bring you more context why this idea has a chance for being a trending subject and is here to stay. The outline of this video is the following:
Because of high initial, as well as perpetual investments required for producing power from solar collectors in Sahara/Nevada and delivering it to northern states, such an investment, contrived in the previous decade under the name "DESERTEC", turned out to be not the best possible investment. The project's relative profitability decreased across the years even more. The reason is, that the costs of production of solar panels dropped so low, that now it makes more sense to place them exactly where the produced power is most needed, even though the solar irradiation is lesser at these places.

On a sentiment / geopolitical side of things, with the rising prices of heating gas, I expect many people will be wanting to save on their gas costs by switching to electrical heating. Since the majority of such heaters demand high power, ranging from 2kW to 2.5kW and since a given population will typically want to switch them on all at the same time, I predict that we'll be facing a decent wave of blackouts in the coming winter. This has motivated me to build my solar farm. 

If you are an individual who likes to take the matters into your own hands, you might have considered building a small solar farm yourself. Although our system won't assume a given user's setup, my particular farm is configured as an isolated island. This means, that I don't sell my overproduction to the grid for the pennies, that the state offers, but rather use the production for mining and cooking, while the overproduction is temporarily stored in a pair of cheap but reliable car batteries. My farm serves as a perfect test bed for the system, that we're going to design and automate for you. Optimized mining of Monero on such a system amortizes the installation costs over the long run, will help you learn about electricity and motivate you to become more resilient. Further compatible extensions are possible, such as small wind generators as well as bikes with flywheels, that [recover kinetic energy](https://www.youtube.com/watch?v=MBW_2gUSMXc). Such systems are already available on the market, that tends to think ahead of the time, so you don’t have to DIY.

# System description

The dynamics of the system, that tries to optimize the mining efficiency has to take into account the following inputs and goals. Some of them are obvious while others maybe not so much.

- Static astronomic data, that describe the relative movement of the Sun across the sky in various latitudes and times of year - yielding the maximal expected power that can be reached
- Weather predictions - a cloudy sky can reduce the power output by more than 80%
- If the predicted power generation is off the measured generation, a warning might be issued to clean the panels
- Voltage (load state) of the batteries, as well as voltage that reaches the DC->AC transformer, as some of it might be lost in the cables, that are either too long or have accidentally formed an inductor
- Predicted load state of the batteries on the next day before the Sun rises and the charging starts, as emptying the chemical batteries below 50% tends to damage them  
- Mining rigs' temperature readouts as it's not worth to meltdown your hardware for those couple of Piconeros being mined.
- A given computer's hashrate per Watt - use the most efficient ones first, but don't overheat them
- A given computer's idle power cost - sometimes it will make sense to switch on certain less efficient computers only if there's really way too much power production, and/or the most efficient ones overheat, or it's predicted that they'd overheat soon under the, also predicted, future conditions.
- Per core efficiency compared against multithreaded efficiency - for CPUs with smaller caches, the efficiency (in this case: hashrate) scales poorly with more threads working at the same time. In such cases it will make sense to spread the mining across longer periods of time on a single core.
- The owners' power usage habits - taking into account, that you might want to use a low powered, compatible electric heating system at a given time of day, by leaving some energy in the batteries for you to consume, before the predicted event – learned either from your usage habits, or from your manually scheduled input.
- The owners' setup – whether an isolated solar island is used, output connected to grid (for selling) or supplementing power losses from the grid (buying) or both of the last 2 options.

The control mechanisms of the system would be the following:
- Downclocking the CPUs - very easy to achieve under Linux with a high precision, thus allowing for a smooth control
- Restarting the mining with a smaller number of cores
- Putting computers to sleep and waking them up with Wake On LAN on the next day

While it would be easy enough to control the system via PID controller, and I know a lot about it, such a system would have little prediction power, delivered only by the first differential part of the controller (the D) and only between the current and the previous state. Using a Time Series Analysis and Prediction tool, such as the already available `tsqsim`, will give the system the ability to look ahead into the future (like at least 48 hours ahead) and plan accordingly to maximize the gain per the unit of energy used, while at the same time planning carefully against overheat of the hardware, under-voltage of the DC->AC transformer, leading to an immediate halt of the system, as well as against under-voltage (as in: capacity) of the batteries, which would otherwise quickly damage them.

The inputs to the system will come in a few forms – either assumed, input by the user or measured. The measurements can be easily supplied via smart plugs or measured directly. Ultimately it has to be left to the user to decide how much time to spend on providing additional inputs, that result in improvements of predictions, thus profitability. The goal here is however to keep the measurements optional, not to impose burden on the user.

# Who
mj – working for Monero since 2 years on the purely technical level. Speeding up compilation and Continuous Integration on GitHub, keeping an eye on overall efficiency, generating [Monero health report](http://cryptog.hopto.org/monero/health/), reviewing technical PRs, helping out new developers. Lately developing Time Series Analysis tool for Monero Research Lab, called `tsqsim`. [Here’s a list](https://github.com/search?q=is%3Apr+author%3Amj-xmr+archived%3Afalse+is%3Aclosed) of all my contributions to Monero and to the supporting software.

Endor – Aerospace Engineering student and a junior Python developer on the side. I already have a few small projects under my belt - one of which related to automation and monitoring of a live system. I've been following the Monero project for over 5 years, learning the ins and outs of cryptocurrency mining and moderating the Supportxmr chat and the Monero Mining room on Matrix (#xmrmine:matrix.org). I am currently developing a comprehensive economic model of mining, and I plan to publish a small paper/series of articles over the next few weeks that will (hopefully) serve as "the ultimate guide to mining" for newcomers and professionals alike. A glimpse into my work can be seen in [this minimalistic script](https://gist.github.com/endorxmr/07364dc54f277abf487574d455d67341), that dynamically calcylates the CPUs mining profitability and compares it across various other CPUs. An example output (though shortened) can be seen below:

```
python3 mining-profitability.py 
Difficulty: 354634073114
Average blocktime @6500 H/s: 631 days, 11:18:08
Price: 201.98 - XXMRZUSD
Expected crypto income/s: 1.236e-08
Expected fiat income/s: 2.496e-06
Profitability: 38.2%
Miner efficiency: 100.0 H/s/W
ROI time: 12577.0 days to recover 750 USD
Breakeven efficiency @0.1/kWh: 72.3 H/s/W
Network power consumption @0.1/kWh: 40849693 W
+--------+--------+-------+--------+
| Period | Profit | Mined | Power  |
+========+========+=======+========+
| Day    |  0.060 | 0.001 |  0.156 |
| Week   |  0.417 | 0.007 |  1.092 |
| Month  |  1.789 | 0.032 |  4.680 |
| Year   | 21.770 | 0.390 | 56.940 |
+--------+--------+-------+--------+
+-------------------------------+--------+-------+------------+--------+
|              CPU              | Speed  | Power | Efficiency | Amount |
+===============================+========+=======+============+========+
| AMD EPYC 7763 (dual)          | 100000 |   750 |    133.333 |  54467 |
| AMD Ryzen Threadripper 3990X  |  65000 |   600 |    108.333 |  68083 |
| AMD Ryzen 3600X               |   7500 |    70 |    107.143 | 583568 |
| Intel Xeon Silver 4216 (dual) |  16157 |   312 |     51.785 | 130929 |
| Intel Core i7-4720HQ          |   1768 |    45 |     39.289 | 907771 |
+-------------------------------+--------+-------+------------+--------+
```

# Milestones

## 1 Initial setup
The initial setup, that is able to use static astronomic data inputs (let’s call it by its name used in the industry: seasonality) and simple weather forecasts (sunny/cloudy/in-between) to make predictions based mostly on user input as to how much power a given computer and its cores consume, taking into account how much power is expected to be consumed in house for other purposes, that have to be treated as of a higher priority. Initially a status message will be displayed about what to do manually to maximize the selected goals. Plots of the inputs and outputs will be displayed, that explain why such a suggestion was presented.

Will be done mostly by mj, since Endor shouldn’t be strained with too many foreign systems, only receive the system’s output signals. This will require about 2 weeks of work full time, that makes:
- 6 (Monday-Saturday) * 2 (weeks) * 8 (hours) = 96 work hours
- 96 work hours / 10h in a week = 9.6 weeks spread.

## 2 Profitability calculator
Profitability calculator, taking into account the power costs, grid’s buy-back prices (if available) and user’s price target, at which to sell the mined coins. Also a very important input will be the time-bound energy availability, delivered through the system from the Milestone 1

This milestone will be done mostly by Endor, due to his experience in the field. I will only support via tips such as obtaining user input and code reviews, design suggestions, etc. I won’t count my pay on this one. This can be started before milestone 1) is finished, on a basis of simple generated sinusoidal signals, that will soon enough be replaced with real data.

Endor’s:
- 6 (Monday-Saturday) * 3 (weeks) * 8 (hours) = 144 work hours
- 144 work hours / 15h in a week = 9.6 weeks spread.


## 3 Measurements
3) Support for various kinds of measurements – smart plugs, digital converters, software temperature readouts and even simple image recognition of LCD/LED displays of the DC→AC transformer and MPPT regulator.

Both of us have experience in various parts here and wish to take equal part in this milestone. I’ll create up to two examples of image recognition.
mj’s:
- 6 (Monday-Saturday) * 2 (weeks) * 8 (hours) = 96 work hours
- 96 work hours / 10h in a week = 9.6 weeks spread.

Endor’s:
- 6 (Monday-Saturday) * 3 (weeks) * 8 (hours) = 144 work hours
- 144 work hours / 15h in a week = 9.6 weeks spread.

## 4 Automation
Automation of the system, including remote CPU downclocking, selecting the number of threads, putting computers to sleep, and waking them up via the Wake On LAN technology. We will be promoting privacy oriented and non-controversial software, namely: [p2pool](https://github.com/SChernykh/p2pool) and [xmrig](https://github.com/xmrig/xmrig), accordingly.

Same as above, both of us have experience and ideas here. I already perform such tasks manually (via scripts) on my solar farm, so I know “the feel” of the system. Endor has many great ideas and a lot of expertise for this milestone as well, as this resonates with his prior experience with mining profitability and a variety of mining software + hardware.

mj’s:
- 6 (Monday-Saturday) * 2 (weeks) * 8 (hours) = 96 work hours
- 96 work hours / 10h in a week = 9.6 weeks spread.

Endor’s:
- 6 (Monday-Saturday) * 3 (weeks) * 8 (hours) = 144 work hours
- 144 work hours / 15h in a week = 9.6 weeks spread.

# Legal & privacy
The project shall be released under AGPLv3. It will send no telemetry by default, unless the user wishes to have their data uploaded and analyzed. The data will surely serve as a stabilization asset of the project and will be included in the automated system tests as one of many test cases. The complete data set to be sent will always be shown to the user for a review and approval.

As I’m familiar with the EU laws regarding solar panels a bit, I will be providing the users non-legally-binding relevant advice.

Even though I’m not strictly an electrical engineer, I know enough tricks in this field and I understand many nuances about the inner workings of such systems. I know what hardware are compatible with each other and how to calculate the supply and demand of the produced power. Therefore I can provide advice in this field as well, yet again: non-legally-binding.

# Proposal
As of 12 April, XMR/EUR is at 214.92 EUR.

## mj:
I will be able to spend about 10 hours / week on the project. An amount so low, that it doesn’t collide with my maintenance assignment, nor Monero Research Laboratory, once I switch there for a while. My rate per hour is 45 EUR. The total number of work hours is: 96 + 96 + 96 = 288. 
288 [h] * 45 [EUR/h] / 214.92 [XMR/EUR] = 60.3 XMR

## Endor:
I will be able to spend about 15 hours / week on the project. My rate in my first ever proposal is at 25 EUR / h. The total number of work hours is: 144 + 144 + 144 = 432. 
432 [h] * 25 [EUR] / 214.92 [XMR/EUR] = 50.25 XMR

Since in this case we are really talking about seasonal data, that doesn’t require a lot of readjustments, further maintenance will not be a burden for any of us. Unless many new features are requested, we will gladly maintain it for you without asking for compensation.

## Summary:
60.3 + 50.25 = 110.55 XMR is what we're asking for. Thanks in advance!

## Deadline calculation
A rough deadline calculation based on the spread of the hours and including the tasks that can be done in parallel:
9.6 [weeks] * 3 / 4.1 [weeks in a month] ~ 7 months.
This coincides with the promise to finalize the project until winter if all goes well with Endor’s plan. If not, I can take over most of the responsibilities, as there are always ~1-1.5 month breaks between my maintenance proposals.

Cheers!

# Expiration date
31 Oct, 2022
