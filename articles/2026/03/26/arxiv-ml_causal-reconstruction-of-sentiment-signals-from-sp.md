---
title: "Causal Reconstruction of Sentiment Signals from Sparse News Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23568"
published: "2026-03-26"
fetched: "2026-03-27T07:14:44.448573"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Causal Reconstruction of Sentiment Signals from Sparse News Data
View PDF HTML (experimental)Abstract:Sentiment signals derived from sparse news are commonly used in financial analysis and technology monitoring, yet transforming raw article-level observations into reliable temporal series remains a largely unsolved engineering problem. Rather than treating this as a classification challenge, we propose to frame it as a causal signal reconstruction problem: given probabilistic sentiment outputs from a fixed classifier, recover a stable latent sentiment series that is robust to the structural pathologies of news data such as sparsity, redundancy, and classifier uncertainty. We present a modular three-stage pipeline that (i) aggregates article-level scores onto a regular temporal grid with uncertainty-aware and redundancy-aware weights, (ii) fills coverage gaps through strictly causal projection rules, and (iii) applies causal smoothing to reduce residual noise. Because ground-truth longitudinal sentiment labels are typically unavailable, we introduce a label-free evaluation framework based on signal stability diagnostics, information preservation lag proxies, and counterfactual tests for causality compliance and redundancy robustness. As a secondary external check, we evaluate the consistency of reconstructed signals against stock-price data for a multi-firm dataset of AI-related news titles (November 2024 to February 2026). The key empirical finding is a three-week lead lag pattern between reconstructed sentiment and price that persists across all tested pipeline configurations and aggregation regimes, a structural regularity more informative than any single correlation coefficient. Overall, the results support the view that stable, deployable sentiment indicators require careful reconstruction, not only better classifiers.
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
