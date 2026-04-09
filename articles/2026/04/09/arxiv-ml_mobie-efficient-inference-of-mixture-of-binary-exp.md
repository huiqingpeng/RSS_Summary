---
title: "MoBiE: Efficient Inference of Mixture of Binary Experts under Post-Training Quantization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06798"
published: "2026-04-09"
fetched: "2026-04-10T07:05:07.702220"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:MoBiE: Efficient Inference of Mixture of Binary Experts under Post-Training Quantization
View PDF HTML (experimental)Abstract:Mixture-of-Experts (MoE) based large language models (LLMs) offer strong performance but suffer from high memory and computation costs. Weight binarization provides extreme efficiency, yet existing binary methods designed for dense LLMs struggle with MoE-specific issues, including cross-expert redundancy, task-agnostic importance estimation, and quantization-induced routing shifts. To this end, we propose MoBiE, the first binarization framework tailored for MoE-based LLMs. MoBiE is built on three core innovations: 1. using joint SVD decomposition to reduce cross-expert redundancy; 2. integrating global loss gradients into local Hessian metrics to enhance weight importance estimation; 3. introducing an error constraint guided by the input null space to mitigate routing distortion. Notably, MoBiE achieves these optimizations while incurring no additional storage overhead, striking a balance between efficiency and model performance. Extensive experiments demonstrate that MoBiE consistently outperforms state-of-the-art binary methods across multiple MoE-based LLMs and benchmarks. For example, on Qwen3-30B-A3B, MoBiE reduces perplexity by 52.2$\%$, improves average zero-shot performance by 43.4$\%$, achieves over 2 $\times$ inference speedup, and further shortens quantization time. The code is available at this https URL.
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
