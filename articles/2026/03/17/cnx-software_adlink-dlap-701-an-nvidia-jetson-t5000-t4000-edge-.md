---
title: "ADLINK DLAP-701 – An NVIDIA Jetson T5000/T4000 Edge AI platform for humanoid robots and vision sensing systems"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/17/adlink-dlap-701-an-nvidia-jetson-t5000-t4000-edge-ai-platform-for-humanoid-robots-and-vision-sensing-systems/"
published: "2026-03-17"
fetched: "2026-03-18T07:00:19.469990"
---

ADLINK has just launched the DLAP-701 Series, a NVIDIA Jetson T5000/T4000-based compact edge AI platform designed for humanoid robots, autonomous mobile robots (AMR), and vision sensing systems (VSS).
It supports up to 128GB LPDDR5X memory and features various I/O options, including dual Gigabit Ethernet, a QSFP port supporting 4×25GbE LAN, multiple USB 3.2 ports, and HDMI output, along with M.2 slots for Wi-Fi 6, 5G, and NVMe storage, as well as an mPCIe slot. It also integrates CAN-FD interfaces for robotics and vehicle control and TPM 2.0 security. With an operating voltage range of 9-36V DC and an industrial temperature range of -20°C to 60°C, it is designed for demanding edge environments.
ADLINK DLAP-701 specifications
- Supported system-on-module – NVIDIA Jetson Thor T5000 or Jetson Thor T4000
- Memory – Up to 128GB (T5000 variant), 64 GB (T4000 variant) 256-bit LPDDR5X (273 GB/s bandwidth)
- Storage
- 128GB SSD for the OS (most probably ADLINK’s ASD+ industrial SSD designed for harsh environments)
- M.2 M-key slot for NVMe SSD expansion
- Display – 2x HDMI 2.0b up to 3840×2160 @ 60Hz
- Audio –2x 3.5mm jacks for Mic-in and Line-out.
- Networking
- 2x Gigabit Ethernet (10/100/1000 Mbps) RJ45 ports
- QSFP28 cage (configurable as 4x 25GbE)
- M.2 E-key slot for Wi-Fi 6
- M.2 3052/3042 B-key slot for 5G, with 2x micro-SIM slots for dual SIM support
- USB
- 4x USB 3.2 Type-A ports
- 2x USB 3.1 Type-C ports (one front, one back)
- USB Type-C dedicated for BSP (Board Support Package) installation on the front
- Expansion
- M.2 2280 M-key slot for NVMe SSD
- M.2 2230 E-key slot for Wi-Fi 6
- M.2 3052/3042 B-key slot for 5G cellular
- mPCIe slot
- 20-pin Euro Terminal Block with
- 1x CAN-FD (Isolated 3KV)
- 3x CAN-FD with Transceiver
- UART, IFC (I2C)
- +5V output (1A)
- +3.3V output (1A)
- Security – Onboard TPM 2.0
- Misc
- RTC battery
- Internal thermal sensor
- Power button (front) and Recovery button (back).
- 3x internal pin headers for fans
- Power Supply – 9-36V +/-5% DC input via terminal block
- Dimensions – 211 x 194 x 94 mm (including rubber feet)
- Weight – 2 kg
- Temperature Range – -20°C to 60°C
- Humidity – 95% @ 40°C (non-condensing)
Regarding software support, the company only mentions support for “Windows, Ubuntu, and EdgeGO”, but this may not be totally correct since we’ve never heard about Jetson T5000/T4000 supporting Windows. However, it should be supported by the Ubuntu-based JetPack SDK with CUDA acceleration, TensorRT, and drivers for the Blackwell GPU, along with the NVIDIA Isaac platform for humanoid robotics, offering libraries, frameworks, and foundational models. EdgeGO is ADLINK’s remote management software.
The number of Jetson Thor-based devices grows. We notably previously covered the ASUS IoT PE3000N MIL-STD-810H rugged modular computer, the Firefly EC-ThorT5000 with support for eight GMSL2 cameras and four 10GbE, and the Lanner EAI-I351 embedded system with 100GbE QSFP28 and eight GMSL2 camera support.
With this announcement, the company also introduced the DLAP-711 and DLAP-IGX series. Compared to the DLAP-701, the DLAP-711 is also based on Jetson T5000/T4000 and designed for humanoid robots, but it features four GbE and two 100Mbps Ethernet ports and comes in a slightly smaller form factor, as well as a wider operating temperature range of -20°C to 65°C (vs. -20°C to 60°C).
The DLAP-IGX series is ADLINK’s industrial, enterprise-grade edge AI platform, built around the NVIDIA IGX T7000, delivering up to 4,293 TFLOPS (FP4 sparse). It supports an optional discrete GPU, such as the NVIDIA RTX PRO 5000 Blackwell, features a 14-core ARM Neoverse-V3AE CPU, and integrates an NVIDIA ConnectX-7 SmartNIC with dual 200GbE QSFP28 ports for ultra-high-bandwidth networking. The platform also offers PCIe Gen5 expansion (x8 and x16), high-speed USB 3.2, and extensive industrial I/O, all within a rugged design suited for demanding AI and edge computing deployments.
The company does not mention any pricing information for the DLAP-701, and like most industrial edge AI systems, you’ll need to contact ADLINK for details. For the DLAP-711, I was unable to find any product page or additional information at the time of writing. Finally, the DLAP-IGX series is marked as “Preliminary,” meaning no pricing or availability information has been disclosed, and final specifications may change without notice. More details can be found in the press release.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
