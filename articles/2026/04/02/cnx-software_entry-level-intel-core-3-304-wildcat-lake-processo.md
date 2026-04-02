---
title: "Entry-level Intel Core 3 304 Wildcat Lake processor details and benchmarks surface"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/04/02/entry-level-intel-core-3-304-wildcat-lake-processor-details-and-benchmarks-surface/"
published: "2026-04-02"
fetched: "2026-04-03T07:13:34.233702"
---

Intel discreetly introduced the Wildcat Lake Core Series 3 CPUs at CES 2026 with some high-level specifications, but no part numbers or exact CPU, GPU, and NPU frequencies. Some leaks reveal more details about the Wildcat Lake parts, notably the Intel Core 3 304 penta-core processor, for which we also have some benchmarks.
Intel Wildcat Lake SKUs
The data below comes from a post by Jaykihn on X.
| Intel Core 3 304 | Intel Core 5 315 | Intel Core 5 320 | Intel Core 5 330 | Intel Core 7 350 | Intel Core 7 360 | |
|---|---|---|---|---|---|---|
| TDP (Base / Turbo) | 15 / 35 W |
|||||
| Core Count | 1P + 4LPE | 2P + 4LPE |
||||
| Base Freq. (P/E) | 1.5/1.4 GHz |
|||||
| Turbo Freq. (1P/2P/LPE) | 4.3/N/A/3.3 GHz | 4.4/4.3/3.3 GHz | 4.6/4.5/3.4 GHz | 4.8/4.7/3.6 GHz |
||
| Graphics | 1x Xe3 @ 2.3 GHz, 9 TOPS | 2x Xe3 @ 2.3 GHz, 18 TOPS | 2x Xe3 @ 2.5 GHz, 20 TOPS | 2x Xe3 @ 2.6 GHz, 21 TOPS |
||
| NPU | 15 TOPS | 16 TOPS | 17 TOPS |
|||
| L3 Cache | 6MB |
|||||
| SIPP | No | Yes | No | Yes |
While we have six SKUs in the table above, the Intel Core 5 320/330 and Core 7 350/360 only differ in terms of SIPP (Intel Stable IT Platform Program) support. SIPP is an enterprise initiative that ensures that key platform components, such as processors, chipsets, graphics, storage, networking, and wireless, remain consistent with minimal or no changes for a guaranteed period.
The GPU turbo clocks are much higher than in Alder Lake-N/Twin Lake chips (typically 1 GHz to 1.35 GHz), and LPDDR5x is clocked up to 7467 MT/s in Wildcat Lake processors, so we should expect much better graphics and AI performance, notwithstanding the extra 15-17 TOPS NPU.
Intel Core 3 304 GeekBench 6.5 benchmark
Besides the SKUs above, VideoCardz also noted GeekBench 6.5 benchmark results for an Intel Core 3 304-based “Wildcat Lake Client Platform” running Windows 11 Pro.
This confirms the penta-core (1P+4LPE) CPU at 1.5 GHz from the leak above. It’s significantly faster than Intel Alder Lake-N platforms (N95, N97, N100, Core i3-N305..). See the penta-core Core 3 304 Wildcat Lake CPU pitted against an octa-core Core i3-N305 Alder Lake-N CPU in the screenshot below.
Single-core performance is almost twice as fast, and multi-core performance is 20% faster despite having three fewer cores. Intel didn’t run GeekBench GPU on the Wildcat Lake platform, but we should expect 2 to 3 times greater 3D graphics performance.
Intel Core 3 304 specifications
If we gather all the details we know so far, the specifications of the Intel Core 3 304 should look like:
- CPU – Penta-core processor with 1x Cougar Cover P-core @ 1.5 GHz / 4.3 GHz (Turbo), 4x Darkmont LPE-cores @ 1.4 GHz / 3.3 GHz (Turbo)
- GPU – 1x Xe-core Intel Xe3 graphics @ 2.3 GHz Turbo (9 TOPS)
- AI accelerator – Intel NPU 5 @ 3.8 GHz Turbo (15 TOPS)
- Cache – 64KB L1 I-Cache per core, 32KB L1 D-Cache per core, 4MB L2 cache, 6MB L3 cache
- System Memory
- Up to 7467 MT/s LPDDR5x
- Up to 6400 MT/s DDR5
- USB/Thunderbolt
- Up to 2x Thunderbolt 4
- 2x USB 3.2
- 8x USB 2.0
- PCIe – 6 lanes PCIe Gen4
- TDP/PBP – 15W (MTP: 35W)
- Manufacturing Process – Intel 18A
I’m less sure about the maximum number of USB interfaces and PCIe lanes, since those may be for the higher-end SKUs.
Historically, mini PCs based on entry-level Intel processors launch for about $200 with memory and storage, before some drift lower to $150 depending on the exact specifications. Sadly, I don’t think it will be the case this year with Wildcat Lake mini PCs due to the RAM situation, and “affordable/cheap” in 2026 might translate into a complete system going for around $400.
Thanks to Anonymous for the tip.
Jean-Luc started CNX Software in 2010 as a part-time endeavor, before quitting his job as a software engineering manager, and starting to write daily news, and reviews full time later in 2011.
Support CNX Software! Donate via cryptocurrencies, become a Patron on Patreon, or purchase goods on Amazon or Aliexpress. We also use affiliate links in articles to earn commissions if you make a purchase after clicking on those links.
