---
title: "ESP32: When Is A P4 A P4, But Not The P4 You Thought It Was"
source: "Hackaday"
url: "https://hackaday.com/2026/03/21/esp32-when-is-a-p4-a-p4-but-not-the-p4-you-thought-it-was/"
published: "2026-03-21"
summarized: "2026-03-22T07:02:32.433529"
ai_provider: "openai"
---

【是什么 / What it is】
Espressif 发布了 ESP32-P4 应用处理器的新修订版本，该版本在硬件（一个引脚从 NC 改为电源轨，需要额外无源元件）和软件（需单独编译固件）上均有变更，但却沿用相同的型号名称和部分 SKU 销售。Espressif has released a new revision of the ESP32-P4 application processor with changes in both hardware (one pin changed from NC to power rail, extra passives required) and software (firmware must be compiled separately), yet it is being sold under the same part number and some of the same SKUs.

【为什么重要 / Why it matters】
这种"隐形"修订导致供应链混乱：设计师无法确定库存芯片版本，已设计的旧版 PCB 可能与新芯片不兼容且难以返工，远程工厂组装时固件版本选择也成为难题。This "silent" revision causes supply chain confusion: designers cannot verify which revision is in stock, existing PCB designs for the old revision may be incompatible with new chips and difficult to rework, and firmware selection becomes problematic for boards assembled at remote factories.

【我能用什么 / How I can use it】
若正在使用 P4，应确保 PCB 设计针对最新修订版，向供应商明确确认芯片版本，并考虑在 BOM 中区分两个修订版的 SKU；对于新项目，建议优先采用新修订版设计以避免兼容性问题。If working with the P4, ensure your board design targets the latest revision, explicitly ask suppliers to verify which chips you will receive, and consider distinguishing SKUs for both revisions in your BOM; for new projects, prioritize designing for the new revision to avoid compatibility issues.
