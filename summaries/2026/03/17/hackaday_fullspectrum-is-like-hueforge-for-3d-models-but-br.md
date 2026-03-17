---
title: "FullSpectrum is Like HueForge for 3D Models, but Bring Your Toolchanger"
source: "Hackaday"
url: "https://hackaday.com/2026/03/17/fullspectrum-is-like-hueforge-for-3d-models-but-bring-your-toolchanger/"
published: "2026-03-17"
summarized: "2026-03-18T07:03:49.430049"
ai_provider: "openai"
---

【是什么 / What it is】
FullSpectrum 是 OrcaSlicer 的一个分支版本，专为换刀式 3D 打印机设计，通过堆叠薄层半透明耗材实现类似 HueForge 的混色效果，从而用有限的原色（如红、蓝、黄）生成更丰富的色彩 palette。它目前主要面向 Snapmaker U1 等四头换刀打印机开发。

FullSpectrum is a fork of OrcaSlicer designed for tool-changing 3D printers that achieves HueForge-like color mixing by stacking thin layers of semi-translucent filament, generating expanded color palettes from limited primaries (e.g., red, blue, yellow). It is currently being developed primarily for four-head tool-changing printers like the Snapmaker U1.

【为什么重要 / Why it matters】
这项技术可能成为推动换刀式打印机普及的"杀手级应用"——相比传统多材料单元（MMU），换刀结构在混色打印上速度优势显著（案例中从 19 小时缩短至 7 小时）。同时，它延续了开源切片软件的 fork 创新链，展示了开放生态如何持续催生新技术。

This could become the "killer app" that popularizes tool-changing printers—offering dramatic speed advantages over traditional MMUs (19 hours reduced to 7 hours in one demo). It also exemplifies how the open-source forking ecosystem continues to drive innovation in 3D printing software.

【我能用什么 / How I can use it】
若拥有换刀式打印机，可尝试 FullSpectrum 进行 0.08-0.12mm 薄层高混色打印，优先选用半透明耗材并参考 HueForge 社区的透光率参数；若无硬件，可关注该工具对耗材透光特性的表征方法，或将此层叠混色思路迁移到其他需要低成本广色域输出的制造场景。

If you own a tool-changing printer, try FullSpectrum with 0.08-0.12mm layer heights using semi-translucent filaments, leveraging HueForge community knowledge on translucency characterization. Without hardware, you can study its material characterization methods or adapt the layer-stacking color-mixing approach to other low-cost wide-gamut manufacturing applications.
