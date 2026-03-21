---
title: "Radxa AICore DX-M1M M.2 2242 low-power AI module delivers 25 TOPS of edge AI performance for just 3W of power"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/21/radxa-aicore-dx-m1m-m-2-2242-low-power-ai-module-delivers-25-tops-of-edge-ai-performance-for-just-3w-of-power/"
published: "2026-03-21"
fetched: "2026-03-21T16:02:55.260032"
---

Radxa AICore DX-M1M is a compact, low-power M.2 edge AI acceleration module built around the DeepX DX-M1M neural processing unit (NPU) and delivers up to 25 TOPS (INT8) of AI performance while consuming only 3W of power.
Designed for industrial robot arms, autonomous mobile robots (ARM), edge servers, drones, and AIoT devices, the module delivers high-performance AI and ML capabilities without blowing the power budget. It relies on a PCIe Gen3 x2 interface and works with both x86 and Arm systems, including the Raspberry Pi 5 and Radxa ROCK SBCs.
AICore DX-M1M specifications:
- AI Accelerator – DeepX DX-M1M neural processing unit (NPU) with up to 25 TOPS AI
- System Memory – 1GB LPDDR4X @ 4266 MT/s (on-chip, supports up to 8GB according to DeepX)
- Storage – 1Gbit QSPI NAND / NOR flash
- Host Interface – PCIe Gen 3.0 x4 (supports Gen 1/2/3 and x1/x2) via M.2 M + B Key connector
- Power Consumption – 3W (Typical)
- Dimensions – 42 x 22 mm (M.2 2242 form factor); compatible with M.2 2280 slots via an adapter
- Temperature Range
- -25°C to 65°C (Stable performance; non-throttling)
- 65°C to 85°C (Thermal protection; throttling)
The Radxa AICore DX-M1M uses the DEEPX DXNN SDK, which supports model compilation, optimization, and hardware-accelerated inference on the DEEPX NPU. It supports PyTorch, ONNX, TensorFlow, and Keras models via the DX-COM compiler, converting them to the proprietary DXNN format.
The SDK includes the DXRT-NPU-Driver (a PCIe kernel driver), the DX-RT runtime for NPU interaction, DX-APP C++/Python demo templates, the DX-STREAM GStreamer plugin for real-time video pipelines, the DX Model Zoo with pre-compiled models ( face detection, image classification, object detection, image denoising, semantic segmentation, and pose estimation), and tools such as DX-Tron for model visualization. The software stack supports Windows 10/11 and Ubuntu Linux (24.04, 22.04, and 20.04 LTS), as well as Docker environments.
To speed up deployment, Radxa also offers the DX-All Suite, a simplified installation package that bundles the compiler and runtime components, allowing developers to quickly set up the complete DXNN environment using Docker or a local installation. More information is available on the getting started guide.
We previously wrote about the iMX8M Mini DX-M1 SOM and the ALPON X5 Edge AI computer, both based on the DeepX DX-M1 chip, and Radxa has also introduced a DX-M1-based AICore module in the past. The difference between the two is that the DX-M1 is a standalone AI accelerator chip that requires external LPDDR5 memory and a more complex hardware design, whereas the DX-M1M is a more integrated solution that combines the same NPU with on-chip LPDDR4X memory, making it easier to deploy in compact, plug-and-play form factors such as M.2 modules. While both deliver similar AI performance of up to 25 TOPS, the DX-M1 offers flexibility for custom designs, whereas the DX-M1M is designed for faster integration. DEEPX also provides the DX-M1ML chip and M.2 module, a light version of the DX-M1M with 13 TOPS of AI performance, but we could not find it for sale at this time.
The Radxa AICore DX-M1M is available on AliExpress for $97.67 and Arace Tech for $85.00. Radxa also notes that for stable performance under continuous load, you need an active cooler, such as the Radxa Heatsink 2012B, or a metal enclosure with thermal pads. More information can be found on the product page.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
