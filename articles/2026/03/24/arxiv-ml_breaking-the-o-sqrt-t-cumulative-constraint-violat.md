---
title: "Breaking the $O(\sqrt{T})$ Cumulative Constraint Violation Barrier while Achieving $O(\sqrt{T})$ Static Regret in Constrained Online Convex Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20671"
published: "2026-03-24"
fetched: "2026-03-25T07:13:04.986962"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Breaking the $O(\sqrt{T})$ Cumulative Constraint Violation Barrier while Achieving $O(\sqrt{T})$ Static Regret in Constrained Online Convex Optimization
View PDFAbstract:The problem of constrained online convex optimization is considered, where at each round, once a learner commits to an action $x_t \in \mathcal{X} \subset \mathbb{R}^d$, a convex loss function $f_t$ and a convex constraint function $g_t$ that drives the constraint $g_t(x)\le 0$ are revealed. The objective is to simultaneously minimize the static regret and cumulative constraint violation (CCV) compared to the benchmark that knows the loss functions and constraint functions $f_t$ and $g_t$ for all $t$ ahead of time, and chooses a static optimal action that is feasible with respect to all $g_t(x)\le 0$. In recent prior work Sinha and Vaze [2024], algorithms with simultaneous regret of $O(\sqrt{T})$ and CCV of $O(\sqrt{T})$ or (CCV of $O(1)$ in specific cases Vaze and Sinha [2025], e.g. when $d=1$) have been proposed. It is widely believed that CCV is $\Omega(\sqrt{T})$ for all algorithms that ensure that regret is $O(\sqrt{T})$ with the worst case input for any $d\ge 2$. In this paper, we refute this and show that the algorithm of Vaze and Sinha [2025] simultaneously achieves regret of $O(\sqrt{T})$ regret and CCV of $O(T^{1/3})$ when $d=2$.
Submission history
From: Haricharan Balasundaram [view email][v1] Sat, 21 Mar 2026 06:19:35 UTC (17 KB)
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
