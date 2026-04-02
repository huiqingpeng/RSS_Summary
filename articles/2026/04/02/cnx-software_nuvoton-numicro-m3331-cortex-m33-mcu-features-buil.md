---
title: "Nuvoton NuMicro M3331 Cortex-M33 MCU features built-in ARGB LED controller, optional USB 2.0 OTG interface"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/04/02/nuvoton-numicro-m3331-cortex-m33-mcu-features-built-in-argb-led-controller-optional-usb-2-0-otg-interface/"
published: "2026-04-02"
fetched: "2026-04-03T07:13:10.707858"
---

Nuvoton’s new NuMicro M3331 is a series of 32-bit Arm Cortex-M33 MCUs clocked at 180 MHz that integrate an ARGB LED controller, a DSP instruction set, a single-precision FPU, and TrustZone security for smart factories, renewable energy systems, and consumer devices.
In the past, we have written about other Cortex-M33 MCUs like the STM32U3B5/C5, Texas Instruments MSPM33C321A, Nordic Semi’s nRF54LM20A, and various others, but the Nuvoton M3331 series specifically features a built-in Enhanced LED Light Strip Interface (ELLSI) and up to 10 standard LLSI channels. This allows the MCU to natively support gaming ARGB Gen1 and Gen2 LED control protocols, completely offloading the CPU to run fluid, dynamic LED effects. It comes in two variants, the M3333 series and the M3334 series, with the latter adding a high-speed USB 2.0 OTG controller with an integrated PHY.
NuMicro M3331 specifications:
- MCU core – Arm Cortex-M33 32-bit CPU @ 180 MHz with single-precision FPU, DSP instructions, and MPU
- Memory – Up to 320 KB SRAM, including 64 KB with hardware parity check
- Storage
- Up to 512 KB Dual Bank Flash memory (APROM) with ECC
- 8 KB user-defined loader (LDROM)
- 1x Secure Digital Host Controller (SDH) supporting up to 45 Mbps
- 1x Quad-SPI interface (up to 45 MHz in Master mode)
- External bus interface (EBI), i80 mode
- Peripherals
- Up to 110x I/O pins with interrupt capability (M3334 features up to 102x I/O pins)
- USB – 1x USB High-Speed device/host/OTG controller with a built-in transceiver (M3334 only)
- Audio
- 1x I2S interface (up to 12 Mbps)
- Up to 3x SPI/I2S interfaces (SPI up to 90 MHz in Master mode)
- Low speed I/Os
- Up to 3x I2C interfaces with SMBus/PMBus support (up to 3.4 Mbps)
- 1x I3C interface
- Up to 2x CAN FD interfaces
- Up to 5x UART interfaces with IrDA support (UART0 supports LIN mode)
- Up to 2x Universal Serial Control Interfaces (USCI), configurable as UART, SPI, or I2C
- Timers and DMA
- 4x 32-bit timers, 1x 24-bit SysTick timer, Real-Time Clock (RTC)
- 1x Watchdog Timer (WDT) and 1x Window Watchdog Timer (WWDT)
- 1x Enhanced Input Capture Unit (ECAP)
- 16-channel Peripheral Direct Memory Access (PDMA)
- LED and motor control
- Enhanced LED Light Strip Interface (ELLSI) and up to 10x LED Light Strip Interfaces (LLSI) for ARGB Gen1 and Gen2
- Up to 28x channels of Parallel Dimming Communication Interface (PDCI) supporting Bi-phase Mark Coding (BMC)
- Up to 48x PWM channels (up to 12x EPWM and 36x BPWM channels)
- 1x Enhanced Quadrature Encoder Interface (EQEI)
- Analog peripherals
- 1x 12-bit SAR ADC with up to 16 channels and 4.2 Msps sampling rate
- 2x analog comparators
- Built-in internal reference voltage (1.6V/2.0V/2.5V/3.0V), temperature sensor, low-voltage reset (LVR), and brown-out detector (BOD)
- Timers
- Up to 4x timers and 2x watchdogs
- 32-bit timers
- 24-bit SysTick timer
- 2× watchdog timer (WDT and WWDT)
- RTC (Real-Time Clock)
- Security
- TrustZone technology, Secure boot (Root of Trust, ROT)
- Flash memory supporting up to 4 regions of Execute-Only-Memory (XOM)
- 2 Kbytes of One Time Programmable (OTP) ROM for data security and key storage
- 96-bit Unique ID (UID) and 128-bit Unique Customer ID (UCID)
- Clocks
- Internal PLL up to 180 MHz
- Internal 48 MHz RC oscillator (± 2% deviation) and 38.4 kHz RC oscillator (± 10% deviation)
- 4 to 32 MHz crystal oscillator (HXT) and 32.768 kHz crystal oscillator (LXT)
- Power
- Operating voltage – 1.7V to 3.6V
- Consumption
- Run – 91 μA/MHz (Normal run)
- NPD2 – 190 μA (Normal power-down 2)
- SPD – 4.93 μA (Standby power-down)
- DPD – 0.62 μA (Deep power-down)
- Packages (Halogen-free, RoHS, TSCA-compliant)
- QFN33 – M333xTIGAE (4×4 mm, 0.4mm pitch)
- QFN48 – M333xYIGAE (5×5 mm, 0.4mm pitch)
- LQFP48 – M333xLIGAE (7×7 mm, 0.5mm pitch)
- LQFP64 – M333xSIGAE (7×7 mm, 0.4mm pitch)
- LQFP128 – M333xKIGAE (14×14 mm, 0.4mm pitch)
- Temperature Range – -40°C to +105°C
While going through the press release, the company referred to these MCUs as the “NuMicro M3331 series”. However, they mention the M3333 and M3334 series as subseries of the M3331 series, which is very confusing, to say the least…
The company provides NuMaker-M3333KI and NuMaker-M3334KI evaluation boards, both of which offer Arduino UNO-compatible extension headers with full-pin extension connectors. Additionally, they integrate the detachable Nu-Link2-Me module, which acts as an on-board debugger and programmer supporting an SWD interface, online/offline programming, and a virtual COM port. For power profiling, the boards include a dedicated ammeter connector for directly measuring the microcontroller’s power consumption. Both boards have the exact same features; the only differences are the MCU and the USB power/HS connector. The company also provides a Getting Started Guide on the product pages.
In terms of software support, the company provides a Board Support Package (BSP) and sample code compatible with major IDEs like Arm Keil MDK, IAR EWARM, and Visual Studio Code. The platform is also fully supported by mainstream real-time operating systems such as FreeRTOS, Zephyr, and RT-Thread, as well as GUI libraries such as emWin and LVGL.
The MCUs don’t seem to be up for sale just yet, or at least public pricing has not been provided, but the NuMaker-M3333KI and NuMaker-M3334KI evaluation boards are available to purchase for $30.00 each on the Nuvoton Direct eStore. More information, along with technical documentation, can be found on Nuvoton’s M3333 series and M3334 series product pages.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
