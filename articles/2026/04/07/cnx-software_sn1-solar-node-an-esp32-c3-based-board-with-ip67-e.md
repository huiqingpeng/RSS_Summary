---
title: "SN1 Solar Node – An ESP32-C3-based board with IP67 enclosure, solar charging, ESPHome firmware"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/04/07/sn1-solar-node-an-esp32-c3-based-board-with-ip67-enclosure-solar-charging-esphome-firmware/"
published: "2026-04-07"
fetched: "2026-04-08T07:01:17.795664"
---

Designed by Granz Scientific LLC, the SN1 Solar Node is an ESP32-C3-based IoT node/development board designed specifically for off-grid IoT projects. Development boards like Seeed Studio Wio Tracker, or industrial controllers like DFRobot LoRaWAN Control Terminal, allow you to handle your own battery management and weatherproofing, or on the other end, you have products like SenseCAP Solar Node P1 that come with everything integrated but do not allow adding custom hardware.
This is where the SN1 Solar Node is different; it features an IP67-rated enclosure with an integrated solar panel on the lid, 18650 battery support, and prototyping strip-board areas for custom circuitry. It also includes a smart power switch that allows the battery to continue charging from the solar panel even when the board is powered off. Additionally, it provides battery voltage monitoring, breaks out most GPIOs for easy access, and includes optional jumpers for an onboard LED and temperature sensor. The board supports either a single or dual 18650 battery configuration (at the cost of prototyping space), and can be powered or charged via solar or USB-C, making it suitable for remote IoT deployments such as environmental monitoring, smart agriculture, and distributed sensor networks.
SN1 Solar Node specifications:
- Core module – ESP32-C3-WROOM-02U
- SoC – ESP32-C3 single-core RISC-V processor @ 160 MHz with 2.4 GHz WiFi 4 and Bluetooth 5.0 LE
- Storage – 4MB QSPI flash (typical)
- External antenna U.FL connector
- USB – USB-C port for programming, power, and charging
- Expansion
- 16-pin GPIO header with UART, I2C, power, and I/O
- Dedicated prototyping strip-board area for custom sensor integration
- Jumpers (J5, J6, J7) for connecting an onboard thermistor (TH1) and an indicator LED (LED1)
- Misc
- SPDT power toggle switch
- Onboard LED
- Onboard thermistor (TH1)
- “CHRG” and “DONE” indicator LEDs (LED2, LED3)
- Voltage divider for battery voltage measurement
- Power
- 5V from USB-C port
- Holders for 1x or 2x 18650 lithium-ion batteries
- Solar panel mounted on the enclosure lid
- Texas Instruments TPS63802 Buck-Boost Converter (U2) supplying +3.3V
- Consonance CN3163-ESOP8 solar/battery charger IC (U6)
- Battery protection circuitry featuring dual DW01A ICs (U4, U5) paired with FS8205A dual N-channel MOSFET
- Dimensions – TBD
- Enclosure – IP67-rated waterproof enclosure
The SN1 Solar Node comes pre-programmed with ESPHome firmware out of the box, with ready-to-use YAML configuration files available on GitHub for Home Assistant integration. Since it is based on the ESP32-C3, it also supports the standard Espressif ESP-IDF framework and Arduino Core, implements low-power modes, and interfaces with sensors and peripherals through widely supported software ecosystems.
The SN1 Solar Node is currently available on Tindie for $49.99 in either single- or dual-18650 holder configuration. The developer notes that batteries are not included with the product, and only button-top 18650 cells are supported, as flat-top batteries will not work with the provided holders.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
