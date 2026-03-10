---
title: "Makerfabs CM0IQ – An ultra-compact (42x36mm) Raspberry Pi CM0 Lite board"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/10/makerfabs-cm0iq-ultra-compact-42x36mm-raspberry-pi-cm0-lite-board/"
published: "2026-03-10"
fetched: "2026-03-10T15:33:15.244704"
---

The CM0IQ is an ultra-compact board based on the Raspberry Pi CM0 Lite Compute Module. It measures just 42 × 36 mm and squeezes multiple interfaces into a 15.1 cm² footprint, making it suitable for space-constrained applications such as robotics, IoT devices, and custom hardware integrations.
Despite being smaller than a Raspberry Pi Zero 2 W (19.5 cm²), the CM0IQ manages to include a full-sized USB-A port, a Micro HDMI port, and 4-lane MIPI CSI and DSI connectors. To fit everything into this small footprint, the designer also relied on a 1.27 mm 40-pin GPIO header rather than the standard 2.54 mm header. The board also features a USB Type-C for power, a microSD card slot for storage, 5V solder pads for power input, and four M2 mounting threads.
Raspberry Pi CM0IQ Specifications:
- SoM – Raspberry Pi CM0 Lite
- SoC – Broadcom BCM2710A1
- CPU – Quad-core Cortex-A53 processor @ 1.0 GHz
- GPU – VideoCore IV GPU supporting OpenGL ES 1.1, 2.0 graphics
- VPU – H.264/MPEG-4 1080p30 video decoding, H.264 1080p30 video encoding
- System Memory – 512MB LPDDR2 RAM
- Storage – 0GB (Raspberry Pi CM0 Lite)
- Wireless – 802.11 b/g/n WiFi 4, Bluetooth 4.2 LE (same module as on Pi Zero 2 W) with IPEX antenna connector
- SoC – Broadcom BCM2710A1
- Storage – MicroSD card slot
- Display Interfaces
- Micro HDMI video output
- 4-lane MIPI DSI connector
- Camera Interface – 4-lane MIPI CSI connector
- Networking – Wi-Fi and Bluetooth on SoM (onboard IPEX antenna connector)
- USB
- USB Type-C port (power and USB gadget mode)
- USB-A host port
- Expansion – 40-pin GPIO header (Raspberry Pi compatible, 1.27 mm pitch)
- Misc – DIP switch for boot mode and USB routing
- Switch 1 – Toggles normal operation vs. pulling nRPI_BOOT low
- Switch 2 – Routes USB data to either the USB-C port or the USB-A port.
- Power input – 5V via USB-C or solder pads
- Dimensions – 42 × 36 mm (15.1 cm²)
- Mounting – Four M2 threaded standoffs
The developer provided a table comparing the CM0IQ with the official Raspberry Pi Zero 2 W, highlighting the trade-offs made to reduce the footprint by over 22%.
| Feature | CM0IQ | RPi Zero 2 W |
|---|---|---|
| Dimensions | 42x36mm (15.1 cm²) | 65x30mm (19.5 cm²) |
| Camera | CSI 4-lane | CSI 2-lane |
| Display | DSI 4-lane | None |
| HDMI | Micro-HDMI | Mini-HDMI |
| USB Host | USB-A connector | Micro-USB (adapter required) |
| GPIO Header | 40-pin 1.27mm pitch | 40-pin 2.54mm pitch |
| Antenna | IPEX-1 antenna connector | Integrated PCB antenna |
On the software side, the bpard runs Raspberry Pi OS, but Makerfabs mentions that MIPI DSI displays and CSI cameras are not automatically detected by the OS, so you need to manually add the appropriate overlays to the /boot/config.txt file
|
1 2 |
dtoverlay=vc4-kms-dsi-ili9881-5inch # 5" Raspberry Pi Touch Display 2 dtoverlay=imx708; # Raspberry Pi Camera Module 3 |
There is also a mechanical warning from the developer saying that the M2 threaded standoffs have a maximum depth of 2mm. Screwing in mounting hardware deeper than 2mm can permanently damage the PCB. The official 5-inch Raspberry Pi Touch Display 2 requires a separate 5V power connection, which must be pulled from the GPIO or the corner solder pads.
The Raspberry Pi CM0IQ can be purchased on Makerfabs for $49.00. Additional documentation, including pinout diagrams and high-resolution images, can be found on the project’s GitHub repository.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
