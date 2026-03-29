---
title: "M5Stack Stamp-P4 – A tiny ESP32-P4 USB-C board with optional Wi-Fi 6 and Bluetooth 5.4"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/29/m5stack-stamp-p4-a-tiny-esp32-p4-usb-c-board-with-optional-wi-fi-6-and-bluetooth-5-4/"
published: "2026-03-29"
fetched: "2026-03-30T07:04:16.275933"
---

M5Stack has just introduced the Stamp-P4, a tiny USB-C development board built around the ESP32-P4 high-performance RISC-V MCU chip, featuring 16MB of Flash and 32MB of PSRAM, and optional Wi-Fi 6 and Bluetooth 5.4 support through the ESP32-C6-MINI-1-based Stamp-AddOn C6 module.
Despite its small size (29.8 x 22.0 x 4.3mm), the Stamp-P4 offers a wide range of interfaces, including a MIPI-CSI camera connector, as well as a MIPI DSI display interface, RMII Ethernet, USB 2.0 HS, and up to 44x GPIOs via 1.27mm/2.00mm pitch castellated holes and a few through holes.
M5Stack Stamp-P4 specifications:
- SoC – Espressif Systems ESP32-P4NRW32
- CPU
- Dual-core RISC-V microcontroller @ 360 MHz with AI instructions extension and single-precision FPU
- Single-RISC-V LP (Low-power) MCU core @ up to 40 MHz
- GPU – 2D Pixel Processing Accelerator (PPA)
- VPU – H.264 and JPEG codecs support
- Memory – 768 KB HP L2MEM, 32 KB LP SRAM, 8 KB TCM, 32MB PSRAM
- Storage – 128 KB HP ROM, 16 KB LP ROM
- CPU
- Storage – 16MB NOR flash
- Display – MIPI DSI (2-lane) via onboard 1.27 mm SMT pins
- Camera – MIPI CSI (2-lane) via BTB (AXE516127D) connector
- Networking
- RMII Ethernet expansion interface via 1.27mm headers
- 2.4 GHz WiFi 6, Bluetooth 5, and 802.15.4 (Zigbee/Thread/Matter) via optional AddOn C6 For P4 module (through SDIO 3.0 BTB connector)
- USB
- 1x USB Type-C port for power and programming
- 1.27mm solderable pads for USB 2.0 OTG (Host via D+/-)
- Expansion – 44x GPIO (G0-G39, G41, G49, G50, G52) routed to 1.27mm/2.00mm pitch SMT stamp holes and 2.54mm pitch DIP headers with UART, I2CHC-PBB40C-20DS-0.4V-2.5-
- Power
- Supply
- 5V DC input
- SY8089AAAC DC-DC converter
- AW32901FCR overvoltage protection (supports >6V input)
- Consumption
- Bare board operation – ~30.76mA @ 5V
- Deep sleep – ~360.84uA @ 5V / 343.90uA @ 3.3V
- Supply
- Dimensions – 29.8 x 22.0 x 4.3mm
- Solder options
- SMT (1.27mm / 2.00mm pitch)
- DIP (2.54mm headers)
- Weight – 2.7g (Product) / 6.1g (Gross)
- Temperature – 0 to 40°C
On the software side, M5Stack mentions that the Stamp-P4 and its C6 companion are supported by its own UiFlow2 visual programming platform, as well as the Arduino IDE, the ESP-IDF framework, and PlatformIO. M5Stack has already provided an Arduino quick-start guide and an example Wi-Fi sketch for the AddOn on the documentation page.
Because the Stamp-P4 module lacks built-in wireless connectivity, M5Stack has also released the “Stamp-AddOn C6 for P4”. This expansion module snaps right into the Stamp-P4’s onboard 20-pin SDIO 3.0 interface to quickly add wireless capabilities.
The Stamp-Add-On C6 is built around the ESP32-C6-MINI-1-N4 module and includes 4 MB of Flash. Measuring just 27.0 x 18.0 x 4.0mm, it’s a drop-in solution for developers building smart security gateways, edge computing devices, or industrial control nodes that require both the power of P4 and wireless connectivity. More information, along with example code and a schematic, can be found in the add-on documentation.
Though we have written about various ESP32-P4-based development boards like the ALIENTEK DNESP32P4M, the FireBeetle 2 ESP32-P4 dev board, and development boards like the Raspberry Pi-sized ESP32-P4-Pi-VIEWE, this is the first time we have seen a fully functional ESP32-P4-based development board that is this compact.
The M5Stamp ESP32-P4 module is available on Aliexpress for $12.95, while the optional Stamp-AddOn C6 Wi-Fi 6 expansion module is priced at $7.00. Both products can also be purchased directly from the M5Stack store for the same price. Shipping costs will vary depending on the country.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
