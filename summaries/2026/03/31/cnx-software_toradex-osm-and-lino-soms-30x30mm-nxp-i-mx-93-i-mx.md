---
title: "Toradex OSM and Lino SoMs – 30×30mm NXP i.MX 93/i.MX 91 modules with solder-down or B2B connector designs"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/31/toradex-osm-and-lino-soms-30x30mm-nxp-i-mx-93-i-mx-91-modules-with-solder-down-or-b2b-connector-designs/"
published: "2026-03-31"
summarized: "2026-04-01T07:00:33.106306"
ai_provider: "openai"
---

【是什么 / What it is】

Toradex 推出了两款基于 NXP i.MX 91/i.MX 93 处理器的超紧凑型（30×30mm）系统级模块（SoM）系列：OSM 和 Lino。OSM 系列遵循 OSM Size-S 标准，采用 332 球焊盘网格直接焊接至载板；Lino 则为专有格式，保留相同尺寸但使用板对板（B2B）连接器，便于更换和升级。

Toradex has launched two ultra-compact (30×30mm) SoM families based on NXP i.MX 91/i.MX 93 processors: OSM and Lino. The OSM series complies with the OSM Size-S standard with a 332-ball LGA grid for solder-down mounting, while Lino uses a proprietary format with board-to-board (B2B) connectors for easier replacement and upgrades.

---

【为什么重要 / Why it matters】

这两款模块面向边缘工业和物联网应用，i.MX 93 版本配备双核 Cortex-A55、Arm Ethos-U65 NPU（0.5 TOPS）和 EdgeLock 安全区，兼顾 AI 推理能力与工业级可靠性（-40°C 至 +85°C）。OSM 标准焊盘设计与 Lino 可插拔方案的差异化选择，为开发者提供了成本优化与维护灵活性之间的权衡空间。

These modules target edge industrial and IoT applications, with the i.MX 93 variant featuring dual-core Cortex-A55, Arm Ethos-U65 NPU (0.5 TOPS), and EdgeLock secure enclave—balancing AI inference capability with industrial-grade reliability (-40°C to +85°C). The choice between OSM's solder-down standard and Lino's pluggable design offers developers a trade-off between cost optimization and maintenance flexibility.

---

【我能用什么 / How I can use it】

若项目追求长期稳定性与最低 BOM 成本，可选择 OSM 焊盘模块（起价 $25.55）；若需现场可更换或预期硬件迭代，Lino B2B 方案（起价 $30.65）更合适。两者均支持 Torizon Linux 和 Yocto，也可按需启用 Zephyr、FreeRTOS 或 Android，建议通过评估套件（含 10.1 英寸触屏和 5MP 摄像头选项）快速验证软件栈后再定制载板。

Choose OSM solder-down modules (from $25.55) for long-term stability and lowest BOM cost, or Lino B2B (from $30.65) if field replaceability or hardware iteration is anticipated. Both support Torizon Linux and Yocto, with Zephyr, FreeRTOS, or Android available on request—evaluate via dev kits (with optional 10.1" touchscreen and 5MP camera) before committing to custom carrier board designs.
