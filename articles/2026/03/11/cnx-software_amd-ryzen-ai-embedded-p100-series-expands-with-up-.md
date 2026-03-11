---
title: "AMD Ryzen AI Embedded P100 series expands with up to 12 Zen 5 cores, 80 TOPS of AI performance"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/11/amd-ryzen-ai-embedded-p100-series-expands-with-up-to-12-zen-5-cores-80-tops-of-ai-performance/"
published: "2026-03-11"
fetched: "2026-03-12T07:01:47.246859"
---

At CES 2026, we saw AMD launch its new Ryzen AI Embedded P100 series of SoCs, with four- and six-core models designed for Edge AI. At the time of writing, the lineup had six SKUs, with higher-core variants to be announced later.
Now at Embedded World 2026, AMD has expanded the Ryzen AI Embedded P100 series with six additional SKUs available in commercial and industrial temperature grades, while the automotive-grade SoCs remain unchanged.
The new SOCs integrate 8-12 Zen 5 CPU cores (upgrade from 4-6 cores ), RDNA 3.5 graphics, and an XDNA 2 NPU on a single chip to deliver up to 80 TOPS (upgrade from 50 TOPS) of combined/system AI performance
AMD claims up to 39% higher multithreaded CPU performance and 2.1× higher total system TOPS compared to Ryzen Embedded 8000 Series. They support unified CPU-GPU memory, enabling low-latency processing for tasks such as multi-camera machine vision, Visual SLAM, and robotic perception, while the NPU handles low-power AI inference workloads, such as object detection and scene understanding.
Another six new SoCs have been added to the Ryzen AI Embedded P100 family: AMD Ryzen AI P164, P174, P185, P164i, P174i, and P185i, targeting commercial and industrial (i) applications. The AMD Ryzen AI Embedded P100 Series is now comprised of 12 different SKUs.
Commercial Temp | Industrial Temp | Automotive Grade |
|||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Model # | P121 | P132 | P164 | P174 | P185 | P121i | P132i | P164i | P174i | P185i | P122a | P132a |
|
| CPU | “Zen 5” CPU Cores | 4 | 6 | 8 | 10 | 12 | 4 | 6 | 8 | 10 | 12 | 4 | 6 |
| Max Frequency | Up to 4.4 GHz | Up to 4.5 GHz | Up to 5.0 GHz | Up to 5.0 GHz | Up to 5.1 GHz | Up to 4.4 GHz | Up to 4.5 GHz | Up to 5.0 GHz | Up to 5.0 GHz | Up to 5.1 GHz | Up to 3.65 GHz | Up to 3.65 GHz |
|
| L3 Shared Cache | 8 MB | 8 MB | 16 MB | 24 MB | 24 MB | 8 MB | 8 MB | 16 MB | 24 MB | 24 MB | 8 MB | 8 MB |
|
| GPU | Work Group Processors | 1 | 2 | 6 | 6 | 8 | 1 | 2 | 6 | 6 | 8 | 2 | 2 |
| 4K120/8Kp120 Displays | 4 / 2 |
||||||||||||
| GPU Max Frequency | 2.7 GHz | 2.8 GHz | 2.8 GHz | 2.8 GHz | 2.9 GHz | 2.7 GHz | 2.8 GHz | 2.8 GHz | 2.8 GHz | 2.9 GHz | 2.0 GHz | 2.4 GHz |
|
| NPU | TOPS | 30 | 50 | 50 | 50 | 50 | 30 | 50 | 50 | 50 | 50 | 30 | 50 |
| Memory | DDR5 (ECC) | 5600 MT/s | N/A | N/A |
|||||||||
| LPDDR5X (ECC) MT/s | 7500 MT/s | 8000 MT/s | 8533 MT/s | 8533 MT/s | 8533 MT/s | 7500 MT/s | 8000 MT/s | 8000 MT/s | 8000 MT/s | 8000 MT/s | 7500 MT/s w/RAS | 7500 MT/s w/RAS |
|
| I/O | 10GE Ports w/TSN | 2 | 2 | N/A | N/A | N/A | 2 | 2 | N/A | N/A | N/A | 2 | 2 |
| USB 4.0 | 2x USB4 | N/A | N/A |
||||||||||
| Other USB | 1x USB 3.2 | 1x USB3.1 | 3x USB2 | 1x USB2 (Secure BIOS) |
||||||||||||
| Power & Thermal | Nominal TDP | 28 W | 45 W |
||||||||||
| TDP Range | 15-54 W | 15-30 W | 25-45 W |
||||||||||
| Junction Temperature | 0 to 105°C | -40 to 105°C |
|||||||||||
| Package, Reliability | Package | 25 mm x 40 mm |
|||||||||||
| Longevity | 2.5 Years (Standard) | Up to 10 Years (Extended) | AEC-Q100 |
The most powerful processors in the series are the Ryzen AI Embedded P185 and P185i, which feature up to 12 Zen 5 CPU cores, 24 MB L3 cache, and GPU frequencies up to 2.9 GHz, while delivering up to 50 TOPS AI performance. One small difference in the specifications is memory support, where the commercial models use slightly faster LPDDR5X memory (up to 8533 MT/s) compared to the industrial variants, which are limited to 8000 MT/s.
On the software side, the company notes that the SoCs now support the AMD ROCm open software stack for running standard AI frameworks (such as PyTorch or TensorFlow) without vendor lock-in. AMD also introduced a virtualized reference stack based on the Xen hypervisor, which allows for the consolidation of mixed-criticality workloads (running a Real-Time OS alongside Windows/Linux) on a single chip. AMD also mentions these chips are optimized for Llama 3.2-Vision, YOLOv12, and MobileSAM.
Previously, we saw Congatec and Sapphire announce the conga-TCRP1, a COM Express 3.1 Type 6 Compact module, and the EDGE+ VPR-7P132 Mini-ITX motherboard, both built around AMD’s Ryzen AI Embedded P100 series. With the release of the new SoCs, more such embedded boards and modules are expected to follow.
The new 8- to 12-core SoCs (P164, P174, P185) are already sampling to early access customers, with production shipments expected in July 2026. The 4- to 6-core models (P121, P132) are expected to reach production earlier, in Q2 2026. More information is available in the press release and on the P100 Series product page.
Debashis Das is a technical content writer and embedded engineer with over five years of experience in the industry. With expertise in Embedded C, PCB Design, and SEO optimization, he effectively blends difficult technical topics with clear communication
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
