---
title: "Activation Quantization of Vision Encoders Needs Prefixing Registers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.04547"
published: "2026-03-20"
fetched: "2026-03-20T14:08:17.436454"
---

Computer Science > Machine Learning
[Submitted on 6 Oct 2025 (v1), last revised 19 Mar 2026 (this version, v4)]
Title:Activation Quantization of Vision Encoders Needs Prefixing Registers
View PDF HTML (experimental)Abstract:Large pretrained vision encoders are central to multimodal intelligence, powering applications from on-device vision processing to vision-language models. Since these applications often demand real-time processing of massive visual data, reducing the inference cost of vision encoders is critical. Quantization offers a practical path, but it remains challenging even at 8-bit precision due to so-called outliers. In this work, we propose $\textit{RegCache}$, a training-free algorithm that mitigates outliers in large-scale pretrained vision encoders and serves as a plug-in module that can be applied on top of other quantization methods. RegCache introduces outlier-prone yet semantically meaningless prefix tokens to the vision encoder, which prevent other tokens from having outliers. Notably, we observe that outliers in vision encoders behave differently from those in language models, motivating two technical innovations: middle-layer prefixing and token deletion. Experimental results show that our method consistently improves quantized model performance across various vision encoders, particularly in extremely low-bit regimes (e.g., 4-bit).
Submission history
From: Seunghyeon Kim [view email][v1] Mon, 6 Oct 2025 07:27:46 UTC (3,171 KB)
[v2] Fri, 10 Oct 2025 06:33:23 UTC (3,171 KB)
[v3] Fri, 28 Nov 2025 12:54:42 UTC (2,918 KB)
[v4] Thu, 19 Mar 2026 12:18:57 UTC (7,842 KB)
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
