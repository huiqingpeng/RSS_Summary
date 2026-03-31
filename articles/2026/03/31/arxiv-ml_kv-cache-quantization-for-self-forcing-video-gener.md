---
title: "KV Cache Quantization for Self-Forcing Video Generation: A 33-Method Empirical Study"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27469"
published: "2026-03-31"
fetched: "2026-04-01T07:24:39.090121"
---

Computer Science > Machine Learning
[Submitted on 29 Mar 2026]
Title:KV Cache Quantization for Self-Forcing Video Generation: A 33-Method Empirical Study
View PDF HTML (experimental)Abstract:Self-forcing video generation extends a short-horizon video model to longer rollouts by repeatedly feeding generated content back in as context. This scaling path immediately exposes a systems bottleneck: the key-value (KV) cache grows with rollout length, so longer videos require not only better generation quality but also substantially better memory behavior. We present a comprehensive empirical study of KV-cache compression for self-forcing video generation on a Wan2.1-based Self-Forcing stack. Our study covers 33 quantization and cache-policy variants, 610 prompt-level observations, and 63 benchmark-level summaries across two evaluation settings: MovieGen for single-shot 10-second generation and StoryEval for longer narrative-style stability. We jointly evaluate peak VRAM, runtime, realized compression ratio, VBench imaging quality, BF16-referenced fidelity (SSIM, LPIPS, PSNR), and terminal drift. Three findings are robust. First, the strongest practical operating region is a FlowCache-inspired soft-prune INT4 adaptation, which reaches 5.42-5.49x compression while reducing peak VRAM from 19.28 GB to about 11.7 GB with only modest runtime overhead. Second, the highest-fidelity compressed methods, especially PRQ_INT4 and QUAROT_KV_INT4, are not the best deployment choices because they preserve quality at severe runtime or memory cost. Third, nominal compression alone is not sufficient: several methods shrink KV storage but still exceed BF16 peak VRAM because the current integration reconstructs or retains large BF16 buffers during attention and refresh stages. The result is a benchmark harness, analysis workflow, and empirical map of which KV-cache ideas are practical today and which are promising research directions for better memory integration. Code, data products, and the presentation dashboard are available at this https URL.
Submission history
From: Suraj Ranganath [view email][v1] Sun, 29 Mar 2026 01:35:16 UTC (10,693 KB)
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
