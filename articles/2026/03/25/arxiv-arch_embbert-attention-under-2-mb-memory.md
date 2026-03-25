---
title: "EmbBERT: Attention Under 2 MB Memory"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2502.10001"
published: "2026-03-25"
fetched: "2026-03-26T07:07:48.798801"
---

Computer Science > Computation and Language
[Submitted on 14 Feb 2025 (v1), last revised 24 Mar 2026 (this version, v3)]
Title:EmbBERT: Attention Under 2 MB Memory
View PDF HTML (experimental)Abstract:Transformer architectures based on the attention mechanism have revolutionized natural language processing (NLP), driving major breakthroughs across virtually every NLP task. However, their substantial memory and computational requirements still hinder deployment on ultra-constrained devices such as wearables and Internet-of-Things (IoT) units, where available memory is limited to just a few megabytes. To address this challenge, we introduce EmbBERT, a tiny language model (TLM) architecturally designed for extreme efficiency. The model integrates a compact embedding layer, streamlined feed-forward blocks, and an efficient attention mechanism that together enable optimal performance under strict memory budgets. Through this redesign for the extreme edge, we demonstrate that highly simplified transformer architectures remain remarkably effective under tight resource constraints. EmbBERT requires only 2 MB of total memory, and achieves accuracy performance comparable to the ones of state-of-the-art (SotA) models that require a $\mathbf{10\times}$ memory budget. Extensive experiments on the curated TinyNLP benchmark and the GLUE suite confirm that EmbBERT achieves competitive accuracy, comparable to that of larger SotA models, and consistently outperforms downsized versions of BERT and MAMBA of similar size. Furthermore, we demonstrate the model resilience to 8-bit quantization, which further reduces memory usage to just 781 kB , and the scalability of the EmbBERT architecture across the sub-megabyte to tens-of-megabytes range. Finally, we perform an ablation study demonstrating the positive contributions of all components and the pre-training procedure. All code, scripts, and checkpoints are publicly released to ensure reproducibility: this https URL.
Submission history
From: Fabrizio Pittorino [view email][v1] Fri, 14 Feb 2025 08:33:31 UTC (589 KB)
[v2] Wed, 11 Feb 2026 10:26:29 UTC (254 KB)
[v3] Tue, 24 Mar 2026 15:21:45 UTC (251 KB)
Current browse context:
cs.CL
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
