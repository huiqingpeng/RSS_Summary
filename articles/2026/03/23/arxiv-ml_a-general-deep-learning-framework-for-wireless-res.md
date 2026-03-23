---
title: "A General Deep Learning Framework for Wireless Resource Allocation under Discrete Constraints"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19322"
published: "2026-03-23"
fetched: "2026-03-24T07:17:04.563413"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:A General Deep Learning Framework for Wireless Resource Allocation under Discrete Constraints
View PDF HTML (experimental)Abstract:While deep learning (DL)-based methods have achieved remarkable success in continuous wireless resource allocation, efficient solutions for problems involving discrete variables remain challenging. This is primarily due to the zero-gradient issue in backpropagation, the difficulty of enforcing intricate constraints with discrete variables, and the inability in generating solutions with non-same-parameter-same-decision (non-SPSD) property. To address these challenges, this paper proposes a general DL framework by introducing the support set to represent the discrete variables. We model the elements of the support set as random variables and learn their joint probability distribution. By factorizing the joint probability as the product of conditional probabilities, each conditional probability is sequentially learned. This probabilistic modeling directly tackles all the aforementioned challenges of DL for handling discrete variables. By operating on probability distributions instead of hard binary decisions, the framework naturally avoids the zero-gradient issue. During the learning of the conditional probabilities, discrete constraints can be seamlessly enforced by masking out infeasible solutions. Moreover, with a dynamic context embedding that captures the evolving discrete solutions, the non-SPSD property is inherently provided by the proposed framework. We apply the proposed framework to two representative mixed-discrete wireless resource allocation problems: (a) joint user association and beamforming in cell-free systems, and (b) joint antenna positioning and beamforming in movable antenna-aided systems. Simulation results demonstrate that the proposed DL framework consistently outperforms existing baselines in terms of both system performance and computational efficiency.
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
