---
title: "Ampisu is a compact pocket-sized USB lab power supply with SCPI and web control (Crowdfunding)"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/24/ampisu-compact-pocket-sized-isolated-usb-lab-power-supply-with-scpi-and-web-control/"
published: "2026-03-23"
fetched: "2026-03-24T07:00:20.761093"
---

The concept of a USB-C-based power supply is not new, and we have previously seen projects like XIAO Powerbread and Axiometa BrodBoost-C. As USB PD-based power adapters and power banks have become much cheaper, adjustable power supplies like the PocketPD and BenchVolt PD have come out. Both have their own limitation: the PocketPD has only a single output channel, thus hardly a lab power supply, and the BenchVolt PD is not quite compact enough to be considered pocket-friendly.
This is where the Ampisu comes in. It’s a compact, pocket-friendly, and isolated three-output lab power supply designed to fit in a pocket and include features of a typical full-sized power supply. Its desigened for low-power embedded work, field debugging, and automated test setups.
Ampisu specifications:
- MCU – Raspberry Pi RP2040 dual-core Cortex-M0+ microcontroller @ 125 MHz with 264KB SRAM
- Storage – Non-volatile memory for saving configurations
- Power Input
- 5V via USB Type-A or USB Type-C port
- Automatically adapts to available host power capabilities (supports up to 3A on USB-C)
- Power Output
- 3x fully galvanically isolated outputs (via dedicated transformer-isolated flyback converters)
- Adjustable Output 1 and 2 – 0 V – 7.5 V @ up to 500 mA each
- Auxiliary channel – 3.3 V @ up to 100 mA (approx. 500 mW limit)
- Combination modes – Parallel up to 1 A (Series up to 15 V or ±7.5 V split-rail)
- Performance
- Resolution – 10 mV / 1 mA
- Ripple – ~8.44 mV RMS / ~39.5 mV peak-to-peak
- Load regulation – < 1%
- Precise dual-channel DACs and ADCs for constant-current source reference and voltage/current measurement
- Low-noise outputs utilizing linear post-regulation
- Protections
- Fast, fine-grained analog current limiting
- ESD, reverse current, overcurrent, and overvoltage protection
- Misc
- 3x RGB status LED (Ideal, CC, CV modes)
- High-resistance grounding path (10 MΩ ∥ 1 nF) from output ground to chassis ground
- Dimensions – 62 x 62 x 20 mm (2.44 x 2.44 x 0.79 inches)
- Weight – ~100 – 110 grams (3.53 – 3.9 oz)
- Enclosure – CNC-machined aluminum
What’s most interesting about this compact isolated lab power supply is the use of dedicated transformer-isolated flyback converters for each output. This is also why we can compare it to power profilers like the Seeed Studio XIAO Debug Mate and Nordic Power Profiler Kit II. The primary job of a power profiler is to measure energy usage, but those typically do not have isolation, meaning their ground is directly connected to your computer’s USB port. With the Ampisu, the outputs are physically separated, allowing you to avoid ground loops and safely create split-rail supplies.
Ampisu can be configured with a browser-based WebUSB GUI, a SCPI command set, and a Python API, which makes it easy to configure with PCs, Raspberry Pi, and automated test systems without requiring driver installation. It can also be controlled over USB with a serial log interface, supports CSV-based sequencing for automated power profiles, and allows all configurations to be stored in non-volatile memory for fully standalone operation. The company also mentions that the project is open-source and the hardware design files, firmware, source code for the web interface, and libraries will be released once the campaign ends.
Ampisu is currently crowdfunding on Crowd Supply for $179. The basic kit includes a CNC-machined aluminum unit and a set of Dupont and banana-jack cables. Shipping is free within the US and $12 to the rest of the world. Orders are expected to ship by August 31, 2026.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
