---
title: "Safe Reinforcement Learning with Preference-based Constraint Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23565"
published: "2026-03-26"
fetched: "2026-03-27T07:14:28.988019"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Safe Reinforcement Learning with Preference-based Constraint Inference
View PDF HTML (experimental)Abstract:Safe reinforcement learning (RL) is a standard paradigm for safety-critical decision making. However, real-world safety constraints can be complex, subjective, and even hard to explicitly specify. Existing works on constraint inference rely on restrictive assumptions or extensive expert demonstrations, which is not realistic in many real-world applications. How to cheaply and reliably learn these constraints is the major challenge we focus on in this study. While inferring constraints from human preferences offers a data-efficient alternative, we identify the popular Bradley-Terry (BT) models fail to capture the asymmetric, heavy-tailed nature of safety costs, resulting in risk underestimation. It is still rare in the literature to understand the impacts of BT models on the downstream policy learning. To address the above knowledge gaps, we propose a novel approach namely Preference-based Constrained Reinforcement Learning (PbCRL). We introduce a novel dead zone mechanism into preference modeling and theoretically prove that it encourages heavy-tailed cost distributions, thereby achieving better constraint alignment. Additionally, we incorporate a Signal-to-Noise Ratio (SNR) loss to encourage exploration by cost variances, which is found to benefit policy learning. Further, two-stage training strategy are deployed to lower online labeling burdens while adaptively enhancing constraint satisfaction. Empirical results demonstrate that PbCRL achieves superior alignment with true safety requirements and outperforms the state-of-the-art baselines in terms of safety and reward. Our work explores a promising and effective way for constraint inference in Safe RL, which has great potential in a range of safety-critical applications.
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
