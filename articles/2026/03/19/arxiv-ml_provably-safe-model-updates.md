---
title: "Provably Safe Model Updates"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.01899"
published: "2026-03-19"
fetched: "2026-03-19T14:10:00.016990"
---

Computer Science > Machine Learning
[Submitted on 1 Dec 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Provably Safe Model Updates
View PDF HTML (experimental)Abstract:Safety-critical environments are inherently dynamic. Distribution shifts, emerging vulnerabilities, and evolving requirements demand continuous updates to machine learning models. Yet even benign parameter updates can have unintended consequences, such as catastrophic forgetting in classical models or alignment drift in foundation models. Existing heuristic approaches (e.g., regularization, parameter isolation) can mitigate these effects but cannot certify that updated models continue to satisfy required performance specifications. We address this problem by introducing a framework for provably safe model updates. Our approach first formalizes the problem as computing the largest locally invariant domain (LID): a connected region in parameter space where all points are certified to satisfy a given specification. While exact maximal LID computation is intractable, we show that relaxing the problem to parameterized abstract domains (orthotopes, zonotopes) yields a tractable primal-dual formulation. This enables efficient certification of updates - independent of the data or algorithm used - by projecting them onto the safe domain. Our formulation further allows computation of multiple approximately optimal LIDs, incorporation of regularization-inspired biases, and use of lookahead data buffers. Across continual learning and foundation model fine-tuning benchmarks, our method matches or exceeds heuristic baselines for avoiding forgetting while providing formal safety guarantees.
Submission history
From: Leo Elmecker-Plakolm [view email][v1] Mon, 1 Dec 2025 17:19:53 UTC (735 KB)
[v2] Wed, 18 Mar 2026 17:29:55 UTC (736 KB)
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
