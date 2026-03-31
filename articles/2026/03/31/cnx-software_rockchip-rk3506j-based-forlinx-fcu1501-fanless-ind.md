---
title: "Rockchip RK3506J-based Forlinx FCU1501 fanless industrial IoT gateway offers dual Ethernet, plenty of I/Os and serial interfaces"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/31/rockchip-rk3506j-based-forlinx-fcu1501-fanless-industrial-iot-gateway-offers-dual-ethernet-plenty-of-i-os-and-serial-interfaces/"
published: "2026-03-31"
fetched: "2026-04-01T07:00:33.998932"
---

Forlinx Technology has recently introduced the FCU1501, a rugged, fanless industrial embedded computer and IoT gateway built around the Rockchip RK3506J processor with a tri-core Cortex-A7 and a single Cortex-M0 core. The system is designed for high-reliability data acquisition and protocol conversion in harsh environments.
The gateway comes in two variants (basic and extended), which have similar dimensions but differ mainly in interface density. Both models feature up to 512MB DDR3 RAM, 8GB eMMC flash, dual Fast Ethernet, dual-band Wi-Fi & Bluetooth 5.0, and 4G LTE Cat 1 support. Applications include automation, rail transit, and smart manufacturing. The system supports a wide industrial temperature range (-40°C to +85°C) and meets Level 3 EMC standards.
Forlinx FCU1501 Specifications:
- SoC – Rockchip RK3506J
- CPU
- 3x Arm Cortex-A7 cores up to 1.5 GHz
- Arm Cortex-M0 real-time core
- GPU – 2D GPU only
- No VPU, no NPU
- CPU
- System Memory – 256MB or 512MB DDR3
- Storage
- 256MB NAND Flash or
- 8GB eMMC flash
- Networking
- 2x 10/100Mbps Fast Ethernet RJ45 ports (auto-sensing, no PoE)
- Dual-band Wi-Fi and Bluetooth 5.0 with dual antenna interfaces
- Optional 4G LTE Cat 1 cellular connectivity via Nano SIM slot
- USB – 1x USB 2.0 Type-A port (supports OS flashing)
- Serial
- 4x RS485, 2x RS232, 1x CAN FD / CAN 2.0B (Basic Version)
- 8x RS485, 2x RS232, 2x CAN FD / CAN 2.0B (Extended Version)
- RS232 is multiplexed with RS485; all channels feature independent digital ground
- Other I/Os
- 2x DI (Dry contact), 2x DO (Relay output, Normally Open, 5A 250VAC / 5A 30VDC) (Basic Version)
- 8x DI, 8x DO (Extended Version)
- Debugging – USB Type-C debug port
- Misc
- 8x LEDs (Power, Run, Error, 3x 4G signal, 2x User-defined)
- Hardware Watchdog, internal battery-backed RTC, built-in buzzer
- “RESET KEY” for one-click network parameter recovery (customizable)
- Power Supply
- 9V to 36V DC wide input via terminal block (Rated 12V/3A)
- Reverse polarity and overcurrent protection
- DC Out (matches input voltage)
- Dimensions
- 177 x 130.5 x 45 mm (Enclosure only)
- 187 x 152 x 45 mm (Including mounts, terminals, and antenna base)
- Weight – 0.8 kg (Basic) / 0.9 kg (Extended)
- Temperature Range – Operating: -40°C to +85°C; Passive cooling / Fanless
- Certifications – CE, FCC, RoHS, Level 3 EMC
Note: 4G LTE modules are notoriously region-locked based on frequency bands. Forlinx does not specify which LTE module they use (e.g., Quectel or SIMCom) or which bands are supported.
Software information is limited, and the company only mentions that the FCU1501 runs a Linux 6.1 kernel and comes pre-loaded with industrial protocols and middleware, including Modbus (TCP/RTU conversion and passthrough), TCP/IP, SSH, OpenVPN, Nginx, and reverse proxy support.
The company also introduces a web-based management interface that lets users configure network settings, adjust communication parameters, and check system status directly from a web browser, without needing any special software, making setup and maintenance easier.
Previously, we have written about other industrial Rockchip RK3506J hardware platforms such as Banana Pi BPI-Forge1 SBC, ArmSoM CM1 SoM, or Forlinx FET3506J-S system-on-module, but it’s the first time we’ve covered an RK3506J IoT gateway or complete system based on Rockchip’s tri-core SoC.
The Forlinx FCU1501 fanless industrial IoT gateway is now available for order on Tmall, priced at ¥929 (around $134.41) for the 4G (512+8GB) extended version with power adapter, which is highly competitive considering the features. More details, including hardware datasheets and user manuals, are available on the product page.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
