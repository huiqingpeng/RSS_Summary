---
title: "SparkFun OpenScale IoT – An ESP32 board with HX711 ADC for smart scales with WiFi and Bluetooth connectivity"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/16/sparkfun-openscale-iot-an-esp32-board-with-hx711-adc-for-smart-scales-with-wifi-and-bluetooth-connectivity/"
published: "2026-03-16"
summarized: "2026-03-17T07:02:49.563248"
ai_provider: "openai"
---

【是什么 / What it is】

SparkFun OpenScale IoT 是一款基于 ESP32 的开源物联网智能秤开发板，集成 HX711 24位模数转换器，可直接读取称重传感器的精确重量数据，无需从零编写代码即可实现基础功能。它支持 WiFi 和蓝牙无线连接、温度补偿、OTA 固件更新，并提供 Qwiic I²C 扩展接口，适用于工业环境的长期重量监测场景。

The SparkFun OpenScale IoT is a ready-to-use ESP32-based IoT smart scale development board featuring an integrated HX711 24-bit ADC for precise load cell readings without custom coding for basic operation. It supports WiFi and Bluetooth connectivity, temperature compensation, OTA firmware updates, and a Qwiic I²C expansion port, designed primarily for industrial long-term weight monitoring applications.

---

【为什么重要 / Why it matters】

该开发板降低了高精度称重物联网应用的开发门槛，将原本需要复杂配置的硬件集成、无线连接和校准流程简化为即插即用方案，加速原型开发和部署。其开源硬件/固件特性与工业级功能（温度补偿、可调增益、双数据速率）的结合，使其在智能农业、仓储物流、健康监测等领域具有广泛适用性，同时 44.95 美元的定价为中小企业提供了高性价比的工业物联网解决方案。

This board significantly lowers the barrier to entry for high-precision weighing IoT applications by simplifying complex hardware integration, wireless connectivity, and calibration into a plug-and-play solution, accelerating prototyping and deployment. The combination of open-source hardware/firmware with industrial-grade features (temperature compensation, adjustable gain, dual data rates) makes it applicable across smart agriculture, warehouse logistics, and health monitoring, while its $44.95 price point offers a cost-effective industrial IoT solution for small and medium enterprises.

---

【我能用什么 / How I can use it】

可直接用于构建远程库存监控系统（通过 WiFi 实时传输重量数据到浏览器）、自动化农业饲喂站（结合 Qwiic 扩展环境传感器）或实验室长期实验数据采集（利用 10/80 SPS 可选采样率和温度补偿确保稳定性）。进阶应用可参考开源 KiCad 文件和 Arduino 固件进行二次开发，或对比 TTGO T-Weigh 等竞品方案根据 LoRaWAN 需求灵活选型。

Use it directly to build remote inventory monitoring systems (streaming weight data to browsers via WiFi), automated agricultural feeding stations (adding environmental sensors via Qwiic expansion), or long-term laboratory data acquisition (leveraging 10/80 SPS selectable sampling rates and temperature compensation for stability). For advanced applications, modify the open-source KiCad files and Arduino firmware for customization, or compare with alternatives like the TTGO T-Weigh to select LoRaWAN connectivity if needed.
