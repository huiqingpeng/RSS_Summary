---
title: "Revisiting the Last-Iterate Convergence of Stochastic Gradient Methods"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2312.08531"
published: "2026-03-20"
fetched: "2026-03-20T14:03:57.433205"
---

Computer Science > Machine Learning
[Submitted on 13 Dec 2023 (v1), last revised 19 Mar 2026 (this version, v4)]
Title:Revisiting the Last-Iterate Convergence of Stochastic Gradient Methods
View PDF HTML (experimental)Abstract:In the past several years, the last-iterate convergence of the Stochastic Gradient Descent (SGD) algorithm has triggered people's interest due to its good performance in practice but lack of theoretical understanding. For Lipschitz convex functions, different works have established the optimal $O(\log(1/\delta)\log T/\sqrt{T})$ or $O(\sqrt{\log(1/\delta)/T})$ high-probability convergence rates for the final iterate, where T is the time horizon and \delta is the failure probability. However, to prove these bounds, all the existing works are either limited to compact domains or require almost surely bounded noise. It is natural to ask whether the last iterate of SGD can still guarantee the optimal convergence rate but without these two restrictive assumptions. Besides this important question, there are still lots of theoretical problems lacking an answer. For example, compared with the last-iterate convergence of SGD for non-smooth problems, only few results for smooth optimization have yet been developed. Additionally, the existing results are all limited to a non-composite objective and the standard Euclidean norm. It still remains unclear whether the last-iterate convergence can be provably extended to wider composite optimization and non-Euclidean norms. In this work, to address the issues mentioned above, we revisit the last-iterate convergence of stochastic gradient methods and provide the first unified way to prove the convergence rates both in expectation and in high probability to accommodate general domains, composite objectives, non-Euclidean norms, Lipschitz conditions, smoothness, and (strong) convexity simultaneously. Additionally, we extend our analysis to obtain the last-iterate convergence under heavy-tailed and sub-Weibull noise.
Submission history
From: Zijian Liu [view email][v1] Wed, 13 Dec 2023 21:41:06 UTC (58 KB)
[v2] Tue, 12 Mar 2024 03:53:46 UTC (58 KB)
[v3] Mon, 29 Dec 2025 04:05:49 UTC (45 KB)
[v4] Thu, 19 Mar 2026 15:40:13 UTC (46 KB)
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
