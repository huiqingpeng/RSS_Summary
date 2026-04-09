---
title: "You’ve All Seen A Hackintosh, But Have You Seen One On A Wii?"
source: "Hackaday"
url: "https://hackaday.com/2026/04/08/youve-all-seen-a-hackintosh-but-have-you-seen-one-on-a-wii/"
published: "2026-04-09"
fetched: "2026-04-10T07:04:39.889772"
---

The Intel era of Apple Macs led to so-called “Hackintoshes”, more normal PCs running x86 MacOS X. Now Bryan Keller proves that a Hackintosh isn’t restricted to the x86 era, not by doing it with a modern ARM version, but by going back to PowerPC, and the Nintendo Wii.
The Wii can be thought of in hardware terms as not too far from a Mac G3 with a little less memory, having a PowerPC 750-family processor, a close relative as those in the first generation of MacOS X capable Macs. Since the roots of MacOS X are shared with its open-source equivalent Darwin, he reasons it should be possible to port just enough Darwin to the Wii to enable the closed-source OS X to run on top of it. He’s running OS X 10.0, the earliest version from 2001.
The write-up is a fascinating path through writing a bootloader and running a patched kernel that flashes the Wii LEDs, and then the process of making the Wii’s very different hardware from a Mac, accessible to the OS. It boots from an SD card and uses a framebuffer for display so perhaps it’s not as fast as you might hope, but he gets it working. Even for someone not versed in MacOS or the Wii, it’s a good write-up that makes its points accessible.
Something that makes us happy about this piece of work is its place in the greater picture, after all the Wii has found itself running classic MacOS too.
