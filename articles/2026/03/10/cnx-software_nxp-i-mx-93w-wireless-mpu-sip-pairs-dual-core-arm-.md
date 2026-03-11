---
title: "NXP i.MX 93W wireless MPU SiP pairs dual-core Arm Cortex-A55 processor with NXP iW610 WiFi 6, Bluetooth LE, and 805.15.4 radio"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/10/nxp-i-mx-93w-wireless-mpu-sip-pairs-dual-core-arm-cortex-a55-processor-with-nxp-iw610-wifi-6-bluetooth-le-and-805-15-4-radio/"
published: "2026-03-10"
fetched: "2026-03-11T09:01:14.383683"
---

NXP i.MX 93W is the company’s first integrated wireless MPU System-in-Package (SiP) and combines a dual-core Cortex-A55 processor (NXP i.MX 93) with an iW610 WiFi 6, Bluetooth LE, and 802.15.4 tri-radio into a single chip.
The 14.2 x 12 mm package also includes all the external radio components needed for wireless connectivity, replacing up to 60 discrete components on the PCB. NXP says it reduces the PCB area, simplifies PCB design and regulatory approval, and speeds up time-to-market.
NXP i.MX 93W specifications:
- CPU
- Dual-Core Arm Cortex-A55 at up to 1.7 GHz
- Arm Cortex-M33 core at 250 MHz for real-time control
- GPU – 2D graphics accelerator
- AI accelerator – Arm Ethos-U65 microNPU
- Memory I/F – Up to 3.7GT/s 16-bit LPDDR4/LPDDR4X with inline ECC
- Storage I/F – 2x SD 3.0/SDIO 3.0/eMMC 5.1
- Display Interfaces
- MIPI DSI up to 1080p60
- LVDS up to 720p60
- 24-bit parallel RGB
- Camera Interface – 2-lane MIPI CSI up to 1080p60
- Audio
- 7x I2S/TDM 32-bit @ 768KHz, SPDIF Tx/Rx
- 8-channel PDM microphone input
- Medium Quality Sound output (sigma-delta modulator)
- Networking
- 2x Gigabit Ethernet with audio/video bridging (AVB), IEEE 1588 for sync, and energy-efficient Ethernet for low power; 1x with time-sensitive networking (TSN)
- Wireless via integrated IW610G tri-radio
- WiFi 6
- 1×1 dual band 2.4 GHz/5 GHz 802.11 a/b/g/n/ax
- 256 quadrature amplitude modulation (QAM), 20 MHz bandwidth, peak throughput: 114.7 Mbps
- Tx power up to +21 dBm
- Wi-Fi 6 Extended Range (ER), Dual Carrier Modulation (DCM), Target Wait Time (TWT)
- Low-power Wi-Fi idle, standby, and sleep modes
- WPA2 / WPA3 Enterprise security
- Support for Matter over Wi-Fi
- Single, dual antenna with diversity
- Bluetooth LE Connectivity
- High-speed 2 Mbps, long range, advertising extensions
- Integrated power amplifier (PA), low noise amplifier (LNA); Switch with up to +15 dBm TX output
- Switchable Bluetooth LE/802.15.4 operation
- UART or USB interface
- 802.15.4
- IEEE 802.15.4-2015 compliant media access control (MAC)
- Zigbee and Matter over Thread in the 2.4 GHz band
- SPI Host Interface
- WiFi 6
- USB – 2x USB 2.0 interfaces with PHY
- Other peripheral interfaces
- 7x UART, 8x I2C, 7x SPI, 2x I3C
- 1x CAN FD
- 4-ch, 12-bit analog‑to‑digital converter (ADC)
- 2x 32-pin FlexIO interfaces (camera, bus, or serial I/O)
- Security – EdgeLock secure enclave
- Dimensions – 14.2 x 12 mm package (FCCSP), 0.5 mm pitch, with an antenna pin
- Temperature Range – -40°C Ta to 105°C
NXP mentions support for Linux OS and FreeRTOS. That should be Linux on the Cortex-A55 cores, and FreeRTOS on the Cortex-M33 core. Since the i.MX 93W wireless MCU SiP mainly combines an NXP i.MX 93 with an NXP iW610 and some passive components, software support should be exactly the same as for designs using two chips. Some target applications include smart home hubs, medical sensors, and energy grid devices.
We don’t often see application processors with built-in wireless connectivity, and the only other chip I can think of right now is the Allwinner V821 with a 32-bit RISC-V core, 64MB on-chip DDR2, and 2.4 GHz WiFi 4 designed for cameras. Looking further down in time, the Snapdragon 410E (IPQ8016E) quad-core Cortex-A53 SoC was introduced with built-in WiFi and Bluetooth in 2016.
NXP unveiled the i.MX 93W wireless SiP at Embedded World 2026, but most people won’t be able to integrate them into their designs right away, since we’re told the “next generation MPU” is “coming in early 2027“. A few additional details may be found on the product page.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
