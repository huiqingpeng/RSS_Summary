---
title: "Making a Better Kitchen Scale out of Junk Parts"
source: "Hackaday"
url: "https://hackaday.com/2026/03/16/making-a-better-kitchen-scale-out-of-junk-parts/"
published: "2026-03-16"
summarized: "2026-03-17T07:05:10.229544"
ai_provider: "openai"
---

【是什么 / What it is】

这篇文章介绍了技术爱好者 Mark Furneaux 如何利用废弃实验室天平的称重传感器（load cell）和金属底座，配合一个 HX710 应变片放大器模块，DIY 制作了一台高精度、实时响应的厨房秤。整个项目几乎完全使用回收零件，仅花费 7 美元购买放大器模块。

This article describes how tech enthusiast Mark Furneaux built a high-precision, real-time responsive kitchen scale using a salvaged load cell and metal base from a discarded laboratory scale, paired with an HX710 strain gauge amplifier module. The entire project used almost entirely recycled parts, with only a $7 amplifier module purchased.

---

【为什么重要 / Why it matters】

市售廉价厨房秤普遍存在噪声过滤过度、响应延迟的问题，导致缓慢添加少量重量时读数不更新，严重影响使用体验。该项目展示了如何通过硬件改造和开源模块，以极低成本显著提升测量精度和实时性，同时体现了电子垃圾再利用的可持续价值。

Commercial kitchen scales commonly suffer from excessive noise filtering and delayed response, causing readings to fail to update when weight is added slowly—severely impacting usability. This project demonstrates how hardware modifications and off-the-shelf modules can dramatically improve measurement precision and real-time performance at minimal cost, while exemplifying the sustainable value of e-waste reuse.

---

【我能用什么 / How I can use it】

可以借鉴此思路改造现有厨房秤：保留其机械结构和称重传感器，替换或升级信号放大与处理电路；也可将 HX710/HX711 等模块与 Arduino 等微控制器结合，开发自定义软件实现数据记录、单位转换或物联网功能。此外，可从废旧工业设备、电子秤中回收应变片和负载传感器用于各类力测量项目。

You can apply this approach to upgrade an existing kitchen scale: retain its mechanical structure and load cell while replacing or upgrading the signal amplification and processing circuitry. Alternatively, combine HX710/HX711 modules with microcontrollers like Arduino to develop custom software for data logging, unit conversion, or IoT functionality. Additionally, salvage strain gauges and load cells from discarded industrial equipment or electronic scales for various force measurement projects.
