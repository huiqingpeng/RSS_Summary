---
title: "Adaptive Auxiliary Prompt Blending for Target-Faithful Diffusion Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19158"
published: "2026-03-20"
fetched: "2026-03-20T16:05:00.653640"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Adaptive Auxiliary Prompt Blending for Target-Faithful Diffusion Generation
View PDF HTML (experimental)Abstract:Diffusion-based text-to-image (T2I) models have made remarkable progress in generating photorealistic and semantically rich images. However, when the target concepts lie in low-density regions of the training distribution, these models often produce semantically misaligned or structurally inconsistent results. This limitation arises from the long-tailed nature of text-image datasets, where rare concepts or editing instructions are underrepresented. To address this, we introduce Adaptive Auxiliary Prompt Blending (AAPB) - a unified framework that stabilizes the diffusion process in low-density regions. AAPB leverages auxiliary anchor prompts to provide semantic support in rare concept generation and structural support in image editing, ensuring faithful guidance toward the target prompt. Unlike prior heuristic prompt alternation methods, AAPB derives a closed-form adaptive coefficient that optimally balances the influence between the auxiliary anchor and the target prompt at each diffusion step. Grounded in Tweedie's identity, our formulation provides a principled and training-free framework for adaptive prompt blending, ensuring stable and target-faithful generation. We demonstrate the effectiveness of adaptive interpolation over fixed interpolation through controlled experiments and empirically show consistent improvements on the RareBench and FlowEdit datasets, achieving superior semantic accuracy and structural fidelity compared to prior training-free baselines.
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
