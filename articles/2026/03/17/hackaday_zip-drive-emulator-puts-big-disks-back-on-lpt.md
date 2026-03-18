---
title: "Zip-Drive Emulator Puts Big Disks Back on LPT"
source: "Hackaday"
url: "https://hackaday.com/2026/03/17/zip-drive-emulator-puts-big-disks-back-on-lpt/"
published: "2026-03-17"
fetched: "2026-03-18T14:11:40.278644"
---

Iomega’s Zip drives filled an interesting niche back in the 1990s. A magnetic disk that was physically floppy-sized, but much larger in capacity– starting at 100 MB, and reaching 750 MB by the end–they never quite had universal appeal, but never really went away until flash memory chased them out of the marketplace in the early 2000s. While not everyone is going to miss them, some of us still think it’s a better form factor than having a USB stick awkwardly protruding from a computer, or microSD cards that are barely large enough to see with the naked eye. [Minh Danh] is one of those who still has affection for Zip drives, and when his parallel port Zip 100 drive started to give up the ghost last year, he decided to do something bold: reverse engineer it, and produce an emulator. First software, and then in hardware.
The first was to create a virtual zip drive that could run on a virtual machine and be accessed with DOS or Windows up to XP. The next task was to move that functionality onto a microcontroller to create something like a GoTek floppy emulator for LPT Zip drives that he’s calling the LPT100. Yes, Zip drives were built for APATI, SCSI, FireWire and USB, too, but [Minh]’s was on the parallel port and that’s what he wanted to replace, so the LPT interface is what set out to recreate.
It works, too, though took more guts than was expected– the 8-bit PIC18F4680 he started with just wasn’t up to the task. He moved up to a 32-bit PIC, the PIC32MZ2048EFH144 to be specific, which proved adaquate when testing with his Book 8088, a new DOS PC from 2023. Iomega’s official driver won’t run on an 8088, but the PALMZIP utility does and was able to transfer files, though only at the slow nibble rate due to limitations with the Book8088’s LPT hardware. Watch it in action below.
Alas, moving up to the Pocket386, it seemed the PIC just could not keep up. [Minh] says he’s thinking of moving to the faster Teensy 4.1, which sounds like a good idea. Considering the Teensy can be configured to serve as a drop-in replacement for a 68000, bit-banging the bus at 7.8 MHz, we’d think it should handle anything a parallel port can throw at it.
Thanks to [Minh Danh] for the tip!
