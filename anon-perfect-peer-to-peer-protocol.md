---
layout: wip
title: "anon: perfect peer to peer protocol from bottom to top"
author: anon
date: 24 Jan 2021
amount: 240.12021
milestones:
  - name: Feb.
    funds: 33% (80.04007 XMR)
    done:
    status: unfinished
  - name: Mar.
    funds: 33% (80.04007 XMR)
    done:
    status: unfinished
  - name: Apr.
    funds: 33% (80.04007 XMR)
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

## What

~~~
Perfection is not attainable, but if we chase perfection we can catch excellence.

On the way to perfect monero blockchain synchronization daemon
  which is correct, simple and efficient.

On the way to perfect peer to peer protocol implementation that
  forbids arbitrary devitation in peers behavior,
  balances available resources between unsynchronized and synchronized peers,
  keeps new block propogation latency as low as possible.

All related layers hierarchy:
     input/output loop
            v
          socket
            v
        ssl socket
            v
        connection
            v
     abstract tcp server
            v
     levin protocol + portable storage
            v
         net node
            v
    cryptonote protocol + core rpc server
            v
     cryptonote core + crypto
            v
      blockchain db + tx pool

The following layers are not correct:
  ssl socket,
  connection,
  abstract tcp server,
  net node,
  cryptonote protocol,
  tx pool.

The following layers are very inefficient:
  portable storage.

All above layers aren't simple.

There are few critical errors that must be fixed first:
  segfaults,
  enormous RAM usage,
  enormous CPU load,
  deadlocks,
  unexpected delays in asynchronous code.

Work will be done in the following order:
  fix critical errors,
  simplify,
  fix incorrect behvaiour,
  simplify,
  add new changes,
  simplify,
  increase efficiency,
  simplify.

The above final aim and related scope require much more than 3 months work.
~~~

## Who

~~~
anon
~~~

## Proposal

~~~
Dedicate at least 3 months (12 hours per each day including weekends) to Monero Project for a total of 240.12021 XMR.
~~~
