---
title: "SparkFun OpenScale IoT – An ESP32 board with HX711 ADC for smart scales with WiFi and Bluetooth connectivity"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/16/sparkfun-openscale-iot-an-esp32-board-with-hx711-adc-for-smart-scales-with-wifi-and-bluetooth-connectivity/"
published: "2026-03-16"
fetched: "2026-03-17T07:00:59.801573"
---

The SparkFun OpenScale – IoT project is a ready-to-use ESP32-based IoT smart scale with open-source hardware and firmware support that makes it easy to read precise weight data from load cells without writing custom code from scratch for basic operation.
It handles amplification via the HX711 24-bit ADC, calibration, temperature compensation (using the onboard TMP102 and an optional external DS18B20 probe), and serial output/configuration through a simple text-based menu. It also features Wi-Fi for live data and OTA firmware updates, requiring no dedicated apps—just standard terminal tools and a browser for viewing data. Additionally, there is a Qwiic I²C connector for adding extra sensors or displays. The board operates from 5 V with a typical current consumption of 80 to 100 mA, supports selectable output data rates of 10 or 80 SPS, and includes an adjustable gain for accurate measurements in long-term monitoring setups.
SparkFun OpenScale – IoT Specifications:
- Wireless module – ESP32-PICO-MINI with 2.4GHz WiFi, Bluetooth/BLE with an on-chip PCB antenna
- Load Cell – HX711 24-bit ADC load cell amplifier with support for 4- or 5-wire load cell
- Sensors
- Onboard TMP102 digital temperature sensor (I²C)
- 3-pin screw terminal for an optional external DS18B20 1-wire sensor
- USB – USB Type-C port for power and serial configuration (via CH340C USB-to-Serial converter)
- Expansion – SparkFun Qwiic connector
- Misc
- Power, Status, TX, and RX LEDs
- Reset and Boot buttons
- Optional external serial interface (TX1, RX1, 5V and GND)
- Selectable data rate (default 10SPS or 80SPS via an open jumper)
- Power
- Operating Voltage – 5 V input
- Consumption – 80–100 mA typical
- onboard RT9080 3.3 V regulator (for ESP32)
- Dimensions – 55.88 x 46.99 mm (2.2 x 1.85-inch)
The original SparkFun OpenScale is also an open-source hardware development board (based on an ATMega328P) created by SparkFun, designed to make reading, calibrating, and configuring load cells (weight sensors) as easy as possible. It lacks wireless connectivity and offers similar functionality to another STC89C52 + HX711 digital scale kit we covered in 2017.
The OpenScale IoT board is plug-and-play and designed so you don’t need custom Arduino sketches to get baseline readings. You can connect to the board via Bluetooth/BLE (Note: Apple devices are not supported for BT terminal configuration) or through a wired USB-C serial connection at 115,200 bps. Additionally, the board can connect to a local 2.4 GHz WiFi network to view live data streams and perform Over-The-Air (OTA) firmware updates. SparkFun also provides the KiCad hardware files, schematics, and Arduino firmware as open-source resources available on their GitHub repository, where you’ll also find detailed documentation.
After WiFi setup (via the serial menu over Bluetooth or USB), the board connects to your 2.4 GHz network and streams live weight/temperature data (read-only) to any device/browser on the network, and supports OTA firmware updates.
By the looks of it, this board is mainly designed for industrial environments where constant weight monitoring is essential. This type of ESP32-based HX711 board for digital scales has been around for a few years, one example being the TTGO T-Weigh ESP32 board, which also provides LoRa/LoRaWAN connectivity.
While writing, I came across Oliexdev’s openScale project on GitHub, which is also an open-source Android application designed to track body weight and health metrics, and is compatible with a range of commercial Bluetooth smart scales. However, though the name is the same, the SparkFun OpenScale project is completely different and is not compatible with this app.
The SparkFun OpenScale IoT is available now on the SparkFun store for $44.95 plus shipping. For users who do not need wireless connectivity, the original ATmega328P-based OpenScale is still available for $34.95, and alternatively, the LoRaWAN-connected Lilygo T-Weigh board goes for about $32 on AliExpress. The video below shows a demonstration of load cell setup, calibration, and weight measurement using the original ATmega-based OpenScale board (not the new IoT variant).
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
