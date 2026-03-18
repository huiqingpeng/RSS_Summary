---
title: "Zip-Drive Emulator Puts Big Disks Back on LPT"
source: "Hackaday"
url: "https://hackaday.com/2026/03/17/zip-drive-emulator-puts-big-disks-back-on-lpt/"
published: "2026-03-17"
summarized: "2026-03-18T14:11:54.291439"
ai_provider: "openai"
---

【是什么 / What it is】

这篇文章介绍了技术爱好者 [Minh Danh] 为 Iomega Zip 100 驱动器开发的并行端口（LPT）硬件模拟器。由于他的原装 Zip 驱动器出现故障，他逆向工程了该设备，先用软件在虚拟机上实现虚拟 Zip 驱动器，随后开发了基于微控制器的硬件模拟器 "LPT100"，让老式电脑能够通过并行接口继续使用 Zip 磁盘功能。

This article introduces a hardware emulator for the Iomega Zip 100 drive's parallel port (LPT) interface developed by tech enthusiast [Minh Danh]. After his original Zip drive failed, he reverse-engineered the device—first creating a software-based virtual Zip drive for virtual machines, then developing a microcontroller-based hardware emulator called "LPT100" that allows vintage computers to continue using Zip disk functionality through the parallel interface.

---

【为什么重要 / Why it matters】

Zip 驱动器代表了 1990 年代至 2000 年代初的一种独特存储形态，在闪存普及前填补了软盘与光盘之间的容量空白。这个模拟器项目不仅保护了即将消失的硬件遗产，也为复古计算社区提供了实用的替代方案，同时展示了个人开发者如何通过逆向工程和开源硬件延续技术生命。

Zip drives represent a unique storage form factor from the late 1990s to early 2000s, filling the capacity gap between floppy disks and optical media before flash memory dominated. This emulator project not only preserves disappearing hardware heritage but also provides practical alternatives for the retrocomputing community, demonstrating how individual developers can extend technological lifespans through reverse engineering and open-source hardware.

---

【我能用什么 / How I can use it】

如果你拥有老式 DOS/Windows 9x 系统或复古电脑项目（如文中所提的 Book 8088、Pocket386），可以关注该项目的硬件设计（PIC32MZ 或未来的 Teensy 4.1 版本）来替代故障的 Zip 驱动器。对于嵌入式开发者，这是学习并行端口通信、存储协议逆向和微控制器性能优化的优秀案例；也可借鉴其思路，为其他 legacy 接口（如 SCSI、IDE）开发类似模拟器。

If you own vintage DOS/Windows 9x systems or retro computer projects (like the Book 8088 or Pocket386 mentioned), you can follow this project's hardware design (PIC32MZ or future Teensy 4.1 version) to replace failing Zip drives. For embedded developers, this serves as an excellent case study for learning parallel port communication, storage protocol reverse engineering, and microcontroller performance optimization; you can also adapt this approach to develop similar emulators for other legacy interfaces like SCSI or IDE.
