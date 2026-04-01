---
title: "Curvature-Guided LoRA: Steering in the pretrained NTK subspace"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29824"
published: "2026-04-01"
fetched: "2026-04-02T07:20:48.583227"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Curvature-Guided LoRA: Steering in the pretrained NTK subspace
View PDF HTML (experimental)Abstract:Parameter-efficient fine-tuning methods such as LoRA enable efficient adaptation of large pretrained models but often fall short of full fine-tuning performance. Existing approaches focus on aligning parameter updates, which only indirectly control model predictions. In this work, we introduce the prediction alignment problem, aiming to match the predictor obtained via PEFT to that of full fine-tuning at the level of outputs. We show that this objective naturally leads to a curvature-aware, second-order formulation, where optimal low-rank updates correspond to a Newton-like, curvature-whitened gradient. Based on this insight, we propose Curvature-Guided LoRA (CG-LoRA), which selects and scales adaptation directions using local curvature information. Our method is computationally efficient and avoids explicit second-order matrix construction. Preliminary experiments on standard natural language understanding benchmarks demonstrate improved performance and faster convergence compared to existing LoRA variants.
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
