---
title: "Computing Pure-Strategy Nash Equilibria in a Two-Party Policy Competition: Existence and Algorithmic Approaches"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.22552"
published: "2026-03-18"
fetched: "2026-03-18T17:13:23.371334"
---

Computer Science > Computer Science and Game Theory
[Submitted on 27 Dec 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Computing Pure-Strategy Nash Equilibria in a Two-Party Policy Competition: Existence and Algorithmic Approaches
View PDF HTML (experimental)Abstract:We formulate two-party policy competition as a two-player non-cooperative game, generalizing Lin et al.'s work (2021). Each party selects a real-valued policy vector as its strategy from a compact subset of Euclidean space, and a voter's utility for a policy is given by the inner product with their preference vector. To capture the uncertainty in the competition, we assume that a policy's winning probability increases monotonically with its total utility across all voters, and we formalize this via an affine isotonic function. A player's payoff is defined as the expected utility received by its supporters. In this work, we first test and validate the isotonicity hypothesis through voting simulations. Next, we prove the existence of a pure-strategy Nash equilibrium (PSNE) in both one- and multi-dimensional settings. Although we construct a counterexample demonstrating the game's non-monotonicity, our experiments show that a decentralized gradient-based algorithm typically converges rapidly to an approximate PSNE. Finally, we present a grid-based search algorithm that finds an $\epsilon$-approximate PSNE of the game in time polynomial in the input size and $1/\epsilon$.
Submission history
From: Chuang-Chieh Lin [view email][v1] Sat, 27 Dec 2025 10:44:32 UTC (1,879 KB)
[v2] Sun, 25 Jan 2026 08:05:11 UTC (1,879 KB)
[v3] Tue, 17 Mar 2026 09:02:34 UTC (1,879 KB)
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
