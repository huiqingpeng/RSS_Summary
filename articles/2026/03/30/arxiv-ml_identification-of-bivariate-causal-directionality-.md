---
title: "Identification of Bivariate Causal Directionality Based on Anticipated Asymmetric Geometries"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26024"
published: "2026-03-30"
fetched: "2026-03-31T07:20:48.178533"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Identification of Bivariate Causal Directionality Based on Anticipated Asymmetric Geometries
View PDFAbstract:Identification of causal directionality in bivariate numerical data is a fundamental research problem with important practical implications. This paper presents two alternative methods to identify direction of causation by considering conditional distributions: (1) Anticipated Asymmetric Geometries (AAG) and (2) Monotonicity Index. The AAG method compares the actual conditional distributions to anticipated ones along two variables. Different comparison metrics, such as correlation, cosine similarity, Jaccard index, K-L divergence, K-S distance, and mutual information have been evaluated. Anticipated distributions have been projected as normal based on dual response statistics: mean and standard deviation. The Monotonicity Index approach compares the calculated monotonicity indexes of the gradients of conditional distributions along two axes and exhibits counts of gradient sign changes. Both methods assume stochastic properties of the bivariate data and exploit anticipated unimodality of conditional distributions of the effect. It turns out that the tuned AAG method outperforms the Monotonicity Index and reaches a top accuracy of 77.9% compared to ANMs accuracy of 63 +/- 10% when classifying 95 pairs of real-world examples (Mooij et al, 2014). The described methods include a number of hyperparameters that impact accuracy of the identification. For a given set of hyperparameters, both the AAG or Monotonicity Index method provide a unique deterministic outcome of the solution. To address sensitivity to hyperparameters, tuning of hyperparameters has been done by utilizing a full factorial Design of Experiment. A decision tree has been fitted to distinguish misclassified cases using the input data's symmetrical bivariate statistics to address the question of: How decisive is the identification method of causal directionality?
Submission history
From: Alex Glushkovsky [view email][v1] Fri, 27 Mar 2026 02:45:46 UTC (1,156 KB)
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
