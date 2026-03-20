---
title: "8-inch ESP32-P4 touch display offers WiFi 6, BLE, 802.15.4 connectivity, optional 4G LTE and LoRaWAN"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/20/8-inch-esp32-p4-touch-display-offers-wifi-6-ble-802-15-4-connectivity-optional-4g-lte-and-lorawan/"
published: "2026-03-20"
fetched: "2026-03-20T14:03:00.621184"
---

Seeed Studio’s reTerminal D1001 is an 8-inch capacitive touch display powered by an ESP32-P4 RISC-V microcontroller and equipped with an ESP32-C6 wireless module, a camera, a dual-microphone array, and a speaker.
The reTerminal D1001 is a fully enclosed solution designed for HMI applications such as control panels, vision-enabled IoT terminals, video intercoms, and smart dashboards. One highlight compared to other ESP32-P4 displays is optional support for 4G LTE cellular connectivity using an mPCIe module and SIM card slot, as well as LoRaWAN using a Stamp module.
reTerminal D1001 specifications:
- SoC – Espressif Systems ESP32-P4NRW32
- CPU
- Dual-core 32-bit RISC-V HP (High-performance) CPU @ up to 400 MHz with AI instructions extension and single-precision FPU
- Single-RISC-V LP (Low-power) MCU core @ up to 40 MHz
- Memory
- 768 KB HP L2MEM (for dual-core CPU), 32 KB LP SRAM, 8 KB TCM (for LP MCU core)
- 32MB PSRAM
- Storage – 128 KB HP ROM, 16 KB LP ROM
- GPU – 2D Pixel Processing Accelerator (PPA)
- VPU – H.264 and JPEG codecs support
- CPU
- Storage
- 32MB QSPI NOR Flash
- MicroSD card slot
- Display
- 8-inch MIPI DSI capacitive touch screen display with 1280 x 800 resolution
- Luminance: 250 cd/㎡
- Driver IC – 9365DA-H3
- Touch IC – GSL3670
- Camera – 2MP SC2356 MIPI CSI sensor with 1608×1208 active array size, up to 30FPS @ 1600×1200 10-bit
- Audio
- Dual microphone
- 2W @ 8Ω NS4150B speaker
- ES8311 low-power audio codec
- ES7210 echo cancellation chip
- Wireless
- ESP32-C6
- 2.4 GHz WiFi 6
- Bluetooth 5.x LE
- 802.15.4 radio for Zigbee, Thread, and Matter
- Optional 4G LTE cellular connectivity via mini PCIe (USB 2.0) module + 4G SIM card slot
- Optional LoRaWAN via Stamp pads (requires soldering)
- On-board antenna for ESP32-C6 and external 4G LTE antenna
- ESP32-C6
- USB – USB Type-C port for power and debugging
- Sensor – 6-axis LSM6DS3TR motion sensor for portrait/landscape mode orientation
- Misc
- Reset and Boot buttons
- Power switch
- Power LED, Status RGB LED
- PCF8563T RTC with support for timed interrupt wake-up
- Power Supply
- 5V via USB-C port
- 2,500 mAh battery
- Dimensions – TBD
The wiki includes instructions for installing the ESP-IDF framework, flashing the factory firmware (ESPBrookesia), and using it. The source code for the factory firmware can be found on GitHub. That means the reTerminal D1001 should be mainly viewed as a development kit since there’s no specific “killer” application for it.
The overall features and hardware design of the reTerminal D1001 are fairly close to the 8-inch version of the Waveshare ESP32-P4-WIFI6-Touch-LCD “tablet”, and can also be viewed as a larger version of the M5Stack Tab5 5-inch devkit. The key differentiating feature is the ability to add 4G LTE and/or LoRaWAN connectivity to the D1001.
The reTerminal D1001 is currently sold for $84.90 on the Seeed Studio store, and might eventually become available on the company’s AliExpress and Amazon stores.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
