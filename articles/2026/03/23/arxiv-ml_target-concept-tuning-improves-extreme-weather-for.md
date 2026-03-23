---
title: "Target Concept Tuning Improves Extreme Weather Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19325"
published: "2026-03-23"
fetched: "2026-03-24T07:17:09.725251"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Target Concept Tuning Improves Extreme Weather Forecasting
View PDF HTML (experimental)Abstract:Deep learning models for meteorological forecasting often fail in rare but high-impact events such as typhoons, where relevant data is scarce. Existing fine-tuning methods typically face a trade-off between overlooking these extreme events and overfitting them at the expense of overall performance. We propose TaCT, an interpretable concept-gated fine-tuning framework that solves the aforementioned issue by selective model improvement: models are adapted specifically for failure cases while preserving performance in common scenarios. To this end, TaCT automatically discovers failure-related internal concepts using Sparse Autoencoders and counterfactual analysis, and updates parameters only when the corresponding concepts are activated, rather than applying uniform adaptation. Experiments show consistent improvements in typhoon forecasting across different regions without degrading other meteorological variables. The identified concepts correspond to physically meaningful circulation patterns, revealing model biases and supporting trustworthy adaptation in scientific forecasting tasks. The code is available at this https URL.
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
