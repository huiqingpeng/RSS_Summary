---
title: "Learning Permutation Distributions via Reflected Diffusion on Ranks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17353"
published: "2026-03-19"
fetched: "2026-03-19T12:09:59.762903"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Learning Permutation Distributions via Reflected Diffusion on Ranks
View PDF HTML (experimental)Abstract:The finite symmetric group S_n provides a natural domain for permutations, yet learning probability distributions on S_n is challenging due to its factorially growing size and discrete, non-Euclidean structure. Recent permutation diffusion methods define forward noising via shuffle-based random walks (e.g., riffle shuffles) and learn reverse transitions with Plackett-Luce (PL) variants, but the resulting trajectories can be abrupt and increasingly hard to denoise as n grows. We propose Soft-Rank Diffusion, a discrete diffusion framework that replaces shuffle-based corruption with a structured soft-rank forward process: we lift permutations to a continuous latent representation of order by relaxing discrete ranks into soft ranks, yielding smoother and more tractable trajectories. For the reverse process, we introduce contextualized generalized Plackett-Luce (cGPL) denoisers that generalize prior PL-style parameterizations and improve expressivity for sequential decision structures. Experiments on sorting and combinatorial optimization benchmarks show that Soft-Rank Diffusion consistently outperforms prior diffusion baselines, with particularly strong gains in long-sequence and intrinsically sequential settings.
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
