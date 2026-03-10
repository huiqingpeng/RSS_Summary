---
title: "Nordic Semi unveils nRF54LS05A and nRF54LS05B entry-level, ultra-low-power Bluetooth LE SoCs"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/09/nordic-semi-nrf54ls05a-nrf54ls05b-entry-level-ultra-low-power-bluetooth-le-socs/"
published: "2026-03-09"
fetched: "2026-03-10T10:41:21.143234"
---

Nordic Semiconductor’s nRF54LS05A and nRF54LS05B are entry-level, ultra-low-power Bluetooth Low Energy (LE) Arm Cortex-M33 microcontrollers designed to be used as the main wireless SoC in simple applications such as sensors, tags, beacons, remotes, and PC peripherals, or operate as a Bluetooth LE companion device in more advanced products.
Both SoCs are clocked at 128 MHz, feature Nordic’s 4th-generation Bluetooth LE radio, analog/digital interfaces, and advanced security. They also come with 0.5 MB of Non-Volatile Memory (NVM), and the only difference is that the nRF54LS05A is equipped with 64 KB of RAM, while the nRF54LS05B offers 96 KB.
Nordic Semi nRF54LS05A/B specifications:
- CPU
- Arm Cortex-M33 core @ 128 MHz
- Performance – 250 CoreMark/mA @ 3V, 500 CoreMark
- Memory
- nRF54LS05A – 64 KB RAM
- nRF54LS05B – 96 KB RAM
- Storage – 508 KB NVM
- Wireless
- Bluetooth LE – 1 Mbps, 2 Mbps
- 2.4 GHz proprietary – GFSK: 4 Mbps, 2 Mbps, 1 Mbps
- Single-ended antenna output (on-chip balun)
- 128-bit AES/ECB/CCM/AAR coprocessor
- Tx power – Configurable from -10 dBm to +4 dBm in 1 dBm step size
- Rx Sensitivity – -96 dBm (1Mbps Bluetooth LE)
- Peripherals
- Up to 37x GPIO pins (8 MHz ports)
- 3x serial interfaces with EasyDMA supporting I2C, SPI controller/peripheral, and UART
- SPI up to 8 MHz (SPIM, SPIS)
- TWI up to 400 kHz and I2C compatible (TWIM, TWIS)
- UART up to 1 Mbps (UARTE)
- 4-channel SAADC: 14-bit at 31.25 ksps (oversampled), 12-bit at 125 ksps (oversampled), 10-bit at up to 1 Msps
- Global RTC can run in System OFF mode and implement a shared system timer (GRTC)
- 1x four-channel pulse width modulator (PWM) with autonomous waveform generation
- 1x quadrature decoder (QDEC)
- 1x watchdog timer
- 3x 32-bit timers with counter mode
- Temperature sensor
- Clocks
- Single 32 MHz crystal operation
- Optional 32.768 kHz crystal
- Security
- Secure boot
- Physical protection – Tamper detectors
- Hardware-accelerated Bluetooth LE encryption
- Supply (and GPIO) Voltage – 1.7 – 3.6 V DC
- Power Consumption @ 3V
- Radio: 3.4 mA for Rx and 4.8 mA for Tx @ 0 dBm
- Sleep modes – from 0.6 μA to 1.2 μA
- Dimensions – 6x6mm QFN48 package, 0.4mm pitch
The new entry-level Bluetooth LE SoCs are supported by the nRF Connect SDK with Bare Metal option, and the company claims they offer a “smooth migration path from the nRF52 Series” to help speed up development. It should be noted that the new nRF54LS05 chips do NOT support features such as Bluetooth Channel Sounding and Bluetooth Mesh.
Nordic highlights reduced design complexity, size, and cost, a mature Bluetooth LE radio and stack, extended battery life, and flexibility with pin-to-pin compatible SoCs in the RF54 series. Documentation is up, but apart from the datasheet, there’s nothing specific to the nRF54LS05A and nRF54LS05B chips yet. Developers will be able to test the new chips with the nRF54LS05-DK development kit basedon the nRF54LS05B, but supporting “emulation” for the nRF54LS05A with less RAM. The development board also features an nRF5340 chip for the debugger, a PMIC, headers for all IOs, four user buttons, and four LEDs.
Nordic says the nRF54LS05A and nRF54LS05B SoCs and the nRF54LS05-DK are now available via the early access program, and production is scheduled for Q3 2026. More information can be found on the product pages for the SoC and the devkit, as well as in the press release.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
