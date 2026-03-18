---
title: "Online Semi-infinite Linear Programming: Efficient Algorithms via Function Approximation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16200"
published: "2026-03-18"
fetched: "2026-03-18T15:41:44.213915"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Online Semi-infinite Linear Programming: Efficient Algorithms via Function Approximation
View PDF HTML (experimental)Abstract:We consider the dynamic resource allocation problem where the decision space is finite-dimensional, yet the solution must satisfy a large or even infinite number of constraints revealed via streaming data or oracle feedback. We model this challenge as an Online Semi-infinite Linear Programming (OSILP) problem and develop a novel LP formulation to solve it approximately. Specifically, we employ function approximation to reduce the number of constraints to a constant $q$. This addresses a key limitation of traditional online LP algorithms, whose regret bounds typically depend on the number of constraints, leading to poor performance in this setting. We propose a dual-based algorithm to solve our new formulation, which offers broad applicability through the selection of appropriate potential functions. We analyze this algorithm under two classical input models-stochastic input and random permutation-establishing regret bounds of $O(q\sqrt{T})$ and $O\left(\left(q+q\log{T})\sqrt{T}\right)\right)$ respectively. Note that both regret bounds are independent of the number of constraints, which demonstrates the potential of our approach to handle a large or infinite number of constraints. Furthermore, we investigate the potential to improve upon the $O(q\sqrt{T})$ regret and propose a two-stage algorithm, achieving $O(q\log{T} + q/\epsilon)$ regret under more stringent assumptions. We also extend our algorithms to the general function setting. A series of experiments validates that our algorithms outperform existing methods when confronted with a large number of constraints.
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
