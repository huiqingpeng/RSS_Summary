---
title: "NASA Artemis Watch 2.0 – An ESP32-S3-powered, NASA-inspired wearable kit for education"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/04/07/nasa-artemis-watch-2-0-an-esp32-s3-powered-nasa-inspired-wearable-kit-for-education/"
published: "2026-04-07"
fetched: "2026-04-08T07:01:19.420097"
---

CircuitMess NASA Artemis Watch 2.0 is a programmable, NASA-themed smartwatch based on an ESP32-S3 WiFi and Bluetooth module and a 1.14-inch monochrome display.
The watch also features an accelerometer, a gyroscope, a buzzer, an RTC, a button, several LEDs, and a USB port for programming and charging the built-in 600 mAh battery.
NASA Artemis Watch 2.0 specifications:
- Core module – ESP32-S3-MINI-1-N4R2
- SoC – ESP32-S3 dual-core Xtensa LX7 processor with WiFi 4 and Bluetooth 5.0 connectivity
- Memory – 2MB PSRAM
- Storage – 4MB QSPI flash
- PCB antenna
- Display – Built-in 1.44-inch display
- USB – 1x USB Type-C port for charging and programming
- Sensors
- 6-axis LSM6DS3TR accelerometer and gyroscope
- Temperature sensor (TBC)
- Misc
- Lever button
- 6x user LEDs, 1x power LED, 1x RGB LED
- Buzzer
- RTC + backup battery
- Power Supply
- 5V via USB-C port
- 600 mAh LiPo battery, good for 2 to 3 hours on a charge
- Dimensions and Weight – TBD
Documentation is all over the place, but I could reconstruct the specifications based on the PDF schematics released on the “build guide” page. The user needs to install the Bangle.js Gadgetbridge app for Android (so iOS is not supported?) on a smartphone and pair the watch via Bluetooth. The watch can then receive notifications, report fitness data, and so on. Some apps are preinstalled and can be selected using the lever button. The video embedded below serves as a user guide. Note that it’s for the first-generation Artemis Watch, but I understand both are nearly identical. The first version was sold as a kit to be assembled, while the Watch 2.0 comes fully assembled and ready to use.
As mentioned in the introduction, the watch is also programmable, and as an education kit, you can do that through the CircuitBlocks visual programming IDE. You can design your own custom watch faces, create interactive games, or even develop your own applications for the watch. The source code is on GitHub, but the repository has been read-only for a few years. The main page is now code.circuitmess.com.
NASA Artemis Watch 2.0 sells for $129 / 169 Euros on the CircuitMess store, with the Euro price including VAT for European users.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
