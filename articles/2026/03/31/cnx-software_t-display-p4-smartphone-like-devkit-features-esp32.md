---
title: "T-Display-P4 smartphone-like devkit features ESP32-P4 MCU, ESP32-C6 wireless SoC, and SX1262/LR2021 LoRa transceiver"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/31/t-display-p4-smartphone-like-devkit-features-esp32-p4-mcu-esp32-c6-wireless-soc-and-sx1262-lr2021-lora-transceiver/"
published: "2026-03-31"
fetched: "2026-04-01T07:00:48.862228"
---

LILYGO T-Display-P4 is a feature-rich ESP32-P4 + ESP32-C6 devkit, but with a smartphone-like design and support for GPS, Ethernet, and LoRaWAN through SX1262 or LR2021 LoRa transceiver, besides the usual WiFi 6, Bluetooth 5.x, and 802.15.4 wireless connectivity.
The T-Display-P4 is offered with either a 4.05-inch IPS display and a 2MP front-facing camera or a 4.1-inch AMOLED with a 2MP rear camera. The devkit is equipped with 32MB PSRAM and 16MB NOR flash for the ESP32-P4, a microSD card slot, a built-in microphone and speaker, a 3.5mm audio jack, a few USB ports, and a 9-axis motion sensor, as well as a GPIO port and two Qwiic connectors for expansion.
T-Display-P4 specifications:
- MCU – ESP32-P4
- CPU
- Dual-core RISC-V microcontroller @ 360 MHz with AI instructions extension and single-precision FPU
- Single-RISC-V LP (Low-power) MCU core @ up to 40 MHz
- GPU – 2D Pixel Processing Accelerator (PPA)
- VPU – H.264 and JPEG codecs support
- Memory – 768 KB HP L2MEM, 32 KB LP SRAM, 8 KB TCM, 32MB PSRAM
- Storage – 128 KB HP ROM, 16 KB LP ROM
- CPU
- Storage
- 16 MB flash
- MicroSD card slot
- Display (one or the other)
- 4.05-inch TFT display with 1168×540 resolution, 10-point capacitive touch
- 4.1-inch AMOLED with 1232 x 568 resolution, 10-point capacitive touch
- Camera (one or the other)
- TFT version – 2MP front-facing camera (OV2710 sensors up to 1080p30, 720p60)
- AMOLED version – 2MP rear camera (OV2710 sensors up to 1080p30, 720p60)
- Audio
- 3.5mm audio jack
- I2S speaker and microphone
- ES8311 audio codec
- NS4150B amplifier
- Wireless Connectivity
- 2.4 GHz Wi-Fi 6 (802.11ax) and Bluetooth 5.x (LE) via ESP32-C6-MINI-1U module with 4MB flash (not PSRAM like on the illustration below)
- Ethernet RJ45 port
- LoRaWAN via SX1262 or LR2102 (note: the latter is listed in the specs, but not an option at the time of order)
- L76K GPS module
- 2x micro-miniature coaxial antenna connectors for LoRa (Sub-GHz/2.4 GHz)
- USB
- USB Type-A high-speed port
- USB Type-C high-speed port
- USB Type-C “basic” port
- Sensor – 9-axis motion sensor (lCM20948)
- Expansion
- 16-pin expansion connector with 8x GPIO, SPI, 5V, 3.3V, GND
- 2x Qwiic I2C connectors
- Misc
- Battery switch
- Boot and Reset buttons for ESP32-P4
- Boot and Reset buttons for ESP32-C6
- PCF8563 RTC
- AW86224AFCR X-axis linear motor (for vibration/haptic feedback)
- RF switch for sub-GHz/2.4GHz LoRa (for LR2102 only)
- Support for an external keyboard (T-Display-P4-Keyboard; under development, not for sale yet)
- XL9535 16-bit GPIO expander
- M.2 thread for mounting
- Power Supply
- 5V, 500 mA via USB-C port
- Legend-Si LGS4056H charge management OC
- TI BQ27220 I2C battery gauge
- Dimensions – 109 x 63 x 22 mm
- Weight – TBD
LILYGO provides support for the ESP-IDF framework using VS Code with various firmware (LVGL UI, xiaozhi voice assistant, iperf, etc.) and code samples for all key features of the devkit. You’ll find all that on GitHub along with PDF schematics and a few tools. The wiki provides information similar to what’s on GitHub, but may have a few additional resources.
Since the T-Display-P4 was first released a few months ago in limited quantities on the LILYGO store, and at least one third-party firmware has been ported to the devkit: MeshCore (note that the basic features are free, but extra features require an 8 GBP one-time license). I also came across a”Meshtastic port”, but it was a vibe-coded attempt… Support for ESP32-P4 targets will be enabled through PR9112, and will be one of the steps required before T-Display-P4 is fully supported.
The T-Display-P4 is sold on AliExpress for about $111 (TFT) or $136 (AMOLED) with SX1262 830-945MHz LoRa transceiver. You can also find the TFT version on Amazon for $104, and the LILYGO store has both models listed as “unavailable” at this time. The device ships with a T-shaped LoRa antenna, but there’s no information about the battery, so it’s probably not included.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
