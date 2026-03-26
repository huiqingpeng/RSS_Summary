---
title: "Circuit Complexity of Hierarchical Knowledge Tracing and Implications for Log-Precision Transformers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23823"
published: "2026-03-26"
fetched: "2026-03-27T07:17:33.806946"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Circuit Complexity of Hierarchical Knowledge Tracing and Implications for Log-Precision Transformers
View PDF HTML (experimental)Abstract:Knowledge tracing models mastery over interconnected concepts, often organized by prerequisites. We analyze hierarchical prerequisite propagation through a circuit-complexity lens to clarify what is provable about transformer-style computation on deep concept hierarchies. Using recent results that log-precision transformers lie in logspace-uniform $\mathsf{TC}^0$, we formalize prerequisite-tree tasks including recursive-majority mastery propagation. Unconditionally, recursive-majority propagation lies in $\mathsf{NC}^1$ via $O(\log n)$-depth bounded-fanin circuits, while separating it from uniform $\mathsf{TC}^0$ would require major progress on open lower bounds. Under a monotonicity restriction, we obtain an unconditional barrier: alternating ALL/ANY prerequisite trees yield a strict depth hierarchy for \emph{monotone} threshold circuits. Empirically, transformer encoders trained on recursive-majority trees converge to permutation-invariant shortcuts; explicit structure alone does not prevent this, but auxiliary supervision on intermediate subtrees elicits structure-dependent computation and achieves near-perfect accuracy at depths 3--4. These findings motivate structure-aware objectives and iterative mechanisms for prerequisite-sensitive knowledge tracing on deep hierarchies.
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
