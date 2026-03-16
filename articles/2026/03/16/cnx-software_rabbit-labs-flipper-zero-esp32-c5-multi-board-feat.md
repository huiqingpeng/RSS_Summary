---
title: "Rabbit-Labs Flipper Zero ESP32-C5 multi-board features CC1101, GPS, and dual-band Wi-Fi 6"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/16/rabbit-labs-flipper-zero-esp32-c5-multi-board-features-cc1101-gps-and-dual-band-wi-fi-6/"
published: "2026-03-16"
fetched: "2026-03-17T07:00:26.751261"
---

Designed by Rabbit-Labs EU, the Flipper Zero ESP32-C5 multi-board is an expansion board for the Flipper Zero built around the ESP32-C5 dual-band Wi-Fi 6 (2.4 GHz and 5 GHz) microcontroller. The board also features a TI CC1101 sub-GHz transceiver, a GPS module, an SD card slot, and a USB-C port for power and programming.
Last month, we wrote about the ESP32 Marauder 5G Apex 5 module, another ESP32-C5-based add-on for the Flipper Zero that comes with dual-band Wi-Fi 6, two sub-GHz radios, an NRF24 radio, and a built-in GPS module, which makes it quite bulky, to say the least. Compared to that, Rabbit Labs’ multi-board can be considered a stripped-down, simpler alternative, with a more compact design and straightforward setup.
ESP32-C5 multi-board specifications:
- Main module – ESP32-C5-WROOM-1U
- SoC – Espressif Systems ESP32-C5
- CPU
- Single-core 32-bit RISC-V processor @ up to 240 MHz
- Low-power RISC-V core @ 40 MHz acting as the main processor for power-sensitive applications
- Memory – 384 KB SRAM on-chip
- Storage – 320 KB ROM
- Connectivity
- Dual-band (2.4/5 GHz) 802.11ax WiFi 6, 802.11b/g/n WiFi 4 backward compatibility
- WiFi modes: Station mode, SoftAP mode, SoftAP + Station mode, and promiscuous mode
- Bluetooth 5.0 Low Energy (LE) with Mesh support, up to 2Mbps data rate
- 802.15.4 radio for Zigbee 3.0, Thread 1.3, and Matter up to 250 Kbps
- CPU
- External antenna connector (U.FL, MHF I, or AMC connector)
- SoC – Espressif Systems ESP32-C5
- Storage – MicroSD card slot for storing logs, captures, and data
- Wireless
- Dual-band WiFi 6, BLE 5, and 802.15.4 radio via ESP32-C5 as described above.
- TI CC1101 transceiver module
- Operates in the 855–925 MHz range
- Optimized packet handling and interrupt timing for stability
- Enhanced FIFO/timeout recovery to prevent hangs
- SMA connector for external antenna
- Integrated GPS module with antenna
- USB – USB Type-C port for power and firmware updates
- Misc
- Boot and Reset buttons
- Power KLED
- 3D printed enclosure
- Dimensions – TBD
The board is designed to run ESP32 Marauder firmware, which provides access to Wi-Fi and RF analysis features, including tools for wireless network scanning, packet capture, wardriving, and other security testing functions. Other than that, the integrated GPS module can be used to log locations during wardriving sessions. Firmware can be flashed through the onboard USB-C port, and captured data or logs can be stored directly on the microSD card.
This is not the first add-on board for the Flipper Zero that we’ve covered. We have previously looked at several similar boards, such as the FlipMods Combo, which is a very similar addon board just with a generic ESP32 instead of an ESP32-C5. Other examples include the Flipper Blackhat, the Mayhem v2, and various other expansion boards designed for wireless and security testing.
The Flipper Zero ESP32-C5 multi-board is listed on Tindie for $125, with international shipping starting at $6 from Czechia. According to the listing, the board is expected to become available around this month (March 2026), although it is currently out of stock.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
