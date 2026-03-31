---
title: "Toradex OSM and Lino SoMs – 30×30mm NXP i.MX 93/i.MX 91 modules with solder-down or B2B connector designs"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/31/toradex-osm-and-lino-soms-30x30mm-nxp-i-mx-93-i-mx-91-modules-with-solder-down-or-b2b-connector-designs/"
published: "2026-03-31"
fetched: "2026-04-01T07:00:18.423628"
---

Toradex has launched two new ultra-compact (30x30mm) System-on-Module (SoM) families: OSM and Lino, powered by NXP i.MX 91 or i.MX 93 Arm Cortex-A55 SoC for Edge industrial and IoT applications.
The OSM iMX91 and OSM iMX93 variants comply with the OSM Size-S standard, featuring a 332-ball contact grid designed to be soldered to the carrier board. The Lino is a proprietary format that keeps the OSM Size-S dimensions but features two board-to-board (B2B) connectors offering more flexibility for potential replacement or future upgrades.
Toradex Lino iMX91/iMX93 system-on-module
Toradex Lino specifications:
- SoC (one or the other)
- NXP i.MX 93
- CPU
- 2x Arm Cortex-A55 up to 1.7 GHz
- 2x Arm Cortex-M33 up to 250 MHz
- GPU – PXP 2D GPU with blending/composition, resize, and color space conversion
- NPU – Arm Ethos-U65 NPU @ 1 GHz up to 0.5 TOPS
- Security – EdgeLock Secure Enclave
- CPU
- NXP i.MX 91
- CPU – Single-core Arm Cortex-A55 up to 1.4 GHz
- GPU – N/A
- NPU – N/A
- Security – EdgeLock Secure Enclave
- NXP i.MX 93
- System Memory – Up to 2 GB LPDDR4 with inline ECC
- Storage – Up to 256 GB eMMC flash
- Two board-to-board connectors
- Storage – 2x SDIO/SD/MMC
- Display (iMX93 only)
- 4-lane MIPI DSI
- Single-channel LVDS
- Camera (iMX93 only) – 2-lane MIPI CSI-2
- Audio – 1x I2S/PDM
- Ethernet – 2x RGMII (1x with TSN)
- USB – USB 2.0 OTG, USB 2.0 Host
- Low-speed I/Os – 3x I2C, 2x I3C, 2x SPI, 4x UART, 3x PWM, 2x CAN FD, 10x GPIO
- Analog – 4x Analog Input (ADC)
- Dimensions – 30 x 30mm
- Temperature Range – -40° to +85°C
- Shock / Vibration – EN 60068-2-6/50g 20ms
- Product Availability – 2040
Toradex provides support for the company’s Torizon Linux distribution and the Yocto Project by default. FreeRTOS, Zephyr OS, QNX, and Android are available upon request
For evaluation and to quickly get started with software development before the custom carrier board is ready, the Lino iMX91/iMX93 evaluation kits are available with an optional 10.1-inch capacitive touch MIPI DSI display (1280×800) and/or a 5MP camera module.
I first thought the photo above was a mistake, since I could only see a SO-DIMM module. And while some Photoshop edits were probably involved in the photo above, a Verdin SO-DIMM module is indeed used, but it’s itself a mini carrier board for the Lino iMX91/iMX93 module.
Samples for the Lino iMX91/iMX93 start at $30.65 and $33.35, respectively. I couldn’t find the price for the evaluation kits, but for reference, the Ivy Verdin carrier board used in the kits goes for $99.20 and up. More details can be found on the Lino modules product page.
OSM iMX91/iMX93 solder-on modules
Toradex OSM iMX91/iMX93 specifications:
- SoC – NXP i.MX 93 or i.MX 91
- System Memory – Up to 2 GB LPDDR4 with inline ECC
- Storage – Up to 256 GB eMMC flash
- 332 LGA contacts
- Storage – 2x SDIO/SD/MMC
- Display (iMX93 only)
- 4-lane MIPI DSI
- Single-channel LVDS
- Camera (iMX93 only) – 2-lane MIPI CSI-2
- Audio – 1x I2S/PDM
- Ethernet – 2x RGMII (1x with TSN)
- USB – USB 2.0 OTG, USB 2.0 Host
- Low-speed I/Os – 2x I2C, 1x I3C, 2x SPI, 4x UART, 3x PWM, 2x CAN FD, 24x GPIO
- Analog – 4x Analog Input (ADC)
- Debugging – JTAG
- Dimensions – 30 x 30mm (OSM Size S form factor)
- Temperature Range – -40° to +85°C
- Shock / Vibration – EN 60068-2-6/50g 20ms
- Product Availability – 2038
Unsurprisingly, software support is the same as for the Lino module, namely Torizon Linux and the Yocto Project by default, while FreeRTOS, Zephyr OS, QNX, and Android can be supported upon request.
The development kit is similar, except it’s based on a larger carrier board with still the same options for a 10.1-inch touch display (1280×800) and a 5MP MIPI CSI camera module.
Toradex has some competition for the OSM modules based on NXP i.MX 91/93 processor, with systems-on-modules such as the ADLINK OSM-IMX93 OSM Size L module, or AVNET OSM-SF-IMX91/OSM-SF-IMX93 Size S modules.
Toradex OSM modules are slightly cheaper than the Lino modules, priced at $25.55 (i.MX 91) and $28.20 (i.MX 93), respectively. I could not find pricing information for the OSM evaluation kits, but you can join a waiting list if you are interested. More details may be found on the product page.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
