---
title: "COMPASS-Hedge: Learning Safely Without Knowing the World"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22348"
published: "2026-03-25"
fetched: "2026-03-26T07:13:05.437684"
---

Computer Science > Machine Learning
[Submitted on 22 Mar 2026]
Title:COMPASS-Hedge: Learning Safely Without Knowing the World
View PDF HTML (experimental)Abstract:Online learning algorithms often faces a fundamental trilemma: balancing regret guarantees between adversarial and stochastic settings and providing baseline safety against a fixed comparator. While existing methods excel in one or two of these regimes, they typically fail to unify all three without sacrificing optimal rates or requiring oracle access to problem-dependent parameters.
In this work, we bridge this gap by introducing COMPASS-Hedge. Our algorithm is the first full-information method to simultaneously achieve: i) Minimax-optimal regret in adversarial environments; ii) Instance-optimal, gap-dependent regret in stochastic environments; and iii) $\tilde{\mathcal{O}}(1)$ regret relative to a designated baseline policy, up to logarithmic factors.
Crucially, COMPASS-Hedge is parameter-free and requires no prior knowledge of the environment's nature or the magnitude of the stochastic sub optimality gaps. Our approach hinges on a novel integration of adaptive pseudo-regret scaling and phase-based aggression, coupled with a comparator-aware mixing strategy. To the best of our knowledge, this provides the first "best-of-three-world" guarantee in the full-information setting, establishing that baseline safety does not have to come at the cost of worst-case robustness or stochastic efficiency.
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
