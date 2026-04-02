---
title: "Orthogonal Learner for Estimating Heterogeneous Long-Term Treatment Effects"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00915"
published: "2026-04-02"
fetched: "2026-04-03T07:25:59.726859"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Orthogonal Learner for Estimating Heterogeneous Long-Term Treatment Effects
View PDFAbstract:Estimation of heterogeneous long-term treatment effects (HLTEs) is widely used for personalized decision-making in marketing, economics, and medicine, where short-term randomized experiments are often combined with long-term observational data. However, HLTE estimation is challenging due to limited overlap in treatment or in observing long-term outcomes for certain subpopulations, which can lead to unstable HLTE estimates with large finite-sample variance. To address this challenge, we introduce the LT-O-learners (Long-Term Orthogonal Learners), a set of novel orthogonal learners for HLTE estimation. The learners are designed for the canonical HLTE setting that combines a short-term randomized dataset $\mathcal{D}_1$ with a long-term historical dataset $\mathcal{D}_2$. The key idea of our LT-O-Learners is to retarget the learning objective by introducing custom overlap weights that downweight samples with low overlap in treatment or in long-term observation. We show that the retargeted loss is equivalent to the weighted oracle loss and satisfies Neyman-orthogonality, which means our learners are robust to errors in the nuisance estimation. We further provide a general error bound for the LT-O-Learners and give the conditions under which quasi-oracle rate can be achieved. Finally, our LT-O-learners are model-agnostic and can thus be instantiated with arbitrary machine learning models. We conduct empirical evaluations on synthetic and semi-synthetic benchmarks to confirm the theoretical properties of our LT-O-Learners, especially the robustness in low-overlap settings. To the best of our knowledge, ours are the first orthogonal learners for HLTE estimation that are robust to low overlap that is common in long-term outcomes.
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
