---
title: "Running Windows 98 on the iPAQ IA-2 Internet Appliance"
source: "Hackaday"
url: "https://hackaday.com/2026/03/18/running-windows-98-on-the-ipaq-ia-2-internet-appliance/"
published: "2026-03-18"
fetched: "2026-03-19T08:02:50.594311"
---

Devices that were limited to only run a web browser were relatively common around 2000, as many people wanted to surf the Information Super Highway, but didn’t quite want to get a regular PC — being in many ways the retro equivalent of a Chromebook. The Compaq iPAQ IA-2 from 2000 that [Dave Luna] got is no exception, with a Microsoft CE-based OS that is meant to be used with Microsoft Network (MSN) dial-up, which amusingly is still available today.
In order to get a more useful OS on it, like Windows 98, you have to jump through quite a few hoops, as [Dave] found out. Although there is an IDE connection on the mainboard, this cannot be booted from, likely due to BIOS limitations. This means that he had to chain boot via the 16 MB NAND Flash drive that the original OS booted from, which was done by writing MS-DOS to the Flash drive using another workaround as it’s not a standard IDE device either.
From this you can then boot Windows 98 from an IDE drive by pretending that it’s an ATAPI IDE device to dodge a limitation on IDE devices. The system’s hardware isn’t really going to make it into a blazing fast retro computer. It only has a 266 MHz Geode GX1 CPU and supports up to 256 MB of SDRAM. The IA-2 is also limited to 800×600, which required the use of an external monitor (as seen above) hooked up to the internal VGA port to set the proper resolution in the OS.
But at least it can run DOOM, so that bare minimum requirement can be ticked off.
