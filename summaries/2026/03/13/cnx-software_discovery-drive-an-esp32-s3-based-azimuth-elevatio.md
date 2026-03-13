---
title: "Discovery Drive – An ESP32-S3-based azimuth/elevation rotator for satellite dishes and SDR antennas (Crowdfunding)"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/13/discovery-drive-esp32-s3-based-azimuth-elevation-rotator-for-satellite-dishes-and-sdr-antennas/"
published: "2026-03-13"
summarized: "2026-03-14T07:01:45.434027"
ai_provider: "openai"
---

【是什么 / What it is】
KrakenRF 推出了一款名为 Discovery Drive 的低成本、全防水自动方位/俯仰（Az/El）天线旋转器，基于 ESP32-S3 控制器，专为卫星天线和 SDR 天线设计，最大可承载 5kg 载荷。与需要 3D 打印和自行采购硬件的 DIY 项目（如 SatNOGS）不同，这是一款即插即用的解决方案，用户只需将其安装到桅杆上、连接天线和电源、通过 Wi-Fi 访问 Web 界面即可开始追踪卫星。

KrakenRF has launched the Discovery Drive, a low-cost, fully weatherproof automatic azimuth/elevation (Az/El) antenna rotator based on the ESP32-S3 controller, designed for satellite dishes and SDR antennas with up to 5kg payload capacity. Unlike DIY projects like SatNOGS that require 3D printing and hardware sourcing, this is a plug-and-play solution where users simply mount it to a mast, connect the antenna and power, and access the web UI via Wi-Fi to start tracking satellites.

---

【为什么重要 / Why it matters】
Discovery Drive 填补了业余无线电和卫星追踪领域中"低成本"与"专业级"之间的空白，以 699 美元的众筹价格提供了传统数千美元商用转台才具备的功能（如自动卫星追踪、Hamlib 协议兼容、IP55 防护）。其低功耗设计（<10W）支持单根 PoE+ 线缆同时为转台和 SDR 设备供电，极大简化了户外部署的布线复杂度，使偏远地区的自动卫星地面站建设成为可能。

The Discovery Drive bridges the gap between "low-cost" and "professional-grade" in amateur radio and satellite tracking, offering features previously found only in commercial rotators costing thousands of dollars—such as automatic satellite tracking, Hamlib protocol compatibility, and IP55 weatherproofing—at a $699 crowdfunding price. Its low power consumption (<10W) enables single-cable PoE+ deployment for both the rotator and SDR equipment, dramatically simplifying outdoor installations and making automated satellite ground stations feasible in remote locations.

---

【我能用什么 / How I can use it】
对于卫星爱好者，可直接搭配 SatDump、GPredict 等软件自动接收 NOAA/METEOR 气象卫星图像；对于无线电天文爱好者，可通过 Stellarium 控制天线指向进行 21cm 氢线测绘；开发者可利用开源固件定制运动控制算法或集成新的传感器（如风速、温度）。此外，其侧轨扩展设计允许挂载 Raspberry Pi 和 RTL-SDR，可构建完全独立的边缘计算节点，适用于 LoRa 定向通信、探空仪追踪或无人机信号监测等场景。

For satellite enthusiasts, pair it with SatDump or GPredict to automatically receive NOAA/METEOR weather satellite imagery; for radio astronomy hobbyists, control antenna pointing via Stellarium for 21cm hydrogen line mapping; developers can leverage the open-source firmware to customize motion control algorithms or integrate additional sensors like wind speed and temperature. The side rail expansion design also allows mounting a Raspberry Pi and RTL-SDR to build a fully standalone edge computing node, suitable for applications like LoRa directional links, radiosonde tracking, or drone signal monitoring.
