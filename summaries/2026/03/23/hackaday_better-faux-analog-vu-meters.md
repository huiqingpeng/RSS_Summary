---
title: "Better Faux-Analog VU Meters"
source: "Hackaday"
url: "https://hackaday.com/2026/03/23/better-faux-analog-vu-meters/"
published: "2026-03-23"
summarized: "2026-03-24T07:12:50.652131"
ai_provider: "openai"
---

【是什么 / What it is】
这篇文章介绍了[mircemk]如何使用ESP32微控制器和GC9A01圆形显示屏，通过LVGL图形库和Squarelinestudio UI编辑器，开发出视觉效果更逼真的模拟复古VU（音量单位）电平表。这是对之前使用Adafruit GFX库制作的锯齿状、数字感较强的版本的重大改进。

This article describes how [mircemk] used an ESP32 microcontroller and GC9A01 round display with the LVGL graphics library and Squarelinestudio UI editor to develop visually more realistic simulated vintage VU (Volume Unit) meters. This represents a significant improvement over an earlier version that used the Adafruit GFX library and produced jerky, jagged, digitally-looking results.

---

【为什么重要 / Why it matters】
这个项目展示了合适的软件工具选择（LVGL vs. Adafruit GFX）如何显著提升嵌入式设备的视觉表现力，使数字模拟更接近真实模拟设备的质感。它为复古美学与现代数字技术的融合提供了实用范例，也反映了DIY电子爱好者社区持续迭代优化项目的文化。

This project demonstrates how choosing the right software tools (LVGL vs. Adafruit GFX) can dramatically enhance the visual quality of embedded devices, bringing digital simulations closer to the feel of real analog hardware. It provides a practical example of blending retro aesthetics with modern digital technology, and reflects the culture of iterative improvement within the DIY electronics community.

---

【我能用什么 / How I can use it】
如果你需要为嵌入式项目创建逼真的仪表盘、仪表或复古风格界面，可以尝试使用LVGL库替代基础的图形库，配合Squarelinestudio等UI编辑器加速开发。该技术可应用于音频设备、智能家居控制面板、汽车改装仪表或任何需要拟物化视觉反馈的交互场景。

If you need to create realistic gauges, meters, or retro-style interfaces for embedded projects, consider using the LVGL library instead of basic graphics libraries, paired with UI editors like Squarelinestudio to accelerate development. This technique can be applied to audio equipment, smart home control panels, car customization dashboards, or any interactive scenario requiring skeuomorphic visual feedback.
