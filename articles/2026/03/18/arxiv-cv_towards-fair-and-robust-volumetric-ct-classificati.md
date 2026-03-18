---
title: "Towards Fair and Robust Volumetric CT Classification via KL-Regularised Group Distributionally Robust Optimisation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15941"
published: "2026-03-18"
fetched: "2026-03-18T18:03:26.160079"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026]
Title:Towards Fair and Robust Volumetric CT Classification via KL-Regularised Group Distributionally Robust Optimisation
View PDF HTML (experimental)Abstract:Automated diagnosis from chest computed tomography (CT) scans faces two persistent challenges in clinical deployment: distribution shift across acquisition sites and performance disparity across demographic subgroups. We address both simultaneously across two complementary tasks: binary COVID-19 classification from multi-site CT volumes (Task 1) and four-class lung pathology recognition with gender-based fairness constraints (Task 2). Our framework combines a lightweight MobileViT-XXS slice encoder with a two-layer SliceTransformer aggregator for volumetric reasoning, and trains with a KL-regularised Group Distributionally Robust Optimisation (Group DRO) objective that adaptively upweights underperforming acquisition centres and demographic subgroups. Unlike standard Group DRO, the KL penalty prevents group weight collapse, providing a stable balance between worst-case protection and average performance. For Task 2, we define groups at the granularity of gender class, directly targeting severely underrepresented combinations such as female Squamous cell carcinoma. On Task 1, our best configuration achieves a challenge F1 of 0.835, surpassing the best published challenge entry by +5.9. On Task 2, Group DRO with {\alpha} = 0.5 achieves a mean per-gender macro F1 of 0.815, outperforming the best challenge entry by +11.1 pp and improving Female Squamous F1 by +17.4 over the Fo- cal Loss baseline.
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
