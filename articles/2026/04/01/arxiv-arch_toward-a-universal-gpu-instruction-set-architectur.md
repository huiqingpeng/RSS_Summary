---
title: "Toward a Universal GPU Instruction Set Architecture: A Cross-Vendor Analysis of Hardware-Invariant Computational Primitives in Parallel Processors"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.28793"
published: "2026-04-01"
fetched: "2026-04-02T07:11:25.850021"
---

Computer Science > Distributed, Parallel, and Cluster Computing
[Submitted on 22 Mar 2026]
Title:Toward a Universal GPU Instruction Set Architecture: A Cross-Vendor Analysis of Hardware-Invariant Computational Primitives in Parallel Processors
View PDF HTML (experimental)Abstract:We present the first systematic cross-vendor analysis of GPU instruction set architectures spanning all four major GPU vendors: NVIDIA (PTX ISA v1.0 through v9.2, Fermi through Blackwell), AMD (RDNA 1 to 4 and CDNA 1 to 4), Intel (Gen11, Xe-LP, Xe-HPG, Xe-HPC), and Apple (G13, reverse-engineered). Drawing on official ISA reference manuals, architecture whitepapers, patent filings, and community reverse-engineering efforts totaling over 5,000 pages of primary sources across 16 distinct microarchitectures, we identify ten hardware-invariant computational primitives that appear across all four architectures, six parameterizable dialects where vendors implement identical concepts with different parameters, and six true architectural divergences representing fundamental design disagreements. Based on this analysis, we propose an abstract execution model for a vendor-neutral GPU ISA grounded in the physical constraints of parallel computation. We validate our model with benchmark results on NVIDIA T4 and Apple M1 hardware, the two most architecturally distant platforms in our study. On five of six benchmark-platform pairs, the abstract model matches or exceeds native vendor-optimized performance. The single outlier (parallel reduction on NVIDIA, 62.5% of native) reveals that intra-wave shuffle must be a mandatory primitive, a finding that refines our proposed model.
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
