---
title: "Splines-Based Feature Importance in Kolmogorov-Arnold Networks: A Framework for Supervised Tabular Data Dimensionality Reduction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.23366"
published: "2026-03-20"
fetched: "2026-03-20T14:07:59.052924"
---

Computer Science > Machine Learning
[Submitted on 27 Sep 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:Splines-Based Feature Importance in Kolmogorov-Arnold Networks: A Framework for Supervised Tabular Data Dimensionality Reduction
View PDF HTML (experimental)Abstract:Feature selection is a key step in many tabular prediction problems, where multiple candidate variables may be redundant, noisy, or weakly informative. We investigate feature selection based on Kolmogorov-Arnold Networks (KANs), which parameterize feature transformations with splines and expose per-feature importance scores in a natural way. From this idea we derive four KAN-based selection criteria (coefficient norms, gradient-based saliency, and knockout scores) and compare them with standard methods such as LASSO, Random Forest feature importance, Mutual Information, and SVM-RFE on a suite of real and synthetic classification and regression datasets. Using average F1 and $R^2$ scores across three feature-retention levels (20%, 40%, 60%), we find that KAN-based selectors are generally competitive with, and sometimes superior to, classical baselines. In classification, KAN criteria often match or exceed existing methods on multi-class tasks by removing redundant features and capturing nonlinear interactions. In regression, KAN-based scores provide robust performance on noisy and heterogeneous datasets, closely tracking strong ensemble predictors; we also observe characteristic failure modes, such as overly aggressive pruning with an $\ell_1$ criterion. Stability and redundancy analyses further show that KAN-based selectors yield reproducible feature subsets across folds while avoiding unnecessary correlation inflation, ensuring reliable and non-redundant variable selection. Overall, our findings demonstrate that KAN-based feature selection provides a powerful and interpretable alternative to traditional methods, capable of uncovering nonlinear and multivariate feature relevance beyond sparsity or impurity-based measures.
Submission history
From: Ange-Clément Akazan [view email][v1] Sat, 27 Sep 2025 15:24:17 UTC (1,352 KB)
[v2] Fri, 21 Nov 2025 12:53:21 UTC (4,047 KB)
[v3] Thu, 19 Mar 2026 16:47:13 UTC (2,751 KB)
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
