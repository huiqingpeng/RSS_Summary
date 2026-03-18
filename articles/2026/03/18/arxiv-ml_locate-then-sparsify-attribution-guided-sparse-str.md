---
title: "Locate-then-Sparsify: Attribution Guided Sparse Strategy for Visual Hallucination Mitigation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16284"
published: "2026-03-18"
fetched: "2026-03-18T16:11:34.263244"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Locate-then-Sparsify: Attribution Guided Sparse Strategy for Visual Hallucination Mitigation
View PDF HTML (experimental)Abstract:Despite the significant advancements in Large Vision-Language Models (LVLMs), their tendency to generate hallucinations undermines reliability and restricts broader practical deployment. Among the hallucination mitigation methods, feature steering emerges as a promising approach that reduces erroneous outputs in LVLMs without increasing inference costs. However, current methods apply uniform feature steering across all layers. This heuristic strategy ignores inter-layer differences, potentially disrupting layers unrelated to hallucinations and ultimately leading to performance degradation on general tasks. In this paper, we propose a plug-and-play framework called Locate-Then-Sparsify for Feature Steering (LTS-FS), which controls the steering intensity according to the hallucination relevance of each layer. We first construct a synthetic dataset comprising token-level and sentence-level hallucination cases. Based on this dataset, we introduce an attribution method based on causal interventions to quantify the hallucination relevance of each layer. With the attribution scores across layers, we propose a layerwise strategy that converts these scores into feature steering intensities for individual layers, enabling more precise adjustments specifically on hallucination-relevant layers. Extensive experiments across multiple LVLMs and benchmarks demonstrate that our LTS-FS framework effectively mitigates hallucination while preserving strong performance.
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
