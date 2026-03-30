---
title: "H-Node Attack and Defense in Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26045"
published: "2026-03-30"
fetched: "2026-03-31T07:21:02.914769"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:H-Node Attack and Defense in Large Language Models
View PDF HTML (experimental)Abstract:We present H-Node Adversarial Noise Cancellation (H-Node ANC), a mechanistic framework that identifies, exploits, and defends hallucination representations in transformer-based large language models (LLMs) at the level of individual hidden-state dimensions. A logistic regression probe trained on last-token hidden states localizes hallucination signal to a small set of high-variance dimensions -- termed Hallucination Nodes (H-Nodes) -- with probe AUC reaching 0.90 across four architectures. A white-box adversarial attack amplifies these dimensions at inference time via a real-time forward hook, achieving a selectivity of 3.02x with less than 10% visibility to the defender. Adaptive ANC defense suppresses H-Node excess in-pass using confidence-weighted cancellation, reducing grounded activation drift by 33-42% over static cancellation. A dynamic iterative extension that re-ranks cancellation targets across successive passes recovers up to 0.69 robustness from a single-pass baseline of 8%. All contributions are validated on OPT-125M, Phi-3-mini-4k-instruct, LLaMA-3-8B-Instruct, and Mistral-7B-Instruct-v0.3 (125M-8B parameters). Perplexity impact is surgical (<5%) and MMLU degradation is at most 3%, confirming that the defense does not impair general reasoning capability.
Current browse context:
cs.LG
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
