---
title: "ODE-free Neural Flow Matching for One-Step Generative Modeling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06413"
published: "2026-04-09"
fetched: "2026-04-10T07:04:58.493356"
---

Computer Science > Machine Learning
[Submitted on 7 Apr 2026]
Title:ODE-free Neural Flow Matching for One-Step Generative Modeling
View PDF HTML (experimental)Abstract:Diffusion and flow matching models generate samples by learning time-dependent vector fields whose integration transports noise to data, requiring tens to hundreds of network evaluations at inference. We instead learn the transport map directly. We propose Optimal Transport Neural Flow Matching (OT-NFM), an ODE-free generative framework that parameterizes the flow map with neural flows, enabling true one-step generation with a single forward pass. We show that naive flow-map training suffers from mean collapse, where inconsistent noise-data pairings drive all outputs toward the data mean. We prove that consistent coupling is necessary for non-degenerate learning and address this using optimal transport pairings with scalable minibatch and online coupling strategies. Experiments on synthetic benchmarks and image generation tasks (MNIST and CIFAR-10) demonstrate competitive sample quality while reducing inference to a single network evaluation.
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
