---
title: "Forest-Chat: Adapting Vision-Language Agents for Interactive Forest Change Analysis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.14637"
published: "2026-03-20"
fetched: "2026-03-20T16:17:14.748560"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 21 Jan 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Forest-Chat: Adapting Vision-Language Agents for Interactive Forest Change Analysis
View PDF HTML (experimental)Abstract:The increasing availability of high-resolution satellite imagery, together with advances in deep learning, creates new opportunities for forest monitoring workflows. Two central challenges in this domain are pixel-level change detection and semantic change interpretation, particularly for complex forest dynamics. While large language models (LLMs) are increasingly adopted for data exploration, their integration with vision-language models (VLMs) for remote sensing image change interpretation (RSICI) remains underexplored, especially beyond urban environments. This paper introduces Forest-Chat, an LLM-driven agent for forest change analysis, enabling natural language querying across multiple RSICI tasks, including change detection and captioning, object counting, deforestation characterisation, and change reasoning. Forest-Chat builds upon a multi-level change interpretation (MCI) vision-language backbone with LLM-based orchestration, incorporating zero-shot change detection via AnyChange and multimodal LLM-based zero-shot change captioning and refinement. To support adaptation and evaluation in forest environments, we introduce the Forest-Change dataset, comprising bi-temporal satellite imagery, pixel-level change masks, and semantic change captions via human annotation and rule-based methods. Forest-Chat achieves mIoU and BLEU-4 scores of 67.10% and 40.17% on Forest-Change, and 88.13% and 34.41% on LEVIR-MCI-Trees, a tree-focused subset of LEVIR-MCI. In a zero-shot capacity, it achieves 60.15% and 34.00% on Forest-Change, and 47.32% and 18.23% on LEVIR-MCI-Trees. Further experiments demonstrate the value of caption refinement for injecting geographic domain knowledge into supervised captions, and the system's limited label domain transfer onto JL1-CD-Trees. These findings demonstrate that interactive, LLM-driven systems can support accessible and interpretable forest change analysis.
Submission history
From: James Brock [view email][v1] Wed, 21 Jan 2026 04:23:33 UTC (21,658 KB)
[v2] Thu, 19 Mar 2026 04:16:46 UTC (12,883 KB)
Current browse context:
cs.CV
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
