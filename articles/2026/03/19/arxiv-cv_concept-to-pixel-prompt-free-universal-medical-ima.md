---
title: "Concept-to-Pixel: Prompt-Free Universal Medical Image Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17746"
published: "2026-03-19"
fetched: "2026-03-19T15:17:07.888906"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Concept-to-Pixel: Prompt-Free Universal Medical Image Segmentation
View PDF HTML (experimental)Abstract:Universal medical image segmentation seeks to use a single foundational model to handle diverse tasks across multiple imaging modalities. However, existing approaches often rely heavily on manual visual prompts or retrieved reference images, which limits their automation and robustness. In addition, naive joint training across modalities often fails to address large domain shifts. To address these limitations, we propose Concept-to-Pixel (C2P), a novel prompt-free universal segmentation framework. C2P explicitly separates anatomical knowledge into two components: Geometric and Semantic representations. It leverages Multimodal Large Language Models (MLLMs) to distill abstract, high-level medical concepts into learnable Semantic Tokens and introduces explicitly supervised Geometric Tokens to enforce universal physical and structural constraints. These disentangled tokens interact deeply with image features to generate input-specific dynamic kernels for precise mask prediction. Furthermore, we introduce a Geometry-Aware Inference Consensus mechanism, which utilizes the model's predicted geometric constraints to assess prediction reliability and suppress outliers. Extensive experiments and analysis on a unified benchmark comprising eight diverse datasets across seven modalities demonstrate the significant superiority of our jointly trained approach, compared to universe- or single-model approaches. Remarkably, our unified model demonstrates strong generalization, achieving impressive results not only on zero-shot tasks involving unseen cases but also in cross-modal transfers across similar tasks. Code is available at: this https URL
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
