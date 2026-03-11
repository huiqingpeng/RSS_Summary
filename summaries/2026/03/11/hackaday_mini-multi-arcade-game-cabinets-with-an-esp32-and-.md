---
title: "Mini Multi-Arcade Game Cabinets with an ESP32 and Galagino"
source: "Hackaday"
url: "https://hackaday.com/2026/03/11/mini-multi-arcade-game-cabinets-with-an-esp32-and-galagino/"
published: "2026-03-11"
summarized: "2026-03-12T07:04:10.087661"
ai_provider: "openai"
---

【是什么 / What it is】
这是一篇介绍基于 ESP32 微控制器的迷你街机游戏柜开源项目的文章。核心项目 Galagino 由 Till Harbaum 开发，能够在廉价硬件上模拟 1980 年代经典街机游戏；社区成员随后将其移植到 PlatformIO 和 Arduino 平台，并设计了 3D 打印外壳，形成了完整的 DIY 解决方案。

This article introduces an open-source project for building mini arcade game cabinets powered by the ESP32 microcontroller. The core project, Galagino, developed by Till Harbaum, emulates 1980s classic arcade games on inexpensive hardware; community members later ported it to the PlatformIO and Arduino platforms and designed 3D-printable enclosures, creating a complete DIY solution.

---

【为什么重要 / Why it matters】
该项目展示了现代低成本微控制器（如 ESP32）如何轻松超越复古街机硬件性能，使个人爱好者能够以极低成本和极小空间复刻经典游戏体验。它也体现了开源硬件社区的协作力量——从核心模拟器到多平台移植、再到实体外壳设计，形成了可快速迭代和定制的生态系统。

This project demonstrates how modern low-cost microcontrollers like the ESP32 can easily outperform retro arcade hardware, enabling hobbyists to recreate classic gaming experiences at minimal cost and footprint. It also exemplifies the collaborative power of the open-source hardware community—from the core emulator to multi-platform ports and physical enclosure designs—forming a rapidly iterable and customizable ecosystem.

---

【我能用什么 / How I can use it】
你可以购买廉价的 "Cheap Yellow Display" (CYD) 开发板（集成 ESP32、触摸屏、SD 卡槽和音频输出），直接刷入 Galagino 固件快速搭建原型；或参考 Davide Gatti 的 Arduino 移植版本和 3D 打印文件，动手制作带双屏显示的完整街机柜。此外，可研究 PlatformIO 移植版中的多游戏支持代码，扩展更多街机 ROM 或定制自己的游戏列表界面。

You can purchase an inexpensive "Cheap Yellow Display" (CYD) board (integrating ESP32, touchscreen, SD card slot, and audio output) and flash the Galagino firmware directly for rapid prototyping; or reference Davide Gatti's Arduino port and 3D-printable files to build a complete cabinet with dual-screen display. Additionally, you can study the multi-game support code in the PlatformIO port to expand more arcade ROMs or customize your own game selection interface.
