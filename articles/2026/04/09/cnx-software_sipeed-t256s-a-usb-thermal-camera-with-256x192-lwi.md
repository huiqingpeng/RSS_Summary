---
title: "Sipeed T256s – A USB thermal camera with 256×192 LWIR sensor, 640×480 AI super resolution"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/04/09/sipeed-t256s-a-usb-thermal-camera-with-256x192-lwir-sensor-up-to-640x480-super-ai-resolution/"
published: "2026-04-09"
fetched: "2026-04-10T07:04:35.395499"
---

Sipeed T256s is a portable USB thermal camera equipped with a native 256×192 Long-Wave Infrared (LWIR) sensor and a built-in 2.4 TOPS NPU for hardware-level AI super-resolution (ISR) up to 640×480 resolution in real time, effectively suppressing image noise without external software.
The UVC camera device supports standard output (Y16 raw and MJPEG) and features both male and female USB Type-C ports on opposite ends for connection to PCs and smartphones. It also includes a 1.69-inch touchscreen for standalone operation with live viewing, palette switching, hotspot tracking, and image capture. Other features include an optional macro lens (~5 cm focus) for inspecting small components, internal storage for snapshots, <50 mK thermal sensitivity, a 25 Hz frame rate, and a durable CNC aluminum enclosure for efficient heat dissipation. The device is designed for electronics R&D, industrial maintenance, and HVAC diagnostics.
Sipeed T256s specifications:
- SoC – Axera AX620Q (updated, see comments section);
Probably based on an Allwinner V831/V833 (or a very close derivative) from the Maix-II family.- CPU- Dual-core Cortex-A53 processor
- AI Accelerator – Built-in 2.4 TOPS NPU for 2.5x AI Super-Resolution (ISR), outputting 640 × 480 locally
- Storage – 32MB internal NAND storage (capacity for ~1,500 snapshot images)
- Display – 1.69-inch 240×280 IPS full-color capacitive touchscreen
- Camera
- Sensor – 256 × 192 native resolution @ 14-bit (Y14) Long-Wave Infrared (LWIR) module
- Lens – Optional detachable macro lens with a 5cm working distance (ideal for PCB inspection)
- Thermal
- Temperature range – -15°C to 500°C (Auto-switching: High-Accuracy mode -15°C to 150°C; Wide-Range mode 50°C to 500°C)
- Accuracy – ±2°C or ±2% of reading
- Sensitivity (NETD) – < 50 mK @ 25°C
- Frame rate – 25 Hz
- Field of view (FOV) – 56° × 42°
- Video formats – MJPEG (pseudo-color image) and Y16 (14-bit raw temperature data) support
- USB
- 1x USB Type-C male port (for direct connection to phones/tablets)
- 1x USB Type-C female port (for connecting to power banks, PCs, or daisy-chaining)
- UVC (USB Video Class) plug-and-play protocol support
- Misc
- 6 switchable color palettes
- 3-spot temperature display (Center, Hot, Cold)
- Digital zoom
- Gallery browser
- Power – 5V via USB Type-C (a stable 5V power supply is critical, or boot loops or screen flickering may occur)
- Dimensions
- 42 x 35 x 14 mm (main body)
- 42 x 42 x 14 mm (including Type-C connector)
- Housing – CNC unibody machined 6061 Aluminum Alloy
We have previously written about various types of thermal cameras, like the HT-102 thermal camera for Android phones, and very advanced modules like Lepton XDS and Luxonis OAK Thermal, but what makes the T256s different is its dual-mode capability. When connected to a power bank via the top USB Type-C female port, the device operates entirely standalone, and you can interact with the touchscreen to switch palettes, track temperatures, and snap photos directly to the internal storage.
But when it connects to a Windows machine, iPad, Android phone, or Raspberry Pi, the T256s supports UVC (USB Video Class) out of the box, meaning it requires no proprietary drivers. It mounts immediately as a standard webcam (/dev/videoX on Linux). It also mounts as a mass storage flash drive, where you will find the saved snapshots, which are named with the temperature data embedded right in the filename (e.g., P001_T32.5_L28.2_H45.6.jpg).
Sipeed provides two video streams over UVC: a MJPEG stream for standard colorized video previews and a Y16 stream containing raw 14-bit grayscale sensor data. Additionally, the company also provides Python snippets using Numpy to convert the raw Y16 stream directly into precise Celsius readings. This is useful for those looking to integrate the camera into custom machine vision pipelines or automated testing rigs. More information, including a user guide, quick start guide, and FAQ, is available on the Wiki.
An optional macro lens that focuses as close as 5cm is also available and makes it easy to map the heat distribution of tiny 0402 or 0201 SMD resistors to hunt down PCB shorts. Note: The FAQ states that the device may periodically freeze with a faint clicking sound. This is due to “NUC shutter calibration,” a standard process that compensates for thermal drift.
The Sipeed T256s AI UVC thermal camera is available on AliExpress for $219.12.
T256S #AI #Thermal Camera with embedded real time Super-Resolution coming out!
2.4T NPU, real time 256×192 -> 640×480, Micro-scale Meticulous Detail~
Support standalone/phone plugin/PC/SBC multi-platform, support raw data read!
Check it out: https://t.co/RaVePxFkjG pic.twitter.com/j3t6Vamm8d— Sipeed (@SipeedIO) April 9, 2026
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
