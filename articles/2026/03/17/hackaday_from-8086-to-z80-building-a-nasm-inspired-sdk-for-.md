---
title: "From 8086 to Z80: Building a NASM-Inspired SDK for 8-Bit Retro Computing"
source: "Hackaday"
url: "https://hackaday.com/2026/03/17/from-8086-to-z80-building-a-nasm-inspired-sdk-for-8-bit-retro-computing/"
published: "2026-03-17"
fetched: "2026-03-18T07:02:49.886158"
---

Assembler syntax is a touchy subject, with many a flamewar having raged over e.g. Intel vs AT&T style syntax. Thus when [Humberto Costa] recently acquired an MSX system for some fun retro-style ASM programming, he was dismayed to see that the available Z80 assemblers did not support the syntax of his favorite ASM tool, NASM. Thus was born the HC SDK project, which seeks to bring more NASM to the Z80, 8085 and a slew of other processors.
There’s both a project site and a GitHub repository, from where both source and pre-compiled releases can be obtained. Supported host platforms are macOS, Windows, OpenBSD, FreeBSD, and Linux, with currently supported targets the 8080, 8085, 8086 and Z80. Support for the 6502 is currently in progress.
The Netwide Assembler (NASM), targets only the x86 architecture, being one of the most popular assemblers for Linux and x86. It uses a variant of the Intel ASM syntax, which contrasts it strongly with the GNU Assembler (GAS) that uses AT&T syntax. Of course, in an ironic twist of fate NASM now also supports AT&T syntax and vice versa, albeit with some subtle gotchas.
Regardless, if ASM for these retro architectures is your thing, then the HC SDK may be worth checking out. [Humberto] also says that he’s looking at adding higher-level language support to make it a more complete development environment for these old systems and new takes on them.
Thanks to [Albert Wolf] for the tip.
