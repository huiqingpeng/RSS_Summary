---
title: "Conway’s Game of Life With Physical Buttons"
source: "Hackaday"
url: "https://hackaday.com/2026/03/20/conways-game-of-life-with-physical-buttons/"
published: "2026-03-20"
summarized: "2026-03-21T08:08:25.258830"
ai_provider: "openai"
---

【是什么 / What it is】
这是一篇关于硬件爱好者 Michal Zalewski 将康威生命游戏（Conway's Game of Life）实体化的项目报道。他用 289 个带 LED 的物理按键（NKK JB15LPF-JF）搭建了一个 17×17 的矩阵，配合定制 PCB 和 AVR 微控制器，让经典的细胞自动机从屏幕走进了可触摸的实体世界。

This article reports on hardware enthusiast Michal Zalewski's physical implementation of Conway's Game of Life. He built a 17×17 matrix using 289 LED-equipped tactile buttons (NKK JB15LPF-JF), paired with a custom PCB and an AVR microcontroller, bringing the classic cellular automaton from the digital screen into a tangible, touchable physical form.

---

【为什么重要 / Why it matters】
这个项目展示了"实体化数字体验"的独特魅力——将抽象算法转化为可交互的物理装置，创造出屏幕无法替代的视觉和触觉反馈。同时它也反映了创客文化中"不计成本追求完美"的精神，即使单个按键成本超过 3 美元，作者仍坚持实现心中所想，最终成果兼具技术深度与美学价值。

This project demonstrates the unique appeal of "tangible digital experiences"—transforming abstract algorithms into interactive physical devices that create visual and tactile feedback impossible to replicate on screens. It also reflects the maker culture spirit of "sparing no expense for perfection"; despite buttons costing over $3 each, the creator persisted in realizing his vision, resulting in a piece that combines technical depth with aesthetic value.

---

【我能用什么 / How I can use it】
可以借鉴其"扫描矩阵+占空比驱动"的硬件方案，用更经济的元件（如普通机械键盘轴体+WS2812 LED）复刻类似项目；也可将生命游戏的演化逻辑应用到交互艺术装置或教育展示中，帮助观众直观理解涌现现象和复杂系统。此外，项目开源的固件和 PCB 文件为学习矩阵扫描、消抖处理和 PWM 调光提供了实用参考。

One can adapt its "scanning matrix + duty cycle driving" hardware approach using more economical components (e.g., mechanical keyboard switches with WS2812 LEDs) to recreate similar projects. The emergent logic of Life can also be applied to interactive art installations or educational exhibits, helping audiences intuitively grasp emergence phenomena and complex systems. Additionally, the project's open-source firmware and PCB files provide practical references for learning matrix scanning, debouncing, and PWM dimming techniques.
