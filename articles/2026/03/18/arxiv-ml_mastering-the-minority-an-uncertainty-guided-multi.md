---
title: "Mastering the Minority: An Uncertainty-guided Multi-Expert Framework for Challenging-tailed Sequence Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15708"
published: "2026-03-18"
fetched: "2026-03-18T15:34:22.966083"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:Mastering the Minority: An Uncertainty-guided Multi-Expert Framework for Challenging-tailed Sequence Learning
View PDF HTML (experimental)Abstract:Imbalanced data distribution remains a critical challenge in sequential learning, leading models to easily recognize frequent categories while failing to detect minority classes adequately. The Mixture-of-Experts model offers a scalable solution, yet its application is often hindered by parameter inefficiency, poor expert specialization, and difficulty in resolving prediction conflicts. To Master the Minority classes effectively, we propose the Uncertainty-based Multi-Expert fusion network (UME) framework. UME is designed with three core innovations: First, we employ Ensemble LoRA for parameter-efficient modeling, significantly reducing the trainable parameter count. Second, we introduce Sequential Specialization guided by Dempster-Shafer Theory (DST), which ensures effective specialization on the challenging-tailed classes. Finally, an Uncertainty-Guided Fusion mechanism uses DST's certainty measures to dynamically weigh expert opinions, resolving conflicts by prioritizing the most confident expert for reliable final predictions. Extensive experiments across four public hierarchical text classification datasets demonstrate that UME achieves state-of-the-art performance. We achieve a performance gain of up to 17.97\% over the best baseline on individual categories, while reducing trainable parameters by up to 10.32\%. The findings highlight that uncertainty-guided expert coordination is a principled strategy for addressing challenging-tailed sequence learning. Our code is available at this https URL.
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
