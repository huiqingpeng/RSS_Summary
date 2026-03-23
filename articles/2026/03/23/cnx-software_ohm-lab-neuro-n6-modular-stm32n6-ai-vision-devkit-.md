---
title: "Ohm Lab Neuro N6 – Modular STM32N6 AI Vision devkit supports rolling shutter, global shutter, or thermal camera (Crowdfunding)"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/23/ohm-lab-neuro-n6-modular-stm32n6-ai-vision-devkit-support-rolling-shutter-global-shutter-or-thermal-camera/"
published: "2026-03-23"
fetched: "2026-03-24T07:11:25.715444"
---

Ohm Lab Neuro N6 is a compact, modular, Arduino-compatible Edge AI/AI Vision development board powered by an STMicro STM32N6 Arm Cortex-M55 microcontroller with a 600 GOPS Neural-ART accelerator.
The Adafruit Feather-sized board features 64MB PSRAM, 32MB flash, a built-in microphone, a 6-axis IMU and magnetometer, a USB-C port for power and programming, and takes power from USB-C (5V) or a LiPo battery. The bottom side of the board features 40-pin and 30-pin high-density connectors for expansion boards, adding a camera (rolling shutter, global shutter, or thermal), a microSD card slot, Ethernet, WiFi, a TFT display, and more.
Neuro N6 specifications:
- MCU – STMicro STM32N6
- MCU Core – 32-bit Arm Cortex-M55 CPU @ up to 800MHz with Arm Helium and Arm MVE
- GPU – Neo-Chrom 2.5D GPU, Chrom-ART Accelerator (DMA2D)
- NPU – ST Neural-ART accelerator @ 1 GHz, 600 GOPS
- BPU – Hardware-accelerated H.264 and JPEG encoders
- Memory – 4.2MB SRAM
- Memory – 64MB PSRAM (400 MB/s)
- Storage – 32MB flash (400MB/s)
- Audio – Built-in microphone
- USB – USB Type-C port (480 Mbps)
- Sensor
- 6-axis IMU sensor (accelerator and gyroscope)
- Magnetometer
- Expansion
- 16-pin + 12-pin Feather-compatible GPIO headers
- 40-pin and 30-pin high-density connectors on the bottom side of the board
- Storage – 4-bit SDMMC
- Display – LTDC (RGB565) LCD screen interface
- Camera – MIPI CSI-2 interface for up to 5MP camera
- Audio – SAI
- I2C, SPI , 4-wire UART
- SWDIO, SWCLK & NRST
- 3V3, 1V8, VIN Power
- Debugging – 6x solder pads for JTAG
- Misc
- User and Reset buttons
- User RGB LED
- Power Supply
- 5V via USB-C
- 2-pin connector for 3.7V LiPo battery; charging circuitry (500 mA charger)
- Dimensions – 53.04 x 22.83 x 8.85mm (Adafruit Feather form factor)
- Weight – 6.7 grams
The Neuro N6 can be programmed with the Arduino IDE, and advanced users can leverage the STM32Cube IDE. You’ll find the firmware and a few Arduino samples (e.g., Yolov8) on GitHub. The company also developed NeuroStudio, an open-source (soon) and cross-platform application to instantly view the live camera feed and inference results directly over USB, without having to configure USB webcam drivers or external tools.
The specifications are quite similar to the OpenMV N6 board introduced last year, so you may also be able to run the MicroPython firmware and OpenMV Python program, but that’s not the same use case. Another STM32N6 AI vision hardware platform is the CamThink NeoEyes NE301 camera, but that’s more of a turnkey solution than a devkit.
The Neuro N6 is modular. While it’s designed for AI Vision applications, it does not include a camera by default. Instead, Ohm Lab provides a range of camera options: the 5MP OV5640 add-on, the OV5640-W adding WiFi and Bluetooth, the 1.5MP ST Cam global shutter camera, and a 1.5MP thermal camera (FLIR 160×120). Another add-on is the Neuro Vision TFT with an 800×480 touchscreen display, an OV5640 image sensor, a ToF sensor, a 1W amplifier and speaker, and a strobe LED. You can also add WiFi and Bluetooth to it. Ethernet connectivity is possible through the Neuro ETH shield.
Ohm Lab launched the Neuro N6 and accessories on Kickstarter with a 5,000 GBP (about $6,669 US) funding target that’s already been surpassed. Rewards start at $73 with the Neuro N6 only, but most people will likely want to add a camera to it, and the $99 Neuro N6 + OV5640 kit is probably the best way to get started. If you have a higher budget, you may consider the $399 Neuro N6 Ultimate Bundle with one board, as well as the Vision TFT, Vision OV5640, and ST Cam add-ons. Shipping costs will be added later and are expected to be 5 GBP to the UK, and 15 to 25 GBP to the rest of the world. Deliveries are scheduled to start in November 2026 if everything goes according to plan.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
