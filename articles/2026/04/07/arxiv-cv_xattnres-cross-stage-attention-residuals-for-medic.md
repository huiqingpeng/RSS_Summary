---
title: "XAttnRes: Cross-Stage Attention Residuals for Medical Image Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03297"
published: "2026-04-07"
fetched: "2026-04-08T07:02:41.258571"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 28 Mar 2026]
Title:XAttnRes: Cross-Stage Attention Residuals for Medical Image Segmentation
View PDF HTML (experimental)Abstract:In the field of Large Language Models (LLMs), Attention Residuals have recently demonstrated that learned, selective aggregation over all preceding layer outputs can outperform fixed residual connections. We propose Cross-Stage Attention Residuals (XAttnRes), a mechanism that maintains a global feature history pool accumulating both encoder and decoder stage outputs. Through lightweight pseudo-query attention, each stage selectively aggregates from all preceding representations. To bridge the gap between the same-dimensional Transformer layers in LLMs and the multi-scale encoder-decoder stages in segmentation networks, XAttnRes introduces spatial alignment and channel projection steps that handle cross-resolution features with negligible overhead. When added to existing segmentation networks, XAttnRes consistently improves performance across four datasets and three imaging modalities. We further observe that XAttnRes alone, even without skip connections, achieves performance on par with the baseline, suggesting that learned aggregation can recover the inter-stage information flow traditionally provided by predetermined connections.
Current browse context:
cs.CV
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
