---
title: "NVIDIA IGX Thor Powers Industrial, Medical, and Robotics Edge AI Applications"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/nvidia-igx-thor-powers-industrial-medical-and-robotics-edge-ai-applications/"
published: "2026-03-23"
fetched: "2026-03-24T07:12:53.142406"
---

Industrial and medical systems are rapidly increasing the use of high-performance AI to improve worker productivity, human-machine interaction, and downtime management. From factory automation cells to autonomous mobile platforms to surgical rooms, operators are deploying increasingly complex generative AI models, more sensors, and higher‑fidelity data streams at the edge.
Safety and regulatory compliance are meanwhile crucial to ensure deterministic behavior, high availability, and verifiable functional safety essential design requirements.
This post introduces NVIDIA IGX Thor, a platform built for the demands of powering industrial AI at the edge, including a deep dive into performance and safety features.
What is NVIDIA IGX Thor?
NVIDIA IGX Thor is an enterprise-ready platform for physical AI. It offers server‑class AI performance together with industrial-grade hardware, advanced functional safety capabilities, extended lifecycle support, and an enterprise software stack in configurations suitable for industrial and medical environments. IGX Thor extends this compute and safety foundation to edge systems where uptime, reliability, and standards compliance are central to system design.
With the IGX Thor platform, developers can build mission-critical edge computers that operate reliably in harsh physical conditions, integrate with secure and regulated infrastructures, and execute state‑of‑the‑art AI inference and sensor fusion pipelines close to where data is generated.
The IGX Thor family is delivered through four purpose-built platforms, designed for industrial-grade deployment and advanced development workflows:
- NVIDIA IGX T5000 System-on-Module (SoM): Delivers high-performance, safety-capable compute in a compact, embedded form factor. Designed for integration into custom carrier boards, the IGX T5000 SoM enables customers to build domain-specific industrial and robotic systems while accelerating time to production.
- NVIDIA IGX T7000 Board Kit: Scales performance and expandability for the most demanding edge AI workloads. Built on a MicroATX form factor, the IGX T7000 combines NVIDIA Thor-class compute with rich I/O, functional safety support, flexibility to increase the AI compute with a discrete GPU, and enterprise-grade networking to power safety-critical, high-throughput edge systems.
- NVIDIA IGX Thor Developer Kit: Provides a full-featured development platform for building, testing, and validating next-generation industrial AI applications. With support for advanced sensing, robotics, and real-time AI pipelines, it enables developers to move from prototype to deployment with confidence.
- NVIDIA IGX Thor Developer Kit Mini: Brings NVIDIA Thor-class capabilities with on-board safety module to a smaller footprint. Optimized for space- and power-constrained environments, it is ideal for mobile robots, autonomous machines, and compact industrial systems that require robust AI performance without compromising the form factor.
Table 1 provides an overview of the NVIDIA IGX Thor family, highlighting how each configuration is tuned for different classes of industrial, medical, and robotics edge workloads.
| NVIDIA IGX T5000 | NVIDIA IGX T7000 | NVIDIA IGX Thor Developer Kit Mini | NVIDIA IGX Thor Developer Kit | |
| AI performance | Up to 2,070 FP4 TFLOPS | Up to 5,581 FP4 TFLOPs | Up to 2,070 FP4 TFLOPS | Up to 5,581 FP4 TFLOPs |
| iGPU | 2,560-core NVIDIA Blackwell architecture GPU with fifth-generation Tensor Cores Multi-instance GPU with 10 TPCs | |||
| iGPU speed | 1.57 GHz | |||
| dGPU | – | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition NVIDIA RTX PRO 5000 Blackwell | NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | |
| Memory | 256-bit 128 GB LPDDR5x | 273 GB/s | |||
| Safety | Functional Safety Island (FSI) in SoC | FSI in SoC and Safety MCU | ||
| BMC | – | Yes | – | Yes |
| Networking | 4x up to 25 Gbps MGBE | 2x RJ45 (1 GbE each) 2x QSFP112 (200 GbE each) Supports ConnectX-7 | 1x 5GBe RJ45 connector 1x QSFP28 (4x 25 GbE) WiFi 6E (Populated on M.2 Key E slot with x1 PCIe Gen5 ) | 2x RJ45 (1 GbE each) 2x QSFP112 (200 GbE each) Supports ConnectX-7 |
Delivering massive AI performance at the edge
NVIDIA IGX Thor delivers a step-function increase in performance. Compared to NVIDIA IGX Orin, it offers up to 8x higher AI compute on the integrated GPU, 2.5x higher AI compute with discrete GPU acceleration, and 2x higher networking bandwidth. This enables significantly more demanding real-time AI workloads for industrial and robotics applications.
IGX T7000 pairs the IGX T5000 Thor module, powered by an NVIDIA Blackwell architecture iGPU delivering 2,070 FP4 TOPS of AI performance, with an NVIDIA RTX PRO 6000 Blackwell Max‑Q discrete GPU that adds an additional 3,511 FP4 TOPS. Together, this configuration significantly boosts total AI compute for demanding edge workloads.
IGX T7000 delivers 5x the generative AI reasoning performance compared to IGX Orin 700. It handles up to 20x more interactive users by using the iGPU and dGPU concurrently, making it an excellent choice for high‑concurrency edge workloads. It also offers robust mixed‑criticality isolation, so workloads running on the dGPU operate independently without degrading performance on the iGPU.
These features make IGX T7000 ideal for scenarios such as smart retail, which involves processing video from many checkout kiosks while running VLM and LLM workloads for smart checkout with low latency for faster checkout. It’s also ideal for industrial safety and building automation applications, among many others.
Figure 2 compares IGX T7000 and IGX Orin 700 on the number of users handled with tokens/sec > 25 and TTFT < 200 msec.
Configuration: dGPU: NVIDIA RTX PRO 6000 Blackwell Max-Q (IGX T7000), NVIDIA RTX 6000 ADA (IGX Orin 700); ISL/OSL: 2028/128; Quantization: NVFP4 (IGX T7000), W4A16 (IGX Orin 700); Framework: VLLM
| Model | NVIDIA IGX Thor (IGX T7000) (tokens/sec) | NVIDIA IGX Orin (IGX Orin 700) (tokens/sec) | Speedup over NVIDIA IGX Orin |
| Qwen3 30B A3B | 1,163 | 807 | 1.4x |
| Qwen3 32B | 468 | 95 | 4.9x |
| Nemotron 9B V2 | 306 | 202 | 1.5x |
| Nemotron 3 30B A3B | 642 | 585 | 1.1x |
| Cosmos Reason 2 2B | 1,630 | 1,250 | 1.3x |
| Cosmos Reason 2 8B | 822 | 540 | 1.5x |
| gpt-oss-20B | 1,072 | 711 | 1.5x |
Configuration: dGPU: NVIDIA RTX PRO 6000 Blackwell Max-Q (IGX T7000), NVIDIA RTX 6000 ADA (IGX Orin 700); ISL/OSL: 2028/128; Quantization: NVFP4 (IGX T7000), W4A16 (IGX Orin 700); Max Conc: 9; Framework: VLLM
Similar to NVIDIA Jetson T5000, the NVIDIA IGX T5000 SoM provides 2,070 TOPS of FP4 performance, paired with 128 GB of LPDDR5X memory and 273 GB/s of memory bandwidth, making it ideal for running generative AI workloads with real-time responsiveness. IGX T5000 delivers the same performance as Jetson T5000 even with industrial features such as full DRAM ECC enabled. These industrial capabilities do not reduce performance or usable memory capacity on IGX T5000.
High-speed connectivity for real-time workloads
The IGX T7000 boardkit significantly advances edge connectivity with dual 200 GbE networking, delivering 2x the bandwidth compared to the IGX Orin dual 100 GbE interfaces. Powered by the NVIDIA ConnectX-7 SmartNIC, this high-speed fabric enables low-latency, high-throughput data movement using RDMA, enabling sensor data to bypass the CPU and flow directly into GPU memory. The result is a substantial boost in end-to-end AI performance, especially for real-time, sensor-intensive workloads.
This leap in networking capability unlocks the full potential of the NVIDIA Holoscan Sensor Bridge (HSB). Designed to aggregate and stream massive volumes of data from high-bandwidth sensors—such as cameras, lidar, radar, and medical imaging devices—HSB relies on deterministic, lossless networking to meet strict latency and synchronization requirements.
With 2×200 GbE and RDMA acceleration, IGX Thor provides the bandwidth and determinism needed to scale multisensor pipelines, enabling faster ingestion, tighter sensor fusion, and higher-fidelity AI inference in safety-critical and real-time systems.
Real-time determinism for edge applications
Many industrial and robotics applications demand strict real-time behavior, and IGX Thor is designed specifically to meet those needs.
- Real-time Linux environment: IGX ships with a preemptible real-time Linux kernel by default. This provides the deterministic behavior needed for tight control loops and low-latency sensor handling in robotic arms, autonomous machines, and closed-loop medical systems.
- Multi-instance GPU (MIG): The NVIDIA Blackwell GPU can be partitioned into fully isolated instances, so safety‑critical, real-time workloads can get hard performance guarantees even when running alongside lower-priority tasks.
- Programmable accelerators: Dedicated engines for vision (PVA), optical flow, hardware codecs, and real-time inference cut latency and offload work from the CPU and GPU, leaving more headroom for large-scale deep learning and complex generative AI pipelines.
- GPU Direct RDMA: With GPU Direct RDMA, sensor inputs can be brought directly inside the GPU for extreme low latency sensor processing.
Built rugged for industrial reality
Industrial applications—from precision manufacturing to medical robotics—demand platforms that can operate reliably in the face of extremes: intense vibration, electrical noise, temperature swings, ECC, and more. They also need to easily integrate with industrial networks. The IGX Thor platform is engineered precisely for these demands.
- Industrial-grade components: Every aspect of IGX Thor, from memory to power delivery, is selected for resilience, supporting an extended temperature range, shock, vibration compliance, and ECC implementation.
- Ruggedized chassis: Available in tough industrial enclosures, IGX Thor can be deployed in factories, warehouses, field vehicles, or anywhere that traditional electronics would falter.
- Long lifecycle, global support: IGX platforms are supported for up to 10 years, providing unmatched reliability and supply chain assurance for regulated industries.
- Extensive I/O: IGX Thor offers rich industrial I/O—multiple PCIe Gen5, SFP+, CAN, and high-speed digital interfaces—simplifying integration with legacy PLCs, sensors, robotics, control networks, and more.
Functional safety and proactive AI safety
IGX Thor unifies high‑performance AI and functional safety in a single platform, enabling both inside‑out and outside‑in robotic safety. Robots can rely on onboard sensors or on infrastructure sensors with an outside-in view for safety decisions.
IGX Thor complies with ISO 26262 and IEC 61508, targets ASIL D/SC3 and ASIL/SIL 2. It incorporates a variety of safety features, including:
- Hardware fault detection
- Safe‑state monitoring
- In‑system test
- DRAM ECC
- Freedom from interference (FFI)
- Dedicated Functional Safety Island (FSI), an independent, redundant safety processor that monitors and handles safety‑critical workloads, providing true hardware separation between safety and nonsafety domains
NVIDIA Halos AI Systems Inspection Lab (accredited by ANAB) helps to ensure that NVIDIA IGX customers meet rigorous safety and cybersecurity standards through impartial assessments. IGX customers receive an inspection report and an inspection certificate to be consumed with technical services or certification agencies for final certification. For more details, see the IGX Thor Safety Product Brief.
Enterprise-grade industrial platform
NVIDIA AI Enterprise – IGX is a software solution for edge AI that makes IGX Thor an enterprise‑grade, production‑ready platform with predictable long‑term support. NVIDIA commits to a lifecycle of up to 10 years for IGX, covering hardware availability, security updates, and full stack maintenance. This means that industrial, medical, and robotics deployments can stay patched and supported over their entire service life.
In addition, NVIDIA AI Enterprise provides a long‑term support (LTS) branch with version‑locked AI frameworks and SDKs maintained for 10 years—alongside enterprise SLAs like Business Standard and Business Critical support. This ensures stable APIs, regular security fixes, and access to NVIDIA experts 24 hours per day, seven days per week when needed. To learn more, see the NVIDIA AI Enterprise – IGX Licensing Guide.
Transition seamlessly from NVIDIA Jetson Thor
The transition from NVIDIA Jetson Thor to NVIDIA IGX Thor is seamless. Jetson T5000 and IGX T5000 are fully compatible in terms of pin, form factor, and function, so the same carrier board design works for both platforms. The software stacks are also aligned—kernel, user space, and AI libraries share the same versions—delivering a consistent experience across Jetson and IGX.
For teams with deeper customization requirements, NVIDIA is introducing JetPack on IGX, bringing JetPack flexibility to the industrial robustness of IGX hardware. For more information, see the NVIDIA IGX User Guide.
Get started with NVIDIA IGX Thor
Automation leaders, medical imaging pioneers, and large-scale manufacturers are already adopting NVIDIA IGX Thor. Leading ODM and Sensor partners can deliver production-ready systems and services to drive faster TTM.
Industrial automation, healthcare, energy, and smart infrastructure are being transformed by AI—accelerating productivity, increasing safety, and lowering costs. But deploying AI in these environments demands more: hardware must survive and thrive in harshness, data must be protected, and systems must meet the world’s toughest functional safety requirements.
NVIDIA IGX Thor delivers at every turn. It bridges the gap between the agility of modern AI and the uncompromising demands of regulated, safety-critical industrial environments. With functional safety engineered from silicon up, support for the best-performing GPUs, and a software stack ready for compliance, management, and AI advancement, IGX Thor is the platform to trust for the next decade of industrial AI.
IGX Thor Developer Kit and IGX Thor Developer Kit mini are available to purchase from distributors worldwide.
Get started with NVIDIA IGX Thor.
To learn more, watch the NVIDIA GTC 2026 keynote with NVIDIA founder and CEO Jensen Huang and explore related GTC sessions on demand.
