---
title: "AngstromIO – A tiny 9.0 x 8.9 mm ATtiny1616 board that fits on top of a USB-C connector"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/26/angstromio-a-tiny-9-0-x-8-9-mm-attiny1616-board-that-fits-on-top-of-a-usb-c-connector/"
published: "2026-03-26"
summarized: "2026-03-27T07:11:06.298480"
ai_provider: "openai"
---

【是什么 / What it is】
AngstromIO 是一款基于 Microchip ATtiny1616 微控制器的超小型开源开发板，尺寸仅为 9.0 x 8.9 毫米，几乎与边缘安装的 USB-C 连接器一样大。该板专为空间极度受限的嵌入式项目设计，集成了 RGB LED、I2C、UART 等接口，并通过 UPDI 接口进行编程。

AngstromIO is an ultra-tiny open-source development board based on Microchip's ATtiny1616 microcontroller, measuring just 9.0 x 8.9 mm—barely larger than its edge-mounted USB-C connector. Designed for highly space-constrained embedded projects, it integrates RGB LEDs, I2C, UART interfaces, and uses UPDI for programming.

---

【为什么重要 / Why it matters】
随着物联网和可穿戴设备的普及，微型化开发板的需求日益增长，AngstromIO 展示了在极小空间内实现完整 MCU 功能的工程可能性。其开源特性和 Arduino IDE 兼容性降低了开发门槛，而配套的 CH340 双路编程器设计解决了 UPDI 编程与串口调试同时进行的痛点。

As IoT and wearable devices proliferate, demand for miniaturized development boards grows, and AngstromIO demonstrates engineering feasibility of complete MCU functionality in minimal space. Its open-source nature and Arduino IDE compatibility lower development barriers, while the accompanying dual CH340 programmer design addresses the pain point of simultaneous UPDI programming and serial debugging.

---

【我能用什么 / How I can use it】
可用于空间受限的智能穿戴、微型传感器节点或隐藏式 LED 控制项目，直接利用 Arduino 生态中的 Wire 和 tinyNeoPixel 库快速开发。建议搭配开发者提供的开源编程器硬件，实现"烧录+调试"一体化工作流程；也可参考其 KiCad 设计文件学习高密度 PCB 布局技巧。

Ideal for space-constrained smart wearables, tiny sensor nodes, or hidden LED control projects, leveraging Arduino ecosystem libraries like Wire and tinyNeoPixel for rapid development. Recommended to pair with the developer's open-source programmer hardware for integrated "flash+debug" workflow; also valuable to study its KiCad design files for high-density PCB layout techniques.
