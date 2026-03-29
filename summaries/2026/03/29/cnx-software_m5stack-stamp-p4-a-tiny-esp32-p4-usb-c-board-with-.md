---
title: "M5Stack Stamp-P4 – A tiny ESP32-P4 USB-C board with optional Wi-Fi 6 and Bluetooth 5.4"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/29/m5stack-stamp-p4-a-tiny-esp32-p4-usb-c-board-with-optional-wi-fi-6-and-bluetooth-5-4/"
published: "2026-03-29"
summarized: "2026-03-30T07:04:29.792755"
ai_provider: "openai"
---

【是什么 / What it is】

M5Stack Stamp-P4 是一款基于 ESP32-P4 高性能 RISC-V 微控制器的超小型 USB-C 开发板，尺寸仅 29.8×22.0×4.3mm，配备 16MB Flash 和 32MB PSRAM，支持 MIPI-CSI 摄像头、MIPI-DSI 显示接口、RMII 以太网和 44 个 GPIO，并可通过可选的 Stamp-AddOn C6 模块扩展 Wi-Fi 6 和蓝牙 5.4 功能。

The M5Stack Stamp-P4 is an ultra-compact USB-C development board (29.8×22.0×4.3mm) powered by the ESP32-P4 high-performance RISC-V MCU, featuring 16MB Flash, 32MB PSRAM, MIPI-CSI camera, MIPI-DSI display, RMII Ethernet, 44 GPIOs, and optional Wi-Fi 6/Bluetooth 5.4 via the Stamp-AddOn C6 module.

---

【为什么重要 / Why it matters】

这是目前市面上最小巧的完整功能 ESP32-P4 开发板，填补了高性能边缘计算与极小尺寸硬件之间的空白，特别适合空间受限的 AIoT 设备、智能安防网关和工业控制节点。其模块化无线扩展设计（SDIO 3.0 接口）也为开发者提供了灵活的连接方案，避免了为不需要无线功能的场景支付额外成本。

This represents the most compact fully-functional ESP32-P4 development board available, bridging the gap between high-performance edge computing and ultra-small form factors—ideal for space-constrained AIoT devices, smart security gateways, and industrial control nodes. Its modular wireless expansion design (via SDIO 3.0) offers developers flexibility and cost optimization by avoiding unnecessary wireless costs for wired-only applications.

---

【我能用什么 / How I can use it】

可用于开发带本地 AI 推理的摄像头项目（利用 P4 的 AI 指令集和 MIPI-CSI 接口）、构建低功耗电池供电设备（深度睡眠仅 ~360μA），或作为 Matter/Zigbee 智能家居网关核心（配合 C6 扩展模块）。建议优先评估 UiFlow2 可视化编程快速验证原型，再迁移至 ESP-IDF 进行生产级开发。

Ideal for camera projects with on-device AI inference (leveraging P4's AI instruction set and MIPI-CSI), low-power battery-operated devices (deep sleep at ~360μA), or Matter/Zigbee smart home hub applications (with C6 add-on). Recommended workflow: rapid prototyping with UiFlow2 visual programming, then migrate to ESP-IDF for production-grade development.
