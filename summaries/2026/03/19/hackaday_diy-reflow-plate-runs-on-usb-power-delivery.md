---
title: "DIY Reflow Plate Runs On USB Power Delivery"
source: "Hackaday"
url: "https://hackaday.com/2026/03/18/diy-reflow-plate-runs-on-usb-power-delivery/"
published: "2026-03-19"
summarized: "2026-03-19T11:03:09.106400"
ai_provider: "openai"
---

【是什么 / What it is】
这是一篇介绍DIY回流焊加热板的文章，由[Vitaly]设计制作。该设备采用USB-C供电，专为小型表面贴装元件焊接设计，工作区域为80mm x 70mm，配备ESP32-C3-WROOM微控制器通过蓝牙提供网页控制面板。

This article introduces a DIY reflow heating plate designed by [Vitaly]. The device is USB-C powered, specifically designed for small surface-mount component soldering with an 80mm x 70mm working area, featuring an ESP32-C3-WROOM microcontroller that provides a web-based control panel via Bluetooth.

【为什么重要 / Why it matters】
传统回流焊设备通常体积大、价格高且需要专用电源，而这款开源设计降低了电子爱好者和小批量生产者的入门门槛。USB PD供电方案使其便携性大幅提升，蓝牙控制无需网络配置，特别适合移动场景和快速原型制作。

Traditional reflow equipment is typically bulky, expensive, and requires dedicated power supplies, while this open-source design lowers the barrier to entry for hobbyists and small-batch producers. The USB PD power solution significantly improves portability, and Bluetooth control eliminates network configuration needs, making it ideal for mobile scenarios and rapid prototyping.

【我能用什么 / How I can use it】
可从GitHub获取设计文件复刻该设备，搭配支持100W USB PD的充电器使用；根据焊锡膏类型选择金属芯PCB加热器（低温Sn42Bi58）或金属陶瓷加热器（高温Sn63Pb37）。可延伸应用于小型PCB批量焊接、现场维修或作为教学演示工具。

You can replicate this device by obtaining design files from GitHub, paired with a 100W USB PD compatible charger; select either the metal core PCB heater (for low-temp Sn42Bi58) or metal ceramic heater (for high-temp Sn63Pb37) based on your solder paste type. It can be extended to small-batch PCB soldering, field repairs, or as an educational demonstration tool.
