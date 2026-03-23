---
title: "CIX ClawCore Armv9.2 CPU family targets OpenClaw deployments"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/23/cix-clawcore-armv9-2-cpu-family-targets-openclaw-deployments/"
published: "2026-03-23"
fetched: "2026-03-24T07:00:34.548235"
---

OpenClaw was just introduced a few months ago, but we’ve already seen several low-footprint implementations, and some companies even ship mini PCs preloaded with OpenClaw. But today, I was just informed that CIX had gone further, and introduced the ClawCore Armv9.2 CPU family specifically designed/optimized for OpenClaw.
The family will be comprised of three main SKUs:
- ClawCore-P (勁螯芯 “Powerful Claw”) – High-performance model with 12-core CPU @ 3.2GHz, Immortalis-G720 GPU, 45 TOPS AI compute, and support for up to 64GB LPDDR5 RAM. Aimed at high-parallelism, large-capacity scenarios. Shipping starts now in March 2026.
- ClawCore-A (智螯芯 “AI/Smart Claw”) – Octa-core CPU @ 3.0GHz, 80 TOPS AI compute (expandable to 200 TOPS via PCIe AI card), up to 64GB LPDDR5. It’s designed for 24/7 use, supports full-chain ECC, hardware security (encryption/key management), and enables up to 50% reduction in model token costs via local inference. In practise, 80 to 90% of requests would happen on the device thanks to this hybrid local/online implementation. It supports running large models (e.g., 27B or up to 120B in collaboration). The launch is planned for June 2026.
- ClawCore-E (靈螯芯 “Efficient Claw”) – Ultra-low-power variant combining Armv9.2 CPU + NPU, with voice/network wake-up for on-demand use. Targeted at edge/IoT devices, and expected by December 2026.
The ClawCore-P specifications match closely the ones for the CIX P1 with 12 Armv9.2 cores, an Immortalis-G720 GPU, and 45 TOPS of AI compute (combined), as well as up to 64GB LPDDR5. They may still have tweaked it since the max CPU frequency for the ClawCore-P is 3.2 GHz, instead of the 2.8 GHz (advertised)/ 2.6 GHz (real) for the P1. ClawCore-P mini PCs and workstations are expected very soon. The ClawCore-A is expected in just three months, so it might be a P1 with fewer cores and a beefier NPU.
Besides the chips themselves, CIX will provide software support with five key “pillars”:
- Open AI Agent Hub where developers can share models and skills
- Out-of-the-box integrated delivery — The chips natively integrate the OpenClaw framework and optimized models
- Smart collaboration mode — Connecting Agents across different systems to form collective intelligence
- Security mechanisms — Hardware encryption to secure the AI agents
- System optimization to lower power consumption on machines designed to operate 24/7.
We’ll see how the latter works, considering CIX P1’s high idle power consumption, but maybe “low-power” takes a different meaning when dealing with AI. CIX will provide developers with an SDK to lower the entry barrier. The CPUs will target Arm SystemReady platform and support Windows, Android, Ubuntu, Tongxin/UnionTech, and Kylin operating systems.
We got the information and images above from an Anue article in Chinese, where they also mention partnerships with a range of companies, including Alibaba Cloud, Iluvatar CoreX, and Houmo.AI. On the hardware side, we should expect laptops, boards, AI NAS, and other systems from Sixunited, Xunlong Software (Orange Pi), Radxa, and Meigao.
Thanks to redefineme for the tip.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
