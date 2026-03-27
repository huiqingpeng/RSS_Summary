---
title: "SparkFun Thing Plus – ESP32-C5 board offers dual-band WiFi 6, Adafruit Feather pinout, LiPo battery support"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/27/sparkfun-thing-plus-esp32-c5-board-offers-dual-band-wifi-6-adafruit-feather-pinout-lipo-battery-support/"
published: "2026-03-27"
fetched: "2026-03-28T07:02:47.959017"
---

Espressif has recently released the ESP-IDF v6.0 framework with support for ESP32-C5 and ESP32-C61, so we can expect more ESP32-C5 boards. Following the launch of boards like DFRobot FireBeetle 2 and the Espressif DevKitC-1, SparkFun has now launched its Thing Plus – ESP32-C5, an Adafruit Feather-compatible board based on the ESP32-C5.
The timing is no coincidence. Although the ESP32-C5 dual-band WiFi 6 SoC was announced back in 2022, hardware makers have been waiting for stable software support. With the release of ESP-IDF v6.0, the ESP32-C5 moves from “preview” to “stable” and adds key features, such as Safe Bootloader OTA updates. This enables the ROM bootloader to fall back to a recovery partition if an update fails, making it reliable enough for companies like SparkFun to launch hardware for remote deployments and Matter-compatible smart home applications.
SparkFun Thing Plus – ESP32-C5 specifications:
- Wireless module – ESP32-C5-WROOM-1
- SoC – Espressif Systems ESP32-C5
- CPU
- Single-core 32-bit RISC-V processor @ up to 240 MHz
- Low-power RISC-V core @ 40 MHz acting as the main processor for power-sensitive applications
- Memory – 384 KB SRAM on-chip; 8MB PSRAM
- Storage – 320 KB ROM, support for external flash
- Connectivity
- Dual-band (2.4/5 GHz) 802.11ax WiFi 6, 802.11b/g/n WiFi 4 backward compatibility
- WiFi modes: Station mode, SoftAP mode, SoftAP + Station mode, and promiscuous mode
- Bluetooth 5.0 Low Energy (LE) with Mesh support, up to 2Mbps data rate
- 802.15.4 radio for Zigbee 3.0, Thread 1.3, and Matter up to 250 Kbps
- CPU
- Storage – 8MB SPI flash
- PCB antenna
- SoC – Espressif Systems ESP32-C5
- Storage – MicroSD card slot for data capture and logging
- USB – USB Type-C port for power and programming
- Expansion
- 28-pin Feather-compatible headers with 19x GPIOs mapped to UART, I2C, SPI, and parallel IO
- 4-pin Qwiic connector for plug-and-play I2C peripherals
- Misc
- Reset and Enable buttons
- Red power LED
- Yellow LiPo charge LED
- WS2812 addressable RGB LED on IO27
- Power Supply
- 5V via USB-C port
- 2-pin JST connector for a 3.7V/4.2V LiPo battery
- Integrated MCP73831 battery charger (213mA @ 3.3V charge rate)
- Integrated MAX17048 I2C fuel gauge (Address: 0x36) for precise battery monitoring
- Dimensions – 2.3″ x 0.9″ (approx. 58.4 x 22.9 mm)
- Form Factor – SparkFun Thing Plus (Feather-compatible)
While the dual-band WiFi 6 board supports Espressif’s ESP-IDF v6.0 framework for advanced users, it comes pre-flashed with MicroPython, or can also be programmed with the Arduino IDE. More technical information and instructions to get started, as well as the KiCad hardware design files, are available on GitHub.
The SparkFun Thing Plus – ESP32-C5 can be purchased from the SparkFun store for $24.95, where you’ll also find a Hookup Guide.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
