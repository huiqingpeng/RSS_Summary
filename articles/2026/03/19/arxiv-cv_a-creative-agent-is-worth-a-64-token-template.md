---
title: "A Creative Agent is Worth a 64-Token Template"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17895"
published: "2026-03-19"
fetched: "2026-03-19T16:18:05.781586"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:A Creative Agent is Worth a 64-Token Template
View PDF HTML (experimental)Abstract:Text-to-image (T2I) models have substantially improved image fidelity and prompt adherence, yet their creativity remains constrained by reliance on discrete natural language prompts. When presented with fuzzy prompts such as ``a creative vinyl record-inspired skyscraper'', these models often fail to infer the underlying creative intent, leaving creative ideation and prompt design largely to human users. Recent reasoning- or agent-driven approaches iteratively augment prompts but incur high computational and monetary costs, as their instance-specific generation makes ``creativity'' costly and non-reusable, requiring repeated queries or reasoning for subsequent generations. To address this, we introduce \textbf{CAT}, a framework for \textbf{C}reative \textbf{A}gent \textbf{T}okenization that encapsulates agents' intrinsic understanding of ``creativity'' through a \textit{Creative Tokenizer}. Given the embeddings of fuzzy prompts, the tokenizer generates a reusable token template that can be directly concatenated with them to inject creative semantics into T2I models without repeated reasoning or prompt augmentation. To enable this, the tokenizer is trained via creative semantic disentanglement, leveraging relations among partially overlapping concept pairs to capture the agent's latent creative representations. Extensive experiments on \textbf{\textit{Architecture Design}}, \textbf{\textit{Furniture Design}}, and \textbf{\textit{Nature Mixture}} tasks demonstrate that CAT provides a scalable and effective paradigm for enhancing creativity in T2I generation, achieving a $3.7\times$ speedup and a $4.8\times$ reduction in computational cost, while producing images with superior human preference and text-image alignment compared to state-of-the-art T2I models and creative generation methods.
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
