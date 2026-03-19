---
title: "Beyond Muon: MUD (MomentUm Decorrelation) for Faster Transformer Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17970"
published: "2026-03-19"
fetched: "2026-03-19T12:18:35.888209"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Beyond Muon: MUD (MomentUm Decorrelation) for Faster Transformer Training
View PDF HTML (experimental)Abstract:Orthogonalized-momentum optimizers such as Muon improve transformer training by approximately whitening/orthogonalizing matrix-valued momentum updates via a short polar-decomposition iteration. However, polar-factor approximations typically require multiple large matrix multiplications, and the resulting overhead can be substantial and hardware-dependent. We introduce MUD (MomentUm Decorrelation), a complementary whitening approach that replaces Muon's polar update with a triangular (Cholesky-like) whitening surrogate inspired by classical Gram--Schmidt and Gauss-Seidel ideas. We show that row-orthonormal matrices are fixed points of the MUD map, relate the inner step to symmetric Gauss-Seidel preconditioning of the Gram matrix, and prove quadratic local convergence near the fixed point. In terms of time-to-perplexity, MUD yields consistent 10-50\% wall-clock improvements over tuned AdamW and Muon in time-to-perplexity, typically converging slightly slower per step than Muon but with substantially lower optimizer overhead -- relative to Muon, MUD improves peak tokens/s by roughly $1.3-2.6\times$ across most settings and up to nearly $3\times$ on GPT-2 large on an A100. We also demonstrate training a ESM-2 150M protein language model, where MUD matches Muon-level validation perplexity in significantly less wall-clock time.
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
