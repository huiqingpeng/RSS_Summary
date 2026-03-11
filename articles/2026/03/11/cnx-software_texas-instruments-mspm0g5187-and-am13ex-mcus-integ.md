---
title: "Texas Instruments MSPM0G5187 and AM13Ex MCUs integrate TinyEngine NPU for Edge AI applications"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/11/texas-instruments-mspm0g5187-and-am13ex-mcus-integrate-tinyengine-npu-for-edge-ai-applications/"
published: "2026-03-11"
fetched: "2026-03-12T07:02:03.052812"
---

Texas Instruments MSPM0G5187 and AM13Ex are two new microcontroller (MCU) families featuring the company’s TinyEngine neural processing unit (NPU) to enable low-latency, high-efficiency Edge AI/Machine Learning inference on the chips.
TI claims that the TinyEngine NPU can run AI models with up to 90 times lower latency and more than 120 times lower energy utilization per inference than similar MCUs without an accelerator. The MSPM0G5187 is a general-purpose, low-power Arm Cortex-M0+ MCU, while the AM13Ex Arm Cortex-M33 microcontroller targets real-time motor control, starting with the AM13E23019 SKU.
TI MSPM0G5187 general-purpose Cortex-M0+ MCU
Key features and specifications:
- CPU – Arm Cortex-M0+ @ 80 MHz
- Memory – 32 KB RAM with ECC
- Storage – 128 KB flash with ECC, 8 KB data flash with ECC
- Accelerators
- TinyEngine NPU for AI/ML delivering up to 2.56GOPS (Giga Operations Per Second) at 80MHz
- MATHACL math accelerator
- Peripherals
- USB – 1x USB 2.0 (12 Mbps)
- Audio – Digital audio interface supporting I2S, PCM, TDM, etc…
- Up to 59x GPIOs, including 2x 5V tolerant
- Up to 3x UART, 2x SPI, 1x I2C
- Timers
- 4x 16-bit timers with up to 14x PWM
- 2x windowed watchdog timers
- RTC with alarm and calendar mode
- Analog
- 12-bit SAR ADC; 26 ADC channels; up to 1.6 Mbps sample rate
- Comparator with 8-pin DAC
- Integrated temperature sensor
- 12-bit DMA controller
- Security – AES encryption, cryptographic acceleration, hardware-enforced isolation, secure boot, secure communication, secure debug, secure firmware & software update, secure storage, software IP protection
- Debugging – 2-pin SWD
- Supply Voltage – 1.62V to 3.6V
- Power modes
- RUN – 103µA/MHz (CoreMark)
- SLEEP – 34µA/MHz
- STOP – 199µA at 4MHz
- STANDBY – 1.5µA at 32kHz with RTC and full SRAM and state retention
- SHUTDOWN – 88nA with IO wake-up capability
- Packages
- 64-pin LQFP (PM) (0.5mm pitch)
- 48-pin LQFP (PT) (0.5mm pitch)
- 48-pin VQFN (RGZ) (0.5mm pitch)
- 32-pin VQFN (RHB) (0.5mm pitch)
- 28-pin DSBGA (YCJ) (0.35mm pitch); note: preview stage
- 28-pin WQFN (RUY) (0.4mm pitch)
- 24-pin VQFN (RGE) (0.5mm pitch)
- 20-pin VSSOP (DGS) (0.5mm pitch)
- Temperature Range – -40 to 125°C
The MSPM0G5187 microcontroller family is supported by the MSPM0 SDK with FreeRTOS and Zephyr RTOS. It targets resource-constrained devices, including battery-powered products, benefiting from AI/ML edge workloads. The company also provides the LP-MSPM0G5187 Launchpad development kit for evaluation. It comes with an XDS110 debug probe, 40-pin BoosterPack headers, a USB-C port, a microSD card slot, one microphone, one audio ADC, and a few LEDs and buttons.
The MSPM0G5187 Cortex-M0+ microcontrollers are available now in production quantities starting at under $1 in 1,000-unit quantities. The LP-MSPM0G5187 Launchpad development kit sells for $22. More details, including documentation and purchase links, can be found on the product page.
TI AM13Ex Arm Cortex-M33 MCU for real-time motor control
AM13E23019 Specifications:
- CPU – Arm Cortex-M33 core @ up to 200 MHz with FPU, MPU, DSP, 32-bit Trigonometric Math Unit (TMU); 310 DMIPS, 800 Coremark
- Memory
- 128 KB RAM with ECC
- External Peripheral Interface (EPI) supporting SDRAM, ASRAM, or ASIC/FPGA external interfaces
- Storage – Up to 512 KB flash (2x 256KB) with ECC
- Accelerator – TinyEngine NPU for AI/ML
- Peripherals
- Flexible System Peripherals
- 12-channel DMA controller
- Nested Vectored Interrupt Controller (NVIC)
- Up to 107x GPIO with Input/Output XBAR connectivity
- 8x GPIOs with Shutdown Wakeup Capability
- 1x windowed watchdog timer (WWDT )
- 2x general-purpose timers: TIMG4 (32-bit), TIMG12 (16-bit)
- Analog
- 3x 12-bit SAR ADCs up to 6.67Msps, up to 32 channels per ADC
- 4x Analog Comparator Sub-systems (CMPSS) with 2x 10-bit effective DAC and 2x digital filters
- 3x Programmable Gain Amplifiers (PGA)
- Programmable analog connections between ADC, PGAs, CMPSS, and DAC
- Real-time Control
- 5x Motor Control Pulse Width Modulation (MCPWM) modules
- 2x Enhanced Capture (eCAP) module
- 3x Enhanced Quadrature Encoder Pulse (eQEP)
- Device Crossbars (INPUTXBAR, OUTPUTXBAR, PWMXBAR) for routing signals from GPIO to other modules
- Enhanced Serial Communication Interfaces
- 2x configurable serial interfaces supporting UART (LIN) or I2C (SMBus/PMBus)
- 4x configurable serial interfaces supporting UART, I2C, or SPI
- 1x Modular Controller Area Network (MCAN) with Flexible Data-rate (CAN FD)
- Flexible System Peripherals
- Clock System
- Internal 4MHz/32MHz oscillator (SYSOSC)
- Internal 32kHz oscillator (LFOSC)
- System Phase-locked loop (SYSPLL) up to 200MHz
- External 4MHz to 25MHz crystal oscillator (XTAL)
- External 4MHz to 48MHz clock input (HFCLK)
- Safety – Enables IEC61508 SIL-2 and SIL-3 systems
- Security
- Secure Boot/FWU/Debug/JTAG Lock
- Secure Key Storage and Management
- Privileged/Non-Privileged resource partitioning
- Flash Write/Erase/Hide Protections
- Device Life Cycle Management
- AES Encryption with 128- or 256-bit Key
- Unique Identification Number (UID)
- Debugging
- 4-pin JTAG and 2-pin SWD
- Micro Trace Buffer (MTB)
- Embedded Trace Macrocell
- Supply voltage – 3.3V
- Power Modes
- RUN: 49mA @ 200MHz
- STANDBY: 1.84mA with CPU execution resume and 32kB SRAM retention
- SHUTDOWN: <5µA with IO wake-up capability
- Packages
- 128-pin PDT Thin Quad Flat Package (TQFP) (0.4mm pitch)
- 100-pin PZ Low-profile Quad Flat Pack (LQFP) (0.5mm pitch)
- 80-pin PN Low-profile Quad Flat Pack (LQFP) (0.5mm pitch)
- 64-pin PM Low-profile Quad Flat Pack (LQFP) (0.5mm pitch)
- 48-pin PT Low-profile Quad Flat Pack (LQFP) (0.5mm pitch)
- 48-pin RGZ Very Thin Quad Flatpack No-Lead (VQFN) (0.5mm pitch)
- Temperature Range – -40°C up to +105°C
The AM13Ex family supports FreeRTOS, Zephyr RTOS, and bare metal programming via the AM13E2 MCU SDK. It targets motor control applications in appliances, robotics, and industrial systems, leveraging machine learning for adaptive control and predictive maintenance. It couldn’t find any development kit for it just yet.
Mass production for the AM13E23019 does not appear to have started, and instead, Texas Instruments mentions it is only available in preproduction quantities. Pricing starts at $2.45 in 1K orders. Check out the product page for more details.
TinyEngine software support
Both microcontrollers are supported by TI’s CCStudio IDE, relying on generative AI support to accelerate code development, system configuration, and debugging. The IDE also integrates more than 60 models and application examples in CCStudio Edge AI Studio.
Some code samples for the TinyEngine include:
- Generic time-series classification
- Arc fault (AFCI)
- Motor fault
- Electrocardiogram (ECG)
The utility also allows users to capture data, train and optimize custom models, and leverage open-source frameworks built-in supporting PyTorch, TensorFlow, and ONNX. You can also check the developer documentation to get started.
Thanks to TLS for the tip.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
