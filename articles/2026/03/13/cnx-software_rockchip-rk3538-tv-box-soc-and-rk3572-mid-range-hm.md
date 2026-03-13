---
title: "Rockchip RK3538 TV Box SoC and RK3572 mid-range HMI processor are coming soon"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/13/rockchip-rk3538-tv-box-soc-rk3572-mid-range-hmi-processor/"
published: "2026-03-13"
fetched: "2026-03-14T07:00:19.888493"
---

While we are eagerly waiting for the RK3668 and RK3688 high-end processors, Rockchip is planning to launch two mid-range SoCs with the RK3538 quad-core Cortex-A55 processor designed for TV boxes, and the RK3572 hexa-core Cortex-A73/A53 SoC for HMI (Human Machine Interface) applications.
Rockchip RK3538 TV box SoC
Rockchip RK3538 specifications:
- CPU – Quad-core Arm Cortex-A55 processor with NEON, FPU, ARMv8 Crypto…
- Cache
- 32KB L1 instruction cache
- 32KB L1 data cache and 64KB L2 data cache
- 512KB unified system L3 cache
- GPU
- Arm Mali-G310 3D GPU with support for OpenCL 3.0, OpenGL ES1.1/2.0/3.2, Vulkan 1.2
- 2D Graphics Engine
- VPU
- Decoder
- H.265, H.264, AV1 (up to two simultaneous 1080p60 channels)
- VP8, VC1, MPEG-4, MPEG-2, MPEG-1 yp to 1920×1088 @ 60 FPS (1088 is not a typo)
- H.263 up to 720p60
- (M)JPEG up to 8176×8176 @ 76 million pixels per second
- Encoder – N/A
- Decoder
- MCU core – RISC-V MCU in PMU domain with dedicated mailbox and watchdog.
- Memory – 32-bit DDR3(L)/LPDDR3/DDR4/LPDDR4(4X) up to 2GB
- Storage – eMMC 5.1, SD 3.0/MMC 4.51, FSPI (Flexible Serial Flash Interface), NANDC interface
- Video Output
- HDMI 2.1 up to 1080p60 10-bit, with HDCP 2.3, HDR10+ support
- CVBS/PAL TV interface
- Audio
- 24-bit audio DAC
- 2x 2-channel SAI (Serial Audio Interface), 1x 8-channel SAI; up to 192 kHz sample rate
- 8-channel PDM up to 192 kHz sample rate
- S/PDIF output
- Networking – 10/100 Mbps Ethernet controller and MAC PHY
- USB
- USB 2.0 DRD
- USB 2.0 Host
- Other peripheral interfaces
- GPIO
- SDIO 3.0
- 6x UART, 2x SPI, 6x I2C
- 8x PWM
- 4-channel DMAC
- Analog
- 13-bit SARADC up to 2 MS/s
- Temperature sensor (TS-ADC)
- Timers
- 2x 64-bit secure timers with interrupt-based operation
- 6x 64-bit non-secure timers with interrupt-based operation
- 1x high precision timer
- Security
- AES, DES, 3DES, SM4 symmetrical algorithms
- RSA, ECC, SM2 asymmetrical algorithms
- SHA-1, SHA-256/224, SHA-512/384, SHA-512, MD5, SM3 hash algorithms
- Key ladder
- Security TRNG and non-security TRNG
- Secure OTP
- Secure debug
- Secure OS…
- Misc – Watchdog timer
- Package – FBGA434L (body:13.3mm x 13.5mm ;ball size: 0.3mm ;ball pitch: 0.65/0.6mm)
- Temperature Range – Junction: up to 125°C; storage: -40 to +125°C
We have more information about the RK3538 since the datasheet is available, but I’m unable to find any device based on it for now. I’d assume the first product will be TV boxes since it’s the target market for the chip.
Rockchip RK3572 HMI SoC
I was first informed about the existence of the RK3572 on the SBCWiki website, but came across the RK3538 when I realized that both processors are often mentioned together on GitHub, which probably means they share some IP blocks, at least the VPU. The RK3572 datasheet and TRM are nowhere to be found at this stage, so most information comes from the SBCWiki website. First, the RK3572 is shown in the Rockchip HMI roadmap, and offers an “Advanced” HMI solution between the RK3568 and RK3576.
Rockchip RK3572 specifications (preliminary):
- Hexa-core CPU – 2x Arm Cortex-A73 @ 2.3 GHz, 4x Arm Cortex-A53 @ 2.0 GHz
- GPU – Arm Mali-G310 v2
- VPU
- 4K @ 120FPS decoder
4K @ 30FPS encoder
- 4K @ 120FPS decoder
- AI accelerator – 3 TOPS NPU
- System Memory – 32-bit LPDDR4/4x or LPDDR5/5x
- Storage – UFS 2.1, eMMC flash
- Video Output – HDMI, DSI, eDP up to 4Kp60
- Camera – MIPI CSI and DVP (TBC); source: blog.csdn.net
- Networking – 2x RGMII (Gigabit Ethernet)
- USB – 2x USB 3.0 OTG
- Other interfaces – DSMC (Local Parallel Bus)/CAN Bus
Mecid Urganci (from the SBCWiki website) was able to check out the official RK3572 EVB (pictured above) at Embedded World 2026. It comes with 4GB RAM, 128GB storage, and runs Debian 13 Trixie 64-bit. I can also see two Gigabit Ethernet ports, a microSD card, a few USB ports, and a PCIe slot. Benchmarks show the RK3572 between RK3568 and RK3576 in the Geekbench 6 multi-core benchmark.
Mecid notes that the single-core benchmark is slightly better on the RK3572, and he also tested Vulkan with Geekbench 6 using the Mali version g29p1 drivers. I notice the EVB does not include a heatsink, so like other Cortex-A73 SoCs, it may not require cooling, or only a small/thin one.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
