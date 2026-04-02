---
title: "Spectral Compact Training: Pre-Training Large Language Models via Permanent Truncated SVD and Stiefel QR Retraction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00733"
published: "2026-04-02"
fetched: "2026-04-03T07:24:03.699444"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Spectral Compact Training: Pre-Training Large Language Models via Permanent Truncated SVD and Stiefel QR Retraction
View PDF HTML (experimental)Abstract:The memory wall remains the primary bottleneck for training large language models on consumer hardware. We introduce Spectral Compact Training (SCT), a method that replaces dense weight matrices with permanent truncated SVD factors W = U diag(s) V^T, where the full dense matrix is never materialized during training or inference. Gradients flow through the compact spectral factors via standard backpropagation, and U, V are retracted to the Stiefel manifold via QR decomposition after each optimizer step. SCT achieves up to 199x memory reduction per MLP layer at rank 32, enabling full training steps of 70B-parameter architectures on a Steam Deck handheld (7.2 GB peak memory vs. 1,245 GB for dense FP32 training with Adam). Rank-sweep experiments on SmolLM2-1.7B (ranks 32-256, 2000 steps, NVIDIA A100) show that all tested ranks converge to the same loss floor (~4.2-4.5), identifying the learning rate schedule -- not MLP rank -- as the primary bottleneck. Rank 128 emerges as the efficiency sweet spot at 11.7x MLP compression with the lowest perplexity. GPU memory drops 46% at rank 32 while training throughput doubles.
Submission history
From: Björn Roman Kohlberger [view email][v1] Wed, 1 Apr 2026 10:53:56 UTC (38 KB)
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
