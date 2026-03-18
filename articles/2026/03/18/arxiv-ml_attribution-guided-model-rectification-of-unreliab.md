---
title: "Attribution-Guided Model Rectification of Unreliable Neural Network Behaviors"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15656"
published: "2026-03-18"
fetched: "2026-03-18T15:33:28.049660"
---

Computer Science > Machine Learning
[Submitted on 8 Mar 2026]
Title:Attribution-Guided Model Rectification of Unreliable Neural Network Behaviors
View PDF HTML (experimental)Abstract:The performance of neural network models deteriorates due to their unreliable behavior on non-robust features of corrupted samples. Owing to their opaque nature, rectifying models to address this problem often necessitates arduous data cleaning and model retraining, resulting in huge computational and manual overhead. In this work, we leverage rank-one model editing to establish an attribution-guided model rectification framework that effectively locates and corrects model unreliable behaviors. We first distinguish our rectification setting from existing model editing, yielding a formulation that corrects unreliable behavior while preserving model performance and reducing reliance on large budgets of cleansed samples. We further reveal a bottleneck of model rectifying arising from heterogeneous editability across layers. To target the primary source of misbehavior, we introduce an attribution-guided layer localization method that quantifies layer-wise editability and identifies the layer most responsible for unreliabilities. Extensive experiments demonstrate the effectiveness of our method in correcting unreliabilities observed for neural Trojans, spurious correlations and feature leakage. Our method shows remarkable performance by achieving its editing objective with as few as a single cleansed sample, which makes it appealing for practice.
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
