---
title: "Evaluating Uplift Modeling under Structural Biases: Insights into Metric Stability and Model Robustness"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20775"
published: "2026-03-24"
fetched: "2026-03-25T07:13:45.409353"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Evaluating Uplift Modeling under Structural Biases: Insights into Metric Stability and Model Robustness
View PDF HTML (experimental)Abstract:In personalized marketing, uplift models estimate incremental effects by modeling how customer behavior changes under alternative treatments. However, real-world data often exhibit biases - such as selection bias, spillover effects, and unobserved confounding - which adversely affect both estimation accuracy and metric validity. Despite the importance of bias-aware assessment, a lack of systematic studies persists. To bridge this gap, we design a systematic benchmarking framework. Unlike standard predictive tasks, real-world uplift datasets lack counterfactual ground truth, rendering direct metric validation infeasible. Therefore, a semi-synthetic approach serves as a critical enabler for systematic benchmarking, effectively bridging the gap by retaining real-world feature dependencies while providing the ground truth needed to isolate structural biases. Our investigations reveal that: (i) uplift targeting and prediction can manifest as distinct objectives, where proficiency in one does not ensure efficacy in the other; (ii) while many models exhibit inconsistent performance under diverse biases, TARNet shows notable robustness, providing insights for subsequent model design; (iii) evaluation metric stability is linked to mathematical alignment with the ATE, suggesting that ATE-approximating metrics yield more consistent model rankings under structural data imperfections. These findings suggest the need for more robust uplift models and metrics. Code will be released upon acceptance.
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
