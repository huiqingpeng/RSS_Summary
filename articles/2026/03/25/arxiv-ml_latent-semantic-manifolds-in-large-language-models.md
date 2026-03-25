---
title: "Latent Semantic Manifolds in Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22301"
published: "2026-03-25"
fetched: "2026-03-26T07:08:43.489036"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Latent Semantic Manifolds in Large Language Models
View PDF HTML (experimental)Abstract:Large Language Models (LLMs) perform internal computations in continuous vector spaces yet produce discrete tokens -- a fundamental mismatch whose geometric consequences remain poorly understood. We develop a mathematical framework that interprets LLM hidden states as points on a latent semantic manifold: a Riemannian submanifold equipped with the Fisher information metric, where tokens correspond to Voronoi regions partitioning the manifold. We define the expressibility gap, a geometric measure of the semantic distortion from vocabulary discretization, and prove two theorems: a rate-distortion lower bound on distortion for any finite vocabulary, and a linear volume scaling law for the expressibility gap via the coarea formula. We validate these predictions across six transformer architectures (124M-1.5B parameters), confirming universal hourglass intrinsic dimension profiles, smooth curvature structure, and linear gap scaling with slopes 0.87-1.12 (R^2 > 0.985). The margin distribution across models reveals a persistent hard core of boundary-proximal representations invariant to scale, providing a geometric decomposition of perplexity. We discuss implications for architecture design, model compression, decoding strategies, and scaling laws
Submission history
From: Mohamed A. Mabrok [view email][v1] Tue, 17 Mar 2026 13:05:56 UTC (1,175 KB)
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
