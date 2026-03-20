---
title: "u-blox JODY-W6 – NXP IW623/AW693 tri-band Wi-Fi 6E and Bluetooth 5.4 LE audio modules"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/20/u-blox-jody-w6-nxp-iw623-aw693-tri-band-wi-fi-6e-and-bluetooth-5-4-le-audio-modules/"
published: "2026-03-20"
fetched: "2026-03-20T16:03:27.755841"
---

u-blox has expanded its JODY family of modules with the NXP IW623/AW693-based JODY-W6 series that adds tri-band Wi-Fi 6E and Bluetooth 5.4 (including LE Audio) in a single package.
There are seven product variants across five main series models, mainly based on NXP’s IW623 chipset for professional use and the AW692/AW693 for automotive use. The modules are optimized for the parallel operation of Wi-Fi and Bluetooth and target high-throughput, low-latency, and secure connectivity use cases such as industrial automation, healthcare systems, smart buildings, network infrastructure, and in-vehicle infotainment and telematics systems. It has a 15.6 × 19.8 mm LGA form factor, and it’s designed for easy migration within the JODY family.
u-blox JODY-W6 specifications
- Wireless SoC
- NXP IW623 (Professional grade – JODY-W672, JODY-W673 )
- NXP AW692 / AW693 (Automotive grade 2 – JODY-W682, JODY-W683, JODY-W663 )
- Connectivity
- Wi-Fi
- Standards – Wi-Fi 6E IEEE 802.11a/b/g/n/ac/ax
- Frequencies – 2.4 GHz (1-13), 5 GHz (36-177), and 6 GHz (1-233) (JODY-W663 supports 2.4 GHz and 5 GHz only)
- Bandwidth – 20, 40, and 80 MHz channels
- Wi-Fi Output Power (EIRP) – 19 dBm
- MIMO – Concurrent dual-band with 2×2 MIMO at 5/6 GHz + 1×1 at 2.4 GHz
- Data Rate – PHY data rates up to 1.2 Gbit/s at 5/6 GHz or combined throughput of 1.34 Gbit/s
- Modes – Access point (AP), Station (STA), P2P (Wi-Fi Direct), or combinations
- Micro Access Point – Supports up to 64 connections
- Dual MAC supported on automotive variants (JODY-W663, JODY-W682, JODY-W683 )
- Bluetooth
- Standard – Bluetooth 5.4 Dual-Mode
- Profiles – HCI, BR/EDR, Low Energy (LE)
- Features – LE Audio uses isochronous channels, LE long range, Advertising extension
- Data Rate – Up to 2 Mbit/s
- Bluetooth Output Power (EIRP) – 12 dBm
- Antenna configurations
- 2-pin variants (JODY-W672, JODY-W682)
- Pin 1 – 5/6 GHz Wi-Fi and Bluetooth
- Pin 2 – 2.4 GHz and 5/6 GHz Wi-Fi
- 3-pin variants (JODY-W673, JODY-W683 and JODY-W663)
- Pins 1 and 2 – 2.4 GHz and 5/6 GHz Wi-Fi
- Pin 3 – Dedicated Bluetooth
- Pins 1 and 2 – 2.4 GHz and 5 GHz Wi-Fi (JODY-W663 only)
- 2-pin variants (JODY-W672, JODY-W682)
- Wi-Fi
- Interfaces
- Wi-Fi
- PCIe (JODY-W672-00B, JODY-W673-00B)
- SDIO (JODY-W672-50B, JODY-W673-50B)
- Bluetooth – High-speed UART (4-wire)
- Bluetooth Audio – PCM and I2S
- Additional GPIOs
- Wi-Fi
- Security
- WPA2/3, AES/CCMP, AES/GCMP, and WAPI encryption
- Secure boot (NXP EdgeLock) on chip
- Misc
- WCI-2 (2-wire) for external radio coexistence
- PTA (5-wire) for external radio coexistence
- Power
- Main supply – 3.3 V and 1.8 V
- I/O power supply – 3.3 V or 1.8 V
- Dimensions – 19.8 x 15.6 x 2.7 mm (94-pin LGA module with additional ground pins)
- Temperature range
- Professional grade – -40°C to +85°C (JODY-W672, JODY-W673 )
- Automotive grade 2 (AEC-Q104) – -40°C to +105°C (JODY-W663, JODY-W682, JODY-W683)
- Compliance – RoHS and REACH compliance, Moisture sensitivity level 4
The company clearly mentions that these are host-based modules and require an external host processor running Linux or Android, with drivers provided directly by NXP. Other than that, the company didn’t provide additional information about the software.
The company also provides the EVK-JODY-W6 evaluation kit, which gives access to PCIe and UART, along with a USB-to-UART bridge for easy Bluetooth connectivity. It also exposes GPIOs via pin headers, supports multiple power supply options, and includes onboard and external SMA tri-band (2.4/5–7 GHz) antennas, and more.
The company also talks about the M2-JODY-W683-10C evaluation kit, on the datasheet, which is supposed to be the standard module mounted on an M.2 card very similar to the Silex SX-SDMAX6E, but there is no product page about the module, and a quick Google search points me to a DigiKey where it is listed as a module only.
JODY-W6 engineering samples are expected to ship in early Q2 2026, and volume production should start by the end of Q2 2026. Pricing has not been officially disclosed yet, which is typical for industrial-grade wireless modules, and is likely to vary depending on volume, variants (antenna configuration), and integration requirements. More information is available on the product page or the press release.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
