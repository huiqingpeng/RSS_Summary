---
title: "Frequency Autoregressive Image Generation with Continuous Tokens"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2503.05305"
published: "2026-03-19"
fetched: "2026-03-19T16:23:43.507610"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 7 Mar 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Frequency Autoregressive Image Generation with Continuous Tokens
View PDF HTML (experimental)Abstract:Autoregressive (AR) models for image generation typically adopt a two-stage paradigm of vector quantization and raster-scan ``next-token prediction", inspired by its great success in language modeling. However, due to the huge modality gap, image autoregressive models may require a systematic reevaluation from two perspectives: tokenizer format and regression direction. In this paper, we introduce the frequency progressive autoregressive (\textbf{FAR}) paradigm and instantiate FAR with the continuous tokenizer. Specifically, we identify spectral dependency as the desirable regression direction for FAR, wherein higher-frequency components build upon the lower one to progressively construct a complete image. This design seamlessly fits the causality requirement for autoregressive models and preserves the unique spatial locality of image data. Besides, we delve into the integration of FAR and the continuous tokenizer, introducing a series of techniques to address optimization challenges and improve the efficiency of training and inference processes. We demonstrate the efficacy of FAR through comprehensive experiments on the ImageNet dataset and verify its potential on text-to-image generation.
Submission history
From: Hu Yu [view email][v1] Fri, 7 Mar 2025 10:34:04 UTC (8,910 KB)
[v2] Wed, 18 Mar 2026 15:04:58 UTC (8,906 KB)
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
