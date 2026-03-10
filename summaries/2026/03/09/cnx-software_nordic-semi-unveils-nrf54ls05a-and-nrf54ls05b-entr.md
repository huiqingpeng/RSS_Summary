---
title: "Nordic Semi unveils nRF54LS05A and nRF54LS05B entry-level, ultra-low-power Bluetooth LE SoCs"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/09/nordic-semi-nrf54ls05a-nrf54ls05b-entry-level-ultra-low-power-bluetooth-le-socs/"
published: "2026-03-09"
summarized: "2026-03-10T10:41:34.053309"
ai_provider: "openai"
---

【是什么 / What it is】

Nordic Semiconductor 推出了两款入门级超低功耗蓝牙 LE SoC——nRF54LS05A 和 nRF54LS05B，基于 128 MHz Arm Cortex-M33 内核，配备第四代蓝牙 LE 射频和 0.5 MB 非易失性存储器，主要区别在于 RAM 容量（64 KB vs 96 KB）。这两款芯片面向简单物联网应用（传感器、标签、信标、遥控器、PC 外设）或作为高级产品的蓝牙 LE 配套设备，预计 2026 年第三季度量产。

Nordic Semiconductor has launched two entry-level ultra-low-power Bluetooth LE SoCs—the nRF54LS05A and nRF54LS05B—featuring 128 MHz Arm Cortex-M33 cores, 4th-gen Bluetooth LE radio, and 0.5 MB NVM, differing only in RAM size (64 KB vs 96 KB). These chips target simple IoT applications (sensors, tags, beacons, remotes, PC peripherals) or serve as Bluetooth LE companion devices in advanced products, with mass production scheduled for Q3 2026.

---

【为什么重要 / Why it matters】

这标志着 Nordic nRF54 系列向入门级市场延伸，以更低成本、更小尺寸（6×6mm QFN48）和 pin-to-pin 兼容性提供成熟的蓝牙 LE 方案，同时保持超低功耗（睡眠模式低至 0.6 μA）。值得注意的是，该系列明确不支持蓝牙信道探测（Channel Sounding）和蓝牙 Mesh，体现了精准的市场细分策略——在功能与成本之间为简单应用找到最佳平衡点。

This marks Nordic's extension of the nRF54 series into the entry-level market, offering a mature Bluetooth LE solution with reduced cost, compact size (6×6mm QFN48), and pin-to-pin compatibility while maintaining ultra-low power consumption (sleep modes down to 0.6 μA). Significantly, the series explicitly excludes Bluetooth Channel Sounding and Bluetooth Mesh, reflecting a precise market segmentation strategy—finding the optimal balance between features and cost for simple applications.

---

【我能用什么 / How I can use it】

若正在开发电池供电的简单无线传感器或信标，可将此芯片作为 nRF52 系列的平滑升级路径，利用 nRF Connect SDK 和 nRF54LS05-DK 开发板提前评估；若需要蓝牙信道探测（用于高精度测距）或 Mesh 组网功能，则需转向 nRF54H 系列等高端型号。此外，可借助其 96 KB RAM 版本（nRF54LS05B）处理更复杂的边缘数据处理任务，同时利用片内 AES 加速器和防篡改检测增强安全性。

For battery-powered simple wireless sensors or beacons, use this chip as a smooth upgrade path from the nRF52 series, leveraging nRF Connect SDK and the nRF54LS05-DK dev kit for early evaluation; if Bluetooth Channel Sounding (for high-precision ranging) or Mesh networking is required, consider higher-end alternatives like the nRF54H series. Additionally, utilize the 96 KB RAM variant (nRF54LS05B) for more complex edge data processing while leveraging the on-chip AES accelerator and tamper detectors for enhanced security.
