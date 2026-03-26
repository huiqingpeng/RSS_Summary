---
title: "picoZ80 – A Z80 microprocessor drop-in replacement based on Raspberry Pi RP2350B and ESP32"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/26/picoz80-a-z80-microprocessor-drop-in-replacement-based-on-raspberry-pi-rp2350b-and-esp32/"
published: "2026-03-26"
fetched: "2026-03-27T07:00:19.317074"
---

The picoZ80 board is a drop-in replacement for the Z80 microprocessor based on the Raspberry Pi RP2350B dual-core Cortex-M33 microcontroller and an ESP32 wireless SoC for WiFi and Bluetooth connectivity.
My first computer was a ZX81 powered by a Zilog Z80 microprocessor, which was eventually phased out in 2024 after almost 50 years of production. But retro computing enthusiasts keep the platform alive, usually with softcore FPGA implementations such as MiSTer. The picoZ80 is different as it relies on the programmable I/O (PIO) state machines from the RP2350B MCU to reproduce cycle-accurate address, data, and control buses of the Z80 MPU.
picoZ80 specifications:
- MCU – Raspberry Pi RP2350B
- CPU – Dual-core Arm Cortex-M33 CPU @ up to 150/300 MHz (the two RISC-V cores do not appear to be used by the project)
- Memory – 520KB SRAM
- Storage – 8KB OTP flash
- Package – QFN-80
- Memory – 8MB PSRAM
- Storage
- 16MB flash
- MicroSD card slot (via ESP32)
- Wireless – WiFi and Bluetooth via ESP32 chip and ceramic antenna
- USB – Micro USB port for flashing RP2350 and ESP32 firmware
- Host interface – Z80 DIP-40 CPU socket of any legacy Z80-based computer; tested on several Sharp MZ machines.
A single human-readable config.json configurable file stored on a microSD card enables the user to reconfigure the board’s memory map, ROM images, or driver selection without having to recompile the firmware. That means you could switch the board from one model to another machine just by changing the JSON file.
Philip Smart also explains that a set of personas is being developed to provide features such as banked RAM/ROM, floppy disk emulation (WD1773), QuickDisk emulation, ROM Filing System, and TranZPUter Filing System. Examples of personas include MZ-700, MZ-80A, MZ-80B, MZ-800, other Sharp machines, and the Amstrad PCW.
The ESP32 enables WiFi connectivity to access a web interface to configure the system, manage files, perform OTA firmware updates, and select the persona matching your hardware.
The picoZ80’s hardware and firmware documentation provides great details about the project. However, it does not look like it has been open-sourced just yet, and an article on X states that the “code and schematics will be open-sourced soon on GitHub”.
It’s not available for sale just yet. You’ll be able to made you own soon, as the picoZ80 hardware design (schematics, PCB layout, KiCad files), firmware, and all associated software will be made available for personal, educational, and non-commercial use. However, any commercial product based on the design will require written permission from Philip Smart.
Via Adafruit
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
