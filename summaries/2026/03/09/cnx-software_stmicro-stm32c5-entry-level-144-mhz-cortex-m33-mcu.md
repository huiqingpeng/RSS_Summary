---
title: "STMicro STM32C5 entry-level, 144 MHz Cortex-M33 MCU features up to 1MB flash, 256KB SRAM, Ethernet, CAN Bus"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/09/stmicro-stm32c5-entry-level-144-mhz-cortex-m33-mcu-features-up-to-1mb-flash-256kb-sram-ethernet-can-bus/"
published: "2026-03-09"
summarized: "2026-03-10T11:18:03.976597"
ai_provider: "openai"
---

【是什么 / What it is】

意法半导体（STMicroelectronics）发布了全新的 STM32C5 系列入门级微控制器，采用 40nm 工艺制造，基于 Arm Cortex-M33 内核，主频高达 144 MHz，配备 128 KB 至 1 MB 闪存和最高 256 KB SRAM，集成以太网、CAN FD、USB 等丰富外设，并达到 SESIP3 和 PSA Certified Level 3 安全认证级别。

STMicroelectronics has launched the new STM32C5 series of entry-level microcontrollers, manufactured on a 40nm process, featuring an Arm Cortex-M33 core running up to 144 MHz, with 128 KB to 1 MB flash and up to 256 KB SRAM, rich peripherals including Ethernet, CAN FD, and USB, and security certifications up to SESIP3 and PSA Certified Level 3.

---

【为什么重要 / Why it matters】

STM32C5 以 0.64 美元的起售价将 Cortex-M33 架构和安全认证带入入门级市场，打破了高性能与安全功能以往只属于高端 MCU 的格局，同时通过 STM32CubeMX2 和 HAL2 优化开发效率，为工业物联网、智能家居等成本敏感型应用提供了极具竞争力的解决方案。

With a starting price of $0.64, the STM32C5 brings Cortex-M33 architecture and security certifications to the entry-level market, breaking the pattern where high performance and security features were reserved for high-end MCUs, while optimized development tools like STM32CubeMX2 and HAL2 boost efficiency, offering a highly competitive solution for cost-sensitive applications in industrial IoT and smart home.

---

【我能用什么 / How I can use it】

开发者可优先选用 NUCLEO-C5A3ZG 开发板快速验证以太网 + 双 CAN FD 的工业网关方案，或利用 STM32C53x 的极小封装（UFQFPN20, 3×3mm）设计电池供电的传感器节点；同时可借助 HAL2 的代码体积优化特性，在 128 KB Flash 的低端型号上预留更多空间给应用层算法。

Developers can prioritize the NUCLEO-C5A3ZG board for rapid validation of industrial gateway designs with Ethernet + dual CAN FD, or utilize the STM32C53x's tiny package (UFQFPN20, 3×3mm) for battery-powered sensor nodes; meanwhile, leverage HAL2's code-size optimization to reserve more space for application-layer algorithms on low-end 128 KB Flash variants.
