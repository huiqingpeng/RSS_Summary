---
title: "M5Stamp C6LoRa tiny (18×15×2.3 mm) SMD module pairs ESP32-C6 with SX1262 LoRa chip"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/16/m5stamp-c6lora-tiny-18x15x2-3-mm-smd-module-pairs-esp32-c6-with-sx1262-lora-chip/"
published: "2026-03-16"
fetched: "2026-03-17T07:02:50.314568"
---

The M5Stamp C6LoRa is a compact LoRa SMD module that combines the ESP32-C6 Wi-Fi 6, Bluetooth LE, and 802.15.4 microcontroller with the SX1262 LoRa transceiver for both high-speed and long-distance communication. The module targets applications such as smart agriculture, remote meter reading, industrial monitoring, and outdoor long-range wireless control systems.
The module measures 18 × 15 × 2.3 mm, making it suitable for space-constrained systems and compact embedded designs. M5Stack has also added an SGM13005L4 low-noise amplifier (LNA) to improve reception performance, along with a PI4IOE5V6408 I/O expander that manages the LoRa control signals without using too many of the ESP32-C6’s GPIO pins.
M5Stamp C6LoRa specifications:
- SoC – Espressif Systems ESP32-C6
- CPU
- Single-core 32-bit RISC-V clocked up to 160 MHz
- Low-power RISC-V core @ up to 20 MHz
- Memory/Storage – 512KB SRAM, 320KB ROM
- Wireless – WiFi 6, BLE 5.3, 802.15.4 (See wireless section)
- CPU
- Storage – 16 MB external NOR flash
- Wireless
- 2.4 GHz WiFi 6, Bluetooth 5.3, and 802.15.4 radio for Thread/Zigbee via ESP32-C6
- LoRa
- Semtech SX1262 LoRa transceiver (850 to 960 MHz)
- Max transmit power – +22 dBm
- Max receive sensitivity – -148 dBm
- SGMICRO SGM13005L4 Low Noise Amplifier (LNA) for enhanced reception
- Antennas – 2x IPEX-4 connectors for external Wi-Fi and LoRa antennas
- Expansion
- 16x GPIOs routed from the ESP32-C6 (G2, G4 – G11, G15 – G18, G20 – G22)
- 5x extended I/Os (EXT_P0 – P4) via a PI4IOE5V6408 I2C I/O expander
- Power
- 3.3V DC input via VDD_3V3 pin
- 3.7V to 5V DC input via BAT pin
- Dimensions – 18.0 x 15.0 x 2.3 mm (SMD surface-mount form factor)
- Weight – 1.7 grams
Because the LoRa control signals are routed through the internal I/O expander, the company mentions that you need to follow a specific initialization sequence to get the LoRa radio working. You’ll need to reset the SX_NRST pin, pull the SX_ANT_SW high to enable the RF antenna switch, and then pull the SX_LNA_EN high to enable the amplifier chip. Firmware flashing can be done via UART (requiring a USB-TTL adapter and pulling GPIO9 low) or via the module’s direct USB pins.
The company also notes that if the module is powered via the BAT pin (3.7V – 5V), the MODULE_EN pin must be pulled high to enable the power supply. If powering via VDD_3V3, no operation on MODULE_EN is required.
On the software side, M5Stack provides a Quick Start guide for the Arduino IDE, as well as configuration details for PlatformIO (using the m5stack-stamp-c6lora environment and M5Unified and RadioLib libraries), and support for UiFlow visual programming environment is also in the works. Additionally, the company provides hardware documentation, including PDF schematics, PCB layout files, a KiCad footprint library, and 3D models for mechanical integration. More information is available on the documentation website.
This is not the first module in the M5Stamp family; we have previously written about similar compact products such as the M5Stack Stamp-S3A, M5Stamp C3U, M5Stamp S3, M5Stamp C3, and various other products, as well as standalone LoRaWAN modules. You can check those out if you are looking for similar compact stamp-sized devices.
The Stamp C6LoRa SMD module is now available for $12.95 on AliExpress and the M5Stack store.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
