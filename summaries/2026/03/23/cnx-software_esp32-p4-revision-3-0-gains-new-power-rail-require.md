---
title: "ESP32-P4 revision 3.0 gains new power rail, requires new PCB design and firmware"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/23/esp32-p4-revision-3-0-gains-new-power-rail-requires-new-pcb-design-and-firmware/"
published: "2026-03-23"
summarized: "2026-03-24T07:11:24.534187"
ai_provider: "openai"
---

【是什么 / What it is】
乐鑫（Espressif）ESP32-P4 芯片的 3.0 及以上版本将原本未连接的 54 号引脚改为新的电源轨（VDD_HP_1），需要额外的无源元件支持，并强制要求更新 PCB 设计和固件。这一变更发生在 2023 年 1 月发布、2024 年 8 月推出官方开发板之后，打破了业界对芯片硬件已冻结的普遍预期。

Espressif's ESP32-P4 revision 3.0 and above converts pin 54 from NC (non-connected) to a new power rail (VDD_HP_1), requiring additional passive components and mandating new PCB designs and firmware updates. This change occurred after the chip's January 2023 announcement and August 2024 official dev board launch, defying industry expectations that the silicon hardware had been finalized.

---

【为什么重要 / Why it matters】
此次修订标志着芯片架构的重大调整，旧版本（1.0、1.1、1.3）已被官方明确不推荐用于新设计，但市场上多数供应商仍以"ESP32-P4"泛称销售，导致采购时难以辨别具体版本。修订版本号隐藏在生产代码中（3.0 为 XFXX，3.1 为 XGXX），增加了供应链管理和库存控制的复杂度，对已进入量产阶段的商业项目构成潜在风险。

This revision represents a significant architectural change, with older versions (1.0, 1.1, 1.3) officially deprecated for new designs, yet most vendors continue selling chips generically as "ESP32-P4" making version identification difficult during procurement. The revision number is embedded in manufacturing codes (XFXX for 3.0, XGXX for 3.1), adding complexity to supply chain management and inventory control, posing potential risks to commercial projects already in mass production.

---

【我能用什么 / How I can use it】
开发者应在 ESP-IDF 中设置 `CONFIG_ESP32P4_REV_MIN` 重新编译固件以适配 3.x 版本，并优先采用官方更新的参考原理图进行新 PCB 设计；若需兼容旧版芯片，可利用 3.x 版 PCB 向下兼容 1.x 版 SoC 的特性降低迭代成本。采购时需主动核查生产代码确认版本，避免混用不同修订版本的芯片导致硬件不稳定或固件不兼容问题。

Developers should recompile firmware with `CONFIG_ESP32P4_REV_MIN` set in ESP-IDF to target 3.x versions, and adopt updated official reference schematics for new PCB designs; if backward compatibility is needed, leverage the fact that Rev 3.x PCBs also work with Rev 1.x SoCs to reduce iteration costs. When procuring, actively verify manufacturing codes to confirm revisions and avoid mixing different chip revisions that could cause hardware instability or firmware incompatibility.
