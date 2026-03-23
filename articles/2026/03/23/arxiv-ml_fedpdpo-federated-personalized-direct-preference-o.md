---
title: "FedPDPO: Federated Personalized Direct Preference Optimization for Large Language Model Alignment"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19741"
published: "2026-03-23"
fetched: "2026-03-24T07:21:46.753657"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:FedPDPO: Federated Personalized Direct Preference Optimization for Large Language Model Alignment
View PDF HTML (experimental)Abstract:Aligning large language models (LLMs) with human preferences in federated learning (FL) is challenging due to decentralized, privacy-sensitive, and highly non-IID preference data. Direct Preference Optimization (DPO) offers an efficient alternative to reinforcement learning with human feedback (RLHF), but its direct application in FL suffers from severe performance degradation under non-IID data and limited generalization of implicit rewards. To bridge this gap, we propose FedPDPO (Federated Personalized Direct Preference Optimization), a personalized federated framework for preference alignment of LLMs. It adopts a parameter-efficient fine-tuning architecture where each client maintains a frozen pretrained LLM backbone augmented with a Low-Rank Adaptation (LoRA) adapter, enabling communication-efficient aggregation. To address non-IID heterogeneity, we devise (1) the globally shared LoRA adapter with the personalized client-specific LLM head. Moreover, we introduce (2) a personalized DPO training strategy with a client-specific explicit reward head to complement implicit rewards and further alleviate non-IID heterogeneity, and (3) a bottleneck adapter to balance global and local features. We provide theoretical analysis establishing the probabilistic foundation and soundness. Extensive experiments on multiple preference datasets demonstrate state-of-the-art performance, achieving up to 4.80% average accuracy improvements in federated intra-domain and cross-domain settings.
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
