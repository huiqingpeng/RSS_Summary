---
title: "Microchip SAM9X75 Hybrid automotive MCU – Surprisingly ARM9 is still a thing in 2026"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/27/microchip-sam9x75-hybrid-automotive-mcu-surprisingly-arm9-is-still-a-thing-in-2026/"
published: "2026-03-27"
fetched: "2026-03-28T07:03:17.691061"
---

When Microchip launched the SAM9X60 in 2020, we were surprised to see a new SoC based on a legacy ARM926EJ-S core. But we were even more surprised to see Microchip doubling down with the SAM9X75, a hybrid automotive-qualified (AEC-Q100 Grade 2) System-in-Package (SiP) with the same classic ARM9 core and integrated DDR2 or DDR3L memory.
The first part will be the SAM9X75D5M SiP with 512MB on-chip DDR2 RAM, but the company also designed the SAM9X75D1G with 1 Gbit DDR3L and the SAM9X75D2G featuring 2 Gbit DDR3L. The SAM9X75 hybrid ARM9 MCU targets developers who need an MCU-like development environment, while benefiting from higher processing and display capabilities of microprocessors for automotive and e-mobility HMI applications.
Microchip SAM9X75D5M specifications:
- CPU subsystem
- Core – ARM926EJ-S running up to 800 MHz (significant increase from older 400-600MHz variants)
- 32 KB data cache, 32 KB instruction cache, and Memory Management Unit (MMU).
- Memory
- 512 Mbit DDR2 SDRAM (SAM9X75D5M)
- 1 Gbit DDR3L SDRAM (SAM9X75D1G)
- 2 Gbit DDR3L SDRAM (SAM9X75D2G)
- 64 KB internal SRAM (SRAM0) with single-cycle access at system speed
- 10 KB OTP memory for secure key storage.
- Storage
- External Bus Interface (EBI) supporting 8-bit NAND Flash with up to 24-bit programmable multi-bit ECC
- Quad/Octal SPI (QSPI/OSPI) controller
- 2x 4-bit SD/MMC interfaces
- 176 KBe total internal ROM (includes an 80 KB secure bootloader and 96 KB ROM for NAND Flash BCH ECC tables)
- Display
- 4-lane MIPI DSI, LVDS, and 24-bit Parallel RGB via 2D Graphics Controller (GFX2D)
- Suppotrts 10.1-inch panels with XGA resolution (1024 x 768)
- Camera
- Image Sensor Controller (ISC) with ITU-R BT 601/656/1120 supports up to 5 MP sensors
- Supports raw Bayer 12, YCbCr, monochrome, and JPEG compressed sensors up to 12 bits.
- 4-lane MIPI CSI-2 and parallel I/F
- Audio
- 1x I2S multi-channel controller with TDM support
- 1x Synchronous Serial Controller (SSC)
- 1x Class-D controller with single-ended or bridge-tied load connection capabilities
- Networking – Gigabit Ethernet (10/100/1000 Mbps) with TSN
- USB
- 1x High-speed USB Device
- 3x High-speed USB Hosts (All feature dedicated on-chip transceivers)
- Peripherals
- 8-channel 12-bit ADC with 4/5-wire resistive touchscreen support
- 4-channel 16-bit PWM controller
- 2x 3-channel 32-bit timers/counters
- 2x high-resolution (64-bit) periodic interval timers
- Expansion
- Up to 106x programmable I/O lines (SiP actually breaks out 67 I/Os)
- 12x Flexcoms (USART, SPI, I2C)
- 2x CAN-FD interfaces
- Security
- SHA and HMAC (FIPS PUB 180 compliant)
- AES (128/192/256-bit keys)
- TDES (2-key or 3-key algorithms
- AES/SHA tight coupling for IPsec hardware acceleration.
- True Random Number Generator (TRNG).
- Physical Unclonable Function (PUF), including a DRNG
- Misc
- Multiple specialized PLLs (System, USB High-Speed 480 MHz, Audio, LVDS, MIPI DPHY)
- Software-programmable ultra-low-power modes (ULP0, ULP1)
- Backup mode with an RTC and shutdown controller
- Supply Voltage – 3.3V to 5.5V
- Package – 243-ball TFBGA, 16 × 16 mm, 0.8 mm pitch
- Operating Temperature – −40°C to +105°C (automotive-grade)
- Qualification – AEC-Q100 Grade 2 (automotive variants)
As noted in the introduction, Microchip specifically calls this a “Hybrid MCU” (even though it’s technically an MPU) because it is designed to be programmed like an MCU (bare-metal/RTOS) while having MPU peripherals. Microchip also claims that this Hybrid approach allows it to boot in milliseconds compared to standard Linux MPUs, which take much more time to boot.
The SAM9X75 chip can be programmed with MPLAB X IDE and is supported by the MPLAB Harmony v3 framework for embedded development. It supports multiple RTOS options, including FreeRTOS and Eclipse ThreadX, as well as C for bare-metal development. For graphics and HMI applications, developers can use Microchip Graphics Suite (MGS) or third-party frameworks such as LVGL and Embedded Wizard to develop GUIs on the device’s integrated display and 2D graphics engine.
To simplify the development process, the company offers SAM9X75 curiosity development boards, marketed as the SAM9X75 Early Access Curiosity Wireless Kit and the SAM9X75 Curiosity LAN Kit, both of which are essentially the same and based on the SAM9X75D2G, the commercial/industrial variant of the MCU. The development board features up to 2 Gbit DDR3L memory, display and camera interfaces (MIPI DSI, LVDS, RGB, MIPI-CSI-2, and 2D GPU), Gigabit Ethernet with TSN, USB, CAN-FD, and various security features like secure boot, TRNG, PUF, and crypto accelerators. The kit further integrates a 4 Gbit SLC NAND, a 64 Mbit QSPI NOR, an Ethernet PHY via a LAN8840 daughter card, Bluetooth (RNBD451), Wi-Fi (M.2 module), a microSD card slot, a 40-pin Raspberry Pi GPIO header, and optimized power management features. The main difference between the two is that the Wireless Kit adds Wi-Fi and Bluetooth modules for connected applications, while the LAN Kit focuses on Ethernet and general-purpose evaluation.
The company also provides reference design support for the SAM9X75 SOM. This SoM can be configured with SAM9X75 SiP (both automotive and industrial variants) with up to 2-Gbit DDR2/DDR3L RAM, up to 4-Gbit NAND Flash, and 64-Mbit QSPI Flash with pre-programmed MAC addresses, along with a Gigabit Ethernet PHY and onboard power management IC. The module can operate in the −40°C to +85°C industrial temperature range, and comes in a compact 35×30 mm 174-pin package with Linux and bare-metal software support.
The SAM9X75D5M SiP can be purchased from Microchip’s store in both industrial and automotive temperature variants, and the SAM9X75D1G/D2G SKUs are currently sampling. Pricing starts at $9.81 for quantities below 25 units, which drops to $8.53 for orders above 500 units. The SAM9X75 System-on-Module (SOM) is also available on the store, priced at approximately $24.46 for low quantities and around $19.89 in higher volumes. To access reference design files, you need to log in and accept Microchip’s terms. Additionally, both the SAM9X75 Early Access Curiosity Wireless Kit and the SAM9X75 Curiosity LAN Kit are priced at about $169.00, with more details available on the press release.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
