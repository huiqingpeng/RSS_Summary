---
title: "VL-RouterBench: A Benchmark for Vision-Language Model Routing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.23562"
published: "2026-03-19"
fetched: "2026-03-19T14:10:41.249441"
---

Computer Science > Machine Learning
[Submitted on 29 Dec 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:VL-RouterBench: A Benchmark for Vision-Language Model Routing
View PDF HTML (experimental)Abstract:Multi-model routing has evolved from an engineering technique into essential infrastructure, yet existing work lacks a systematic, reproducible benchmark for evaluating vision-language models (VLMs). We present VL-RouterBench to assess the overall capability of VLM routing systems systematically. The benchmark is grounded in raw inference and scoring logs from VLMs and constructs quality and cost matrices over sample-model pairs. In scale, VL-RouterBench covers 14 datasets across 3 task groups, totaling 30,540 samples, and includes 15 open-source models and 2 API models, yielding 519,180 sample-model pairs and a total input-output token volume of 34,494,977. The evaluation protocol jointly measures average accuracy, average cost, and throughput, and builds a ranking score from the harmonic mean of normalized cost and accuracy to enable comparison across router configurations and cost budgets. On this benchmark, we evaluate 10 routing methods and baselines and observe a significant routability gain, while the best current routers still show a clear gap to the ideal Oracle, indicating considerable room for improvement in router architecture through finer visual cues and modeling of textual structure. We will open-source the complete data construction and evaluation toolchain to promote comparability, reproducibility, and practical deployment in multimodal routing research.
Submission history
From: Zhehao Huang [view email][v1] Mon, 29 Dec 2025 16:01:19 UTC (3,556 KB)
[v2] Wed, 18 Mar 2026 02:42:13 UTC (3,019 KB)
Current browse context:
cs.LG
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
