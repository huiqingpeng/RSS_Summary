---
title: "LUMINA: LLM-Guided GPU Architecture Exploration via Bottleneck Analysis"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.05904"
published: "2026-03-19"
fetched: "2026-03-19T12:04:13.602178"
---

Computer Science > Hardware Architecture
[Submitted on 6 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:LUMINA: LLM-Guided GPU Architecture Exploration via Bottleneck Analysis
View PDF HTML (experimental)Abstract:GPU design space exploration (DSE) for modern AI workloads, such as Large-Language Model (LLM) inference, is challenging because of GPUs' vast, multi-modal design spaces, high simulation costs, and complex design optimization objectives (e.g. performance, power and area trade-offs). Existing automated DSE methods are often prohibitively expensive, either requiring an excessive number of exploration samples or depending on intricate, manually crafted analyses of interdependent critical paths guided by human heuristics.
We present LUMINA, an LLM-driven GPU architecture exploration framework that leverage AI to enhance the DSE efficiency and efficacy for GPUs. LUMINA extracts architectural knowledge from simulator code and performs sensitivity studies to automatically compose DSE rules,which are auto-corrected during exploration. A core component of LUMINA is a DSE Benchmark that comprehensively evaluates and enhances LLMs' capabilities across three fundamental skills required for architecture optimization, which provides a principled and reproducible basis for model selection and ensuring consistent architectural reasoning.
In the design space with 4.7 million possible samples, LUMINA identifies 6 designs of better performance and area than an A100 GPU efficiently, using only 20 steps via LLM-assisted bottleneck analysis. In comparison, LUMINA achieves 17.5x higher than design space exploration efficiency, and 32.9% better designs (i.e. Pareto Hypervolume) than Machine-Learning baselines, showcasing its ability to deliver high-quality design guidance with minimal search cost.
Submission history
From: Tao Zhang [view email][v1] Fri, 6 Mar 2026 04:47:18 UTC (5,015 KB)
[v2] Wed, 18 Mar 2026 01:29:51 UTC (5,015 KB)
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
