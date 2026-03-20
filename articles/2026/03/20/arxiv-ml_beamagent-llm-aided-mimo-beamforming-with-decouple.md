---
title: "BeamAgent: LLM-Aided MIMO Beamforming with Decoupled Intent Parsing and Alternating Optimization for Joint Site Selection and Precoding"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18855"
published: "2026-03-20"
fetched: "2026-03-20T13:16:44.766900"
---

Computer Science > Information Theory
[Submitted on 19 Mar 2026]
Title:BeamAgent: LLM-Aided MIMO Beamforming with Decoupled Intent Parsing and Alternating Optimization for Joint Site Selection and Precoding
View PDF HTML (experimental)Abstract:Integrating large language models (LLMs) into wireless communication optimization is a promising yet challenging direction. Existing approaches either use LLMs as black-box solvers or code generators, tightly coupling them with numerical computation. However, LLMs lack the precision required for physical-layer optimization, and the scarcity of wireless training data makes domain-specific fine-tuning impractical. We propose BeamAgent, an LLM-aided MIMO beamforming framework that explicitly decouples semantic intent parsing from numerical optimization. The LLM serves solely as a semantic translator that converts natural language descriptions into structured spatial constraints. A dedicated gradient-based optimizer then jointly solves the discrete base station site selection and continuous precoding design through an alternating optimization algorithm. A scene-aware prompt enables grounded spatial reasoning without fine-tuning, and a multi-round interaction mechanism with dual-layer intent classification ensures robust constraint verification. A penalty-based loss function enforces dark-zone power constraints while releasing optimization degrees of freedom for bright-zone gain maximization. Experiments on a ray-tracing-based urban MIMO scenario show that BeamAgent achieves a bright-zone power of 84.0\,dB, outperforming exhaustive zero-forcing by 7.1 dB under the same dark-zone constraint. The end-to-end system reaches within 3.3 dB of the expert upper bound, with the full optimization completing in under 2 s on a laptop.
Current browse context:
cs.IT
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
