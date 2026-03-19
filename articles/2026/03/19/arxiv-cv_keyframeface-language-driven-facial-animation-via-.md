---
title: "KeyframeFace: Language-Driven Facial Animation via Semantic Keyframes"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.11321"
published: "2026-03-19"
fetched: "2026-03-19T16:29:23.266843"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 12 Dec 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:KeyframeFace: Language-Driven Facial Animation via Semantic Keyframes
View PDF HTML (experimental)Abstract:Facial animation is a core component for creating digital characters in Computer Graphics (CG) industry. A typical production workflow relies on sparse, semantically meaningful keyframes to precisely control facial expressions. Enabling such animation directly from natural-language descriptions could significantly improve content creation efficiency and accessibility. However, most existing methods adopt a text-to-continuous-frames paradigm, directly regressing dense facial motion trajectories from language. This formulation entangles high-level semantic intent with low-level motion, lacks explicit semantic control structure, and limits precise editing and interpretability. Inspired by the keyframe paradigm in animation production, we propose KeyframeFace, a framework for semantic facial animation from language via interpretable keyframes. Instead of predicting dense motion trajectories, our method represents animation as a sequence of semantically meaningful keyframes in an interpretable ARKit-based facial control space. A language-driven model leverages large language model (LLM) priors to generate keyframes that align with contextual text descriptions and emotion cues. To support this formulation, we construct a multimodal dataset comprising 2,100 expression scripts paired with monocular videos, per-frame ARKit coefficients, and manually annotated semantic keyframes. Experiments show that incorporating semantic keyframe supervision and language priors significantly improves expression fidelity and semantic alignment compared to methods that do not use facial action semantics.
Submission history
From: Jingchao Wu [view email][v1] Fri, 12 Dec 2025 06:45:02 UTC (17,649 KB)
[v2] Wed, 18 Mar 2026 15:44:53 UTC (21,633 KB)
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
