---
title: "Spectral Edge Dynamics Reveal Functional Modes of Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06256"
published: "2026-04-09"
fetched: "2026-04-10T07:04:54.176541"
---

Computer Science > Machine Learning
[Submitted on 6 Apr 2026]
Title:Spectral Edge Dynamics Reveal Functional Modes of Learning
View PDF HTML (experimental)Abstract:Training dynamics during grokking concentrate along a small number of dominant update directions -- the spectral edge -- which reliably distinguishes grokking from non-grokking regimes. We show that standard mechanistic interpretability tools (head attribution, activation probing, sparse autoencoders) fail to capture these directions: their structure is not localized in parameter or feature space. Instead, each direction induces a structured function over the input domain, revealing low-dimensional functional modes invisible to representation-level analysis.
For modular addition, all leading directions collapse to a single Fourier mode. For multiplication, the same collapse appears only in the discrete-log basis, yielding a 5.9x improvement in concentration. For subtraction, the edge spans a small multi-mode family. For $x^2+y^2$, no single harmonic basis suffices, but cross-terms of additive and multiplicative features provide a 4x variance boost, consistent with the decomposition (a+b)^2 - 2ab. Multitask training amplifies this compositional structure, with the $x^2+y^2$ spectral edge inheriting the addition circuit's characteristic frequency (2.3x concentration increase).
These results suggest that training discovers low-dimensional functional modes over the input domain, whose structure depends on the algebraic symmetry of the task.
These results suggest that spectral edge dynamics identify low-dimensional functional subspaces governing learning, whose representation depends on the algebraic structure of the task. Simple harmonic structure emerges only when the task admits a symmetry-adapted basis; more complex tasks require richer functional descriptions.
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
