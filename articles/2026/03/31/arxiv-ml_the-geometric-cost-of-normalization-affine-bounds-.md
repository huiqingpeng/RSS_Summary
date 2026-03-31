---
title: "The Geometric Cost of Normalization: Affine Bounds on the Bayesian Complexity of Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27432"
published: "2026-03-31"
fetched: "2026-04-01T07:23:59.902067"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:The Geometric Cost of Normalization: Affine Bounds on the Bayesian Complexity of Neural Networks
View PDF HTML (experimental)Abstract:LayerNorm and RMSNorm impose fundamentally different geometric constraints on their outputs - and this difference has a precise, quantifiable consequence for model complexity. We prove that LayerNorm's mean-centering step, by confining data to a linear hyperplane (through the origin), reduces the Local Learning Coefficient (LLC) of the subsequent weight matrix by exactly $m/2$ (where $m$ is its output dimension); RMSNorm's projection onto a sphere preserves the LLC entirely. This reduction is structurally guaranteed before any training begins, determined by data manifold geometry alone.
The underlying condition is a geometric threshold: for the codimension-one manifolds we study, the LLC drop is binary -- any non-zero curvature, regardless of sign or magnitude, is sufficient to preserve the LLC, while only affinely flat manifolds cause the drop. At finite sample sizes this threshold acquires a smooth crossover whose width depends on how much of the data distribution actually experiences the curvature, not merely on whether curvature exists somewhere.
We verify both predictions experimentally with controlled single-layer scaling experiments using the wrLLC framework. We further show that Softmax simplex data introduces a "smuggled bias" that activates the same $m/2$ LLC drop when paired with an explicit downstream bias, proved via the affine symmetry extension of the main theorem and confirmed empirically.
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
