---
title: "SolidRun P100 COM Express Type 6 module features LPCAMM2 memory, up to 12-core AMD Ryzen AI Embedded P185 SoC"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/12/solidrun-p100-com-express-type-6-module-features-lpcamm2-memory-up-to-12-core-amd-ryzen-ai-embedded-p185-soc/"
published: "2026-03-11"
fetched: "2026-03-12T07:00:22.918315"
---

We just reported that the AMD Ryzen AI Embedded P100 series has been expanded with six additional SKUs, and, timed with that, SolidRun has announced its new P100 COM Express Type 6 module family. These compact (95 x 95mm) modules are among the first to support the newly released 8- to 12-core Zen 5 SKUs, with up to 50 TOPS from the NPU and 80 TOPS of total system AI.
Another fairly unique feature of the new SolidRun computer-on-module is support for LPCAMM2 LPDDR5X memory. The company uses a screw-lock mechanism to deliver high-bandwidth LPDDR5X performance (up to 9600 MT/s) while maintaining the mechanical reliability required for “systems in motion,” such as autonomous mobile robots (AMRs), heavy machinery, and rail systems. A mini-ITX development kit for the module is also available.
SolidRun P100 COM Express Type 6 module
SolidRun P100 COM Express Type 6 module specifications:
- AMD Ryzen AI Embedded P100 Series SoCs (one of the other)
- AMD Ryzen AI Embedded P132 – 6-core/ 12-thread Zen 5 processor up to 4.5 GHz, 6MB L2 and 8MB L3 Cache, 4x RDNA3.5 graphics @ 2800 MHz; TDP: 28W/54W turbo; NPU:50 TOPS (59 Combined)
- AMD Ryzen AI Embedded P164 – 8-core / 16-thread Zen 5 processor up to 5.0 GHz, 8MB L2 and 16MB L3 cache, 6× RDNA3.5 graphics @ 2800 MHz; TDP: 28W / 54W turbo; NPU: 50 TOPS (80 TOPS combined)
- AMD Ryzen AI Embedded P174 – 10-core / 20-thread Zen 5 processor up to 5.0 GHz, 10MB L2 and 24MB L3 cache, 6× RDNA3.5 graphics @ 2800 MHz; TDP: 28W / 54W turbo; NPU: 50 TOPS (80 TOPS combined)
- AMD Ryzen AI Embedded P185 – 12-core / 24-thread Zen 5 processor up to 5.1 GHz, 12MB L2 and 24MB L3 cache, 8× RDNA3.5 graphics @ 2900 MHz; TDP: 28W / 54W turbo; NPU: 50 TOPS (80 TOPS combined)
- AMD Ryzen AI Embedded P132a – 6-core/12-thread Zen 5 processor up to 3.65 GHz, 6MB L2 and 8MB L3 cache, 2 WGP (4x RDNA 3.5 graphics cores) @ 2400 MHz; TDP: 45W (25-45W range); NPU: 50 TOPS; Note: Features RAS support, no USB4.
- AMD Ryzen AI Embedded P122a – 4-core/8-thread Zen 5 processor up to 3.65 GHz, 4MB L2 and 8MB L3 cache, 2 WGP (4x RDNA 3.5 graphics cores) @ 2000 MHz; TDP: 28W (15-30W range); NPU: 30 TOPS; Note: Features RAS support, no USB4.
- Industrial and Automotive variants (P132i/P185i/P174i/P164i) available with -40°C to +105°C support
- System Memory – LPCAMM2 LPDDR5 slot up to 9600 MT/s; includes screw-lock retention for high-vibration environments.
- Storage
- M.2 2280 NVMe slot on module
- 48MB SPI Flash for BIOS/UEFI firmware
- PCIe to SATA converter
- Display – DP to LVDS converter (Default assembly bypass)
- Networking – Onboard Intel i226 2.5GbE Ethernet controller
- USB – 2x USB hub controller
- 2x 220-pin standard board-to-board connectors
- Storage – 2x SATA III (6Gb/s) ports
- Display
- 4x DisplayPort (DP) interfaces.
- Optional eDP to LVDS bridge (default is eDP)
- Supports up to 4x 4K displays @ 120Hz or 2x 8K displays @ 120Hz
- Audio – HD Audio over DDI ports or HDA interface
- Networking – 2.5Gbps Ethernet
- USB
- 2x USB4 (via USBC0/1) providing up to 40Gbps and integrated DisplayPort tunneling (DDI1/DDI2)
- 1x Native USB 3.x port; 3x USB 3.x ports via an onboard High-Speed USB Hub
- 8x USB 2.0 ports (Lanes 0-7) via an onboard USB 2.0 Hub
- PCIe
- 13x PCIe Gen4 lanes
- Additional 3x lanes optional, depending on SATA/NVMe/NIC configuration
- Low-speed I/Os – 2x UART, SPI, SMBus, I2C, 4x GPI, 4x GPO
- Security – dTPM 2.0; BMC ready
- Misc
- Power LED
- Thermal monitor
- Power Management
- Configurable TDP – 15 W to 54 W
- ACPI 6.0 with battery support
- Dimensions – 95 x 95 mm (Standard COM Express Type 6 Compact form factor)
- Temperature Range – Commercial: 0°C to +85°C; Industrial: -40°C to +85°C
- Humidity – 10% – 90% non-condensing
While writing the specification, I noticed that the processor section (in the datasheet) mentions “Krackan2e.” Which could be likely internal codenames for the processor or platform. “Krackan2e” is probably a typo or variant of “KrackenZE,” which aligns with AMD’s “Kraken” codename family (e.g., Kraken Point, a rumored or upcoming AMD APU lineup for mobile/embedded use). “ZE” might stand for “Zen Enhanced” or a specific variant. For some unknown reason, the COM Express module does not ship with the four-core P121 SoC.
The module supports Windows 10/11/IoT and Linux. Like other Ryzen AI Embedded P100 platforms, it also works with AMD’s ROCm open software stack and a virtualized reference stack based on the Xen hypervisor, allowing developers to run real-time tasks alongside standard OS environments.
It offers an alternative to the Congatec conga-TCRP1 COM Express Type 6 that was first unveiled with the 4-core and 6-core Ryzen AI Embedded P100 SKUs last January, and now updated to include the new 8-core and 12-core variants introduced at Embedded World 2026.
HoneyComb Ryzen P100 Mini-ITX Board
The COM Express module will also power the HoneyComb Ryzen AI Embedded P100 Mini-ITX board with the following specifications:
- Core Module – COM Express Type 6 Compact module based on AMD Ryzen AI Embedded P100 Series SoC (As described above)
- System Memory – Rugged, serviceable LPCAMM2 memory with screw-lock retention (On the COM Express module)
- Storage
- M.2 NVMe PCIe Gen 4 x4 socket (on carrier)
- M.2 NVMe PCIe Gen 4 x1 socket (located on the COM module)
- 2x SATA 3.0 ports
- Display
- 1x HDMI 2.1 port
- 2x Mini DisplayPort (mDP)
- 50-pin eDP connector
- Networking – 2x 2.5GbE RJ45 ports (one via COM module, one via onboard controller)
- USB
- 2x USB 3.2 ports (upper: 10Gbps; Lower: 5 Gbps)
- 3x USB 3.0 (5Gbps)
- Internal – 2x USB 2.0 headers
- Expansion
- PCIe x16 slot (physically x16, but with 8 active Gen 4 lanes); configurable as 1×8 or 2×4 PCIe Gen 4
- COM GPI/GPO GPIO header
- Debug – Micro USB connector for COM console (via FTDI)
- Misc
- CR2032 battery socket
- 4-pin PWM/TACH fan header
- A colour-coded header (possibly from panel LED, buttons etc)
- Power – Standard ATX Power/LED header
- Temperature Range
- Commercial – 0°C to 70°C
- Industrial – -40°C to +85°C
- Dimensions – 170 x 170 mm (Standard Mini-ITX form factor)
Following AMD’s production schedule, the 4- and 6-core variants are expected to ship in Q2 2026, while the high-performance 8- to 12-core models (P164 through P185) are slated for July 2026. SolidRun guarantees up to 10 years of longevity for these modules.
Yet, SolidRun says the Ryzen AI Embedded P100 module family and HoneyComb evaluation platform are “available today,” though pricing has not yet been publicly listed on the shop. A few more details about the Ryzen AI P100 COM Express Type 6 module and HoneyComb P100 carrier board can be found on the product page and in the press release.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
