---
title: "Fixed Anchors Are Not Enough: Dynamic Retrieval and Persistent Homology for Dataset Distillation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.24144"
published: "2026-03-18"
fetched: "2026-03-18T18:33:08.068496"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 27 Feb 2026 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Fixed Anchors Are Not Enough: Dynamic Retrieval and Persistent Homology for Dataset Distillation
View PDF HTML (experimental)Abstract:Decoupled dataset distillation (DD) compresses large corpora into a few synthetic images by matching a frozen teacher's statistics. However, current residual-matching pipelines rely on static real patches, creating a fit-complexity gap and a pull-to-anchor effect that reduce intra-class diversity and hurt generalization. To address these issues, we introduce RETA -- a Retrieval and Topology Alignment framework for decoupled DD. First, Dynamic Retrieval Connection (DRC) selects a real patch from a prebuilt pool by minimizing a fit-complexity score in teacher feature space; the chosen patch is injected via a residual connection to tighten feature fit while controlling injected complexity. Second, Persistent Topology Alignment (PTA) regularizes synthesis with persistent homology: we build a mutual k-NN feature graph, compute persistence images of components and loops, and penalize topology discrepancies between real and synthetic sets, mitigating pull-to-anchor effect. Across CIFAR-100, Tiny-ImageNet, ImageNet-1K, and multiple ImageNet subsets, RETA consistently outperforms various baselines under comparable time and memory, especially reaching 64.3% top-1 accuracy on ImageNet-1K with ResNet-18 at 50 images per class, +3.1% over the best prior.
Submission history
From: Muquan Li [view email][v1] Fri, 27 Feb 2026 16:21:07 UTC (1,979 KB)
[v2] Mon, 16 Mar 2026 09:13:08 UTC (2,057 KB)
[v3] Tue, 17 Mar 2026 12:09:31 UTC (2,058 KB)
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
