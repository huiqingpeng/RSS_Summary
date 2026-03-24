---
title: "Upcoming ESP32-S31 dual-core RISC-V MCU offers Gigabit Ethernet, WiFi, Bluetooth, and 802.15.4 connectivity"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/24/esp32-s31-dual-core-risc-v-mcu-offers-gigabit-ethernet-wifi-bluetooth-and-802-15-4-connectivity/"
published: "2026-03-24"
fetched: "2026-03-25T07:02:29.140300"
---

It looks like Espressif Systems has a new powerful wireless microcontroller in the works, with the ESP32-S31 sharing some features of the ESP32-P4 and ESP32-S3 microcontrollers.
The ESP32-S31 is a dual-core RISC-V MCU with one high-performance core with FPU and SIMD instructions, and one low-power RISC-V core, featuring 62 GPIOs, a Gigabit Ethernet MAC, WiFi, Bluetooth, and 802.15.4 (Thread/Zigbee/Matter) wireless connectivity, and more.
ESP32-S31 preliminary specifications:
- MCU subsystem
- RISC-V HP (High-performance) RV32IMAFCP CPU with FPU, SIMD, etc.
- RISC-V LP (Low-power) MCU core
- Memory & Storage I/F
- 512 KB SRAM
- 32 KB RTC SRAM
- Support for external octal PSRAM and flash up to 64MB
- GPU – 2D Pixel Processing Accelerator (PPA)
- VPU – (M)JPEG codec support
- Peripherals
- Display I/F – Parallel LCD interface
- Camera I/F – MIPI-CSI with integrated ISP and parallel camera interface
- Audio – 2x I2S
- Networking
- Gigabit Ethernet
- 2.4 GHz WiFi 802.11 b/g/n
- Bluetooth
- 802.15.4 for Zigbee, Thread, and Matter
- USB – USB OTG
- Up to 62x GPIOs
- 4x MCPWM (Motor Control PWM)
- 4x UART, 2x I2C, 2x SPI
- ADC
- Touch sensor
- System timer (2 counters, 3 alarms)
- Low-power core peripherals – Analog input, UART, IC, SPI
- Security
- eFuse with key-purpose field
- Flash encryption (XTS-AES-128/256)
- Physical Memory Protection (PMP) with 128-byte granularity
- AES, SHA, RSA, ECC
- Misc – 40 MHz XTAL support
I put the specs above together from the ESP32 forum, as well as the esp32s31.peripherals.ld and soc_caps.h files in the ESP-IDF framework source code. They likely have some mistakes and omissions, so correct me in the comments if I missed something important.
There’s only one high-performance RISC-V core against two for the ESP32-P4, and the ESP32-S31 apparently lacks H.264 VPU, MIPI DSI, and MIPI CSI interfaces, so its multimedia capabilities are more limited. It’s still probably the most powerful wireless SoC from Espressif Systems so far, and it also comes with 62 GPIOs, more than any other ESP32 microcontroller, as well as Gigabit Ethernet.
Thanks to Loic for the tip.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
