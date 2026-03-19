---
title: "Industrial RS-485/Modbus Raspberry Pi HAT works with OpenPLC, supports 7V-32V DC input"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/19/industrial-rs485-modbus-raspberry-pi-hat-works-with-openplc-supports-7v-32v-dc-input/"
published: "2026-03-19"
fetched: "2026-03-19T16:16:27.184710"
---

We have previously written about various industrial Raspberry Pi systems and gateways that come with RS-485 built in, but we had yet to cover a dedicated RS-485 Raspberry Pi HAT. To fill this gap, EngineElectronicAccessories, a developer based in Sweden, has introduced the “Industrial RS485 / Modbus HAT” designed for industrial automation, monitoring, and the OpenPLC open-source PLC suite.
The board features an onboard RS-485 transceiver with TVS diode protection and supports long-distance communication over the RS-485 standard. It uses the Pi’s hardware UART interface and includes Tx/Rx LEDs for diagnostics. The board also accepts 7V to 32V DC input, so you can power both the HAT and the Raspberry Pi directly from a standard 24V rail, eliminating the need for a separate USB power supply in a control cabinet.
Industrial RS-485/ Modbus HAT specifications:
- Compatibility – All Raspberry Pi boards with 40-pin GPIO header (Pi 3, Pi 4, Pi 5, Pi Zero, etc.)
- Host interface – UART (/dev/ttyAMA0 or /dev/ttyS0) via 40-pin GPIO header
- Communication
- 5-pin heavy-duty screw terminals with RS-485 A, B, and GND signals (and power signals)
- Off-the-shelf RS485 to TLL module (See AliExpress link)
- Misc
- Onboard Tx and Rx diagnostic LEDs
- Built-in TVS diodes for ESD and voltage spike protection
- Power
- Input Voltage – 7V to 32V DC via screw terminals (supports standard 12V and 24V industrial rails)
- Integrated DC-DC buck converter (Mini560 DC 5V 5A step-down module)
- 5V DC to power both the Raspberry Pi and the RS-485 transceiver
- Dimensions – Compact HAT form factor (fits most DIN-rail and standard Pi enclosures).
The board is explicitly “OpenPLC Optimized,” with its pinout and timing tuned for low-latency ladder-logic execution. This makes it very useful for energy-monitoring projects, such as reading SDM smart meters or interfacing with solar/battery systems. The project is partially open source, and you can find the PDF schematics and documentation on GitHub (note that the RS-485 interface is not galvanically isolated, which is typical for this price range).
The Industrial RS485 / Modbus HAT is available on Tindie for $9. It ships from Sweden with a shipping cost between $7.4 and $15, depending on the destination country. While we had not written about RS-485 HATs for Raspberry Pi SBCs so far, several other models can be found on AliExpress and Amazon.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
