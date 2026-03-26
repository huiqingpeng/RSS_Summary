---
title: "AngstromIO – A tiny 9.0 x 8.9 mm ATtiny1616 board that fits on top of a USB-C connector"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/26/angstromio-a-tiny-9-0-x-8-9-mm-attiny1616-board-that-fits-on-top-of-a-usb-c-connector/"
published: "2026-03-26"
fetched: "2026-03-27T07:10:57.358681"
---

Dieu-de-l-elec’s AngstromIO is an incredibly tiny open-source development board based on Microchip’s ATtiny1616 MCU. Measuring just 9.0 x 8.9 mm, the board is barely larger than the edge-mounted USB Type-C connector that powers it, making it ideal for highly space-constrained embedded projects.
Despite its tiny footprint, AngstromIO packs a QFN20-packaged ATtiny1616 MCU, two addressable SK6805-EC15 RGB LEDs, and includes access to various usable GPIOs, including I2C, UART, and UPDI for programming.
AngstromIO specifications:
- MCU – Microchip ATtiny1616 8-bit AVR microcontroller @ up to 20 MHz with 16KB flash, 2KB SRAM, 256 bytes EEPROM
- USB – 1x USB Type-C port (power only, no data lines connected to the MCU)
- Expansion via solder pads
- UPDI pin for programming
- I2C (SDA, SCL)
- 2x GPIOs (PB2/TX, PA3)
- 5V and GND
- Misc – 2x SK6805-EC15 addressable RGB LEDs
- Power Supply
- 5V via USB-C port
- Ultra-low power consumption (down to 200nA in power-down mode)
- Dimensions – 9.0 x 8.9 mm
Since the USB-C port is only for 5V power, the board features a dedicated UPDI (Unified Program and Debug Interface) pad for flashing the firmware. The board is fully compatible with the Arduino IDE using SpenceKonde’s megaTinyCore. You can easily use libraries such as Wire for I2C communication and tinyNeoPixel to control the onboard addressable LEDs without writing bare-metal AVR code.
Since the MCU uses the UPDI interface, a dedicated programmer is required to flash firmware, and the developer provides hardware design files for a dual CH340-based programmer with two USB-C ports. This setup allows simultaneous UPDI programming and one-way serial debugging (TX only), enabling you to monitor serial output on your computer while flashing new firmware.
Additionally, the developer mentions a CH32V003-based experimentation board, likely added to better utilize the PCB panel. Compared to the tiny AngstromIO board, this is a larger, breadboard-friendly design featuring a built-in 4×5 charlieplexed LED matrix, making it a simple and low-cost platform for experimenting with multiplexing and learning the CH32V003 toolchain.
The concept is very similar to PegorK’s f32 ESP32-C3 board, with similar features and a similar form factor, but without USB programming.
The AngstromIO, along with its companion programmer and RISC-V experimentation board, is a fully open-source hardware project. All KiCad schematics, PCB layouts, Gerber files, and sample code are available on Dieu-de-l-elec’s GitHub repository.
Via Adafruit
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
