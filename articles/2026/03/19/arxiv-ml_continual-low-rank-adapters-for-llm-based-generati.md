---
title: "Continual Low-Rank Adapters for LLM-based Generative Recommender Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.25093"
published: "2026-03-19"
fetched: "2026-03-19T14:08:22.964246"
---

Computer Science > Machine Learning
[Submitted on 29 Oct 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Continual Low-Rank Adapters for LLM-based Generative Recommender Systems
View PDF HTML (experimental)Abstract:While large language models (LLMs) achieve strong performance in recommendation, they face challenges in continual learning as users, items, and user preferences evolve over time. Existing LoRA-based continual methods primarily focus on preserving performance on previous tasks, but this overlooks the unique nature of recommendation: the goal is not to predict past preferences, and outdated preferences can even harm performance when current interests shift significantly. To address this, we propose PESO (Proximally rEgularized Single evolving lOra, a continual adaptation method for LoRA in recommendation. PESO introduces a proximal regularizer that anchors the current adapter to its most recent frozen state, enabling the model to flexibly balance adaptation and preservation, and to better capture recent user behaviors. Theoretically, we show that this proximal design provides data-aware, direction-wise guidance in the LoRA subspace. Empirically, PESO consistently outperforms existing LoRA-based continual learning methods.
Submission history
From: Hyunsik Yoo [view email][v1] Wed, 29 Oct 2025 01:57:38 UTC (564 KB)
[v2] Sun, 8 Mar 2026 22:04:58 UTC (567 KB)
[v3] Tue, 17 Mar 2026 19:55:42 UTC (567 KB)
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
