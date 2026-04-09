---
title: "STQuant: Spatio-Temporal Adaptive Framework for Optimizer Quantization in Large Multimodal Model Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06836"
published: "2026-04-09"
fetched: "2026-04-10T07:05:08.256336"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:STQuant: Spatio-Temporal Adaptive Framework for Optimizer Quantization in Large Multimodal Model Training
View PDF HTML (experimental)Abstract:Quantization is an effective way to reduce the memory cost of large-scale model training. However, most existing methods adopt fixed-precision policies, which ignore the fact that optimizer-state distributions vary significantly across layers and training steps. Such uniform designs often introduce noticeable accuracy degradation. To move beyond fixed quantization, we propose STQuant, a distributed training framework that reduces the memory footprint of optimizer states via dynamic precision allocation across layers, state variables, and training steps, while maintaining model quality. Naively applying dynamic quantization during training is challenging for two reasons. First, optimizer states are numerically sensitive, and quantization noise can destabilize quality. Second, jointly considering multiple states and layers induces a large combinatorial search space. STQuant addresses these challenges with two key techniques: 1) a provably near-optimal factor selection strategy that accurately identifies the most influential factors for precision adaptation. 2) a dynamic transition decision algorithm that reduces the search cost from exponential to linear complexity. Experiments on GPT-2 and ViT show that STQuant reduces optimizer-state memory by 84.4%, achieving an average bit-width of as low as 5.1 bits, compared with existing solutions. Moreover, STQuant incurs only O(N/K) computational overhead and requires O(1) extra space.
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
