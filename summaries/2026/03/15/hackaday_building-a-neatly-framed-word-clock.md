---
title: "Building a Neatly Framed Word Clock"
source: "Hackaday"
url: "https://hackaday.com/2026/03/14/building-a-neatly-framed-word-clock/"
published: "2026-03-15"
summarized: "2026-03-16T07:02:23.824955"
ai_provider: "openai"
---

【是什么 / What it is】
这是一篇关于DIY电子项目的文章，介绍了一位创客[povey_tech]如何自制一款"文字时钟"（word clock）——一种用英文单词而非数字来显示时间的时钟。该项目基于ESP32微控制器，配合DS1307实时时钟模块、环境光传感器和WS2812可寻址LED，通过激光切割的亚克力字母面板和橡木相框呈现。

This article describes a DIY electronics project where a maker [povey_tech] built a "word clock" — a timepiece that displays time using English words instead of numbers. The project is built around an ESP32 microcontroller, paired with a DS1307 real-time clock module, ambient light sensor, and WS2812 addressable LEDs, presented through laser-cut acrylic letter panels in an oak picture frame.

【为什么重要 / Why it matters】
这个项目展示了开源硬件和可寻址LED技术如何大幅降低创意时钟的制作门槛，让个人爱好者能以远低于商业产品的成本实现专业级效果。它也体现了创客文化中"看到喜欢的东西但嫌贵，就自己做一个"的典型精神，同时为未来智能家居集成（如Home Assistant）预留了扩展空间。

This project demonstrates how open-source hardware and addressable LED technology have dramatically lowered the barrier to creating artistic clocks, enabling hobbyists to achieve professional results at a fraction of commercial costs. It embodies the maker culture spirit of "see something you like but too expensive, build your own," while leaving room for future smart home integration like Home Assistant.

【我能用什么 / How I can use it】
可以参考这个项目的硬件组合（ESP32+DS1307+WS2812+VEML7700）作为自己LED显示项目的模板，学习如何通过内置网页服务器实现设备配置界面。也可以将激光切割亚克力+相框的封装思路应用到其他信息显示项目中，或为其添加MQTT/Home Assistant支持来实现智能家居联动。

You can reference this project's hardware stack (ESP32+DS1307+WS2812+VEML7700) as a template for your own LED display projects, and learn how to implement device configuration via built-in web server. The laser-cut acrylic + picture frame packaging approach can be adapted to other information displays, or you could add MQTT/Home Assistant support to enable smart home automation.
