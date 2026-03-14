---
title: "Esparagus Audio Brick ESP32-based DIN-rail 65W Hi-Fi amplifier supports Home Assistant and Squeezelite (Crowdfunding)"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/14/esparagus-audio-brick-esp32-based-din-rail-65w-hi-fi-amplifier-supports-home-assistant-squeezelite/"
published: "2026-03-14"
fetched: "2026-03-15T07:00:20.947237"
---

Sonocotta (Andriy Malyshenko), the developer of Esparagus “Media Center”, HiFi-Amped, Louder Raspberry Pi, and Louder Raspberry Hat Plus, has returned to Crowd Supply with the Esparagus Audio Brick, a compact ESP32 or ESP32-S3-powered Hi-Fi Class-D amplifier with Home Assistant support. With support for Music Assistant, Snapcast, and Logitech Media Server (LMS), the module can be used to build whole-home audio setups, retrofit vintage speakers with modern streaming features, or power custom speaker configurations such as subwoofers or bi-amp systems.
The board is built around an ESP32 or ESP32-S3 dual-core microcontroller with 16 MB flash and 8 MB PSRAM, and features Wi-Fi with optional W5500 SPI Ethernet for connectivity. Audio is processed via a Texas Instruments TAS5825M stereo I²S DAC with an integrated 65 W Class-D amplifier, and includes a DSP for a 15-band equalizer and hardware fault management. Other features include a USB Type-C port with a CH340 chip for flashing the firmware, an RGB LED for status, and an optional OLED display. The device comes in a DIN-rail mountable enclosure, uses snap-in connectors for power and speakers, and supports OTA firmware updates.
Esparagus Audio Brick specifications:
- SoC options – Espressif ESP32-WROVER-N8R8 or ESP32-S3-WROOM-N8R8 dual-core processor
- Display – Optional 128×64 OLED display via headers (SSD1306 or SH1106)
- Connectivity
- 10/100Mbps Ethernet via W5500 SPI controller
- 2.4 GHz Wi-Fi & Bluetooth (native to ESP32/ESP32-S3)
- Audio Hardware
- Interface – 4-pin snap-in speaker connector
- DAC/Amp – 1x (Stereo) or 2x (2.1-channel configuration) via Texas Instruments TAS5825M I2S DAC with integrated Class-D amplifier
- Output Power
- 2x 10 W @ 12 V, 4 Ω (THD+N 1%, efficiency mode)
- 1x 20 W @ 12 V, 3 Ω (THD+N 1%, efficiency mode)
- 2x 30 W @ 24 V, 8 Ω (THD+N 1%, power mode)
- 1x 65 W @ 24 V, 4 Ω (THD+N 1%, power mode)
- DSP
- Digital volume/gain control
- 15-band parametric EQ per channel
- 128-tap FIR filter
- 3-band Dynamic Range Compression (DRC)
- Automatic Gain Limiter (AGL)
- Smart Excursion, Smart Thermal, Smart Bass, and SmartEQ
- Up to 90% efficiency (>80% typical)
- Protection features
- Over-temperature protection
- Over-current protection
- Over-voltage and under-voltage protection
- Misc – RGB status LED
- Power Supply – 5V to 26V DC via 4-pin snap-in connector (rated up to 10 A)
- Dimensions – 110 x 100 x 50 mm
- Enclosure – Plastic case with attached DIN-rail mount and an aluminum heat sink
The Esparagus Audio Brick is available in two variants, one based on the ESP32 and the other based on the ESP32-S3. Hardware-wise, both versions use the same hardware design and audio components, and the only differences are in software support. The ESP32-S3 version is designed mainly for Home Assistant integration via ESPHome, whereas the ESP32 version is designed for standalone audio streaming software such as Squeezelite-ESP32 and Snapclient. Both versions use the same hardware design and audio components.
The Squeezelite-ESP32 is designed to stream audio from the Lyrion Music Server (LMS), supporting Spotify Connect, AirPlay, and Bluetooth. The Home Assistant integration enables features such as media playback, text-to-speech announcements, and automation control. For synchronized multi-room audio setups, it can operate as a Snapclient (Snapcast client). Additionally, you also have the option to build custom firmware using Arduino or ESP-IDF, thanks to the board’s standard I²S audio interface and accessible GPIOs. The project is fully open-source with more information available on GitHub.
Both the ESP32 and ESP32-S3-based Esparagus Audio Brick are available on Crowd Supply for $59. The package includes an aluminum heat sink and a plastic DIN-rail enclosure. Shipping is free within the US, while worldwide shipping costs $12. The campaign runs until April 23, 2026, and deliveries handled by Mouser Electronics are expected to start around July 24, 2026.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
