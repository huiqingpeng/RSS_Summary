---
title: "Building an LC Meter with a Franklin Oscillator"
source: "Hackaday"
url: "https://hackaday.com/2026/03/18/building-an-lc-meter-with-a-franklin-oscillator/"
published: "2026-03-18"
summarized: "2026-03-18T16:03:29.488162"
ai_provider: "openai"
---

【是什么 / What it is】

本文介绍了一种基于富兰克林振荡器（Franklin oscillator）的LC测量仪设计方案。该电路源自1920年代马可尼公司，以其高频稳定性著称，现被爱好者[nobcha]用于构建精密电感电容测量仪。核心原理是利用Arduino测量LC谐振电路在添加未知元件前后的频率变化，从而计算出元件值。

This article describes a design for an LC meter based on the Franklin oscillator, a circuit originating from the Marconi Company in the 1920s and valued for its high-frequency stability. Hobbyist [nobcha] utilized this oscillator to build a precise inductance-capacitance meter, using an Arduino to measure frequency changes in the resonant LC circuit before and after adding an unknown component to calculate its value.

---

【为什么重要 / Why it matters】

富兰克林振荡器虽历史悠久却相对冷门，本文展示了经典模拟电路与现代数字测量技术的有效结合。该方案通过测量频率差而非绝对值，有效抑制了寄生效应，实现了低至0.1 µH的电感测量精度，为业余无线电爱好者和电子制作者提供了高性价比的精密测量解决方案。

Despite its historical significance, the Franklin oscillator remains relatively obscure; this article demonstrates effective integration of classic analog circuitry with modern digital measurement techniques. By measuring frequency differences rather than absolute values, this approach minimizes parasitic effects and achieves precision down to 0.1 µH, offering hobbyists and makers a cost-effective solution for accurate component measurement.

---

【我能用什么 / How I can use it】

可参考此设计复刻个人LC测量仪，尤其适合需要测量小电感或高频元件的场景；可将Arduino替换为其他微控制器（如ESP32、STM32）以提升采样率或添加无线功能；也可将此频率差测量原理迁移至其他传感器设计，如构建高精度的电容式接近传感器或湿度检测装置。

You can replicate this design to build a personal LC meter, particularly suitable for measuring small inductances or high-frequency components; consider replacing the Arduino with alternative microcontrollers (ESP32, STM32) to improve sampling rates or add wireless capabilities; the frequency-difference measurement principle can also be adapted to other sensor designs, such as high-precision capacitive proximity sensors or humidity detectors.
