---
title: "Luckfox Lume – A compact Allwinner T153 SBC with dual GbE, PoE, GPIO header, and MIPI interfaces for industrial HMI applications"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/27/luckfox-lume-allwinner-t153-industrial-sbc-with-dual-gbe-poe-gpio-mipi/"
published: "2026-03-27"
fetched: "2026-03-28T07:02:29.958599"
---

Luckfox Lume is a compact industrial SBC powered by an Allwinner T153 quad-core Cortex-A7 SoC with a low-power RISC-V core, and equipped with 128MB DDR3, 256MB SPI NAND flash, and dual Gigabit Ethernet
The board also features a microSD card slot, a USB 2.0 Type-A port, a USB Type-C port, MIPI DSI and CSI connectors, and a 40-pin GPIO header suitable for a range of HMI applications. By default, the board is powered through USB-C, but a PoE model is also available.
Luckfox Lume specifications:
- SoC – Allwinner T153 M3-QCX
- CPU
- 4x Arm Cortex-A7 cores @ up to 1.6GHz
- XuanTie E907 RISC-V core @ up to 600MHz
- GPU – 2D GPU only
- No VPU, no NPU
- System Memory – 128 MB built-in DDR3 (TBC)
- CPU
- Storage
- 256 MB SPI NAND flash (Winbond 25N02KVZEIR)
- MicroSD card slot
- Display Interface – 4-lane MIPI DSI
- Camera Interface – 2-lane MIPI CSI
- Networking – 2x Gigabit Ethernet RJ45 ports via Maxio MAE0621A-Q3C transceivers, one with optional PoE support
- USB
- USB 2.0 Type-C port
USB 2.0 Type-A port
- USB 2.0 Type-C port
- Expansion – 40-pin GPIO header with up to 6x UART, 2x I2C, 1x SPI, 4x ADC, 5V, 3.3V, and GND
- Misc
- Reset and FEL buttons
- Dual-color status LED
- 2-pin RTC battery header
- Power Input
- 5V via USB-C port
- Optional PoE support
- Dimensions – 68 x 55 mm
There’s some documentation to get started with a buildroot Linux image, but the wiki is currently only available in Chinese. The instructions also rely exclusively on Windows tools like Allwinner’s Phoenix Suite.
Optional PoE support is implemented through a Waveshare PoE Module (B), for which I can’t find details, but it should provide enough power for the board and accessories like a touchscreen display and a camera module.
I was somewhat confused by the 128 MB DDR3 RAM at first, since I could not find the chip anywhere on the Lume SBC, and the Forlinx FET153-S system-on-module clearly features both storage and memory chips along with the Allwinner T153 SoC. So I believe the Allwinner T153 M3-QSX is a system-on-package (SiP) with 128 MB on-chip DDR3 memory, while the Allwinner T153 MX-BCX found on the Forlinx SoM relies on external memory for higher capacities.
The Luckfox Lume can be purchased for $24.99/$29.99 on AliExpress, with the price depending on whether you need PoE. Strangely, the PoE version is cheaper, so I assume the company mixed up the two models, and they’ll probably fix that soon enough. Alternatively, you’ll also find both variants on the Waveshare shop for $20.99/$25.99.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
