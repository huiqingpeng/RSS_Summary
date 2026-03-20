---
title: "EffectErase: Joint Video Object Removal and Insertion for High-Quality Effect Erasing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19224"
published: "2026-03-20"
fetched: "2026-03-20T16:06:12.419457"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:EffectErase: Joint Video Object Removal and Insertion for High-Quality Effect Erasing
View PDF HTML (experimental)Abstract:Video object removal aims to eliminate dynamic target objects and their visual effects, such as deformation, shadows, and reflections, while restoring seamless backgrounds. Recent diffusion-based video inpainting and object removal methods can remove the objects but often struggle to erase these effects and to synthesize coherent backgrounds. Beyond method limitations, progress is further hampered by the lack of a comprehensive dataset that systematically captures common object effects across varied environments for training and evaluation. To address this, we introduce VOR (Video Object Removal), a large-scale dataset that provides diverse paired videos, each consisting of one video where the target object is present with its effects and a counterpart where the object and effects are absent, with corresponding object masks. VOR contains 60K high-quality video pairs from captured and synthetic sources, covers five effects types, and spans a wide range of object categories as well as complex, dynamic multi-object scenes. Building on VOR, we propose EffectErase, an effect-aware video object removal method that treats video object insertion as the inverse auxiliary task within a reciprocal learning scheme. The model includes task-aware region guidance that focuses learning on affected areas and enables flexible task switching. Then, an insertion-removal consistency objective that encourages complementary behaviors and shared localization of effect regions and structural cues. Trained on VOR, EffectErase achieves superior performance in extensive experiments, delivering high-quality video object effect erasing across diverse scenarios.
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
