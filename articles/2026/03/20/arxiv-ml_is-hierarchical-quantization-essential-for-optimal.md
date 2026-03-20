---
title: "Is Hierarchical Quantization Essential for Optimal Reconstruction?"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.22244"
published: "2026-03-20"
fetched: "2026-03-20T15:03:28.298186"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 29 Jan 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Is Hierarchical Quantization Essential for Optimal Reconstruction?
View PDF HTML (experimental)Abstract:Vector-quantized variational autoencoders (VQ-VAEs) are central to models that rely on high reconstruction fidelity, from neural compression to generative pipelines. Hierarchical extensions, such as VQ-VAE2, are often credited with superior reconstruction performance because they split global and local features across multiple levels. However, since higher levels derive all their information from lower levels, they should not carry additional reconstructive content beyond what the lower-level already encodes. Combined with recent advances in training objectives and quantization mechanisms, this leads us to ask whether a single-level VQ-VAE, with matched representational budget and no codebook collapse, can equal the reconstruction fidelity of its hierarchical counterpart. Although the multi-scale structure of hierarchical models may improve perceptual quality in downstream tasks, the effect of hierarchy on reconstruction accuracy, isolated from codebook utilization and overall representational capacity, remains empirically underexamined. We revisit this question by comparing a two-level VQ-VAE and a capacity-matched single-level model on high-resolution ImageNet images. Consistent with prior observations, we confirm that inadequate codebook utilization limits single-level VQ-VAEs and that overly high-dimensional embeddings destabilize quantization and increase codebook collapse. We show that lightweight interventions such as initialization from data, periodic reset of inactive codebook vectors, and systematic tuning of codebook hyperparameters significantly reduce collapse. Our results demonstrate that when representational budgets are matched, and codebook collapse is mitigated, single-level VQ-VAEs can match the reconstruction fidelity of hierarchical variants, challenging the assumption that hierarchical quantization is inherently superior for high-quality reconstructions.
Submission history
From: Shirin Reyhanian [view email][v1] Thu, 29 Jan 2026 19:09:50 UTC (8,503 KB)
[v2] Thu, 19 Mar 2026 09:12:28 UTC (8,503 KB)
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
