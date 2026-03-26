---
title: "GeneTEK: Low-power, high-performance and scalable FPGA architecture for exact unit-cost edit distance"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2509.01020"
published: "2026-03-26"
fetched: "2026-03-27T07:13:11.075513"
---

Computer Science > Hardware Architecture
[Submitted on 31 Aug 2025 (v1), last revised 25 Mar 2026 (this version, v2)]
Title:GeneTEK: Low-power, high-performance and scalable FPGA architecture for exact unit-cost edit distance
View PDF HTML (experimental)Abstract:The advent of next-generation sequencing (NGS) has revolutionized genomic research by enabling cost-effective, high-throughput sequencing of a diverse range of organisms. This breakthrough has unleashed a "Cambrian explosion" in genomic data volume and diversity. This volume of workloads places genomics among the top four big data challenges anticipated for this decade. In this context, pairwise sequence alignment represents a very time- and energy-intensive step in common bioinformatics pipelines. Speeding up this step requires the implementation of heuristic approaches, optimized algorithms, and/or hardware acceleration. Although state-of-the-art CPU and GPU implementations have demonstrated significant performance gains, recent FPGA implementations have shown improved energy efficiency. However, the latter often suffer from limited read-length scalability due to constraints on hardware resources when aligning longer sequences. In this work, we present a flexible FPGA-based accelerator template scalable up to 1000 bp that implements Myers's algorithm to compute exact unit-cost edit-distance using high-level synthesis and a worker-based architecture. GeneTEK, a set of instances of this accelerator template in a Xilinx Zynq UltraScale+ FPGA, achieves up to 113% increase in execution speed and up to 111x reduction in energy consumption compared to leading CPU and GPU solutions, while fitting comparison matrices up to 13x larger than previous FPGA-based systolic-array solutions. By following a SW-HW co-design approach, GeneTEK exploits parallelization at multiple levels and efficient memory use to deliver a scalable and accurate FPGA-based accelerator. These results reaffirm the potential of FPGAs as an energy-efficient platform for pairwise alignment of read-lengths up to 1000 bp.
Submission history
From: Ruben Rodriguez Alvarez [view email][v1] Sun, 31 Aug 2025 23:11:48 UTC (734 KB)
[v2] Wed, 25 Mar 2026 14:19:01 UTC (930 KB)
References & Citations
export BibTeX citation
Loading...
Bibliographic and Citation Tools
Bibliographic Explorer (What is the Explorer?)
Connected Papers (What is Connected Papers?)
Litmaps (What is Litmaps?)
scite Smart Citations (What are Smart Citations?)
Code, Data and Media Associated with this Article
alphaXiv (What is alphaXiv?)
CatalyzeX Code Finder for Papers (What is CatalyzeX?)
DagsHub (What is DagsHub?)
Gotit.pub (What is GotitPub?)
Hugging Face (What is Huggingface?)
Papers with Code (What is Papers with Code?)
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
