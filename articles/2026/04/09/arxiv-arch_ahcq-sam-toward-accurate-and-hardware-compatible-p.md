---
title: "AHCQ-SAM: Toward Accurate and Hardware-Compatible Post-Training Segment Anything Model Quantization"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2503.03088"
published: "2026-04-09"
fetched: "2026-04-10T07:04:53.119915"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 5 Mar 2025 (v1), last revised 8 Apr 2026 (this version, v4)]
Title:AHCQ-SAM: Toward Accurate and Hardware-Compatible Post-Training Segment Anything Model Quantization
View PDF HTML (experimental)Abstract:The Segment Anything Model (SAM) has revolutionized image and video segmentation with its powerful zero-shot capabilities. However, its massive parameter scale and high computational demands hinder efficient deployment on resource-constrained edge devices. While Post-Training Quantization (PTQ) offers a practical solution, existing methods still fail to handle four critical quantization challenges: (1) ill-conditioned weights; (2) skewed and long-tailed post-GELU activations; (3) pronounced inter-channel variance in linear projections; and (4) exponentially scaled and heterogeneous attention scores. To mitigate these bottlenecks, we propose AHCQ-SAM, an accurate and hardware-compatible PTQ framework featuring four synergistic components: (1) Activation-aware Condition Number Reduction (ACNR), which regularizes weight matrices via a proximal point algorithm to suppress ill-conditioning; (2) Hybrid Log-Uniform Quantization (HLUQ), which combines power-of-two and uniform quantizers to capture skewed post-GELU activations; (3) Channel-Aware Grouping (CAG), which clusters channels with homogeneous statistics to achieve high accuracy with minimal hardware overhead; and (4) Logarithmic Nonlinear Quantization (LNQ), which utilizes logarithmic transformations to adaptively adjust quantization resolution for exponential and heterogeneous attention scores. Experimental results demonstrate that AHCQ-SAM outperforms current methods on SAM. Compared with the SOTA method, it achieves a 15.2% improvement in mAP for 4-bit SAM-B with Faster R-CNN on the COCO dataset. Furthermore, we establish a PTQ benchmark for SAM2, where AHCQ-SAM yields a 14.01% improvement in J&F for 4-bit SAM2-Tiny on the SA-V Test dataset. Finally, FPGA-based implementation validates the practical utility of AHCQ-SAM, delivering a 7.12x speedup and a 6.62x power efficiency improvement over the floating-point baseline.
Submission history
From: Wenlun Zhang [view email][v1] Wed, 5 Mar 2025 01:04:45 UTC (2,968 KB)
[v2] Wed, 9 Jul 2025 08:26:21 UTC (4,034 KB)
[v3] Sat, 12 Jul 2025 01:30:20 UTC (4,034 KB)
[v4] Wed, 8 Apr 2026 13:11:29 UTC (5,272 KB)
Current browse context:
cs.CV
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
