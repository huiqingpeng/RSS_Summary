---
title: "VertAX: a differentiable vertex model for learning epithelial tissue mechanics"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06896"
published: "2026-04-09"
fetched: "2026-04-10T07:05:09.071370"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:VertAX: a differentiable vertex model for learning epithelial tissue mechanics
View PDF HTML (experimental)Abstract:Epithelial tissues dynamically reshape through local mechanical interactions among cells, a process well captured by vertex models. Yet their many tunable parameters make inference and optimization challenging, motivating computational frameworks that flexibly model and learn tissue mechanics. We introduce VertAX, a differentiable JAX-based framework for vertex-modeling of confluent epithelia. VertAX provides automatic differentiation, GPU acceleration, and end-to-end bilevel optimization for forward simulation, parameter inference, and inverse mechanical design. Users can define arbitrary energy and cost functions in pure Python, enabling seamless integration with machine-learning pipelines. We demonstrate VertAX on three representative tasks: (i) forward modeling of tissue morphogenesis, (ii) mechanical parameter inference, and (iii) inverse design of tissue-scale behaviors. We benchmark three differentiation strategies-automatic differentiation, implicit differentiation, and equilibrium propagation-showing that the latter can approximate gradients using repeated forward, adjoint-free simulations alone, offering a simple route for extending inverse biophysical problems to non-differentiable simulators with limited additional engineering effort.
Current browse context:
cs.LG
Change to browse by:
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
