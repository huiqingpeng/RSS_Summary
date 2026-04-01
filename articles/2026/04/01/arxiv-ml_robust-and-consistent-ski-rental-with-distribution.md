---
title: "Robust and Consistent Ski Rental with Distributional Advice"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29233"
published: "2026-04-01"
fetched: "2026-04-02T07:16:32.919544"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Robust and Consistent Ski Rental with Distributional Advice
View PDF HTML (experimental)Abstract:The ski rental problem is a canonical model for online decision-making under uncertainty, capturing the fundamental trade-off between repeated rental costs and a one-time purchase. While classical algorithms focus on worst-case competitive ratios and recent "learning-augmented" methods leverage point-estimate predictions, neither approach fully exploits the richness of full distributional predictions while maintaining rigorous robustness guarantees. We address this gap by establishing a systematic framework that integrates distributional advice of unknown quality into both deterministic and randomized algorithms.
For the deterministic setting, we formalize the problem under perfect distributional prediction and derive an efficient algorithm to compute the optimal threshold-buy day. We provide a rigorous performance analysis, identifying sufficient conditions on the predicted distribution under which the expected competitive ratio (ECR) matches the classic optimal randomized bound. To handle imperfect predictions, we propose the Clamp Policy, which restricts the buying threshold to a safe range controlled by a tunable parameter. We show that this policy is both robust, maintaining good performance even with large prediction errors, and consistent, approaching the optimal performance as predictions become accurate.
For the randomized setting, we characterize the stopping distribution via a Water-Filling Algorithm, which optimizes expected cost while strictly satisfying robustness constraints. Experimental results across diverse distributions (Gaussian, geometric, and bi-modal) demonstrate that our framework improves consistency significantly over existing point-prediction baselines while maintaining comparable robustness.
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
