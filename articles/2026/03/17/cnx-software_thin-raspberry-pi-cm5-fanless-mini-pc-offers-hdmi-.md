---
title: "Thin Raspberry Pi CM5 fanless mini PC offers HDMI video output, 2.5GbE + GbE, dual USB, M.2 Key-M socket"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/17/thin-raspberry-pi-cm5-fanless-mini-pc-offers-hdmi-video-output-2-5gbe-gbe-dual-usb-m-2-key-m-socket/"
published: "2026-03-17"
fetched: "2026-03-18T07:01:21.318862"
---

Waveshare “Gigabit / 2.5G Dual Ethernet Mini-Computer (B)” is a thin Raspberry Pi CM5 fanless mini PC with a 4K HDMI video output, 2.5GbE and Gigabit Ethernet RJ45 jacks, two USB ports, a microSD card slot, and USB-C power.
Internally, it features an M.2 Key-M socket for a 2230/2242/2280 NVMe SSD or AI accelerator, two MIPI DSI/CSI connectors for cameras or displays, and a 40-pin GPIO header. The flat cables for the MIPI devices can be passed through an opening under the HDMI and USB 2.0 ports of the metal case, and the GPIO headers are also accessible externally through a small cover under the enclosure.
Gigabit / 2.5G Dual Ethernet Mini-Computer (B) specifications:
- Main board – CM5-DUAL-ETH-BASE-B
- Supported SoMs – Raspberry Pi CM5 or CM5 Lite (and potentially other electrically compatible modules like the Banana Pi BPI-CM5 Pro, Radxa CM5, and Orange Pi CM5, but it’s not been tested or advertised by Waveshare)
- Storage
- MicroSD card slot
- M.2 Key-M (PCIe Gen 2.1/3 x1) socket for 2230/2242/2280 NVMe SSD.
- Video Output – HDMI 2.0 port up to 4Kp60
- Networking
- 2.5GbE RJ45 port; note: the Ethernet transceiver model is not listed, but the blurry photo of that side of the board (not added to this article) shows a Realtek module soldered to the board. I suspect it might be implemented through a USB 3.0 to 2.5GbE chip like the Realtek RTL8156BG
- Gigabit Ethernet RJ45 port
- USB
- USB 3.2 Gen 1 (5 Gbps) port
- USB 2.0 port
- USB Type-C port for power and eMMC flashing
- Misc
- Power button
- RTC battery connector
- Dual-color status LED
- Onboard BOOT switch (ON: eMMC flashing mode, OFF: normal operation)
- Power Supply – 5V via USB-C port
- Enclosure – Aluminum alloy case for fanless operation
- Accessories
- 5x pink thermal pads
- Silicone thermal pad for the optional SSD/AI accelerator
- Screwdriver and screws pack
- Dimensions – 101 x 62 x 23.40 mm
Note that WiFi and Bluetooth are possible in theory through the wireless module on the Raspberry Pi CM5, but I don’t see any antenna openings in the metal case, so it would require drilling holes for external antennas, and even then, routing the antenna cables might be tricky since it looks tight. Better find another solution if you need to use WiFi and/or Bluetooth.
The “Gigabit / 2.5G Dual Ethernet Mini-Computer (B)” supports Raspberry Pi OS. The documentation is up and points to instructions to flash the OS, enable the SSD and SSD boot, install and configure MIPI DSI/CSI, configure the RTC, and adjust fan settings, although the latter is not applicable for this specific product…
The company has released other CM5-DUAL-ETH-BASE and CM5-DUAL-ETH-4G/5G-BASE boards in the past, but their design are completely different from the “B” version used here.
The closest thin Raspberry Pi CM5 fanless system with dual Ethernet and HDMI I could find is the IRIV EdgeAI CM5, but it also includes an AI accelerator, lacks 2.5GbE, and it’s pricier as an industrial-grade device. You’d have many more options if you go beyond the Raspberry Pi ecosystem and don’t need MIPI CSI/DSI support, with products such as the NanoPi R76S or Banana Pi BPI-M7 with the official metal case, or even some x86 mini PC, although pricing is usually a little higher with this feature set.
Waveshare sells the “Gigabit / 2.5G Dual Ethernet Mini-Computer (B)” kit for $86.39 on AliExpress, $98.99 on Amazon, and $72.99 on their own shop. The Raspberry Pi CM5/CM5 Lite and accessories, like a 5V/5A power supply, are not included, so you’d need to purchase those separately.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
