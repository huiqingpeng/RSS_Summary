---
title: "You Can Now Run MS-DOS Applications on the Apple IIe"
source: "Hackaday"
url: "https://hackaday.com/2026/03/25/you-can-now-run-ms-dos-applications-on-the-apple-iie/"
published: "2026-03-25"
fetched: "2026-03-26T07:03:38.257235"
---

After a lot of debugging, [Seth Kushniryk] has managed to get the last issuess shaken out of his port of MS-DOS 2.0 to the Apple II, and has released the project to the public. If you have the requisite AD8088 or similar co-processor expansion card with onboard x86 CPU, this should be all you need to get started.
Although this co-processor card contains effectively a self-contained x86 system, its only I/O goes via the expansion bus, so it has to play nice with the 6502 CPU of the Apple II system. When we last reported on [Seth]’s efforts he had just managed to get MS-DOS 2.0 booting and basically in a barebones working state.
Since then he’s been working on the bridge program that provides communication between the 8088 on the card and the Apple II’s 6502, relocating it in RAM to enable high-resolution graphics, as well as other tweaks and optimizations. Also a lot of bug hunting, including an undocumented ProDOS constraint with a request count.
With all of this done it’s now possible to run basically any MS-DOS 2.0 compatible software, assuming it doesn’t try to write directly to video memory. This does limit the software selection somewhat, but back in the day it would probably have been amazing to have that 8 MHz 8088 purring along the 6502 to run both Apple and DOS software titles. Props to [Seth] for restoring this software functionality that had been lost to the ages.
