---
title: "Deep Expert Injection for Anchoring Retinal VLMs with Domain-Specific Knowledge"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.07131"
published: "2026-03-20"
fetched: "2026-03-20T16:18:17.858193"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 7 Mar 2026 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:Deep Expert Injection for Anchoring Retinal VLMs with Domain-Specific Knowledge
View PDF HTML (experimental)Abstract:Large Vision Language Models (LVLMs) show immense potential for automated ophthalmic diagnosis. However, their clinical deployment is severely hindered by lacking domain-specific knowledge. In this work, we identify two structural deficiencies hindering reliable medical reasoning: 1) the Perception Gap, where general-purpose visual encoders fail to resolve fine-grained pathological cues (e.g., microaneurysms); and 2) the Reasoning Gap, where sparse visual evidence is progressively overridden by massive language priors in deeper transformer layers, leading to ungrounded hallucinations. To bridge these gaps, we propose EyExIn, a data-efficient framework designed to anchor retinal VLMs with expert knowledge via a Deep Expert Injection mechanism. Our architecture employs an Expert-Aware Dual-Stream encoding strategy that decouples visual representation into a general stream for anatomical context and a specialized expert stream for pathological semantics. To ensure high-fidelity integration, we design a Semantic-Adaptive Gated Fusion module, which dynamically amplifies subtle lesion signals while filtering irrelevant background noise. Furthermore, we introduce Adaptive Deep Expert Injection to embed persistent "Vision Anchors" by integrating fused visual features as residual biases directly into intermediate LLM layers. This mechanism creates a visual shortcut that forces the reasoning stack to remain strictly grounded in visual evidence. Extensive experiments across four benchmarks demonstrate that our model consistently outperforms massive proprietary systems. EyExIn significantly enhances domain-specific knowledge embedding and achieves state-of-the-art precision in ophthalmic visual question answering, advancing the development of trustworthy ophthalmic AI.
Submission history
From: Shuai Lu [view email][v1] Sat, 7 Mar 2026 09:43:49 UTC (734 KB)
[v2] Tue, 10 Mar 2026 05:28:24 UTC (732 KB)
[v3] Thu, 19 Mar 2026 08:24:18 UTC (732 KB)
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
