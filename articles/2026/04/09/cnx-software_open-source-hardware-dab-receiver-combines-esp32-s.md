---
title: "Open-source hardware DAB+ receiver combines ESP32 SoC with Skyworks SI4684 digital radio chip"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/04/09/open-source-hardware-dab-receiver-combines-esp32-soc-with-skyworks-si4684-chip/"
published: "2026-04-09"
fetched: "2026-04-10T07:04:34.035039"
---

When I wrote about a DIY ESP32-S3 internet radio last week, “raspbeguy” commented he’d rather choose an ESP32-based DIY DAB+ receiver kit, such as the one offered by the PE5PVB project based on a Skyworth SI4684 receiver.
I first heard about DAB (Digital Audio Broadcast) in 2003 when we considered adding it to a CD player. It’s basically the digital equivalent of analog FM/AM radios, and I haven’t heard much about it since DAB and the “new” DAB+ standard are mostly a European story (see coverage map below). PE5PVB’s open-source hardware DAB receiver might still be worth a look.
PE5PVB’s SI4684 ESP32 DAB+ receiver features:
- Controller – ESP32 microcontroller with WiFi and Bluetooth (DoIT ESP32 devkit v1)
- Storage – MicroSD card slot
- Display – Color LCD screen with 320×240 resolution (SPI)
- Audio
- 2x RCA connectors for speakers
- 3.5mm headphone jack with amplifier
- DAB+ receiver – Skyworks SI4684 loaded with DAB+ firmware at startup.
- Misc – 2x rotary encoders, 3x push buttons
- Top encoder – Frequency or memory channel
- Bottom encoder – Service or set headphones’ volume
- Top button – Short press: Service information; long press: Stand-by mode
- Middle button – Short press: Set mode; long press: Open menu
- Lower button – Toggle slideshow view.
- Power Supply – 12V DC input
As mentioned in the introduction, most of Europe has DAB+ coverage (I understand the DAB is still being used in the UK), but DAB+ should also be available in Australia, South Korea, and a few countries in the Middle East and North Africa. For other countries, you’d need some test equipment to generate DAB+ signals…
The project is fully open-source with the KiCad hardware design files (schematics and PCB layout) for the ESP32 controller board and mainboard (SI4684), Gerbers, 3D files for the enclosure, and the PlatformIO/Arduino firmware, all available on GitHub. It’s going to be quite more complicated than simply loading Arduino firmware like for the ESP32 Internet Radio, as you’ll need to order the PCBs and components, solder the components, print the enclosure, and assemble everything first.
Since the project is about 2 years old, I thought I might find it on AliExpress, but the radio above is not listed there. Instead, another PV5PVB project looks more popular: “TEF6686 with ESP32” with FM/LW/MW/SW radio support, which offers similar features to the LILYGO T-Embed SI4732 ESP32-S3 development board we wrote about last year. It’s sold on AliExpress for about $40 and up.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
