---
title: "Grinn GenioSoM-360 MediaTek Genio 360P LGA system-on-module enables Edge AI in space-constrained applications"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/19/grinn-geniosom-360-mediatek-genio-360p-lga-system-on-module-enables-edge-ai-in-space-constrained-applications/"
published: "2026-03-19"
fetched: "2026-03-19T13:05:07.569440"
---

Grinn GenioSoM-360 is the first system-on-module (SoM) based on MediaTek Genio 360P octa-core Cortex-A76/A55 SoC with a 7.4 TOPS AI accelerator. It comes in a compact (30x30mm) LGA package targeting edge AI applications in space-constrained applications.
The SoM features up to 8GB LPDDR4x RAM, up to 64GB eMMC flash, a PMIC, and exposes all I/Os through 303 pads, notably MIPI DSI, LVDS, eDP/DP display interfaces, MIPI CSI camera interfaces, Gigabit Ethernet, USB 3.2/2.0 interfaces, PCIe Gen2, CAN FD, and more
Grinn GenioSoM-360 specifications:
- SoC – MediaTek Genio 360P (MT8367); note the photo above shows the MT8366, the hexa-core Genio 360 variant
- Octa-core CPU
- 2x Arm Cortex-A76 cores clocked at up to 1.9 GHz (industrial) / 2.0GHz (commercial)
- 6x Arm Cortex-A55 cores clocked at up to 1.7 GHz (industrial) / 2.0GHz (commercial)
- GPU – Arm Mali-G57 MC2 at up to 700MHz with support for OpenGL ES 3.2, Vulkan 1.1, OpenCL 2.0
- VPU
- Video Decode – H.264/H.265/VP9 up to 4Kp30
- Video Encode – H.264/H.265 up to 1080p90
- JPEG – Decode – 250 MP/s; Encode – 400 MP/s
- AI accelerator – MediaTek 8th-Gen NPU with 1x MDLA5.3, GenAI up to 7.4 TOPS
- Octa-core CPU
- System Memory – Up to 8GB 32-bit LPDDR4X-3733
- Storage – 16GB to 64GB eMMC5.1 flash
- Host interface – 303x pads
- Display
- 4-lane MIPI DSI/LVDS
- 4-lane MIPI DSI
- 4-lane eDP 1.2 or DP 1.4
- Camera – 2x 4-lane MIPI CSI-2
- Audio – I2S, TDM, PCM, PDM
- Networking – RGMII (Gigabit Ethernet)
- USB – USB 3.0, 2x USB 2.0
- PCIe – PCIe Gen2 x1
- Low-speed I/OT
- CAN-FD
- 4x UART, 6x SPI, 8x I2C
- 4x analog inputs
- Display
- Power Management
- Input Voltage – 3.15V-5.0V
- On-module Mediatek MT6365 PMIC
- Dimensions – 30 x 30mm (303-pad LGA package)
- Temperature Range – Operating: -20°C – 70°C; storage: -40°C – 85°C (TBC)
Grinn failed to mention anything about software support. However, from the MediaTek Genio 360/360P announcement, we know that MediaTek will provide support for Android, Yocto Linux support is planned for Q3 2026, and Ubuntu for Q4 2026.
The company did not unveil a development or evaluation board, but I’d expect a board similar to its GenioBoard SBC might become available with the GenioSOM-360 in due time. Note that the previous generation Genio-SOM510 and Genio-SOM700 are larger (37 x 42.6 mm) and feature 312 LGA pads, and a different baseboard will be required with a cutout for the passive components on the bottom side of the module.
The Grinn GenioSOM-360 is well-suited for industrial automation (e.g., smart controllers and high-resolution HMI panels), portable healthcare devices (diagnostic tools and patient monitoring), Smart City infrastructure (e.g., smart security cameras), Smart Home applications, and robotics.
The company didn’t provide any availability and pricing information in the email press release we received, and there’s limited additional information on the product page. Grinn also showed the module at Embedded World 2026, and Charbax shot a video about the company’s products. There’s no demo about the MediaTek Genio 360P system-on-module per se, but the company showcased previous-generation Genio and Renesas modules in various demos. So I’ve still embedded the video below to show what kind of applications are possible with this type of small Edge AI modules, including AI vision-enabled robotics arms, ultra-compact smart cameras, gesture recognition, and so on.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
