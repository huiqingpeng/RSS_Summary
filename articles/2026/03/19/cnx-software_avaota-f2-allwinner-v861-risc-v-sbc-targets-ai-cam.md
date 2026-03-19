---
title: "Avaota F2 – Allwinner V861 RISC-V SBC targets AI cameras with PTZ and audio support"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/19/avaota-f2-allwinner-v861-risc-v-sbc-targets-ai-cameras-with-ptz-and-audio-support/"
published: "2026-03-19"
fetched: "2026-03-19T19:03:40.209989"
---

Avaota F2 is the first SBC based on an Allwinner V861 dual-core 64-bit RISC-V SoC with 128MB on-chip DDR3 memory, support for 4K cameras, a H.265 video codec, and a 1 TOPS AI accelerator.
It’s an update to the earlier Avaota F1 camera board based on an Allwinner V821 SoC. The new open-source hardware F2 SBC offers several benefits, including support for both Full HD and 4K camera sensors, motor control for the PTZ (Pan-Tilt-Zoom) feature, and improved audio support through speaker (one) and microphone (two) connectors. However, the F1 also included WiFi, which the Avaota F2 lacks.
Avaota F2 specifications:
- SoC – Allwinner V861M2-XXX
- CPU
- Dual-Core RISC-V XuanTie C907 (RV64GCBV/RV32GGCBV) clocked up to 1.4GHz with RVV 1.0 extensions
- Single-core RISC-V XuanTie E907 (RV32IMAFC) clocked up to 800MHz
- VPU
- Video Encoder
- H.264/H.265 up to 4K @ 25fps
- (M)JPEG up to 8192×8192
- Video Decoder – (M)JPEG up to 1080p60
- Video Encoder
- AI accelerator – 1 TOPS (INT8) NPU dubbed “AI-ISP 2.0”
- Memory – 128MB DDR3
- CPU
- Storage
- 16MB NOR flash (PY25Q128)
- MicroSD card slot
- Display – Support for SPI screens via headers, including a 3.5-inch 320×480 display and a 1.54-inch 240×240 display
- Camera
- 4-lane MIPI CSI connector
- 2-lane MIPI CSI connector
- Support for GC2083 (1920×1080 @ 30fps) and GC8613 (3840×2160 @ 15fps)
- Audio
- Speaker connector
- Two microphone connectors
- USB – USB Type-C port for power, data, and serial output
- Expansion
- 2x 17-pin headers (through and castellated holes) with up to 28x GPIO
- 8x castellated holes for motor control (useful for PTZ camera)
- Debugging – UART serial and ADB USB debugging are supported
- Misc
- Power and FEL (Firmware flashing) buttons
- User LED
- Power Supply
- 5V via USB-C port
- Integrated AXP333 power management chip (also used for PTZ)
- Dimensions – About 40 x 22mm (6-layer PCB)
The Avaota F2 is open-source hardware with PDF schematics, EasyEDA Pro PCB files, Gerber files, the 3D STEP file, a bill of materials, and pick-and-place instructions available on GitHub under a Creative Commons CC0.
GitHub lacks software information, but the developer shared a screenshot showing the board runs OpenWrt 21.04 (fork) with Linux 6.6, a few months ago, part of Allwinner’s Tina Linux SDK. Instructions to download the SDK can be found on the documentation website, along with tutorials to use Allwinner V861 features, sadly, in Chinese only at this time.
The Avaota F2 is not for sale now, but should show up on Taobao shortly. The previous model (Avaota F1) is currently sold on AliExpress for about $33 as part of a kit with a camera, a “2-in-1 serial port module”, a USB debug board, and a USB-C port.
Via GLGH_ on X
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
