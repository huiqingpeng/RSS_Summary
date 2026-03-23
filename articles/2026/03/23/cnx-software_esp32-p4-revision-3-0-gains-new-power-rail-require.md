---
title: "ESP32-P4 revision 3.0 gains new power rail, requires new PCB design and firmware"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/23/esp32-p4-revision-3-0-gains-new-power-rail-requires-new-pcb-design-and-firmware/"
published: "2026-03-23"
fetched: "2026-03-24T07:01:16.154313"
---

Espressif’s ESP32-P4 revision 3.0 and greater converts pin 54 of the chip from NC (non-connected) to a power rail (VDD_HP_1), requires a few extra passives, and an updated firmware.
Espressif Systems first unveiled the 400 MHz ESP32-P4 dual-core RISC-V SoC in January 2023, and the official ESP32-P4-Function-EV development board was launched in August 2024, with commercial solutions slowly ramping up last year. You’d think the silicon and related hardware would now be frozen, but apparently not.
The pin 54 was likely converted from NC (not connected) to VDD_HP_1 to improve the stability of the high-performance digital domain. The old revisions 1.0, 1.1, and 1.3 are not recommended for new designs, and the company advises people to use revision 3.0 or 3.1. They also provided updated reference schematics with the following key changes:
The main differences between chip revisions v1.0/v1.3 (not recommended for new designs) and v3.0 and later versions include the definition of pin 54, the 1 MΩ resistor on the DP pin, the two 499 kΩ resistors and one 22 pF capacitor in the DCDC circuit.
The last two diagrams do not require a new PCB layout, as it’s just a matter of adding or removing components, but the new VDD_HP_1 pin and components around it may require a new PCB layout or an ugly rework with a few wires and components. [Update: on a positive side, a Rev 3.x PCB should also work with an ESP32-P4 Rev 1.x SoC. See comments section]
Since Rev 3.x is a major revision of Rev 1.x, the firmware needs to be recompiled as well by setting CONFIG_ESP32P4_REV_MIN accordingly in the ESP-IDF framework. Most vendors sell the ESP32-P4 as “ESP32-P4” so it’s not always obvious to find out which exact revision you will get. The revision is embedded in the manufacturing code, where Revision 3.0 shows as XFXX and Revision 3.1 as XGXX.
Via Hackaday
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
