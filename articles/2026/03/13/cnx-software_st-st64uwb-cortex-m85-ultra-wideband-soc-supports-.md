---
title: "ST ST64UWB Cortex-M85 ultra-wideband SoC supports IEEE 802.15.4z and 802.15.4ab UWB standards, radar sensing"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/13/st-st64uwb-cortex-m85-ultra-wideband-soc-supports-ieee-802-15-4z-and-802-15-4ab-uwb-standards-radar-sensing/"
published: "2026-03-13"
fetched: "2026-03-14T07:01:46.292155"
---

STMicroelectronics ST64UWB Arm Cortex-M85 ultra-wideband (UWB) SoC family supports both the current IEEE 802.15.4z and the upcoming IEEE 802.15.4ab UWB standards for longer-range, more reliable positioning and secure proximity-based interactions. It mainly targets digital car keys, hands-free access, and smart-device detection.
The family includes the ST64UWB-A100 (automotive entry), ST64UWB-A500 (automotive premium), and ST64UWB-C100 (industrial/smart home), all built on an 18 nm FD-SOI process that improves the RF link budget by ~3 dB, yielding roughly 50% additional range beyond what IEEE 802.15.4ab alone provides. The automotive-focused A-series offers ASIL-A(B) safety support, while the ST64UWB-C100 targets consumer and commercial applications.
ST64UWB family specifications:
- MCU Core
- 32-bit Arm Cortex-M85 CPU with DP-FPU, MVE, and ETM
- Frequency
- Up to 100 MHz (ST64UWB-C100, ST64UWB-A100)
- Up to 256 MHz (ST64UWB-A500)
- Memory/Storage
- Integrated PCM Memory
- SRAM and Back-up SRAM
- Wireless Connectivity
- Ultra-wideband (UWB) Radio
- IEEE 802.15.4z-2020 and IEEE 802.15.4ab support
- UWB channels 5, 6, 8, 9, 10, 12 (6.49 GHz to 8.99 GHz)
- BPRF and HPRF modulation
- 2× transmit/receive antenna ports
- CCC, ICCE automotive standards (ST64UWB-A500 and ST64UWB-A100 only)
- Narrow-band assisted radio (NBA)
- Supported standard for NBA radio
- UNII-3 / UNII-5 frequency bands (5.7–6.4 GHz)
- Single Tx/Rx antenna port
- Radar sensing (A500 only)
- Multi-moving target detection
- Distance and angle sensing
- Automotive kick sensor support
- Child presence detection (CPD)
- Ultra-wideband (UWB) Radio
- Peripherals
- Up to 20x GPIOs (some multiplexed with communication interfaces)
- 2x SPI, 2x I2C, USART, LPUART
- 2x I3C (ST64UWB-C100 only)
- FDCAN (ST64UWB-A500 and ST64UWB-A100 only)
- General Purpose ADC (GP ADC)
- Security
- Arm TrustZone with Armv8.1-M security extensions
- Secure enclave
- Tamper detection
- PSA and SESIP Level 3 security certification
- Clock sources
- External 32 MHz crystal
- Optional 32.768 kHz crystal
- Internal LSI (32 kHz)
- Misc – Integrated digital temperature sensor
- Debugging – On-chip debugging
- Power – Internal power management
- Package
- HWQFN40 with wettable flank (6 x 6 mm, 0.5 mm pitch)
- ECOPACK 2 compliant
- Temperature Range (for ST64UWB-A500 and ST64UWB-A100)
- Operating – -40°C to +115°C
- Junction Temperature – +125°C
- Compliance (for ST64UWB-A500 and ST64UWB-A100)
- AEC-Q100 grade 2 qualified
- ISO21434 (Automotive Cybersecurity Level 2) and ISO26262 (ASIL-A)
The company mentions that the radar system on the A500 benefits from the new IEEE 802.15.4ab Kaiser pulse shape and the 1.3 GHz bandwidth of UWB channel 11, which provides roughly twice the spatial accuracy compared to traditional 500 MHz UWB channels. IEEE 802.15.4ab also introduces narrow-band assisted multi-millisecond ranging (MMS), which increases link budget by up to 18 dB and can extend secure ranging distance by up to eight times.
On the software side, the ST64UWB supports a UWB software stack implementing the PHY and MAC layers, along with radar-processing tools for sensing applications. The company also mentions development boards, antenna reference designs, and application examples, but I cannot find any information about those at the time of writing.
The platform integrates with industry ecosystems such as the Car Connectivity Consortium (CCC) Digital Key, Intelligent Car Connectivity Industry Alliance (ICCE), and Aliro Alliance. These standards define how smartphones, vehicles, and smart locks securely communicate using technologies such as UWB for car keys, hands-free access control, precise device localization, and radar-based sensing.
In the product brief, the company notes that the new UWB standard (IEEE 802.15.4ab) is better than the current 802.15.4z for car access systems.
The next image explains how a car uses the new UWB system to identify the correct user and unlock automatically.
The ST64UWB devices are currently sampling with major suppliers and OEMs, and no official pricing has been announced yet. More information is available on the press release and product page.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
