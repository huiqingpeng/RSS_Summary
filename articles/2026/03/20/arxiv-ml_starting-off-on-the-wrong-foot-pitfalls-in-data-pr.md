---
title: "Starting Off on the Wrong Foot: Pitfalls in Data Preparation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18190"
published: "2026-03-20"
fetched: "2026-03-20T13:10:15.400911"
---

Statistics > Machine Learning
[Submitted on 18 Mar 2026]
Title:Starting Off on the Wrong Foot: Pitfalls in Data Preparation
View PDF HTML (experimental)Abstract:When working with real-world insurance data, practitioners often encounter challenges during the data preparation stage that can undermine the statistical validity and reliability of downstream modeling. This study illustrates that conventional data preparation procedures such as random train-test partitioning, often yield unreliable and unstable results when confronted with highly imbalanced insurance loss data. To mitigate these limitations, we propose a novel data preparation framework leveraging two recent statistical advancements: support points for representative data splitting to ensure distributional consistency across partitions, and the Chatterjee correlation coefficient for initial, non-parametric feature screening to capture feature relevance and dependence structure. We further integrate these theoretical advances into a unified, efficient framework that also incorporates missing-data handling, and embed this framework within our custom InsurAutoML pipeline. The performance of the proposed approach is evaluated using both simulated datasets and datasets often cited in the academic literature. Our findings definitively demonstrate that incorporating statistically rigorous data preparation methods not only significantly enhances model robustness and interpretability but also substantially reduces computational resource requirements across diverse insurance loss modeling tasks. This work provides a crucial methodological upgrade for achieving reliable results in high stakes insurance applications.
Current browse context:
stat.ML
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
