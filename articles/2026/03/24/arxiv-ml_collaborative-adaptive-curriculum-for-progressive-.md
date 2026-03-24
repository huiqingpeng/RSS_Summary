---
title: "Collaborative Adaptive Curriculum for Progressive Knowledge Distillation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20296"
published: "2026-03-24"
fetched: "2026-03-25T07:07:06.873346"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Collaborative Adaptive Curriculum for Progressive Knowledge Distillation
View PDF HTML (experimental)Abstract:Recent advances in collaborative knowledge distillation have demonstrated cutting-edge performance for resource-constrained distributed multimedia learning scenarios. However, achieving such competitiveness requires addressing a fundamental mismatch: high-dimensional teacher knowledge complexity versus heterogeneous client learning capacities, which currently prohibits deployment in edge-based visual analytics systems. Drawing inspiration from curriculum learning principles, we introduce Federated Adaptive Progressive Distillation (FAPD), a consensus-driven framework that orchestrates adaptive knowledge transfer. FAPD hierarchically decomposes teacher features via PCA-based structuring, extracting principal components ordered by variance contribution to establish a natural visual knowledge hierarchy. Clients progressively receive knowledge of increasing complexity through dimension-adaptive projection matrices. Meanwhile, the server monitors network-wide learning stability by tracking global accuracy fluctuations across a temporal consensus window, advancing curriculum dimensionality only when collective consensus emerges. Consequently, FAPD provably adapts knowledge transfer pace while achieving superior convergence over fixed-complexity approaches. Extensive experiments on three datasets validate FAPD's effectiveness: it attains 3.64% accuracy improvement over FedAvg on CIFAR-10, demonstrates 2x faster convergence, and maintains robust performance under extreme data heterogeneity ({\alpha}=0.1), outperforming baselines by over 4.5%.
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
