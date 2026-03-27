---
title: "No Single Metric Tells the Whole Story: A Multi-Dimensional Evaluation Framework for Uncertainty Attributions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24524"
published: "2026-03-27"
fetched: "2026-03-28T07:11:21.121475"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:No Single Metric Tells the Whole Story: A Multi-Dimensional Evaluation Framework for Uncertainty Attributions
View PDF HTML (experimental)Abstract:Research on explainable AI (XAI) has frequently focused on explaining model predictions. More recently, methods have been proposed to explain prediction uncertainty by attributing it to input features (uncertainty attributions). However, the evaluation of these methods remains inconsistent as studies rely on heterogeneous proxy tasks and metrics, hindering comparability. We address this by aligning uncertainty attributions with the well-established Co-12 framework for XAI evaluation. We propose concrete implementations for the correctness, consistency, continuity, and compactness properties. Additionally, we introduce conveyance, a property tailored to uncertainty attributions that evaluates whether controlled increases in epistemic uncertainty reliably propagate to feature-level attributions. We demonstrate our evaluation framework with eight metrics across combinations of uncertainty quantification and feature attribution methods on tabular and image data. Our experiments show that gradient-based methods consistently outperform perturbation-based approaches in consistency and conveyance, while Monte-Carlo dropconnect outperforms Monte-Carlo dropout in most metrics. Although most metrics rank the methods consistently across samples, inter-method agreement remains low. This suggests no single metric sufficiently evaluates uncertainty attribution quality. The proposed evaluation framework contributes to the body of knowledge by establishing a foundation for systematic comparison and development of uncertainty attribution methods.
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
