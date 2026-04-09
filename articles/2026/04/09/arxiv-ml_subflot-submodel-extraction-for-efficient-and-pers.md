---
title: "SubFLOT: Submodel Extraction for Efficient and Personalized Federated Learning via Optimal Transport"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06631"
published: "2026-04-09"
fetched: "2026-04-10T07:05:04.237131"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:SubFLOT: Submodel Extraction for Efficient and Personalized Federated Learning via Optimal Transport
View PDF HTML (experimental)Abstract:Federated Learning (FL) enables collaborative model training while preserving data privacy, but its practical deployment is hampered by system and statistical heterogeneity. While federated network pruning offers a path to mitigate these issues, existing methods face a critical dilemma: server-side pruning lacks personalization, whereas client-side pruning is computationally prohibitive for resource-constrained devices. Furthermore, the pruning process itself induces significant parametric divergence among heterogeneous submodels, destabilizing training and hindering global convergence. To address these challenges, we propose SubFLOT, a novel framework for server-side personalized federated pruning. SubFLOT introduces an Optimal Transport-enhanced Pruning (OTP) module that treats historical client models as proxies for local data distributions, formulating the pruning task as a Wasserstein distance minimization problem to generate customized submodels without accessing raw data. Concurrently, to counteract parametric divergence, our Scaling-based Adaptive Regularization (SAR) module adaptively penalizes a submodel's deviation from the global model, with the penalty's strength scaled by the client's pruning rate. Comprehensive experiments demonstrate that SubFLOT consistently and substantially outperforms state-of-the-art methods, underscoring its potential for deploying efficient and personalized models on resource-constrained edge devices.
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
