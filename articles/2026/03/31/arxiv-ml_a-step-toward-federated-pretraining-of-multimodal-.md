---
title: "A Step Toward Federated Pretraining of Multimodal Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26786"
published: "2026-03-31"
fetched: "2026-04-01T07:18:03.997425"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:A Step Toward Federated Pretraining of Multimodal Large Language Models
View PDF HTML (experimental)Abstract:The rapid evolution of Multimodal Large Language Models (MLLMs) is bottlenecked by the saturation of high-quality public data, while vast amounts of diverse multimodal data remain inaccessible in privacy-sensitive silos. Federated Learning (FL) offers a promising solution to unlock these distributed resources, but existing research focuses predominantly on fine-tuning, leaving the foundational pre-training phase largely unexplored. In this paper, we formally introduce the Federated MLLM Alignment (Fed-MA) task, a lightweight pre-training paradigm that freezes the vision encoder and LLM while collaboratively training the cross-modal projector. We identify two critical challenges in this setting: (i) parameter interference in aggregating local projectors; and (ii) gradient oscillations in one-pass collaborative SGD. To address these challenges, we propose Fed-CMP, a pioneering framework for federated MLLM pre-training. Fed-CMP employs Canonical Reliability-Aware Aggregation, which constructs a canonical space to decompose client projectors into a shared alignment basis and client-specific coefficients, then performs reliability-weighted fusion to suppress parameter interference. Furthermore, Fed-CMP introduces Orthogonality-Preserved Momentum, which applies momentum to the shared alignment basis via orthogonal projection, accumulating historical optimization directions while preserving geometric structure. We construct four federated pre-training scenarios based on public datasets, and extensive experiments validate that Fed-CMP significantly outperforms existing baselines.
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
