---
title: "Build This Open-Source Graphics Calculator"
source: "Hackaday"
url: "https://hackaday.com/2026/03/23/build-this-open-source-graphics-calculator/"
published: "2026-03-23"
summarized: "2026-03-24T07:11:58.396784"
ai_provider: "openai"
---

【是什么 / What it is】
NumOS 是一个开源的图形计算器系统，基于 ESP32-S3 微控制器和 ILI9341 屏幕开发，旨在对标卡西欧 fx-991EX ClassWiz 和德州仪器 TI-84 Plus CE 等主流科学图形计算器。它内置完整的计算机代数系统和自定义数学引擎，支持符号微积分运算，并采用类似 Casio Natural V.P.A.M 的直观显示方式，将分数、积分等数学表达式以手写形式呈现。

NumOS is an open-source scientific and graphing calculator system built on the ESP32-S3 microcontroller with an ILI9341 screen, designed to rival mainstream calculators like the Casio fx-991EX ClassWiz and TI-84 Plus CE. It features a full computer algebra system, a custom math engine for symbolic calculus operations, and a Natural V.P.A.M-like display that renders mathematical expressions such as fractions and integrals in intuitive handwritten-style notation.

---

【为什么重要 / Why it matters】
图形计算器市场长期被少数厂商垄断，产品技术陈旧却定价高昂（通常超过 100 美元），NumOS 为这一"技术死胡同"提供了打破垄断的替代方案。作为完全开源的项目，它赋予用户从底层硬件到软件逻辑的完全掌控权，推动了教育工具的去中心化和可定制化发展，同时也为嵌入式系统与数学计算引擎的融合提供了实践范例。

The graphing calculator market has long been dominated by a few manufacturers with outdated yet overpriced products (typically over $100), and NumOS offers an alternative that breaks this monopoly. As a fully open-source project, it gives users complete control from底层 hardware to software logic, promoting decentralization and customization of educational tools while also serving as a practical example of integrating embedded systems with mathematical computation engines.

---

【我能用什么 / How I can use it】
硬件爱好者可基于公开的 ESP32-S3 + ILI9341 方案自行组装，成本远低于市售产品，同时可根据需求扩展功能或修改界面；开发者可深入研究其自定义数学引擎和计算机代数系统的实现，将其算法移植到其他嵌入式项目或学习符号计算的原理。需注意该设备目前无法用于标准化考试，更适合作为日常学习、编程实践或研究开源 CAS 系统的工具。

Hardware enthusiasts can assemble their own device based on the documented ESP32-S3 + ILI9341 setup at a fraction of commercial costs, with freedom to extend features or customize interfaces; developers can study its custom math engine and CAS implementation to port algorithms to other embedded projects or learn symbolic computation principles. Note that this device is currently not permitted in standardized exams, making it best suited for everyday learning, programming practice, or researching open-source CAS systems.
