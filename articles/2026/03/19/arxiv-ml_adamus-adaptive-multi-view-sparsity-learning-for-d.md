---
title: "AdaMuS: Adaptive Multi-view Sparsity Learning for Dimensionally Unbalanced Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17610"
published: "2026-03-19"
fetched: "2026-03-19T12:14:28.946158"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:AdaMuS: Adaptive Multi-view Sparsity Learning for Dimensionally Unbalanced Data
View PDF HTML (experimental)Abstract:Multi-view learning primarily aims to fuse multiple features to describe data comprehensively. Most prior studies implicitly assume that different views share similar dimensions. In practice, however, severe dimensional disparities often exist among different views, leading to the unbalanced multi-view learning issue. For example, in emotion recognition tasks, video frames often reach dimensions of $10^6$, while physiological signals comprise only $10^1$ dimensions. Existing methods typically face two main challenges for this problem: (1) They often bias towards high-dimensional data, overlooking the low-dimensional views. (2) They struggle to effectively align representations under extreme dimensional imbalance, which introduces severe redundancy into the low-dimensional ones. To address these issues, we propose the Adaptive Multi-view Sparsity Learning (AdaMuS) framework. First, to prevent ignoring the information of low-dimensional views, we construct view-specific encoders to map them into a unified dimensional space. Given that mapping low-dimensional data to a high-dimensional space often causes severe overfitting, we design a parameter-free pruning method to adaptively remove redundant parameters in the encoders. Furthermore, we propose a sparse fusion paradigm that flexibly suppresses redundant dimensions and effectively aligns each view. Additionally, to learn representations with stronger generalization, we propose a self-supervised learning paradigm that obtains supervision information by constructing similarity graphs. Extensive evaluations on a synthetic toy dataset and seven real-world benchmarks demonstrate that AdaMuS consistently achieves superior performance and exhibits strong generalization across both classification and semantic segmentation tasks.
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
