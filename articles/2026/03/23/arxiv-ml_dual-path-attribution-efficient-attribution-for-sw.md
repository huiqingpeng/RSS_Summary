---
title: "Dual Path Attribution: Efficient Attribution for SwiGLU-Transformers through Layer-Wise Target Propagation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19742"
published: "2026-03-23"
fetched: "2026-03-24T07:21:55.840398"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Dual Path Attribution: Efficient Attribution for SwiGLU-Transformers through Layer-Wise Target Propagation
View PDF HTML (experimental)Abstract:Understanding the internal mechanisms of transformer-based large language models (LLMs) is crucial for their reliable deployment and effective operation. While recent efforts have yielded a plethora of attribution methods attempting to balance faithfulness and computational efficiency, dense component attribution remains prohibitively expensive. In this work, we introduce Dual Path Attribution (DPA), a novel framework that faithfully traces information flow on the frozen transformer in one forward and one backward pass without requiring counterfactual examples. DPA analytically decomposes and linearizes the computational structure of the SwiGLU Transformers into distinct pathways along which it propagates a targeted unembedding vector to receive the effective representation at each residual position. This target-centric propagation achieves O(1) time complexity with respect to the number of model components, scaling to long input sequences and dense component attribution. Extensive experiments on standard interpretability benchmarks demonstrate that DPA achieves state-of-the-art faithfulness and unprecedented efficiency compared to existing baselines.
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
