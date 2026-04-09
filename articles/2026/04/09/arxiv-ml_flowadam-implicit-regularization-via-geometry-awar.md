---
title: "FlowAdam: Implicit Regularization via Geometry-Aware Soft Momentum Injection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06652"
published: "2026-04-09"
fetched: "2026-04-10T07:05:04.760108"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:FlowAdam: Implicit Regularization via Geometry-Aware Soft Momentum Injection
View PDF HTML (experimental)Abstract:Adaptive moment methods such as Adam use a diagonal, coordinate-wise preconditioner based on exponential moving averages of squared gradients. This diagonal scaling is coordinate-system dependent and can struggle with dense or rotated parameter couplings, including those in matrix factorization, tensor decomposition, and graph neural networks, because it treats each parameter independently. We introduce FlowAdam, a hybrid optimizer that augments Adam with continuous gradient-flow integration via an ordinary differential equation (ODE). When EMA-based statistics detect landscape difficulty, FlowAdam switches to clipped ODE integration. Our central contribution is Soft Momentum Injection, which blends ODE velocity with Adam's momentum during mode transitions. This prevents the training collapse observed with naive hybrid approaches. Across coupled optimization benchmarks, the ODE integration provides implicit regularization, reducing held-out error by 10-22% on low-rank matrix/tensor recovery and 6% on Jester (real-world collaborative filtering), also surpassing tuned Lion and AdaBelief, while matching Adam on well-conditioned workloads (CIFAR-10). MovieLens-100K confirms benefits arise specifically from coupled parameter interactions rather than bias estimation. Ablation studies show that soft injection is essential, as hard replacement reduces accuracy from 100% to 82.5%.
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
