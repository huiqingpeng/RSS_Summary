---
title: "Ampisu is a compact pocket-sized USB lab power supply with SCPI and web control (Crowdfunding)"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/24/ampisu-compact-pocket-sized-isolated-usb-lab-power-supply-with-scpi-and-web-control/"
published: "2026-03-23"
summarized: "2026-03-24T07:00:33.766653"
ai_provider: "openai"
---

【是什么 / What it is】
Ampisu 是一款正在众筹的紧凑型口袋级 USB 实验室电源，采用 Raspberry Pi RP2040 主控，提供三路全隔离可调输出（两路 0-7.5V/500mA + 一路 3.3V/100mA），支持 WebUSB、SCPI 指令集和 Python API 控制。它通过专用变压器隔离反激转换器实现输出隔离，专为低功耗嵌入式开发、现场调试和自动化测试场景设计。

Ampisu is a crowdfunding compact pocket-sized USB lab power supply featuring a Raspberry Pi RP2040 MCU, three fully galvanically isolated adjustable outputs (two 0-7.5V/500mA channels plus one 3.3V/100mA auxiliary), and supports WebUSB, SCPI command set, and Python API control. It uses dedicated transformer-isolated flyback converters for output isolation, targeting low-power embedded development, field debugging, and automated test setups.

---

【为什么重要 / Why it matters】
相比同类 USB-PD 电源（如 PocketPD 单通道限制、BenchVolt PD 体积过大），Ampisu 在口袋尺寸内实现了真正的三通道隔离实验室电源功能，解决了地环路问题和分轨供电安全需求。其开源硬件/软件设计、免驱 Web 控制界面和自动化测试支持，降低了专业电源设备的门槛，契合嵌入式开发和硬件调试的便携化、智能化趋势。

Unlike USB-PD alternatives (PocketPD's single-channel limitation, BenchVolt PD's bulky size), Ampisu delivers true three-channel isolated lab power supply functionality in a pocket form factor, solving ground loop issues and enabling safe split-rail supply creation. Its open-source hardware/software, driver-free Web control, and automation support lower the barrier for professional power equipment, aligning with the portable and intelligent trends in embedded development and hardware debugging.

---

【我能用什么 / How I can use it】
嵌入式开发者可将其作为随身携带的调试电源，利用隔离特性安全调试敏感模拟电路或创建 ±7.5V 分轨供电；自动化测试工程师可通过 Python API 或 SCPI 指令集成到 CI/CD 流水线，实现可编程电源序列和功耗分析。此外，可关注其众筹进展并参考其开源设计（RP2040 + 隔离反激架构）用于自定义电源项目开发。

Embedded developers can use it as a portable debugging power supply, leveraging isolation to safely debug sensitive analog circuits or create ±7.5V split-rail supplies; automation test engineers can integrate it into CI/CD pipelines via Python API or SCPI commands for programmable power sequencing and power profiling. Additionally, one can follow its crowdfunding progress and reference its open-source design (RP2040 + isolated flyback architecture) for custom power supply projects.
