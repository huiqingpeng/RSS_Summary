---
title: "ODMA: On-Demand Memory Allocation Strategy for LLM Serving on LPDDR-Class Accelerators"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2512.09427"
published: "2026-03-26"
fetched: "2026-03-27T07:13:15.966746"
---

Computer Science > Hardware Architecture
[Submitted on 10 Dec 2025 (v1), last revised 25 Mar 2026 (this version, v3)]
Title:ODMA: On-Demand Memory Allocation Strategy for LLM Serving on LPDDR-Class Accelerators
View PDF HTML (experimental)Abstract:Existing memory management techniques severely hinder efficient Large Language Model serving on accelerators constrained by poor random-access this http URL static pre-allocation preserves memory contiguity,it incurs significant overhead due to worst-case this http URL,fine-grained paging mitigates this overhead but relies on HBM's high random-access tolerance, making it unsuitable for LPDDR systems where non-sequential access rapidly degrades bandwidth. Furthermore, prior works typically assume static distributions and HBM characteristics, thereby failing to resolve the critical fragmentation and bandwidth constraints inherent to LPDDR hardware. We present ODMA, an on-demand memory allocation strategy tailored for random-access-constrained accelerators, such as the Cambricon MLU this http URL advances generation-length prediction by addressing two critical limitations in production workloads: (i) distribution drift that invalidates static bucket boundaries, and (ii) performance fragility under heavy-tailed request patterns. ODMA integrates a lightweight length predictor with adaptive bucket partitioning and a fallback safety pool. Bucket boundaries are dynamically recalibrated via online histograms to maximize utilization, while the safety pool ensures robustness against prediction errors. On Alpaca and Google-NQ benchmarks, ODMA improves S3's prediction accuracy from 98.60% to 99.55% and 82.68% to 93.36%, respectively. Deployment with DeepSeek-R1-Distill-Qwen-7B on Cambricon MLU370-X4 accelerators demonstrates that ODMA increases KV-cache utilization by up to 19.25% (absolute) and throughput (TPS) by 23-27% over static baselines, validating the efficacy of predictor-driven contiguous allocation for LPDDR-class devices.
Submission history
From: Guoqiang Zou [view email][v1] Wed, 10 Dec 2025 08:52:20 UTC (833 KB)
[v2] Mon, 29 Dec 2025 07:47:50 UTC (770 KB)
[v3] Wed, 25 Mar 2026 08:56:03 UTC (719 KB)
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
