---
title: "ESP32-P4-Pi-VIEWE – A Raspberry Pi-inspired ESP32-P4 + ESP32-C6 board with Ethernet, USB, 40-pin GPIO header, and more"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/27/esp32-p4-pi-viewe-raspberry-pi-esp32-p4-esp32-c6-board/"
published: "2026-03-27"
fetched: "2026-03-28T07:03:03.354358"
---

The ESP32-P4-Pi-VIEWE is a Raspberry Pi-inspired development board equipped with a VIEWE ESP32-P4C6-Core module, combining a 400 MHz ESP32-P4 dual-core RISC-V MCU with an ESP32-C6 chip for Wi-Fi 6 and Bluetooth 5.0 wireless connectivity, as well as 32MB PSRAM and 16MB NOR flash.
The board also offers 10/100Mbps Ethernet connectivity, MIPI DSI, and CSI connectors for display and/or camera, two onboard microphones, a speaker output, a USB 2.0 port, a micro SD card slot, and the usual 40-pin GPIO header, all in a familiar 85 x 56 mm credit card form factor.
ESP32-P4-Pi-VIEWE specifications:
- Main module – VIEWE ESP32-P4C6-Core
- Microcontroller – ESP32-P4NRW32
- MCU
- Dual-core RISC-V microcontroller @ 360/400 MHz with AI instructions extension and single-precision FPU
- Single-RISC-V LP (Low-power) MCU core @ up to 40 MHz
- GPU – 2D Pixel Processing Accelerator (PPA)
- VPU – H.264 and JPEG codecs support
- Memory – 768 KB HP L2MEM, 32 KB LP SRAM, 8 KB TCM, 32MB PSRAM
- Storage – 128 KB HP ROM, 16 KB LP ROM
- MCU
- Wireless – 2.4 GHz WiFi 6, Bluetooth 5, and 802.15.4 (Zigbee/Thread/Matter) via ESP32-C6FH4 SoC (SDIO interface)
- Storage – 16MB NOR flash
- Microcontroller – ESP32-P4NRW32
- Storage – MicroSD card slot
- Display I/F – 2-lane MIPI DSI connector
- Camera I/F – 2-lane MIPI CSI connector compatible with GC0308, OV2640, OV2710, OV5645, OV5647, SC030IOT, SC101IOT, and SC2336 sensors
- Audio
- ES8311 audio codec
- 2-pin header supporting 8Ω/2W speaker
- 2x microphones + ES7210 AEC chip
- Networking
- 100Mbps Ethernet RJ45 port via IP101GR chip + 4-pin header for optional PoE module
- WiFi 6 and Bluetooth 5 (via ESP32-C6) – The 802.15.4 radio is not listed in the specs.
- Antenna support
- Ceramic antenna for WiFi and Bluetooth
- IPEX antenna connector on ESP32-P4C6-Core module
- USB
- 1x USB 2.0 OTG Type-A port
- 1x USB Type-C port for power, programming, and debugging
- 1x USB Type-C port for power and programming
- Expansion – 40-pin GPIO header compatible with the header on Raspberry Pi SBCs
- Debugging
- USB-C port for debugging
- 4-pin UART connector for ESP32-C6
- 3-axis accelerometer and 3-axis gyroscope
- Misc
- Boot and Reset buttons
- RGB LED
- Power Supply
- 5V via USB-C port
- Optional PoE via 4-pin PoE header
- Dimensions – 85 x 56 mm
VIEWE provides instructions to get started with the ESP-IDF framework and some sample code for audio, Ethernet, camera, display (LVGL), and the usual ESP-Brookesia demo, as well as the PDF schematics on GitHub.
If this type of ESP32-P4 + ESP32-C6 credit card-sized board feels familiar, it shares many of the same features as the Waveshare ESP32-P4-Module-DEV-KIT we covered in April 2025. The main differences are that the Waveshare board comes with four USB Type-A ports, and the VIEWE board integrates two microphones instead of one, and also adds an accelerometer and a gyroscope.
Both are also based on a single module combining an ESP32-P4 with 32MB PSRAM, an ESP32-C6, and 16MB flash. Even the IPEX connector is in the same position.
VIEWE usually offers a slightly lower price point, and the ESP32-P4 Pi VIEWE can be purchased for $33.13 on AliExpress, including shipping, or on the VIEWE store for $17.99 plus shipping. One advantage of the Waveshare model is that it’s also offered in kits with a camera, a display, and other accessories, and it’s less obvious how to do that with the VIEWE model.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
