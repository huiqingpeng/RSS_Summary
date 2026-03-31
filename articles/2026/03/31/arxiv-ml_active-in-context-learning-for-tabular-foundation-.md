---
title: "Active In-Context Learning for Tabular Foundation Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27385"
published: "2026-03-31"
fetched: "2026-04-01T07:23:15.225092"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:Active In-Context Learning for Tabular Foundation Models
View PDF HTML (experimental)Abstract:Active learning (AL) reduces labeling cost by querying informative samples, but in tabular settings its cold-start gains are often limited because uncertainty estimates are unreliable when models are trained on very few labels. Tabular foundation models such as TabPFN provide calibrated probabilistic predictions via in-context learning (ICL), i.e., without task-specific weight updates, enabling an AL regime in which the labeled context - rather than parameters - is iteratively optimized. We formalize Tabular Active In-Context Learning (Tab-AICL) and instantiate it with four acquisition rules: uncertainty (TabPFN-Margin), diversity (TabPFN-Coreset), an uncertainty-diversity hybrid (TabPFN-Hybrid), and a scalable two-stage method (TabPFN-Proxy-Hybrid) that shortlists candidates using a lightweight linear proxy before TabPFN-based selection. Across 20 classification benchmarks, Tab-AICL improves cold-start sample efficiency over retrained gradient-boosting baselines (CatBoost-Margin and XGBoost-Margin), measured by normalized AULC up to 100 labeled samples.
Submission history
From: Fabrizio Pittorino [view email][v1] Sat, 28 Mar 2026 19:37:13 UTC (322 KB)
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
