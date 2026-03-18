---
title: "Review of Open Nextion ESP32-S3-based HMI displays with the Arduino IDE and the ESP-IDF framework"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/18/review-open-nextion-esp32-s3-based-hmi-displays-with-the-arduino-ide-and-the-esp-idf-framework/"
published: "2026-03-18"
fetched: "2026-03-18T15:31:24.160808"
---

ITEAD has sent us samples of the Open Nextion ONX3248G035 and ONX2432G028 ESP32-S3 HMI displays for review. Open Nextion is a new product line that differs from the original Nextion HMI family, which relies on the Nextion Editor for UI design and UART communication for control. Instead, the Open Nextion features an ESP32-S3 wireless microcontroller handling logic processing, display control, and wireless connectivity, all in one integrated package.
ITEAD fully supports the ESP-IDF framework and the Arduino IDE with LVGL graphics library support. The ONX3248G035 model features a 3.5-inch screen, while the ONX2432G028 variant has a 2.8-inch screen. The Open Nextion HMI wireless displays also take accessories such as a dual-microphone array, a speaker, and an I/Os adapter.
The new Open Nextion product line is especially well-suited to embedded developers/makers who want an all-in-one board with HMI and wireless capabilities, IoT terminal and Smart HMI panel prototyping, students interested in exploring LVGL and ESP32-S3, as well as industrial applications requiring a wireless display and sensors.
Open Nextion HMI display kits unboxing
ITEAD sent us the two displays and accessories. Let’s check the ONX3248G035 board (3.5-inch) and the ONX2432G028 board (2.8-inch) packages first.
Both ship with a USB-C cable, and the boards, while quite similar, have a few small differences.
The Nextion Dual MIC board is a dual-microphone array with two PDM microphones for voice input.
The Nextion BOX speaker enables audio output.
The Nextion IO Adapter V2 exposes a 20-pin GPIO header with 2.54mm pitch and is connected to the HMI board through an FPC connector.
Open Nextion ONX2432G028 and ONX3248G035 specifications
| Features | ONX2432G028 (2.8″) | ONX3248G035 (3.5″) |
|---|---|---|
| Display size | 2.8" | 3.5" |
| Resolution | 240×320 | 320×480 |
| Number of colors | 262K | 262K |
| Brightness | 300 nits | 300 nits |
| Touchscreen type | CTP (Capacitive) | CTP (Capacitive) |
| Touch driver | CST826 | CST826 |
| Panel driver | ST7789 | ST7796 |
| MCU | ESP32-S3R8 | ESP32-S3R8 |
| CPU Speed | Up to 240 MHz | Up to 240 MHz |
| Flash | 16 MB | 16 MB |
| PSRAM | 8 MB | 8 MB |
| ROM / SRAM | 384 KB / 512 KB | 384 KB / 512 KB |
| MicroSD slot | Yes | Yes |
| Wireless | 2.4 GHz Wi-Fi + BT 5 (LE) | 2.4 GHz Wi-Fi + BT 5 (LE) |
| USB Interface | CH340K USB-to-UART (no USB OTG) | CH340K USB-to-UART (no USB OTG) |
| Power Input | DC 5V 1A (USB-C) | DC 5V 1A (USB-C) |
| Battery | Li-ion 3.7V + RTC 3V | Li-ion 3.7V + RTC 3V |
| Temp. Range | -20~70°C | -20°C~70°C |
Overall, the specifications are almost identical, with the main differences being the screen size and resolution.
Board Design and Layout
The ONX2432G028 (2.8″) and ONX3248G035 (3.5″) boards feature a user-friendly layout and design. Two particularly interesting points are the inclusion of the BLX8563-PARC RTC chip, which is rarely seen on other boards, as well as the NS4168 Class D DAC + Amplifier chip delivering up to 2.5W of output power. The interfaces for the ONX3248G035 are described below. The ONX2432G028 is similar, except that the FPC display cable and microSD card slot are on the other side of the PCB.
List of ports and features:
- USB-C for power and programmer
- BOOT and RESET buttons
- ON/OFF switch
- 4-pin UART0 connector
- I2C and UART1 Grove connectors
- 4-pin FPC connector for the microphone array
- 14-pin GPIO FPC connector
- 24-pin camera connector (not used in this review)
- MicroSD card slot
- 2-pin speaker connector
- 2-pin battery connector
- 2-pin RTC battery connector
- IPEX-1 antenna connector to extend the WiFi range; note: the user also needs to remove a resistor to switch to the external antenna instead of the PCB antenna.
Comparison between Nextion HMI and Open Nextion (Genius series)
| Features | Nextion HMI | Open Nextion (Genius Series) |
|---|---|---|
| UI design | Nextion Editor (drag & drop) | LVGL / SquareLine Studio |
| MCU control | Support for external MCU boards (Arduino, STM32, ESP32, etc.) | Build-in ESP32-S3 |
| Wireless | N/A (except Intelligent Series) | Built-in Wi-Fi 4 + Bluetooth 5 LE |
| Programming | Script in Nextion Editor | ESP-IDF framework, Arduino IDE |
| USB OTG | Via external MCU | No |
| Open Source | Closed-source software | Open-source ESP-IDF and LVGL |
| Learning Curve | Low (for UI design) | Medium (knowledge of ESP32 development tools needed) |
| Price (3.5-inch model) | ~$25–35 | $34.90 |
| Suitable for | Quick UI development through no code tool | More flexible UI development, wireless connectivity |
In conclusion, the Nextion HMI product line remains a good choice for developers who want a ready-to-use UI design tool and prefer not to write code for their UI. However, for projects that require built-in wireless connectivity, an open ecosystem, or full control of everything from a single board, Open Nextion is a much better fit, and at a similar price point.
Testing Open Nextion with Arduino IDE and the ESP-IDF framework
Setting up the development environment for Open Nextion can be done in two main ways, depending on the developer’s experience level and requirements. The Arduino is best for beginners, and the ESP-IDF framework offers more flexibility and improved performance for experienced developers.
Using Open Nextion with the Arduino IDE
You can configure and use it directly as an ESP32-S3 board with an ST7789 display. The pin definitions and example code are as follows:
|
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 |
#include <LovyanGFX.hpp> #define LCD_SCLK_PIN GPIO_NUM_5 #define LCD_MOSI_PIN GPIO_NUM_1 #define LCD_MISO_PIN GPIO_NUM_2 #define LCD_RST_PIN GPIO_NUM_NC #define LCD_DC_PIN GPIO_NUM_3 #define LCD_CS_PIN LCD_MISO_PIN #define LCD_BL_PIN GPIO_NUM_6 class LGFX : public lgfx::LGFX_Device { lgfx::Panel_ST7789 _panel_instance; lgfx::Bus_SPI _bus_instance; lgfx::Light_PWM _light_instance; public: LGFX(void) { { auto cfg = _bus_instance.config(); cfg.spi_host = SPI2_HOST; cfg.spi_mode = 0; cfg.freq_write = 40000000; cfg.freq_read = 16000000; cfg.spi_3wire = false; cfg.use_lock = true; cfg.dma_channel = SPI_DMA_CH_AUTO; cfg.pin_sclk = LCD_SCLK_PIN; cfg.pin_mosi = LCD_MOSI_PIN; cfg.pin_miso = LCD_MISO_PIN; cfg.pin_dc = LCD_DC_PIN; _bus_instance.config(cfg); _panel_instance.setBus(&_bus_instance); } { auto cfg = _panel_instance.config(); cfg.pin_cs = LCD_CS_PIN; cfg.pin_rst = LCD_RST_PIN; cfg.pin_busy = GPIO_NUM_NC; cfg.panel_width = 320; cfg.panel_height = 480; cfg.offset_x = 0; cfg.offset_y = 0; cfg.offset_rotation = 4; cfg.dummy_read_pixel = 8; cfg.dummy_read_bits = 1; cfg.readable = false; cfg.invert = false; cfg.rgb_order = false; cfg.dlen_16bit = false; cfg.bus_shared = false; _panel_instance.config(cfg); } { auto cfg = _light_instance.config(); cfg.pin_bl = LCD_BL_PIN; cfg.invert = false; cfg.freq = 44100; cfg.pwm_channel = 7; _light_instance.config(cfg); _panel_instance.setLight(&_light_instance); } setPanel(&_panel_instance); } }; LGFX display; void setup() { Serial.begin(115200); display.init(); display.setRotation(1); display.setBrightness(200); display.fillScreen(TFT_WHITE); display.setTextDatum(middle_center); display.setTextColor(TFT_BLUE, TFT_WHITE); display.setFont(&fonts::FreeSansBold18pt7b); display.drawString("Open Nextion", display.width() / 2, display.height() / 2 - 30); display.drawString("Arduino Version", display.width() / 2, display.height() / 2 + 30); Serial.println("Display OK"); } void loop() { } |
You could also use another Arduino graphics library, such as LVGL.
Using Open Nextion HMI displays with the ESP-IDF framework (professional development)
For those who want maximum performance or low-level control, you can use ESP-IDF through Windows PowerShell or the VSCode Extension. ITEAD has prepared a total of nine ESP-IDF sample programs, which can be downloaded from zip files for the ONX3248G035 (3.5″) and the ONX2432G028 (2.8″).
After powering the boards for the very first time (before testing the Arduino part), the screen immediately displays the LVGL widget demo. Both the 3.5-inch and 2.8-inch versions display the interfaces normally, with good color and brightness levels that are clearly visible from most viewing angles. The capacitive touch responds well with no issues observed. However, when comparing colors, it is clearly noticeable that the ONX2432G028 (2.8″) has noticeably brighter and more vivid colors than the 3.5″ model.”
Let’s now connect one of the displays to Wi-Fi. We can scan 2.4 GHz WiFi networks and connect to our SSID successfully within about 5 seconds.
Let’s now test the capacitive touch panel using the relevant demo. When swiping a finger across the screen, it responds smoothly. A red dot follows the finger precisely with no noticeable delay. However, when testing by dragging to the edges on the ONX2432G028 (2.8″), one side of the screen has an edge area where touch input is not detected at all near the border. In contrast, the ONX3248G035 (3.5″) shows no such issue and registers touches right up to the edges without problem.
We can also load images from a microSD card. They load fast, and the colors look accurate with no distortion or color shift observed from any viewing angle. The screen refresh and image rendering speed are very quick, and no screen drawing or tearing is visible during updates.
Next up, we’ll play music stored on a microSD card using the speaker for audio output. The audio quality is not too bad, as you can check for yourself in the video below.
We’ll finally test audio recording and playback through the speaker. The audio played back is clear with good recording quality overall.
Conclusion
The Open Nextion ONX3248G035 and ONX2432G028 HMI development boards are great for embedded developers wanting a complete display + wireless solution in a single board. Powered by a 240 MHz ESP32-S3 microcontroller with 8 MB PSRAM, 16 MB Flash, and built-in Wi-Fi & Bluetooth 5 LE, they enable fully self-contained IoT HMI terminal development without needing an external MCU. The capacitive touchscreen also provides a better user experience compared to the resistive touch commonly found in similarly priced HMI boards.
In the next part of the review, we will experiment with building a full-featured IoT application.
Pros
- ESP32-S3 handles everything on a single board, no need for an external MCU board
- Supports the popular ESP-IDF framework, Arduino IDE, and LVGL library
- 8 MB PSRAM + 16 MB Flash makes it ready for complex HMI applications
- Responsive capacitive touch
- Built-in Wi-Fi + Bluetooth 5 LE for IoT capability
- Multimedia support with microSD card slot, optional camera, microphone array, and speaker
- Complete set of example programs and a continuously updated wiki
Observations/Cons
- No USB OTG functionality. Although the ESP32-S3 has two USB interfaces (USB Serial/JTAG and USB OTG), this board uses the CH340K USB-to-UART chip instead, so there is no USB OTG connector exposed. Projects that require USB peripherals (e.g., USB keyboard) or need the board to act as a USB HID device should consider other boards.
- GPIO multiplexing – 24 GPIO pins are shared with UART1, MIC PDM, and Camera interfaces, so careful interface planning is required. Additionally, USB_UART and UART0 share TXD/RXD lines and cannot be used simultaneously.
- Requires solid embedded development knowledge—not plug-and-play like the classic Nextion HMI.
We’d like to thank ITEAD for sending the 3.5-inch and 2.8-inch Open Nextion boards along with accessories for this review. They can be purchased on the ITEAD official store for $22.90 (ONX3248G035) and $19.44 (ONX2432G028), and even less with the 10% discount code CNXSOFTSONOFF. Note these prices are promotional, and regular prices are $34.90 and $29.90.
CNXSoft: This article is a translation of the original review on CNX Software Thailand by Arnon Thongtem, edited by Suthinee Kerdkaew.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
