---
layout: fr
title: Monero Kubernetes Operator
author: Ciro S. Costa (utxobr)
date: May 3, 2021
amount: 22.86
milestones:
  - name: Proof of concept
    funds: 0
    done: 02 May 2021
    status: finished
  - name: Prototype refactoring, installation improvements and docs
    funds: 2.47
    done:
    status: unfinished
  - name: Support annonimity networks
    funds: 3.71
    done:
    status: unfinished
  - name: Improve observability of nodes
    funds: 3.71
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


## Brief Intro

My name is Ciro S. Costa (https://github.com/cirocosta,
https://twitter.com/utxobr), I'm currently a staff engineer, having previously
being a core contributor to https://concourse-ci.org.

Monero-wise, I've been mostly focused on the networking side of it, having
implemented the basics of Levin's handshake in Go
(https://github.com/cirocosta/go-monero) with full support for the
Portablestorage format, which lets me create some interesting reports on node
distribution (see https://twitter.com/utxobr/status/1386458317405540360) by
crawling the P2P network.


## Problem

_**tl;dr**: there's no good solution for running a large number of monero
nodes_

For those with more than a machine or two to run Monero nodes (or even miners),
there's not a good solution out there for having those up and running in an
easy to upgrade fashion.

It's great that folks like Seth provide wonderful guides on how to run Monero
nodes (see https://sethsimmons.me/guides/run-a-monero-node-advanced/), and that
within the functional tests in the codebase we can tell how to run regtest, but
none of that helps with running a larger-scale setup.


## Proposal

_**tl;dr**: extend the Kubernetes API via its common extension system to provide
semantics that make deploying clusters of monero nodes or miners with ease. See
proof of concept at https://github.com/cirocosta/monero-operator_

Kubernetes (see [what is kubernetes]) provides us with this vendor-neutral API
for expressing what the desired state should be, and then behind the scenes,
having that state achieved (and maintained) through the use of small
programs whose whole job is to deal with going from current state to desired state.

Aside from being offered by pretty much every cloud provider (and many VPS
offerings out there too) and still remaining not vendor-specific, its API is
open for extension, which we can leverage to provide extra functionality that
it didn't have before.

By extending the Kubernetes API via the use of [Custom Resources], we're able
to provide a new semantics for the users of those clusters so that we simplify
*a lot* running, say a few Monero nodes all configured the same across
different machines


```yaml
kind: MoneroNodeSet
apiVersion: utxo.com.br/v1alpha1
metadata:
  name: nodes
spec:
  replicas: 3
  hardAntiAffinity: true
  monerod:
    image: utxobr/monerod:v0.17.2.0     # if testing a release candidate,  then
    args:                               # just bump the image and the operator
      - --public                        # will take care of rolling out, preserving
      - --enable-dns-blocklist          # the data already synced.
      - --enforce-dns-checkpointing
      - --out-peers=1024
      - --in-peers=1024
      - --limit-rate=128000
```

which could be very useful for businesses like CakeWallet that run sets of full
nodes (or literally anyone wanting to run highly-available monerod
deployments), but it can be also useful for folks doing research like me,
wanting to roll out a regtest network with many peers:

```yaml
kind: MoneroNetwork
apiVersion: utxo.com.br/v1alpha1
metadata:
  name: regtest
spec:
  replicas: 20

  template:
    spec:
      monerod:
        args:                           # each replica has these args
          - --regtest                   # plus `--add-exclusive-node`
          - --fixed-difficulty=1        # pointing just at the other
                                        # peers, forming a closed net
```

_(^ which under the hood gets materialized in the form of `monerod` instances
pointing one at each other, with volumes attached and everything you'd want for
a real setup.)_

Naturally, we can do the same for miners, for instance, we can get to run 10
replicas of `xmrig` against a pool like so:

```yaml
kind: MoneroMiningNodeSet
apiVersion: utxo.com.br/v1alpha1
metadata:
  name: miners
spec:
  replicas: 10
  hardAntiAffinity: true

  xmrig:
    args:
      - -o
      - cryptonote.social:5556
      - -u
      - 891B5keCnwXN14hA9FoAzGFtaWmcuLjTDT5aRTp65juBLkbNpEhLNfgcBn6aWdGuBqBnSThqMPsGRjWVQadCrhoAT6CnSL3.node-$(id)
      - --tls
```

and then, if we regret chosing that pool, all it takes is patching the object
and under the hood, our extension to Kubernetes takes care of rolling the
updates out.

_(aside: couple this with [horizontal pod autoscaler (HPA)] and you don't even
need to pre-provision any underlying machines - if your provider supports HPA -
as by making use of proper resource reservation, asking for extra replicas
would trigger the creation of new machines)._


[what is kubernetes]: https://kubernetes.io/docs/concepts/overview/what-is-kubernetes
[Custom Resources]: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources
[horizontal pod autoscaler (HPA)]: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
[OpenMetrics]: https://github.com/OpenObservability/OpenMetrics/blob/main/specification/OpenMetrics.md
[Prometheus]: https://prometheus.io/


## The scope

I currently have a working proof of concept
(https://github.com/cirocosta/monero-operator) that implements those three
custom resources mentioned above (`MoneroMiningNodeSet`, `MoneroNodeSet`, and
`MoneroNetwork`).

This CCS would cover:

1. boosting the confidence in the codebase by providing more tests to cover
   edge cases glanced over while building the prototype, as well as improving
   installation and documentation as a whole

2. adding support for Tor and I2P so that nodes and networks can be deployed on
  annonimity networks with a line or two in the yaml while still running the
  services with high availability

3. improving the observability of the deployed `monerod` instances introducing a
  sidecar to expose `monerod` metrics for any [OpenMetrics] consumer (like
  [Prometheus])


As a result, the community will end up with:

- a Kubernetes extension that lets anyone deploy highly-available `monerod`
  (and miners) on any Kubernetes-enabled platform

- a Go package that they can rely on for interacting with `monerod`


## The structure, milestones, and price.

Working on this during my personal hours, I plan to do the work a few hours a
day on the side (with a few healthy periods of break) until completion.

The proposal is structured to be paid along with the delivery of the three points above:

1. confidence in the codebase + installation/doc guides: ~10Hr
2. support for Tor and I2P for full nodes and whole networks: ~15Hr
3. observability of `monerod`: ~15Hr

Assuming a rate of 100$/hr and a current rate of 404 USD/xmr (May 3rd, 2021):

| deliverable | hours | usd | xmr |
|-----|------|-----|-----|
| 1 | 10 | $ 1000 | XMR 2.47 |
| 2 | 15 | $ 1500 | XMR 3.71 |
| 3 | 15 | $ 1500 | XMR 3.71 |

