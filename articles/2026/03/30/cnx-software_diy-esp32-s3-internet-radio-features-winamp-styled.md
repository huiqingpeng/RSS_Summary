---
title: "DIY ESP32-S3 Internet radio features Winamp-styled user interface"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/30/diy-esp32-s3-internet-radio-features-winamp-styled-user-interface/"
published: "2026-03-30"
fetched: "2026-03-31T07:01:10.607357"
---

Volos Projects recently showcased an easy-to-reproduce, inexpensive DIY ESP32-S3 Internet radio based on a Waveshare ESP32-S3-LCD-1.54 development board and an Arduino sketch with a Winamp-styled user interface.
As its name implies, the hardware is based on the ESP32-S3 WiFi and Bluetooth SoC, connected to a 1.54-inch 240×240 color display and a speaker that delivers better-than-expected audio quality, according to Volos Projects.
Waveshare ESP32-S3-LCD-1.54 specifications:
- SoC – Espressif ESP32-S3R8
- CPU – Dual-core Tensilica LX7 microcontroller up to 240 MHz with vector instructions for AI acceleration
- Memory – 512KB SRAM, 8MB PSRAM
- Wireless – WiFi 4 and Bluetooth 5.0 LE + Mesh connectivity
- Storage
- 16MB NOR flash
- MicroSD card slot
- Display
- 1.54-inch IPS display with 240×240 resolution, 262K colors
- 4-wire SPI ST7789 driver
- Optional CST816 capacitive touch controller (not used by the DIY Radio project)
- Audio
- Speaker
- 2x microphones
- NS4150B audio amplifier
- ES8311 low-power audio codec
- ES7210 AEC (acoustic echo cancellation) chip
- USB – USB Type-C port for power and programming
- Sensor – QMI8658 6-axis IMU with gyroscope and accelerometer
- Misc
- Power, Boot, and “PLUS” user buttons
- Ceramic antenna
- Power Supply
- 5V via USB Type-C port
- 2-pin connector for a 3.7V lithium battery; supports charging and discharging
- Dimensions – 46 x 46 x 22.5 mm
Waveshare provides basic instructions and a few code samples to use the device with the Arduino IDE and the ESP-IDF framework. Companies like Waveshare and LILYGO offer plenty of low-cost MCU boards with a range of interesting features, but those should be considered development kits, since users need to develop their own firmware.
What’s interesting for the ESP32-S3-LCD-1.54 is that we now have a ready-to-use Arduino sketch to easily convert the kit into an Internet radio with a retro, Winamp-like user interface. You’d just need to modify the code to add your own WiFi credentials and the array with your list of radio stations:
|
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 |
String ssid = "xxxxxxxxx"; // ################### DONT FORGET EDIT THIS String password = "xxxxxxxxxx"; .... #define ns 6 //number of stations max 9 String stations[ns]={ "https://discodiamond.radioca.st/autodj", "https://listen.radioking.com/radio/175279/stream/216784", "http://sc6.radiocaroline.net:8040/stream", "https://club-high.rautemusik.fm/;", "http://greece-media.monroe.edu/wgmc.mp3", "https://audio.radio-banovina.hr:9998/;" }; |
Required libraries: esp32-audio-I2S-master 3.4.0, GFX Library for Arduino 1.6.0, LovyanGFX 1.2.19, and Arduino WiFiMulti 1.0.0.
You can check what the DIY ESP32-S3 internet radio looks like in action in the video below.
The ESP32-S3-LCD-1.54 sells for just $14.99 on the Waveshare store without a battery, or $15.99 with a battery. The devkit can also be purchased on Amazon ($27.99) and AliExpress (~$16). In theory, the DIY radio project should also work on other ESP32 platforms with a display and ES8311 audio codec, such as the M5Stack CardPuter-Adv, Waveshare ESP32-C6-Touch-AMOLED-1.8, Espressif EchoEar, and so on, but you’d need to modify the pins for the codec and display, as well as the whole UI if the resolution is not 240×240, since everything is hardcoded.
Via XDA Developers
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
