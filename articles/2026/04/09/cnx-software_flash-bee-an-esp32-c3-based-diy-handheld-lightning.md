---
title: "Flash Bee – An ESP32-C3-based DIY handheld lightning detector"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/04/09/flash-bee-an-esp32-c3-based-diy-handheld-lightning-detector/"
published: "2026-04-09"
fetched: "2026-04-10T07:04:36.305949"
---

Flash Bee is an easy-to-make DIY handheld lightning detector based on off-the-shelf parts such as the XIAO ESP32C3 board and the Round Display for XIAO, as well as a 3D-printed enclosure.
The design relies on the AMS AS3935 Franklin lightning sensor that’s been around for years, and found in kits like Sparkfun’s Arduino IoT weather station, which is capable of detecting lightning up to 40 km away with 1km accuracy. While it’s not quite new technology, I found the Flash Bee design to be rather cute and convenient, and it looks really easy to reproduce.
Flash Bee key components:
- Seeed Studio XIAO ESP32-C3 with Wi-Fi 4 & Bluetooth LE 5.0 connectivity ($4.90)
- Round Display for XIAO – 1.28-inch touchscreen display with 240×240 resolution, 65K colors, 100 Hz refresh rate ($18)
- Grove Lightning Sensor AS3935 ($26.90, alternative link if out of stock)
- 3.7V 400mAh LiPo battery
- Slide switch
- 2x M2 5mm and 2x M3 10mm screws
- Connecting wires
- B7000 glue
- 3D printed antenna cover, back body, front cover, and add-on.
Some soldering is required, but it’s minimal, notably to wire the AS3935 module to the ESP32-C3 board and for the battery and related switch. You’ll also need a 3D printer for the plastic parts. It should probably cost around $60 in hardware costs. You’ll find instructions and 3D files on Instructables.
On the software/firmware side, an Arduino sketch is provided on the same page. It relies on the Seeed_Arduino_RoundDisplay and Seeed_GFX libraries. The interface displays the strike distance, a strike energy + indicator, a strike count, and the strike energy history. There’s also an overhead strike alert, and the device is said to last about 6 to 7 hours on a charge.
Watch the video below for an overview of the project, assembly instructions, and demos.
Via XDA Developers
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
