---
title: "SineProject: Machine Unlearning for Stable Vision Language Alignment"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.18444"
published: "2026-03-18"
fetched: "2026-03-18T18:29:19.156956"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 23 Nov 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:SineProject: Machine Unlearning for Stable Vision Language Alignment
View PDF HTML (experimental)Abstract:Multimodal Large Language Models (MLLMs) increasingly need to forget specific knowledge such as unsafe or private information without requiring full retraining. However, existing unlearning methods often disrupt vision language alignment, causing models to reject both harmful and benign queries. We trace this failure to the projector network during unlearning, its Jacobian becomes severely illconditioned, leading to unstable optimization and drift in cross modal embeddings. We introduce SineProject, a simple method that augments the frozen projector with sinusoidally modulated trainable parameters, improving the Jacobian's spectral conditioning and stabilizing alignment throughout unlearning. Across standard safety and privacy unlearning benchmarks using LLaVA v1.5 7B and 13B, SineProject reduces benign query refusals while achieving complete forgetting of targeted information, yielding state of the art forget retain trade offs with negligible computational overhead.
Submission history
From: Arpit Garg [view email][v1] Sun, 23 Nov 2025 13:29:28 UTC (2,076 KB)
[v2] Tue, 17 Mar 2026 02:42:20 UTC (2,079 KB)
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
