---
title: "Matryoshka Gaussian Splatting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19234"
published: "2026-03-20"
fetched: "2026-03-20T16:07:10.504858"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Matryoshka Gaussian Splatting
View PDF HTML (experimental)Abstract:The ability to render scenes at adjustable fidelity from a single model, known as level of detail (LoD), is crucial for practical deployment of 3D Gaussian Splatting (3DGS). Existing discrete LoD methods expose only a limited set of operating points, while concurrent continuous LoD approaches enable smoother scaling but often suffer noticeable quality degradation at full capacity, making LoD a costly design decision. We introduce Matryoshka Gaussian Splatting (MGS), a training framework that enables continuous LoD for standard 3DGS pipelines without sacrificing full-capacity rendering quality. MGS learns a single ordered set of Gaussians such that rendering any prefix, the first k splats, produces a coherent reconstruction whose fidelity improves smoothly with increasing budget. Our key idea is stochastic budget training: each iteration samples a random splat budget and optimises both the corresponding prefix and the full set. This strategy requires only two forward passes and introduces no architectural modifications. Experiments across four benchmarks and six baselines show that MGS matches the full-capacity performance of its backbone while enabling a continuous speed-quality trade-off from a single model. Extensive ablations on ordering strategies, training objectives, and model capacity further validate the designs.
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
