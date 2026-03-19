---
title: "HoloByte: Continuous Hyperspherical Distillation for Tokenizer-Free Modeling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16917"
published: "2026-03-19"
fetched: "2026-03-19T12:05:30.271854"
---

Computer Science > Machine Learning
[Submitted on 10 Mar 2026]
Title:HoloByte: Continuous Hyperspherical Distillation for Tokenizer-Free Modeling
View PDF HTML (experimental)Abstract:Sequence modeling universally relies on discrete subword tokenization to circumvent the $\mathcal{O}(N^2)$ computational intractability of native byte-level attention. However, this heuristic quantization imposes artificial morphological boundaries, enforces vocabulary dependence, and fractures the continuity of the optimization landscape. To resolve this dichotomy, we introduce \textbf{HoloByte}: a strictly tokenizer-free framework utilizing Continuous Hyperspherical Distillation. HoloByte partitions discrete byte sequences into fixed-capacity chunks and projects them into a continuous, strictly bounded hyperspherical manifold via an invertible, dimension-preserving orthogonal rotation operator. This spatial superposition allows a macroscopic transformer to operate exclusively on compressed continuous representations, formally reducing the exact attention time complexity from $\mathcal{O}(N^2D)$ to $\mathcal{O}\left( \frac{N^2}{W^2}D + ND^2 \right)$. A localized causal micro-decoder subsequently unbinds these representations to compute exact byte-level distributions. To govern this continuous trajectory, we propose a dual-objective formulation incorporating a mathematically precise Holographic Latent Mean Squared Error, which strictly bounds the gradient and guarantees asymptotic stability. Theoretically, we derive the minimal embedding dimension $D = \Omega(W \ln |\mathcal{V}|)$ required to ensure error-free discrete recovery from the continuous manifold. Empirically, under strictly matched parameter constraints, HoloByte is systematically outperforming a comparable discrete Byte-Pair Encoding (BPE) baseline. These results establish Continuous Hyperspherical Distillation as a mathematically rigorous and computationally tractable foundation for vocabulary-invariant sequence modeling. The code is available at this https URL
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
