---
title: "Self-Attention And Beyond the Infinite: Towards Linear Transformers with Infinite Self-Attention"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.00175"
published: "2026-03-19"
fetched: "2026-03-19T16:31:47.631556"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v4)]
Title:Self-Attention And Beyond the Infinite: Towards Linear Transformers with Infinite Self-Attention
View PDF HTML (experimental)Abstract:The quadratic cost of softmax attention limits Transformer scalability in high-resolution vision. We introduce Infinite Self-Attention (InfSA), a spectral reformulation that treats each attention layer as a diffusion step on a content-adaptive token graph, accumulating multi-hop interactions through a discounted Neumann series over attention matrices. This links self-attention to classical graph centrality (Katz, PageRank, eigenvector centrality) for interpretable token weighting. We also show the Neumann kernel equals the fundamental matrix of an absorbing Markov chain, so a token's centrality is its expected number of random-walk visits before absorption. We then propose Linear-InfSA, a linear-time variant that approximates the principal eigenvector of the implicit attention operator without forming the full attention matrix. It keeps an auxiliary state of fixed size proportional to per-head dimension dh (independent of sequence length N), is drop-in compatible with Vision Transformers, and supports stable training at 4096 by 4096 and inference at 9216 by 9216 (about 332k tokens). In a 4-layer ViT (53.5M parameters, 59 GFLOPs at 224 by 224), Linear-InfSA reaches 84.7% top-1 on ImageNet-1K, a +3.2 point architectural gain over an equal-depth softmax ViT trained with the same recipe. On ImageNet-V2, InfViT variants outperform all compared baselines (up to 79.8% vs 76.8%), indicating robustness under distribution shift. On an A100 40GB GPU, Linear-InfViT runs at 231 images/s and 0.87 J/image (13x better throughput and energy than equal-depth ViT) and is the only tested model to complete 9216 by 9216 inference without out-of-memory. The linear approximation closely matches the dominant eigenvector of the quadratic operator (cosine 0.985). Code available at: this https URL or this https URL
Submission history
From: Giorgio Roffo [view email][v1] Thu, 26 Feb 2026 18:34:26 UTC (828 KB)
[v2] Sun, 8 Mar 2026 20:24:11 UTC (633 KB)
[v3] Tue, 10 Mar 2026 17:08:43 UTC (633 KB)
[v4] Wed, 18 Mar 2026 11:23:44 UTC (636 KB)
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
