---
title: "Adaptive Domain Models: Bayesian Evolution, Warm Rotation, and Principled Training for Geometric and Neuromorphic AI"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18104"
published: "2026-03-20"
fetched: "2026-03-20T13:09:00.519028"
---

Computer Science > Artificial Intelligence
[Submitted on 18 Mar 2026]
Title:Adaptive Domain Models: Bayesian Evolution, Warm Rotation, and Principled Training for Geometric and Neuromorphic AI
View PDF HTML (experimental)Abstract:Prevailing AI training infrastructure assumes reverse-mode automatic differentiation over IEEE-754 arithmetic. The memory overhead of training relative to inference, optimizer complexity, and structural degradation of geometric properties through training are consequences of this arithmetic substrate. This paper develops an alternative training architecture grounded in three prior results: the Dimensional Type System and Deterministic Memory Management framework [6], which establishes stack-eligible gradient allocation and exact quire accumulation as design-time verifiable properties; the Program Hypergraph [8], which establishes grade preservation through geometric algebra computations as a type-level invariant; and the b-posit 2026 standard [10], which makes posit arithmetic tractable across hardware targets conventionally considered inference-only. Their composition enables depth-independent training memory bounded to approximately twice the inference footprint, grade-preserving weight updates, and exact gradient accumulation, applicable uniformly to loss-function-optimized and spike-timing-dependent neuromorphic models. We introduce Bayesian distillation, a mechanism by which the latent prior structure of a general-purpose model is extracted through the ADM training regime, resolving the data-scarcity bootstrapping problem for domain-specific training. For deployment, we introduce warm rotation, an operational pattern in which an updated model transitions into an active inference pathway without service interruption, with structural correctness formalized through PHG certificates and signed version records. The result is a class of domain-specific AI systems that are smaller and more precise than general-purpose models, continuously adaptive, verifiably correct with respect to the physical structure of their domains, and initializable from existing models.
Current browse context:
cs.AI
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
