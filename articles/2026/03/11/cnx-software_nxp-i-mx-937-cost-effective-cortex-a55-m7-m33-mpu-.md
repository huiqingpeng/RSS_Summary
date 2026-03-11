---
title: "NXP i.MX 937 cost-effective Cortex-A55/M7/M33 MPU is a drop-in replacement for NXP i.MX 95 SoC family"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/11/nxp-i-mx-937-cost-effective-cortex-a55-m7-m33-mpu-is-a-drop-in-replacement-for-nxp-i-mx-95-soc-family/"
published: "2026-03-11"
fetched: "2026-03-11T09:00:11.989690"
---

The 1 .4 GHz NXP i.MX 937 quad-core Cortex-A55 microprocessor (MPU) for HMI and Edge AI applications aims to fill the gap between entry-level NXP i.MX 93 SoCs and higher-end parts like the NXP i.MX 952 processor family, while offering pin-to-pin compatibility with the latter.
The i.MX 937 MPU also features a dedicated 667 MHz Arm Cortex -M7 for real-time workloads and a low-power Arm Cortex-M33 core for system management tasks, supports LPDDR4x or LPDDR5 memory, integrates an Arm Mali G310 3D GPU, a VPU for 1080p H.26x video encoding and decoding, and a 2 eTOPS NXP eIQ Neutron NPU for machine learning (ML) acceleration. Since it targets HMI applications, we’ll also find MIPI DSI and LVDS display interfaces, and a 4-lane MIPI CSI camera interface, plus various other I/Os.
NXP i.MX 937 specifications: (highlights in bold compared to other i.MX 93 parts)
- CPU
- Up to 4x Arm Cortex-A55 cores @ up to 1.4 GHz
- 1x Arm Cortex-M7 core @ up to 667 MHz
- 1x Arm Cortex-M33 low-power system manager core
- GPU
- Arm Mali G310 3D GPU
- 2D GPU
- VPU
- Video Decode – 1080p60 H.265/H.264
- Video Encode – 1080p60 H.264
- JPEG Encoder/Decoder
- AI accelerator – NXP eIQ Neutron NPU (2 eTOPS)
- Memory I/F – Up to 4,500 MT/s 16-bit/32-bit LPDDR5 or up to 3733 MT/s 16-bit/32-bit LPDDR4x with inline ECC
- Storage I/F
- 3x SD 3.0/SDIO3.0/eMMC 5.1
- 1x xSPI, including support for SPI NOR and SPI NAND memories
- Display I/F
- 4-lane MIPI DSI
- 1x 8-lane or 2x 4-lane LVDS up to 1080p60
- Camera I/F – 4-lane MIPI CSI with PHY
- Audio
- 17x I2S TDM (32-bit @ 768KHz)
- 8-channel PDM microphone input
- MQS: Medium Quality Sound output (sigma-delta modulator)
- Networking – 2x Gigabit Ethernet: TSN, AVB & IEEE 1588 for sync, EEE for low power
- USB – 2x USB 2.0 with integrated PHY
- Serial
- 2x CAN-FD
- 8x UART/USART
- Other peripherals
- 8x I2C, 8x SPI
- 8-ch, 12-bit ADC
- 2x 32-pin FlexIO interfaces (bus or serial I/O)
- 1x PCIe Gen3 x1
- Security
- EdgeLock Secure Enclave (Advanced Profile)
- EdgeLock Prime Accelerator
- Post‑quantum cryptography (PQC)
- Packaging (pin-to-pin compatible with NXP i.MX 95 series)
- 15 x 15 mm, FCBGA, 0.5 mm pitch
- 19 x 19 mm, FCBGA, 0.7 mm pitch
- Temperature Ranges & Qualifications
- Consumer – 0ºC to 90ºC
- Industrial – -40ºC to 105ºC
- Extended industrial – -40ºC to 125ºC
- Automotive – -40ºC to 125ºC (plus I assume some automovie “qualifications”)
NXP says the new MPU will support Linux and Android BSPs. The main “raison d’être” of i.MX 937 is to offer easier scaling from entry-level and high-performance models. In practise, that means the i.MX 937 and the i.MX 95/952 share a unified development ecosystem with the same BSP, security architecture, and boot structure, so you can upgrade or cut costs as needed.
Hardware design is also simplified thanks to pin-to-pin compatibility. The 15 x 15 mm FCBGA package is pin-to-pin compatible with the i.MX 952 family, and the larger 19 x 19 mm package is compatible with both the i.MX 952 and i.MX 95 families. The company also plans to introduce an i.MX 937 FRDM board, but has yet to provide details about it. I assume its design will be closer to the FRDM i.MX 95 (FRDM‑IMX95) development board pictured below than the FRDM i.MX 93 development board.
Like most Embedded World 2026 announcements, it’s an early preview, and the FRDM i.MX 937 development board will be available in late 2026, while the NXP i.MX 937 MPU should become available in Q1 2027. More details may be found on the product page and the relevant blog post.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
