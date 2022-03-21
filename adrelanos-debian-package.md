---
layout: wip
title: "Monero Debian Package Repository for 2 years"
amount: 73
author: Patrick Schleizer
date: 15 April 2020
milestones:
  - name: "Monero Debian Package Initial Packaging"
    funds: 50% (37 XMR)
    done: 31 December 2020
    status: finished
  - name: "Monero Debian Package Maintenance 2021"
    funds: 25% (18 XMR)
    done: 31 December 2021
    status: finished
  - name: "Monero Debian Package Maintenance 2022"
    funds: 25% (18 XMR)
    done:
    status: unfinished
payouts:
  - date: 18 February 2021
    amount: 37
  - date: 21 March 2022
    amount: 18
  - date:
    amount:
---

### Importance to the Monero Community

Ease of installation and timely software upgrade on popular stable Linux distributions such as Debian is important to gain better usability and greater adaption.

A higher share of privacy conscious users are using Linux rather than Windows.

This is also a preparatory step for installation of Monero by default in (privacy focused) Linux operating systems such as Whonix (which I happen to be the founder). Other Debian based Linux distributions such as Tails (also privacy focused) are welcome to use the package as well.

### User Experience

Instructions for users, simplified.

How to install monero GUI using apt-get

Download the repository signing key.

    wget https://www.whonix.org/patrick.asc

Add the signing key.

    sudo apt-key --keyring /etc/apt/trusted.gpg.d/monero.gpg add ~/patrick.asc

Add APT repository.

    echo "deb https://deb.whonix.org buster main" | sudo tee /etc/apt/sources.list.d/monero.list

Update your package lists.

    sudo apt-get update

Install monero-gui.

    sudo apt-get install monero-gui

### Technical Implementation Details

The focus is the user. Usability. No frills.

I would simply grab the monero-gui binaries provided by getmonero.org, download them, check software (gpg) signatures, put these into deb packages, add these to a Debian package repository, and upload the repository.

What I would not do is creating the binaries during package build process. While this is nice to have, it doesn't help user experience and blocks the progress on reaching this goal. See next chapter.

The monero-gui binary includes it all:

* monero-wallet-gui
* monero-wallet-cli
* monerod

Therefore monero-gui package would come with all of that too. The package would be usable by both, desktop and headless computers.

Hosting on whonix.org rather than getmonero.org to keep maintenance effort low. Therefore no coordination with getmonero.org DNS required. Saves money for purchasing a domain. Contributes to decentralization since the maintainer of Whonix would maintain the Monero Debian packages independently. Maintaining another package on the domain which hosts many packages already is lower effort than a completely separate Debian package repository.

`packages.debian.org` is out of scope since Debian does not upgrade often enough to keep up with Monero fork cycle and for other reasons as well.

64 bit only.

The contents of monero-gui will be placed in folder `/usr/share/monero/monero-gui-v0.14.1.0`, unmodified. Folder `/usr/bin` will contain wrapper scripts pointing to the binaries in `/usr/share/monero/monero-gui-v0.14.1.0`.

### Why simply put the pre-build Monero binaries into a deb package?

1) After bitcoin existing for more than 10 years, being popular and being in Debian unstable (sid) it still never made its way into Debian testing, let alone stable. Reason being explained that a difference in underlying libraries (even just security fixes) during compilation may result in a network split. Binaries compiled during packaging on different versions of Linux distributions might have different libraries that might cause a network fork / chain split.

References:

* https://packages.debian.org/search?keywords=bitcoin-qt
* https://packages.debian.org/sid/bitcoin-qt
* [upstream does not support stable releases (block migration to testing)](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=718272)

(Note: above website saying Tags: `fixed-upstream` is probably a mistake as discussion at bottom says.)

2) The [github issue of packaging monero](https://github.com/monero-project/monero/issues/2395) stalled.

3) By shipping the same binaries as provided by getmonero.org reduces the chances of introducing a backdoor.

### Included in the First Milestone

* Monero in a Debian repository. `deb https://deb.whonix.org buster main` as per above `User Experience`.
* User documentation on how to install the `monero-gui` package from the repository.
* Build documentation detailing how to build the package oneself.
* Use the usual Whonix news channels to call for testers. Fix any bugs that users might report.
* Simplification of [Monero users instructions for Whonix users](https://www.whonix.org/wiki/Monero) saying "install this package".
* Test monero GUI in Debian buster, Whonix and Qubes Debian buster template.
* Start menu entries.
* Replying to (most) (reasonable) unanswered support requests related to the packaging.

### Non-Goals

Installation of Monero by default in Whonix. While Monero will very likely be installed by default in Whonix it is not guaranteed and not part of this proposal. I've already posted a number of comments on monero GUI issue tracker which should help to ensure that Monero keeps suitable for installation by default in Whonix, see [this list](https://forums.whonix.org/t/supporting-monero-as-the-default-cryptocurrency/6410/14).

### Funding for First Milestone

2000 USD

(Includes initial packaging and and maintenance until the end of the year 2020.)

### Timeline

Doable quickly within 1 week.

By comparison, the electrum (bitcoin) AppImage was recently added to a Debian package (binaries-freedom) by me and is now easily installable in Whonix. Pre-installed in stable version of Whonix already.

### Ongoing Maintenance Cost

* year 2021: 1000 USD
* year 2022: 1000 USD

### About Me

I am the founder of [Whonix](https://www.whonix.org/), which I am maintaining at present for more than 8 years.

Whonix (formerly TorBOX) is a Debian GNU/Linuxbased security-focused Linux distribution. It aims to provide privacy, security and anonymity on the internet.

You can see an overview of packages I am maintaining on [my github profile](https://github.com/adrelanos).

To proof that this monero gitlab account `adrelanos` corresponds the same person maintaining whonix.org, it is added [here](https://www.whonix.org/wiki/Official_Whonix_Online_Profiles).

[This idea was previously discussed on reddit.](https://www.reddit.com/r/Monero/comments/cowjun/idea_proposal_monero_debian_deb_packages_debian/)

### Credits

Thanks to @rehrar for helping me with this proposal!
