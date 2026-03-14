---
title: "Porting MS-DOS 2.0 to the Apple IIe"
source: "Hackaday"
url: "https://hackaday.com/2026/03/13/porting-ms-dos-2-0-to-the-apple-iie/"
published: "2026-03-14"
fetched: "2026-03-15T07:03:27.832783"
---

Although the Apple II range of computers were based around the 6502 processor, they could still run x86 software using expansion cards that were effectively self-contained computers. This way an Apple IIe owner, for example, could install an Intel 8088-based AD8088 co-processor card by ALF Products and run CP/M-86 as well as MS-DOS. Unfortunately, as [Seth Kushniryk] discovered while digging into this MS-DOS option, there don’t seem to be any remaining copies of the accompanying MS-DOS 2.0 software.
The obvious response to this is of course to try and port it once again, which [Seth] did. So far he got it to boot, though it’s not quite ready for prime-time yet. Although the AD8088 card is fairly self-contained, it still has to talk with the Apple IIe system, which poses some challenges. To help with the porting he’s using the MS-DOS 2.0 OEM Adaptation Kit that was released along with the sources a while back.
The Apple II has to first load the basic MS-DOS files into the 8088’s RAM before handing over control, which works now along with the basic functionality. Before [Seth] releases the port to the public he still wants to fix a number of issues, in particular the clock. ProDOS on the Apple IIe encodes the year differently than MS-DOS, so that the latter’s clock is off by a few years, and the console driver is still not quite as robust as [Seth] would like it to be.
Beyond this there is also working with the other cards in the Apple II2 system, including the Super Serial Card, and working with the ProDOS filesystem.
