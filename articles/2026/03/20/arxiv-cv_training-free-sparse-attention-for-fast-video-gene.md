---
title: "Training-Free Sparse Attention for Fast Video Generation via Offline Layer-Wise Sparsity Profiling and Online Bidirectional Co-Clustering"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18636"
published: "2026-03-20"
fetched: "2026-03-20T15:13:33.099461"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Training-Free Sparse Attention for Fast Video Generation via Offline Layer-Wise Sparsity Profiling and Online Bidirectional Co-Clustering
View PDF HTML (experimental)Abstract:Diffusion Transformers (DiTs) achieve strong video generation quality but suffer from high inference cost due to dense 3D attention, leading to the development of sparse attention technologies to improve efficiency. However, existing training-free sparse attention methods in video generation still face two unresolved limitations: ignoring layer heterogeneity in attention pruning and ignoring query-key coupling in block partitioning, which hinder a better quality-speedup trade-off. In this work, we uncover a critical insight that the attention sparsity of each layer is its intrinsic property, with minor effects across different inputs. Motivated by this, we propose SVOO, a training-free Sparse attention framework for fast Video generation via Offline layer-wise sparsity profiling and Online bidirectional co-clustering. Specifically, SVOO adopts a two-stage paradigm: (i) offline layer-wise sensitivity profiling to derive intrinsic per-layer pruning levels, and (ii) online block-wise sparse attention via a novel bidirectional co-clustering algorithm. Extensive experiments on seven widely used video generation models demonstrate that SVOO achieves a superior quality-speedup trade-off over state-of-the-art methods, delivering up to $1.93\times$ speedup while maintaining a PSNR of up to 29 dB on Wan2.1.
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
