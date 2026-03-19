---
title: "Improving Epidemic Analyses with Privacy-Preserving Integration of Sensitive Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2506.22342"
published: "2026-03-19"
fetched: "2026-03-19T14:03:47.823325"
---

Computer Science > Machine Learning
[Submitted on 27 Jun 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Improving Epidemic Analyses with Privacy-Preserving Integration of Sensitive Data
View PDF HTML (experimental)Abstract:Epidemic analyses increasingly rely on heterogeneous datasets, many of which are sensitive and require strong privacy protection. Although differential privacy (DP) has become a standard in machine learning and data sharing, its adoption in epidemiological modeling remains limited. In this work, we introduce DPEpiNN, a unified framework that integrates deep neural networks with a mechanistic SEIRM-based metapopulation model under formal DP guarantees. DPEpiNN supports multiple epidemic tasks (including multi-step forecasting, nowcasting, effective reproduction number $(R_t)$ estimation, and intervention analysis) within a single differentiable pipeline. The framework jointly learns epidemic parameters from heterogeneous public and sensitive datasets, while ensuring privacy via input perturbation mechanisms. We evaluate DPEpiNN using COVID-19 data from three regions. Results show that incorporating sensitive datasets substantially improves predictive performance even under strong privacy constraints. Compared with a deep learning baseline, DPEpiNN achieves higher accuracy in forecasting and nowcasting while producing reliable estimates of $R_t$. Furthermore, the learned epidemic transmission models remain inherently private due to the post-processing property of differential privacy, enabling downstream policy analyses such as simulation of social distancing interventions. Our work demonstrates that interpretability (through mechanistic modeling), predictive accuracy (through neural integration), and rigorous privacy guarantees can be jointly achieved in modern epidemic modeling.
Submission history
From: Zihan Guan [view email][v1] Fri, 27 Jun 2025 15:52:12 UTC (8,487 KB)
[v2] Tue, 17 Mar 2026 18:55:34 UTC (851 KB)
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
