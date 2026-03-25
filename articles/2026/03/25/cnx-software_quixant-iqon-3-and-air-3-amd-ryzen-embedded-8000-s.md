---
title: "Quixant IQON 3 and Air 3 AMD Ryzen Embedded 8000 systems target casino and arcade gaming"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/25/quixant-iqon-3-and-air-3-amd-ryzen-embedded-8000-systems-target-casino-and-arcade-gaming/"
published: "2026-03-25"
fetched: "2026-03-26T07:00:34.348403"
---

Quixant IQON 3 and IQON Air 3 are two new Ryzen Embedded 8000-based industrial systems designed specifically for casinos, sports betting, and arcade gaming machines. Built around AMD Ryzen 5 and Ryzen 7 PRO R8000 Series SoCs, they support four independent 4K displays and feature game-specific hardware, including 4MB of battery-free MRAM for instant state saving, eleven physical intrusion-detection monitors, dedicated LED controllers, and casino-standard serial interfaces such as ccTalk, JCM ID003, and SAS.
Both systems are very similar in hardware specifications, but the IQON 3 is a passively cooled, fanless system, whereas the IQON Air 3 comes with a cooling fan enabling a higher TDP (ranging from 15W to 54W) for graphics-intensive workloads.
Quixant IQON 3 and IQON Air 3 specifications:
- SoC – AMD Ryzen 5 or 7 PRO R8000 Embedded Series SoCs with Zen 4 cores, AMD Radeon 7x0M graphics (RDNA 3), and AMD XDNA NPU
- System Memory
- Up to 64GB via 2x DDR5 5600MT/s SODIMM sockets (ECC options supported)
- NVRAM (State Memory) – 4MB battery-free MRAM over a fast 64-bit PCIe interface with bank mirroring, copying, and CRC support
- Storage
- M.2 NVMe Gen4x4 socket
- 2x CFast 2.0 sockets
- 2x SATA3 sockets
- 2Kbits of user EEPROM storage (optional up to 128 Kbits)
- Display – 4x 4K UHD displays via DisplayPort 1.4
- Audio
- Integrated HD audio controller with 7.1 channels
- 2x stereo 22W/channel 8-Ohm digital amplified outputs
- Networking – 2x Gigabit Ethernet RJ45 ports via PCIe LAN interfaces
- USB
- 4x USB 3.2 ports (front)
- 4x USB 2.0 ports (side)
- 2x vertical internal USB-A (1x USB 3.2, 1x USB 2.0)
- 2x USB 2.0 internal pin headers
- Serial
- 6x serial ports (2x RS232 full, 2x RS232 Tx/Rx)
- Up to 4x SAS (Slot Accounting System) interfaces
- Up to 2x ccTalk, 1x JCM ID003, 1x RS485
- 1x I2C interface and 1x SPI header for clock serial peripherals
- Up to 2x iButton interfaces
- Expansion
- M.2 NVMe Gen4x4 socket (internal)
- Up to 32 digital inputs (hardware debounce)
- 32 digital outputs (tamper/disconnect detection for physical audit meters)
- Security
- TPM 2.0
- 2Kb secure EEPROM with SHA-3 engine
- Embedded hardware AES256 engine
- Active storage write-protect monitoring
- Unique electronic serial number
- Misc
- Up to 6x LED strip interfaces driving 1-wire/2-wire strips (up to 3000 LEDs total)
- 9x PWM outputs for brightness
- 11x monitored intrusions with system event logging
- Temperature & voltage monitoring
- Watchdog timer
- RTC
- Automatic battery health check
- Cooling
- Active cooling system (IQON Air 3 only)
- Fanless passive cooling (IQON 3 only)
- Power – 12V operating voltage
- Dimensions – TBD (metal case with keylock)
- Compliance – GLI-11 and global gaming compliance
While writing the specifications, I noticed a discrepancy in the IQON Air 3 audio output: the datasheet lists 2x 15W/ch (4Ω), while the product page specifies 2x 22W/ch (8Ω).
In terms of software support, Quixant provides its Essential and Enhanced Software Suite, which includes tools for QSys temperature/voltage monitoring, hardware authentication, and API integrations for the onboard GPIO and LED controllers. Other than that, no information is present at the time of writing.
The company also notes that while its design is primarily for the gaming sector, the device can also be used in Pro AV, digital signage, and broadcast control rooms through Quixant’s sister company, Densitron, which leverages IQON’s Ryzen Embedded 8000 architecture, specifically its NPU, for AI-assisted video processing to power industrial video walls and studio multi-viewers.
This is not the first time we have written about products designed for casino or arcade gaming. Previously, we covered the Axiomtek GMB850 mini-ITX motherboard for casino gaming machines, as well as similar boards like the Kontron D3724-R (mSTX) and Kontron D3723-R.
Pricing and availability information have not been made public, which is typical for B2B gaming hardware. The company also mentions that both the IQON 3 and IQON Air 3 have a 10-year supply lifecycle. More details can be found on their respective product pages and AMD’s press release.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
