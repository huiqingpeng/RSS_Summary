---
title: "Clintech Pico – The first Raspberry Pi RP2354B board offers 48 GPIOs in Raspberry Pi Pico form factor"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/19/clintech-pico-raspberry-pi-rp2354b-board-raspberry-pi-pico-form-factor/"
published: "2026-03-19"
fetched: "2026-03-19T20:03:22.751170"
---

Designed by Clintech Ltd. in Bulgaria, the Clintech Pico Board appears to be the first development board based on the Raspberry Pi RP2354B chip with 2MB on-chip memory. It retains the same form factor as a Raspberry Pi Pico 2 but adds extra GPIOs to make use of the 48 general-purpose GPIOs provided by the RP2354B chip.
Like the Raspberry Pi Pico 2, this board features 40 castellated and through holes on the sides, exposing GPIOs 0–22 and 26–28, along with 3 debug pins. Additionally, the board includes 27 extra on-board through holes that break out the remaining GPIOs (23–25 and 29–47) as well as the QSPI interface (SD0–SD3 and SCLK) for external memory.
Clintech Pico specifications:
- SoC – Raspberry Pi RP2354B
- CPU
- Memory – 520 KB on-chip SRAM
- Storage – 2MB of stacked (in-package) flash memory
- Storage – Up to 16 MB of external QSPI flash or PSRAM via 4x through holes on the bottom
- USB – USB Type-C port for power and data
- Expansion
- 2x 20-pin headers with GPIO, UART, SPI, I2C, PWM, and ADC
- 27x additional on-board through-holes for all GPIOs and QSPI
- I/Os above include 3x PIO blocks, 12x PIO (Programmable IO) state machines
- Debugging – 3-pin SWD debug interface
- Misc – Boot Select button, onboard LED (GPIO25)
- Power
- 5V input via USB-C (VBUS) or VSYS rail
- Onboard 3.3V LDO regulator (up to 500 mA)
- Dimensions – 51 x 21 mm (4-layer ENIG PCB, compatible with Raspberry Pi Pico / Pico 2 modules)
- Temperature
- Operating – TBD
- Storage – 15°C and 25°C (according to the board’s datasheet, potentially overly conversative…)
- Humidity – Between 30% to 60%
- Compliance – RoHS (Directive 2011/65/EU) and EMC (Directive 2014/30/EU) compliant
Like other pico boards, it runs a standard bootloader that supports UF2 drag-and-drop firmware flashing over USB mass storage mode by holding the BOOTSEL button during connection. It is also compatible with the standard Raspberry Pi Pico C/C++ and MicroPython SDKs.
Previously we have written about various Raspberry Pi Pico compatible boards like the Nexus RP2350 LiPo, which adds battery support, the Waveshare RP2350 CAN, which adds an MCP2515 CAN Bus controller, the CPico RP2350 is another development board with a USB-C port, 8MB flash, 2MB PSRAM, a Reset button, and Bconnect I2C and debug ports, there was also the Pico W5 which adds dual-band (2.4GHz/5GHz) WiFi 4 and Bluetooth 5.0 connectivity through a B&T BW16 wireless module. The Clintech Pico is the first board to rely on the new Raspberry Pi RP2354B microcontroller and offer 48 GPIOs, helped with the space saved by the on-chip 2MB flash.
The Clintech Pico is available on Tindie for $20, with worldwide shipping offered from Bulgaria via standard postal services. More information about the product, mostly the datasheet, can be found on Clintech’s website.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
