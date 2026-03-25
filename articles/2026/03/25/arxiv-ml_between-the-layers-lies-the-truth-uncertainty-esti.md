---
title: "Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22299"
published: "2026-03-25"
fetched: "2026-03-26T07:08:31.047090"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores
View PDF HTML (experimental)Abstract:Large language models (LLMs) are often confidently wrong, making reliable uncertainty estimation (UE) essential. Output-based heuristics are cheap but brittle, while probing internal representations is effective yet high-dimensional and hard to transfer.
We propose a compact, per-instance UE method that scores cross-layer agreement patterns in internal representations using a single forward pass.
Across three models, our method matches probing in-distribution, with mean diagonal differences of at most $-1.8$ AUPRC percentage points and $+4.9$ Brier score points. Under cross-dataset transfer, it consistently outperforms probing, achieving off-diagonal gains up to $+2.86$ AUPRC and $+21.02$ Brier points. Under 4-bit weight-only quantization, it remains robust, improving over probing by $+1.94$ AUPRC points and $+5.33$ Brier points on average.
Beyond performance, examining specific layer--layer interactions reveals differences in how disparate models encode uncertainty. Altogether, our UE method offers a lightweight, compact means to capture transferable uncertainty in LLMs.
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
