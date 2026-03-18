---
title: "Informative Perturbation Selection for Uncertainty-Aware Post-hoc Explanations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14894"
published: "2026-03-18"
fetched: "2026-03-18T17:07:29.020053"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Informative Perturbation Selection for Uncertainty-Aware Post-hoc Explanations
View PDF HTML (experimental)Abstract:Trust and ethical concerns due to the widespread deployment of opaque machine learning (ML) models motivating the need for reliable model explanations. Post-hoc model-agnostic explanation methods addresses this challenge by learning a surrogate model that approximates the behavior of the deployed black-box ML model in the locality of a sample of interest. In post-hoc scenarios, neither the underlying model parameters nor the training are available, and hence, this local neighborhood must be constructed by generating perturbed inputs in the neighborhood of the sample of interest, and its corresponding model predictions. We propose \emph{Expected Active Gain for Local Explanations} (\texttt{EAGLE}), a post-hoc model-agnostic explanation framework that formulates perturbation selection as an information-theoretic active learning problem. By adaptively sampling perturbations that maximize the expected information gain, \texttt{EAGLE} efficiently learns a linear surrogate explainable model while producing feature importance scores along with the uncertainty/confidence estimates. Theoretically, we establish that cumulative information gain scales as $\mathcal{O}(d \log t)$, where $d$ is the feature dimension and $t$ represents the number of samples, and that the sample complexity grows linearly with $d$ and logarithmically with the confidence parameter $1/\delta$. Empirical results on tabular and image datasets corroborate our theoretical findings and demonstrate that \texttt{EAGLE} improves explanation reproducibility across runs, achieves higher neighborhood stability, and improves perturbation sample quality as compared to state-of-the-art baselines such as Tilia, US-LIME, GLIME and BayesLIME.
Submission history
From: Sumedha Chugh [view email][v1] Mon, 16 Mar 2026 06:48:56 UTC (502 KB)
[v2] Tue, 17 Mar 2026 05:41:30 UTC (502 KB)
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
