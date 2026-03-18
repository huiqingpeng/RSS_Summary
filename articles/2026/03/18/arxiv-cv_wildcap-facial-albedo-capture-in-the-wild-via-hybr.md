---
title: "WildCap: Facial Albedo Capture in the Wild via Hybrid Inverse Rendering"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.11237"
published: "2026-03-18"
fetched: "2026-03-18T18:31:12.124395"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 12 Dec 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:WildCap: Facial Albedo Capture in the Wild via Hybrid Inverse Rendering
View PDF HTML (experimental)Abstract:Existing methods achieve high-quality facial albedo capture under controllable lighting, which increases capture cost and limits usability. We propose WildCap, a novel method for high-quality facial albedo capture from a smartphone video recorded in the wild. To disentangle high-quality albedo from complex lighting effects in in-the-wild captures, we propose a novel hybrid inverse rendering framework. We first apply a data-driven method, i.e., SwitchLight, to convert the captured images into more constrained conditions and then adopt model-based inverse rendering. However, unavoidable local artifacts in network predictions, such as shadow-baking, are non-physical and thus hinder accurate inverse rendering of lighting and material. To address this, we propose a novel texel grid lighting model to explain non-physical effects as clean albedo illuminated by local physical lighting. During optimization, we jointly sample a diffusion prior for the albedo map and optimize the lighting, effectively resolving scale ambiguity between local lights and albedo. Other reflectance maps are then predicted from the albedo. Our method achieves significantly better results than prior arts in the same capture setup, closing the quality gap between in-the-wild and controllable recordings by a large margin.
Submission history
From: Yuxuan Han [view email][v1] Fri, 12 Dec 2025 02:37:03 UTC (9,241 KB)
[v2] Tue, 17 Mar 2026 13:12:15 UTC (18,205 KB)
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
