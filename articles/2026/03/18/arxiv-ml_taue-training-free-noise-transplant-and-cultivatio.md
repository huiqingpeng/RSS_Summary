---
title: "TAUE: Training-free Noise Transplant and Cultivation Diffusion Model"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.02580"
published: "2026-03-18"
fetched: "2026-03-18T17:12:36.433154"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 4 Nov 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:TAUE: Training-free Noise Transplant and Cultivation Diffusion Model
View PDF HTML (experimental)Abstract:Despite the remarkable success of text-to-image diffusion models, their output of a single, flattened image remains a critical bottleneck for professional applications requiring layer-wise control. Existing solutions either rely on fine-tuning with large, inaccessible datasets or are training-free yet limited to generating isolated foreground elements, failing to produce a complete and coherent scene. To address this, we introduce the Training-free Noise Transplantation and Cultivation Diffusion Model (TAUE), a novel framework for layer-wise image generation that requires neither fine-tuning nor additional data. TAUE embeds global structural information from intermediate denoising latents into the initial noise to preserve spatial coherence, and integrates semantic cues through cross-layer attention sharing to maintain contextual and visual consistency across layers. Extensive experiments demonstrate that TAUE achieves state-of-the-art performance among training-free methods, delivering image quality comparable to fine-tuned models while improving inter-layer consistency. Moreover, it enables new applications, such as layout-aware editing, multi-object composition, and background replacement, indicating potential for interactive, layer-separated generation systems in real-world creative workflows.
Submission history
From: Ryugo Morita [view email][v1] Tue, 4 Nov 2025 13:56:39 UTC (13,546 KB)
[v2] Tue, 17 Mar 2026 10:21:32 UTC (10,316 KB)
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
