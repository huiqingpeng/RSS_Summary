---
title: "AgriPath: A Systematic Exploration of Architectural Trade-offs for Crop Disease Classification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.13354"
published: "2026-03-18"
fetched: "2026-03-18T17:16:11.045561"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 8 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:AgriPath: A Systematic Exploration of Architectural Trade-offs for Crop Disease Classification
View PDF HTML (experimental)Abstract:Reliable crop disease detection requires models that perform consistently across diverse acquisition conditions, yet existing evaluations often focus on single architectural families or lab-generated datasets. This work presents a systematic empirical comparison of three model paradigms for fine-grained crop disease classification: Convolutional Neural Networks (CNNs), contrastive Vision-Language Models (VLMs), and generative VLMs. To enable controlled analysis of domain effects, we introduce AgriPath-LF16, a benchmark containing 111k images spanning 16 crops and 41 diseases with explicit separation between laboratory and field imagery, alongside a balanced 30k subset for standardized training and evaluation. All models are trained and evaluated under unified protocols across full, lab-only, and field-only training regimes using macro-F1 and Parse Success Rate (PSR) to account for generative reliability. The results reveal distinct performance profiles. CNNs achieve the highest accuracy on lab imagery but degrade under domain shift. Contrastive VLMs provide a robust and parameter-efficient alternative with competitive cross-domain performance. Generative VLMs demonstrate the strongest resilience to distributional variation, albeit with additional failure modes stemming from free-text generation. These findings highlight that architectural choice should be guided by deployment context rather than aggregate accuracy alone.
Submission history
From: Hamza Mooraj [view email][v1] Sun, 8 Mar 2026 17:28:01 UTC (870 KB)
[v2] Tue, 17 Mar 2026 10:54:10 UTC (869 KB)
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
