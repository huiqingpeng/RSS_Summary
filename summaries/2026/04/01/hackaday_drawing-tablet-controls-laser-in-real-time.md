---
title: "Drawing Tablet Controls Laser In Real-Time"
source: "Hackaday"
url: "https://hackaday.com/2026/04/01/drawing-tablet-controls-laser-in-real-time/"
published: "2026-04-01"
summarized: "2026-04-02T07:08:10.009977"
ai_provider: "openai"
---

【是什么 / What it is】
BeamInk 是一个将 Wacom 数位板与 xTool F1 激光雕刻机实时联动的开源项目。通过 Python 脚本读取数位板的笔触事件，并将其转换为激光功率与移动控制的 G-code 指令，实现"数位板作画，激光实时雕刻"的创意效果。

BeamInk is an open-source project that connects a Wacom drawing tablet to an xTool F1 laser engraver in real time. A Python script captures pen events from the tablet and converts them into G-code commands for laser power and movement, enabling users to draw on the tablet and see instant laser engraving results.

---

【为什么重要 / Why it matters】
该项目展示了消费级硬件（数位板+激光雕刻机）通过简单软件桥接即可创造全新交互范式，降低了数字制造工具的创意门槛。其模块化设计也为 CNC、机械臂等其他运动控制设备的实时人机交互提供了可复用的技术参考。

This project demonstrates how consumer-grade hardware (drawing tablet + laser engraver) can create novel interaction paradigms through simple software bridging, lowering the creative barrier for digital fabrication tools. Its modular design also provides a reusable technical reference for real-time human-machine interaction with other motion control devices like CNC machines or robotic arms.

---

【我能用什么 / How I can use it】
可直接复用其 evdev + G-code 生成的核心逻辑，将游戏手柄、MIDI 控制器等输入设备改造为其他制造工具的实时控制器。对于教育场景，可基于此快速搭建"数字手绘→物理制造"的直观教学演示系统。

You can reuse its core logic of evdev event capture + G-code generation to repurpose game controllers, MIDI devices, or other input hardware as real-time controllers for different fabrication tools. For educational contexts, this can serve as a foundation to quickly build intuitive teaching demos that bridge "digital drawing" to "physical making."
