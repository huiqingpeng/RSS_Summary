---
title: "Gradient-Based Data Valuation Improves Curriculum Learning for Game-Theoretic Motion Planning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00388"
published: "2026-04-02"
fetched: "2026-04-03T07:21:01.631650"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Gradient-Based Data Valuation Improves Curriculum Learning for Game-Theoretic Motion Planning
View PDF HTML (experimental)Abstract:We demonstrate that gradient-based data valuation produces curriculum orderings that significantly outperform metadata-based heuristics for training game-theoretic motion planners. Specifically, we apply TracIn gradient-similarity scoring to GameFormer on the nuPlan benchmark and construct a curriculum that weights training scenarios by their estimated contribution to validation loss reduction. Across three random seeds, the TracIn-weighted curriculum achieves a mean planning ADE of $1.704\pm0.029$\,m, significantly outperforming the metadata-based interaction-difficulty curriculum ($1.822\pm0.014$\,m; paired $t$-test $p=0.021$, Cohen's $d_z=3.88$) while exhibiting lower variance than the uniform baseline ($1.772\pm0.134$\,m). Our analysis reveals that TracIn scores and scenario metadata are nearly orthogonal (Spearman $\rho=-0.014$), indicating that gradient-based valuation captures training dynamics invisible to hand-crafted features. We further show that gradient-based curriculum weighting succeeds where hard data selection fails: TracIn-curated 20\% subsets degrade performance by $2\times$, whereas full-data curriculum weighting with the same scores yields the best results. These findings establish gradient-based data valuation as a practical tool for improving sample efficiency in game-theoretic planning.
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
