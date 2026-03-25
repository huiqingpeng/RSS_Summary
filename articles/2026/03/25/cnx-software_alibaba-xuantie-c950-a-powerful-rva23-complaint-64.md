---
title: "Alibaba XuanTie C950 – A powerful, RVA23-complaint 64-bit RISC-V core for Edge AI computing"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/25/alibaba-xuantie-c950-a-powerful-rva23-complaint-64-bit-risc-v-core-for-edge-ai-computing/"
published: "2026-03-25"
fetched: "2026-03-26T07:00:17.822549"
---

Alibaba has introduced the XuanTie C950 high-performance, 64-bit multi-core CPU IP with an out-of-order superscalar microarchitecture, RVA23 profile compliant, and support for “all optional extensions” such as Vector Crypto, Zacas, and Zama16.
The company also says the XuanTie C950 supports the proprietary XuanTie AME (Attached Matrix Extension) ISA and supports integration with the company’s XuanTie TPE (Tensor Processing Engine) IP. The new 64-bit RISC-V core will be found in SoCs with up to eight cores per cluster, targeting high-performance applications, such as cloud computing, edge computing, and AI computing.
XuanTie C950 specifications:
- Architecture – RVA23 Profile
- Up to 8x cores clocked at 3.2 GHz; 22+/GHz Specint2006 base, or a score of around 70 at 3.2 GHz
- Pipeline – Superscalar out-of-order microarchitecture with 8-wide decode
- Floating Point – RISC-V F/D Extension
- Vector – RISC-V Vector Extension v1.0 with Vector Crypto support
- Matrix – XuanTie TPE coprocessor integration (AME v0.5)
- Hypervisor – Suitable for Type #1 and Type #2 hypervisor
- Cache system
- Private L1 and L2 Cache; L2 cache options: 256KB, 512KB, 1024KB, 2048KB, 3072KB
- Optional L3 shared cache: 1MB, 2MB, 3MB, 4MB, or 8MB
- MMU – Sv57/Sv48/Sv39 with PA48
- Bus Architecture
- Direct Connect Mode: CHI.E/CHI.F
- Multi-Processor Mode: AXI4.0/ACE4.0
- Security – CFI (Landing Pad, Shadow Stack)/Smmtt
- QoS
- CBQRI (Capacity and Bandwidth Controller QoS Register Interface)
- Ssqosid (Quality-of-Service Identifiers)
- Interrupt – AIA (Advanced Interrupt Architecture) v1.0
- Debug – RISC-V Debug Specification v1.0.
- Trace – RISC-V Nexus Trace v1.0
- RAS – RERI (RAS Error Record Interface)
- Manufacturing – 5nm process
On the software front, Alibaba says the compiler, assembler, linker, debugger, and binary tools are contributed to GNU/LLVM and supported officially, and so is QEMU support. The company also provides “optimized runtime library for enhanced performance”, an “Integrated Development Environment (CDS)”, and multi-OS support without going into details.
Performance-wise, the C950’s score of 70 at 3.2 GHz is said to be a new record for a RISC-V core, and three times faster than the company’s C920 core. Alibaba also introduced the C925 LITTLE core, which delivers 12+/GHz in Specint2006 base. It is is 34% smaller than the earlier C930 core, but offers 11% power efficiency improvements, and also supports RVA23.1.
Since the XuanTie C950 can be interfaced with the XuanTie TPE (Tensor Processing Engine) AI co-processor, it is suitable for generative AI, large language model inference, and computer vision. The company notably highlights support for Qwen3-256B-A22B and DeepSeek V3-671B.
More details can be found on the product page, which contains a datasheet (see mirror, courtesy of The Register), and a social media post on QQ.
Via tphuang on X and The Register
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
