---
title: "A Decoupled Basis-Vector-Driven Generative Framework for Dynamic Multi-Objective Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00508"
published: "2026-04-02"
fetched: "2026-04-03T07:22:02.987242"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:A Decoupled Basis-Vector-Driven Generative Framework for Dynamic Multi-Objective Optimization
View PDF HTML (experimental)Abstract:Dynamic multi-objective optimization requires continuous tracking of moving Pareto fronts. Existing methods struggle with irregular mutations and data sparsity, primarily facing three challenges: the non-linear coupling of dynamic modes, negative transfer from outdated historical data, and the cold-start problem during environmental switches. To address these issues, this paper proposes a decoupled basis-vector-driven generative framework (DB-GEN). First, to resolve non-linear coupling, the framework employs the discrete wavelet transform to separate evolutionary trajectories into low-frequency trends and high-frequency details. Second, to mitigate negative transfer, it learns transferable basis vectors via sparse dictionary learning rather than directly memorizing historical instances. Recomposing these bases under a topology-aware contrastive constraint constructs a structured latent manifold. Finally, to overcome the cold-start problem, a surrogate-assisted search paradigm samples initial populations from this manifold. Pre-trained on 120 million solutions, DB-GEN performs direct online inference without retraining or fine-tuning. This zero-shot generation process executes in milliseconds, requiring approximately 0.2 seconds per environmental change. Experimental results demonstrate that DB-GEN improves tracking accuracy across various dynamic benchmarks compared to existing algorithms.
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
