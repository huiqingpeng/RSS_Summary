---
title: "Porting MS-DOS 2.0 to the Apple IIe"
source: "Hackaday"
url: "https://hackaday.com/2026/03/13/porting-ms-dos-2-0-to-the-apple-iie/"
published: "2026-03-14"
summarized: "2026-03-15T07:03:34.274790"
ai_provider: "openai"
---

【是什么 / What it is】
这篇文章讲述了[Seth Kushniryk]将MS-DOS 2.0移植到Apple IIe计算机上的项目。Apple IIe通过ALF Products的AD8088协处理器卡（内置Intel 8088处理器）可以运行x86软件，但原版MS-DOS 2.0软件已失传，因此需要重新移植。他利用微软发布的MS-DOS 2.0 OEM适配套件和源代码进行开发，目前已实现基本启动功能。

This article describes [Seth Kushniryk]'s project to port MS-DOS 2.0 to the Apple IIe computer. The Apple IIe could run x86 software through the ALF Products AD8088 co-processor card (with built-in Intel 8088 processor), but the original MS-DOS 2.0 software has been lost to time, necessitating a new port. He is using Microsoft's released MS-DOS 2.0 OEM Adaptation Kit and source code for development, with basic boot functionality already achieved.

---

【为什么重要 / Why it matters】
这个项目具有双重价值：一是保护了濒临消失的计算机历史遗产，通过现代技术手段复原80年代的软硬件生态；二是展示了开源社区在数字考古中的力量，利用公开的OEM套件让失传系统重获新生。它也揭示了早期个人电脑通过协处理器扩展架构的巧妙设计思路。

This project holds dual significance: it preserves endangered computing heritage by restoring 1980s software/hardware ecosystems through modern techniques, and demonstrates the open-source community's power in digital archaeology—reviving lost systems using publicly available OEM kits. It also reveals the ingenious design approach of early personal computers using co-processor expansion architectures.

---

【我能用什么 / How I can use it】
对于复古计算爱好者，可关注该项目的GitHub发布，尝试在真实硬件或模拟器上运行；对于开发者，可研究MS-DOS OEM适配套件的处理方式，学习如何将旧系统移植到新（或旧）硬件平台。这也是了解早期文件系统（ProDOS与MS-DOS时钟差异）和串口驱动开发的实践案例。

For retrocomputing enthusiasts: follow the project's public release and try running it on real hardware or emulators. For developers: study how the MS-DOS OEM Adaptation Kit is utilized, learning techniques for porting legacy systems to new (or old) hardware platforms. This also serves as a practical case study for understanding early filesystems (ProDOS vs. MS-DOS clock differences) and serial driver development.
