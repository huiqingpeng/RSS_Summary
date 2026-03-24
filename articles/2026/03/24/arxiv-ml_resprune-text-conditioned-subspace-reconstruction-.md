---
title: "ResPrune: Text-Conditioned Subspace Reconstruction for Visual Token Pruning in Large Vision-Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.21105"
published: "2026-03-24"
fetched: "2026-03-25T07:18:52.204974"
---

Computer Science > Machine Learning
[Submitted on 22 Mar 2026]
Title:ResPrune: Text-Conditioned Subspace Reconstruction for Visual Token Pruning in Large Vision-Language Models
View PDF HTML (experimental)Abstract:Large Vision-Language Models (LVLMs) rely on dense visual tokens to capture fine-grained visual information, but processing all these tokens incurs substantial computational and memory overhead during inference. To address this issue, we propose ResPrune, a training-free visual token pruning framework that enables efficient LVLM inference by selecting a compact yet informative subset of visual tokens. ResPrune formulates visual token pruning as a subspace reconstruction problem and employs a greedy subspace expansion strategy guided by residual energy, allowing it to preserve the geometric structure of the original visual token space. To further incorporate cross modal alignment, the selection process is conditioned on textual relevance, encouraging the retention of tokens that are both informative and instruction-relevant. The proposed method is lightweight and model-agnostic, and can be seamlessly integrated into existing LVLM pipelines without retraining or architectural modifications. Extensive experiments on multiple LVLM backbones, including LLaVA-1.5, LLaVA-NeXT, and Qwen2.5-VL, demonstrate that ResPrune consistently outperforms existing pruning approaches across a wide range of benchmarks, while achieving effective reductions in computation, memory consumption, and inference latency.
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
