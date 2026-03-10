---
title: "STMicro STM32C5 entry-level, 144 MHz Cortex-M33 MCU features up to 1MB flash, 256KB SRAM, Ethernet, CAN Bus"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/09/stmicro-stm32c5-entry-level-144-mhz-cortex-m33-mcu-features-up-to-1mb-flash-256kb-sram-ethernet-can-bus/"
published: "2026-03-09"
fetched: "2026-03-10T11:17:51.433168"
---

Not to be confused with the just-released STM32U3B5/C5 ultra-low-power MCUs, the entry-level STM32C5 Arm Cortex-M33 MCU family is designed for industrial sensors, smart home devices, electronic locks, thermostats, wearables, robotic actuators, and computer peripherals.
The MCUs are manufactured using ST’s 40 nm flash process, clocked at up to 144 MHz, and feature 128 KB to 1 MB of flash and up to 256 KB of SRAM, with a dynamic power consumption of <80 µA/MHz. Key features include Ethernet, USB, OctoSPI, CAN bus, DMA, and various peripherals, including ADCs, comparators, and an op-amp. Security is also enhanced, with the series targeting SESIP3 and PSA Certified Level 3 through features such as side-channel attack-resistant crypto, Hardware Unique Keys (HUK), and a Coupling and Chaining Bridge (CCB) for secure key storage.
STM32C5 key features and specifications:
- MCU core
- Arm Cortex-M33 32-bit CPU @ 144 MHz with single-precision FPU, DSP instructions, and MPU
- Performance – Up to 593 CoreMark (4.12 CoreMark/MHz)
- Accelerators
- CORDIC coprocessor for trigonometric operations
- ART accelerator enabling 0-wait-state flash execution
- Memory/Storage
- SRAM
- 64 KB (STM32C531 / STM32C542)
- 128 KB (STM32C55x / STM32C562)
- 256 KB (STM32C59x / STM32C5A3)
- Flash
- 128 KB to 256 KB (STM32C531 / STM32C542)
- 256 KB to 512 KB (STM32C55x)
- 512 KB (STM32C562)
- 512 KB to 1 MB (STM32C59x)
- 1 MB (STM32C5A3)
- ECC support on Flash and SRAM
- 64 KB user/data flash for EEPROM emulation
- 4.5 KB OTP (one-time programmable memory)
- Octo-SPI interface for external memory (STM32C59x / STM32C5A3 only)
- SRAM
- Peripherals
- Up to 118x I/O ports with interrupt capability (Up to 52 I/Os on STM32C53/C542)
- Ethernet MAC with DMA (STM32C59x / STM32C5A3 only)
- USB – USB 2.0 Full-Speed host/device
- Audio – 3x with I2S audio support
- Low speed I/Os
- 2x I2C FM+(1 Mbit/s), SMBus/PMBus
- 1x I3C (SDR), with support of I2C FM+ mode
- 4x USARTs and 3x UARTs, 1x LPUART
- 3x SPIs
- CAN FD controllers
- 0–1× (STM32C55x / STM32C562)
- Up to 2× (STM32C531 / STM32C542 / STM32C59x / STM32C5A3)
- DMA
- 2× LPDMA controllers
- Up to 16 channels (8+8 on higher-end devices; 8 or 12 on smaller variants)
- Analog peripherals
- ADC
- 1x 12-bit ADC (STM32C531 / STM32C542)
- 2x 12-bit ADCs (STM32C55x / STM32C562)
- 3x 12-bit ADCs (STM32C59x / STM32C5A3)
- Up to 28 external channels
- Up to 4.5 MSPS dual interleaved mode
- DAC
- 2x DACs (STM32C531 / STM32C542)
- 1x DAC (STM32C55x / STM32C562 / STM32C59x / STM32C5A3)
- Analog comparator (1 or 2, depending on the device)
- Operational amplifier (STM32C531 / STM32C542 only)
- ADC
- Up to 17x timers and 2x watchdogs
- 2x 16-bit advanced motor‑control
- General-purpose timers
- Basic timers
- Low-power timer
- SysTick timer
- 2× watchdog timer
- RTC with hardware calendar, alarms, and calibration
- Up to 4× 32-bit timers on higher-end models
- Security and cryptography
- True Random Number Generator (TRNG)
- HASH accelerator (SHA-1 / SHA-224 / SHA-256)
- AES accelerator (STM32C542 / STM32C562 / STM32C5A3)
- Dual AES with DPA resistance (STM32C5A3)
- PKA (Public Key Accelerator) (STM32C5A3)
- ECDSA signature verification (STM32C59x)
- Hardware Unique Key (HUK) (STM32C59x / STM32C5A3)
- 96-bit unique device ID
- RDP security lifecycle scheme
- Clock
- Internal oscillators
- 144 MHz HSI ((with ± 1% accuracy over temperature range -20°C : 130°C)
- PSI (160/144/100 MHz)
- 32 kHz LSI
- External oscillators
- 4–50 MHz HSE
- 32.768 kHz LSE
- Internal oscillators
- Debugging – Serial-wire debug (SWD), JTAG, Embedded Trace Macrocell (ETM), and others
- Supply Voltage – 2.7 V – 3.6 V
- Power management – Embedded regulator (LDO)
- Packages – All ECOPACK2 compliant (RoHS+)
- UFQFPN20 – 3 x 3 mm (STM32C53x, STM32C542)
- TSSOP20 – 6.5 x 4.4 mm (STM32C53x, STM32C542)
- UFQFPN24 – 4 x 4 mm (STM32C53x, STM32C542)
- LQFP32 – 7 x 7 mm (All series models)
- LQFP48 – 7 × 7 mm (All series models)
- LQFP64 – 10 × 10 mm (All series models)
- UFQFPN48 – 7 x 7 mm (All series models)
- UFQFPN32 – 5 x 5 mm (All series models)
- LQFP80 – 12 x 12 mm (STM32C55, STM32C562, STM32C59, STM32C5A)
- LQFP100 – 14 × 14 mm (STM32C55, STM32C562, STM32C59, STM32C5A)
- LQFP144 – 14 x 14 mm (STM32C59x, STM32C5A3)
- Temperature Range – -40°C to +125°C (Up to +140°C junction)
The STM32C5 series is fully supported by the STM32Cube ecosystem to simplify development. A key update is STM32CubeMX2, a configuration tool that provides faster access to reference code and improves code reuse. The new HAL2 (Hardware Abstraction Layer) also includes code-size-optimized drivers, allowing more memory to be used for application code. ST also provides IDEs, such as STM32CubeIDE and STM32CubeIDE for VS Code, along with production-ready example projects to accelerate development. The MCUs are also compatible with third-party toolchains such as Keil MDK, IAR Embedded Workbench, and GNU Arm Embedded Toolchain, and include built-in bootloader support for firmware updates via interfaces such as USART, USB, FDCAN, and SPI.
To make the development process simpler, the company provides not one but three development boards: the NUCLEO-C542RC and NUCLEO-C562RE STM32 Nucleo-64 boards, and the larger NUCLEO-C5A3ZG STM32 Nucleo-144 board. These boards integrate an on-board ST-LINK debugger/programmer and feature Arduino Uno V3 and ST morpho connectors for easy expansion with shields and external hardware. The Nucleo-144 model also adds more connectivity options, including Ethernet, USB, and additional expansion headers, providing developers with a flexible platform for evaluating and prototyping designs based on the STM32C5 microcontrollers.
The STM32C5 series microcontrollers are now entering production with pricing starting at $0.64 per unit for the entry-level STM32C53x models in quantities of 10,000, making the STM32C5 family a cost-efficient option for entry-level smart devices. The NUCLEO-C542RC and NUCLEO-C562RE boards are available on the company’s store for $20.62, while the full-featured NUCLEO-C5A3ZG board is expected to be available soon. You’ll find more details on the product page and the press release.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
