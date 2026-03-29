---
title: "PineTime Pro smartwatch to feature dual-core Cortex-M33 MCU, 2.13-inch AMOLED, GPS, and more"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/30/pinetime-pro-smartwatch-to-feature-dual-core-cortex-m33-mcu-2-13-inch-amoled-gps/"
published: "2026-03-29"
fetched: "2026-03-30T07:02:26.258475"
---

Pine64 has announced progress on the PineTime Pro smartwatch, powered by a dual-core Cortex-M33 microcontroller with Bluetooth 5.2 Classic and LE and 800KB SRAM. The watch also features a 2.13-inch AMOLED display, GPS support, a heart rate monitor, and a 6-axis motion sensor.
It’s an upgrade to the PineTime project unveiled in September 2019, and one of the most popular Pine64 devices thanks to open-source software projects such as InfiniTime firmware. For reference, the PineTime ships with a Nordic nRF52 Arm Cortex-M4 Bluetooth MCU with 64 KB SRAM, a 1.3-inch display, and basic HRM and accelerometer. The PineTime Pro is a massive upgrade that should support a wider range of firmware.
PineTime Pro specifications:
- SoC – Unnamed wireless MCU
- CPU – Arm Cortex-M33 MCU @ up to 200 MHz
- Memory – 800 KB SRAM
- Wireless – Bluetooth 5.2 Classic (BR/EDR) & Low Energy (additional Cortex-M33)
- Memory – 8 MB PSRAM
- Storage – 8 MB QSPI flash
- Display – 2.13-inch AMOLED touch screen display with 502 x 410 resolution
- Audio – Microphone and speaker
- GNSS – GPS supported
- Sensors
- Heart rate sensor with blood oxygen measurement capability
- 6-axis IMU (Inertial Measurement Unit) sensor
- Misc
- Digital crown that also acts as an extra button
- Vibration motor
- Power Supply / Debug
- 4-pin connector for power and debugging (SWD)/programming
- I²C battery charger
- Dimensions – TBD
The PineTime Pro will benefit from both InfiniTime and WaspOS firmware available for the PineTime, as developers are already on it. It should be much easier to add new features with the extra SRAM, PSRAM, and flash. It could also eventually support PebbleOS, although nobody seems to officially work on a port at this time.
Pine64 views the PineTime and PineTime Pro as two different product offerings, and both will continue to exist, although more resources may now be dedicated to the Pro model.
Besides the specifications, Pine64 developers didn’t expand too much on the source of the microcontrollers, but it looks to be a custom chip for smartwatches, and the SDK will be open:
Things became much more concrete when PineStore started collaborating with a large smartwatch manufacturer in China that had developed its own chip. That collaboration has been very valuable so far: PineStore and the community have been working together on the hardware design, and documentation and SDK materials have been shared to help software development move forward. All of these resources will also be available to the community once the device enters production.
Some large watch manufacturers in China include Huawei, Xiaomi, Imoo, and Huami, but I was unable to find any watch with a dual-core Cortex-M33 MCU and 800 KB SRAM. A Huawei/HiSilicon chip would complicate distribution outside of China, so it’s unlikely to be used in the PineTime Pro, which narrows the list somewhat. In any case, we’ll have to wait and see to get more details.
We have no information about the launch date either, as it’s still early, with low-level drivers and demo code still being worked on. Hopefully, it will launch later this year. A few more details can be found in the announcement.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
