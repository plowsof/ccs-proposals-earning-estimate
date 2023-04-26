---
layout: wip
title: Maintaining Flatpak package
author: BigmenPixel
date: March 21, 2023
amount: 10.02
milestones:
  - name: manifest to core repo
    funds: 3.5
    done:
    status: unfinished
  - name: 3 month maintenance
    funds: 1.63
    done:
    status: unfinished
  - name: 3 month maintenance
    funds: 1.63
    done:
    status: unfinished
  - name: 3 month maintenance
    funds: 1.63
    done:
    status: unfinished
  - name: 3 month maintenance
    funds: 1.63
    done:
    status: unfinished
payouts:
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

## **Maintaining flatpak package `org.getmonero.Monero`**

## Summary

I have been maintaining `org.getmonero.Monero` on Flathub since July 2021. Now I want to move its manifest to the [monero-gui](https://github.com/monero-project/monero-gui) repository. The org.getmonero.Monero github repo which is now used to push files to flathub will be discontinued. The files will be built and pushed directly from the monero-gui repository. Users will then be able to compare the hashes of files on their machines to those from the monero-gui workflow run. We can then give Monero-gui flatpak app a "verified" checkmark. This is an optional step for the community to decide at a later date. Flatpak installs will still remain 3rd-party and users are encouraged to confirm hashes, as they are with any other package repository.

Thanks to this, users will be able to trust this flatpak package more.

## Installing and using

The `org.getmonero.Monero` flatpak package is a good replacement for ordinary packages in GNU/Linux distributions, for example it can be used in Whonix to [replace](https://forums.whonix.org/t/how-to-verify-the-monero-binaries-that-are-shipped-with-whonix/16439/10) the Debian package. 

At first you have to [setup flatpak](https://flatpak.org/setup) with Flathub repository on your GNU/Linux distribution. After that, run this command:
```
$ flatpak install flathub org.getmonero.Monero
```

By default, `org.getmonero.Monero` has access only to the `~/Monero` directory, if you need more, do it:
```
$ flatpak --user override --filesystem=/path_to_your_directory org.getmonero.Monero
```

Some people need access to the `monerod` command:
```
$ flatpak run --command=monerod org.getmonero.Monero [options|settings] [daemon_command...]
```

## About me

I am [BigmenPixel](https://github.com/BigmenPixel0), who maintains Monero GUI on Flathub and some packages in the [AUR](https://aur.archlinux.org/account/BigmenPixel).

### Milestone 1 (3.5XMR)

Move the manifest to the [monero-gui](https://github.com/monero-project/monero-gui) repository.

### Milestone 2 (6.5XMR)

1 year of maintenance to be paid quarterly @1.63XMR after performance review (updates are ready in a timely manner / critical issues solved).

These rates are based off of the previous [debian package maintenance](https://ccs.getmonero.org/proposals/adrelanos-debian-package.html) proposal.
