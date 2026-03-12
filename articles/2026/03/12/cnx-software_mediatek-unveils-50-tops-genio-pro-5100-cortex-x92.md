---
title: "MediaTek unveils 50 TOPS Genio Pro 5100 Cortex-X925/X4/A720 SoC, 7.2 TOPS Genio 420 Cortex-A78/A55 SoC for AIoT applications"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/12/mediatek-50-tops-genio-pro-5100-cortex-x925-x4-a720-soc-7-2-tops-genio-420-cortex-a78-a55-soc-for-aiot-applications/"
published: "2026-03-12"
fetched: "2026-03-13T07:00:20.812603"
---

After launching the Genio 360/360P hexa/octa-core SoCs last month, MediaTek has now expanded the lineup with the Genio Pro 5100 and Genio 420 AIoT SoCs at Embedded World 2026.
The Genio Pro 5100 is a 3nm SoC with an “all big-core” architecture and a 50+ TOPS NPU for Edge AI applications. The Genio 420, on the other hand, is a cost-efficient 6nm platform designed for smart home, retail, and industrial IoT devices.
MediaTek Genio Pro 5100
The Genio Pro 5100 integrates one Cortex-X925, three Cortex-X4, and four Cortex-A720 cores, as well as an Arm Immortalis-G925 GPU, and supports LPDDR5X memory up to 8533 Mbps. It can handle up to three 4K displays, up to 16 cameras via virtual channels, and 8K30 video encode/decode, and offers interfaces such as PCIe Gen4, USB 3.2 Gen2, USB 2.0, and dual 2.5GbE MAC.
Genio Pro 5100 (MT8894) specifications:
- CPU – 8-core Arm v9.2 processor
- 1x Arm Cortex-X925
- 3x Arm Cortex-X4
- 4x Arm Cortex-A720
- Dual-core RV55 real-time processor
- 12MB shared L3 cache, Arm TrustZone
- GPU – Arm Immortalis-G925 MC11 GPU (supports OpenGL, Vulkan, OpenCL)
- VPU
- Video Encode – H.264, H.265 up to 8K30
- Video Decode – H.264, H.265, AV1, VP9 up to 8K30
- JPEG – Encode – 2x 400 MP/s; decode – 314 MP/s
- Image Signal Processor – 3x ISP supporting 2x 4K30 + 8x FHD30 cameras
- AI acceleration – MediaTek 8th generation NPU(4x MDLA5.5 + 2x MVPU, GenAI; 53 TOPS AI performance)
- DSP – 2x Cadence Tensilica HiFi 5 DSP
- Memory – 64-bit LPDDR5x up to 8533 MT/s (up to 30GB)
- Storage – UFS 4.1 (2-lane), SD 3.0, SPI-NOR
- Display
- 4-lane eDP 1.5
- DisplayPort 1.4 (MST)
- 3x 4-lane MIPI DSI
- Up to 3x 4Kp60 displays supported
- Camera – 4x MIPI-CSI (Up to 16x 1080p30 via virtual channels)
- Audio
- 7x I2S / TDM
- 3x PDM
- HiFi-5 DSP audio processing
- Networking
- 2x 2.5GbE MAC (TSN)
- Wi-Fi 7 and Bluetooth 5.4 support via external module
- USB
- 1x USB 3.2 Gen2 (Host/Device) shared with DP
- 1x USB 2.0 Host
- 2x USB 2.0 Host/Device
- PCIe
- 2-lane PCIe 4.0
- 2x 1-lane PCIe 4.0
- Low-speed I/O – 6x UART, 7x I2C, 8x I3C, 8x SPI, 4x PWM, GPIO
- Security
- Secure boot (RSA-4096)
- Crypto engine
- Hardware RNG
- Secure JTAG
- eFuse custom fields
- Power-good detector
- Misc
- Watchdog timer
- System timer and general timers
- DMA engine
- Temperature sensor
- Package – ETFC TFBGA 15.9 × 16.6 mm, 0.35 mm pitch
- Temperature Range -40°C to 105°C (Tj) (Industrial)
- Manufacturing – TSMC 3nm process node
The Genio Pro 5100 supports Android (NDA required for docs) with various Linux distributions, including Yocto, Debian, and Ubuntu, as well as the ROS 2 (Robot Operating System) framework for robotics development. It also supports MediaTek’s NeuroPilot SDK for AI workloads using frameworks such as PyTorch, ONNX Runtime, and TensorFlow Lite.
MediaTek Genio 420
The Genio 420 octa-core Armv8 processor is built on a 6nm process with two Cortex-A78 and six Cortex-A55 cores, a Mali-G57 MC2 GPU, and up to 7.2 TOPS of AI acceleration. It supports up to 16GB of LPDDR5X memory, dual 2.5K60 displays or a single UW5K60/4K60 display, and is pin-to-pin compatible with the Genio 720 and Genio 520, allowing OEMs to scale designs across platforms.
Genio 420 (MT8371LV) specifications:
- CPU – 8-core Armv8 processor
- 2x Arm Cortex-A78 @ 1.8 GHz
- 6x Arm Cortex-A55 @ 1.6 GHz
- 1MB L3 cache, Arm TrustZone
- GPU – Arm Mali-G57 MC2 GPU (OpenGL, Vulkan, OpenCL support)
- VPU
- Video Encode – H.264, H.265 up to 4Kp30
- Video Decode – H.264, H.265, VP9 up to 4Kp60; MPEG4/VP8 up to 1080p60
- JPEG – Encode – 400 MP/s; decode – 250 MP/s
- Image Signal Processor – 1x Single ISP supporting up to 16MP @ 30fps camera
- AI acceleration – MediaTek 8th generation MDLA 5.3 NPU (6.1 TOPS, 7.2 TOPS total system AI performance)
- Memory
- LPDDR4X up to 4266 MT/s up to 8GB
- LPDDR5/LPDDR5X up to 6400 MT/s up to 16GB
- Storage
- 2-lane UFS 3.1
- eMMC 5.1
- SD 3.0 / SDIO 3.0
- SPI-NOR
- Display
- 4Kp60 or 2x 2.5Kp60
- Ultra-wide 5K display support
- eDP, DP, LVDS, MIPI-DSI outputs
- Dual display support
- Camera – 2x MIPI-CSI (Up to 6x 1080p30 via virtual channels)
- Audio
- Input – 2x I2S, 1x PCM, 2x DMIC
- Output – 2x I2S, 1x PCM
- Networking
- GbE MAC with TSN
- Optional Wi-Fi 6 (1×1) + Bluetooth 5.3 via MT6631X
- Optional Wi-Fi 6E (2×2) + Bluetooth 5.3 via MT6637X
- USB
- 3x USB 2.0 host
- 1x USB 3.2 Gen1 host
- 1x USB 3.2 Gen1 host/device (shared with DisplayPort)
- PCIe – 1x PCIe 2.0 (1-lane, RC, WoWLAN)
- Low-speed I/O – 4x UART, 9x I2C, 6x SPI, 3x PWM, GPIO, JTAG
- Security
- ARM TrustZone
- Secure boot (RSA-4096)
- Crypto engine
- Random number generator
- eFuse custom field
- Secure JTAG
- Power good detector
- Misc
- Watchdog
- System timer/timers
- DMA
- Boundary scan
- Temperature sensor
- Package – VFBGA 13.8 × 11.8 mm, 0.4 mm pitch
- Temperature Range – -20°C to 95°C (Tj)
- Manufacturing – TSMC 6nm process node
The Genio 420 runs on MediaTek’s unified Genio software platform, which supports Android, Yocto Linux, and Ubuntu via the official SDK and BSP. AI development is supported through the NeuroPilot SDK, which is also compatible with TensorFlow Lite, PyTorch, and ONNX, as well as optimized models from MediaTek’s Model Hub and NVIDIA TAO catalog.
The MediaTek Genio Pro 5100 and Genio 420 expand the Genio IoT platform lineup. The Genio Pro 5100 adds a new high-performance “Pro” version with an all big-core Armv9 CPU configuration and a 50+ TOPS NPU for edge GenAI workloads. The Genio 420 will fall somewhere between the Genio 720 and Genio 520, and it’s designed for a mainstream IoT processor with Cortex-A78 and Cortex-A55 cores and a 6.1 TOPS AI accelerator. You can read the highlights in the table below, or check out the full comparison table in the PDF provided by MediaTek.
At the time of writing, I cannot find any information about a development board for the Genio Pro 5100 or Genio 420. The company mentions that Genio Pro 5100 will start sampling in Q1 2026, with mass production slated for Q3 2026. The Genio 420 will begin sampling in April 2026. The previously announced Genio 360 series is currently being sampled with partners. More details can be found on the Genio website and the press release.
Thanks to TLS for the tip.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
