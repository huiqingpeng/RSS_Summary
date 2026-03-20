---
title: "MedQ-UNI: Toward Unified Medical Image Quality Assessment and Restoration via Vision-Language Modeling"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18465"
published: "2026-03-20"
fetched: "2026-03-20T15:09:29.234826"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:MedQ-UNI: Toward Unified Medical Image Quality Assessment and Restoration via Vision-Language Modeling
View PDF HTML (experimental)Abstract:Existing medical image restoration (Med-IR) methods are typically modality-specific or degradation-specific, failing to generalize across the heterogeneous degradations encountered in clinical practice. We argue this limitation stems from the isolation of Med-IR from medical image quality assessment (Med-IQA), as restoration models without explicit quality understanding struggle to adapt to diverse degradation types across modalities. To address these challenges, we propose MedQ-UNI, a unified vision-language model that follows an assess-then-restore paradigm, explicitly leveraging Med-IQA to guide Med-IR across arbitrary modalities and degradation types. MedQ-UNI adopts a multimodal autoregressive dual-expert architecture with shared attention: a quality assessment expert first identifies degradation issues through structured natural language descriptions, and a restoration expert then conditions on these descriptions to perform targeted image restoration. To support this paradigm, we construct a large-scale dataset of approximately 50K paired samples spanning three imaging modalities and five restoration tasks, each annotated with structured quality descriptions for joint Med-IQA and Med-IR training, along with a 2K-sample benchmark for evaluation. Extensive experiments demonstrate that a single MedQ-UNI model, without any task-specific adaptation, achieves state-of-the-art restoration performance across all tasks while generating superior descriptions, confirming that explicit quality understanding meaningfully improves restoration fidelity and interpretability.
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
