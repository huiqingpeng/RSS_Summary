---
title: "Joint Value Estimation and Bidding in Repeated First-Price Auctions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2502.17292"
published: "2026-03-19"
fetched: "2026-03-19T13:18:44.456660"
---

Computer Science > Machine Learning
[Submitted on 24 Feb 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Joint Value Estimation and Bidding in Repeated First-Price Auctions
View PDF HTML (experimental)Abstract:We study regret minimization in repeated first-price auctions (FPAs), where a bidder observes only the realized outcome after each auction -- win or loss. This setup reflects practical scenarios in online display advertising where the actual value of an impression depends on the difference between two potential outcomes, such as clicks or conversion rates, when the auction is won versus lost. We incorporate causal inference into this framework and analyze the challenging case where only the treatment effect admits a simple dependence on observable features. Under this framework, we propose algorithms that jointly estimate private values and optimize bidding strategies under two different feedback types on the highest other bid (HOB): the full-information feedback where the HOB is always revealed, and the binary feedback where the bidder only observes the win-loss indicator. Under both cases, our algorithms are shown to achieve near-optimal regret bounds. Notably, our framework enjoys a unique feature that the treatments are actively chosen, and hence eliminates the need for the overlap condition commonly required in causal inference.
Submission history
From: Yuxiao Wen [view email][v1] Mon, 24 Feb 2025 16:21:50 UTC (114 KB)
[v2] Sun, 28 Sep 2025 22:07:44 UTC (114 KB)
[v3] Tue, 17 Mar 2026 21:24:05 UTC (500 KB)
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
