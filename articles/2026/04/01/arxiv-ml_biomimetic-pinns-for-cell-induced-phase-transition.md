---
title: "Biomimetic PINNs for Cell-Induced Phase Transitions: UQ-R3 Sampling with Causal Gating"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29184"
published: "2026-04-01"
fetched: "2026-04-02T07:16:05.832694"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Biomimetic PINNs for Cell-Induced Phase Transitions: UQ-R3 Sampling with Causal Gating
View PDF HTML (experimental)Abstract:Nonconvex multi-well energies in cell-induced phase transitions give rise to sharp interfaces, fine-scale microstructures, and distance-dependent inter-cell coupling, all of which pose significant challenges for physics-informed learning. Existing methods often suffer from over-smoothing in near-field patterns. To address this, we propose biomimetic physics-informed neural networks (Bio-PINNs), a variational framework that encodes temporal causality into explicit spatial causality via a progressive distance gate. Furthermore, Bio-PINNs leverage a deformation-uncertainty proxy for the interfacial length scale to target microstructure-prone regions, providing a computationally efficient alternative to explicit second-derivative regularization. We provide theoretical guarantees for the resulting uncertainty-driven ``retain-resample-release" adaptive collocation strategy, which ensures persistent coverage under gating and establishing a quantitative near-to-far growth bound. Across single- and multi-cell benchmarks, diverse separations, and various regularization regimes, Bio-PINNs consistently recover sharp transition layers and tether morphologies, significantly outperforming state-of-the-art adaptive and ungated baselines.
Current browse context:
cs.LG
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
