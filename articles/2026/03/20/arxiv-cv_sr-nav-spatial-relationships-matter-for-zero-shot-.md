---
title: "SR-Nav: Spatial Relationships Matter for Zero-shot Object Goal Navigation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18443"
published: "2026-03-20"
fetched: "2026-03-20T15:08:48.926048"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:SR-Nav: Spatial Relationships Matter for Zero-shot Object Goal Navigation
View PDF HTML (experimental)Abstract:Zero-shot object-goal navigation aims to find target objects in unseen environments using only egocentric observation. Recent methods leverage foundation models' comprehension and reasoning capabilities to enhance navigation performance. However, when faced with poor viewpoints or weak semantic cues, foundation models often fail to support reliable reasoning in both perception and planning, resulting in inefficient or failed navigation. We observe that inherent relationships among objects and regions encode structured scene priors, which help agents infer plausible target locations even under partial observations. Motivated by this insight, we propose Spatial Relation-aware Navigation (SR-Nav), a framework that models both observed and experience-based spatial relationships to enhance both perception and planning. Specifically, SR-Nav first constructs a Dynamic Spatial Relationship Graph (DSRG) that encodes the target-centered spatial relationships through the foundation models and updates dynamically with real-time observations. We then introduce a Relation-aware Matching Module. It utilizes relationship matching instead of naive detection, leveraging diverse relationships in the DSRG to verify and correct errors, enhancing visual perception robustness. Finally, we design a Dynamic Relationship Planning Module to reduce the planning search space by dynamically computing the optimal paths based on the DSRG from the current position, thereby guiding planning and reducing exploration redundancy. Experiments on HM3D show that our method achieves state-of-the-art performance in both success rate and navigation efficiency. The code will be publicly available at this https URL
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
