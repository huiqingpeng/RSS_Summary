---
title: "High-end 25MP global shutter camera with 10GbE interface is designed for NVIDIA Holoscan platform"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/18/high-end-25mp-global-shutter-camera-with-10gbe-interface-is-designed-for-nvidia-holoscan-platform/"
published: "2026-03-18"
fetched: "2026-03-18T14:11:08.945323"
---

Leopard Imaging LI-IMX530-10GigE-NL is a high-end 25MP global shutter camera designed specifically for the NVIDIA Holoscan edge AI platform. The camera utilizes a 10GbE interface for high-bandwidth, low-latency data transmission, making it suitable for gesture recognition, iris scanning, head roll, and eye tracking.
At the core of the camera module is the Sony IMX530, a 1.2-inch CMOS sensor with 5328 × 4608 resolution and a 2.74 μm pixel size. The sensor data is handled by a Lattice CertusPro-NX FPGA, and a Marvell 10GbE PHY takes care of high-bandwidth data transfer to GPU systems. The camera supports NVIDIA Jetson AGX Orin, IGX Orin, and Thor platforms.
LI-IMX530-10GigE-NL specifications:
- FPGA – Lattice CertusPro-NX FPGA
- 52K to 96K logic cells
- 7.3 Mb total embedded memory
- External LPDDR4 memory support
- Up to 156x (18 x 18) multipliers within sysDSP blocks for AI/ML workloads
- 10 Gigabit Ethernet PCS blocks
- Image sensor
- Sony IMX530 Diagonal 19.3 mm CMOS color image sensor
- Sensor active area – 5328 × 4608 pixels ~25MP
- Pixel size – 2.74 μm × 2.74 μm
- Lens – Supports C-mount lens
- Networking – Marvell 10Gbps Ethernet PHY with RJ45 connector
- Power Supply – External 12 VDC input via a power jack
- Dimensions – 140 x 55 x 50 mm
- Weight – ~307 grams
One of the most important parameters of any global-shutter camera is the maximum frame rate, and Leopard Imaging does not even mention it on their datasheet or product page, but we can make an educated guess based on the hardware. The sensor itself maxes out at 106 FPS, but when piped through a 10GbE interface, the bandwidth bottleneck typically limits uncompressed 24.5MP output to somewhere between 35 and 50 FPS, depending on whether it’s running in 8-bit or 12-bit mode.
There is limited information about software support, and the company states that the driver is available upon request, enabling integration with custom machine-vision and edge-AI software stacks. Again, the camera is optimized for NVIDIA Holoscan, for direct sensor-to-GPU data transfer over Ethernet.
Previously, we wrote about the Arducam KingKong global-shutter camera designed for the Raspberry Pi CM4, and reviewed the Raspberry Pi Global Shutter Camera and the e-con Systems See3CAM_24CUG USB 3.1 global shutter camera. While all these are also global shutter cameras, the Leopard Imaging LI-IMX530-10GigE-NL is in a different class with a 25MP camera sensor and 10GbE networking.
The LI-IMX530-10GigE-NL is currently available for $1,699.00 through the Leopard Imaging web store. Some more details can be found in the press release. In the package, you will receive the camera module, a CAT-8 10G Ethernet Cable, and a 12 VDC Power Supply Adaptor.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
