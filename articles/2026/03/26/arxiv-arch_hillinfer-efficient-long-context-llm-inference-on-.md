---
title: "HillInfer: Efficient Long-Context LLM Inference on the Edge with Hierarchical KV Eviction using SmartSSD"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2602.18750"
published: "2026-03-26"
fetched: "2026-03-27T07:13:24.030483"
---

Computer Science > Hardware Architecture
[Submitted on 21 Feb 2026 (v1), last revised 25 Mar 2026 (this version, v2)]
Title:HillInfer: Efficient Long-Context LLM Inference on the Edge with Hierarchical KV Eviction using SmartSSD
View PDF HTML (experimental)Abstract:Deploying Large Language Models (LLMs) on memory-constrained AI Personal Computers (AIPCs) enables low-latency, privacy-preserving inference, but long-context generation is fundamentally bottlenecked by the linearly growing Key-Value (KV) cache. While dynamic KV eviction mitigates this memory wall, existing offloading strategies either trigger crippling PCIe I/O bottlenecks on standard SSDs or suffer from FPGA resource exhaustion by forcing compute-intensive exact attention on a single, weak Computational Storage Drive (CSD). In this paper, we propose HillInfer, a CSD-assisted KV eviction framework that introduces a paradigm shift: offloading strictly lightweight token importance evaluation to a single CSD (e.g., SmartSSD) on AIPCs. To fully capitalize on this lightweight offloading strategy, HillInfer orchestrates a Hierarchical KV Cache Manager (HKM) that leverages temporal locality and dynamic token hit rates to physically partition cache pools, thereby eliminating cross-device I/O thrashing. Additionally, we design an Adaptive Prefetch-based Pipeline (APP) that adaptively balances the evaluation workload between the host CPU and the SmartSSD, effectively masking the heterogeneous straggler effect. Finally, we introduce a CSD-based Evaluation Configuration (CEC) to enable resource-efficient near-data processing on the FPGA. Extensive experiments on a commodity AIPC demonstrate that HillInfer achieves up to an 8.56$\times$ speedup over state-of-the-art baselines, delivering low-latency, I/O-efficient long-context inference without sacrificing model accuracy.
Submission history
From: He Sun [view email][v1] Sat, 21 Feb 2026 08:19:59 UTC (1,047 KB)
[v2] Wed, 25 Mar 2026 06:46:30 UTC (1,230 KB)
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
