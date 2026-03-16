---
title: "ATtiny85 Plays the Chrome Dinosaur Game"
source: "Hackaday"
url: "https://hackaday.com/2026/03/16/attiny85-plays-the-chrome-dinosaur-game/"
published: "2026-03-16"
summarized: "2026-03-17T07:06:20.537567"
ai_provider: "openai"
---

【是什么 / What it is】
这篇文章介绍了一个使用 Digispark ATtiny85 微控制器制作的自动化硬件项目，该设备通过光敏电阻传感器检测 Chrome 浏览器离线恐龙游戏中的障碍物（仙人掌和飞鸟），并自动发送 USB HID 键盘信号来控制游戏角色跳跃。这是一个将嵌入式硬件与计算机视觉简化方案相结合的趣味创客项目。

This article describes a DIY hardware project using a Digispark ATtiny85 microcontroller that automatically plays Chrome's offline dinosaur game. The device uses light-dependent resistor (LDR) sensors to detect on-screen obstacles (cacti and birds) and sends USB HID keyboard signals to control jumps, combining embedded hardware with a simplified computer vision approach.

【为什么重要 / Why it matters】
该项目展示了低成本微控制器如何实现物理世界与数字界面的交互，为自动化测试、无障碍辅助技术等领域提供了启发；同时体现了创客社区将经典 Easter egg 游戏转化为硬件挑战的创意趋势，以及 USB HID 协议在跨平台设备控制中的实用性。

This project demonstrates how low-cost microcontrollers can bridge physical hardware with digital interfaces, offering insights for automated testing and accessibility tools. It also reflects the maker community's trend of turning classic Easter eggs into hardware challenges, while showcasing the versatility of USB HID for cross-platform device control.

【我能用什么 / How I can use it】
可以借鉴其光电传感方案为其他需要屏幕状态检测的自动化场景（如游戏挂机、UI 测试）提供低成本实现思路；学习 USB HID 设备模拟技术应用于键盘/鼠标自动化或自定义控制器开发；或将其核心逻辑迁移到更强大的平台（如 ESP32-CAM）实现基于计算机视觉的升级版方案。

You can adapt its photoelectric sensing approach for other automation scenarios requiring screen state detection (game botting, UI testing). Study the USB HID emulation technique for keyboard/mouse automation or custom controller development. Alternatively, port the core logic to more capable platforms like ESP32-CAM for a computer vision-based upgrade.
