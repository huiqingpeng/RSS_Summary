---
title: "Beyond a Single Signal: SPECTREG2, A Unified MultiExpert Anomaly Detector for Unknown Unknowns"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.21160"
published: "2026-03-24"
fetched: "2026-03-25T07:19:22.425517"
---

Computer Science > Machine Learning
[Submitted on 22 Mar 2026]
Title:Beyond a Single Signal: SPECTREG2, A Unified MultiExpert Anomaly Detector for Unknown Unknowns
View PDF HTML (experimental)Abstract:Epistemic intelligence requires machine learning systems to recognise the limits of their own knowledge and act safely under uncertainty, especially when faced with unknown unknowns. Existing uncertainty quantification methods rely on a single signal such as confidence or density and fail to detect diverse structural anomalies. We introduce SPECTRE-G2, a multi-signal anomaly detector that combines eight complementary signals from a dual-backbone neural network. The architecture includes a spectral normalised Gaussianization encoder, a plain MLP preserving feature geometry, and an ensemble of five models. These produce density, geometry, uncertainty, discriminative, and causal signals. Each signal is normalised using validation statistics and calibrated with synthetic out-of-distribution data. An adaptive top-k fusion selects the most informative signals and averages their scores. Experiments on synthetic, Adult, CIFAR-10, and Gridworld datasets show strong performance across diverse anomaly types, outperforming multiple baselines on AUROC, AUPR, and FPR95. The model is stable across seeds and particularly effective for detecting new variables and confounders. SPECTRE-G2 provides a practical approach for detecting unknown unknowns in open-world settings.
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
