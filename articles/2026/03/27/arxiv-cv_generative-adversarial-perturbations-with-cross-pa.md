---
title: "Generative Adversarial Perturbations with Cross-paradigm Transferability on Localized Crowd Counting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24821"
published: "2026-03-27"
fetched: "2026-03-28T07:17:14.792426"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:Generative Adversarial Perturbations with Cross-paradigm Transferability on Localized Crowd Counting
View PDF HTML (experimental)Abstract:State-of-the-art crowd counting and localization are primarily modeled using two paradigms: density maps and point regression. Given the field's security ramifications, there is active interest in model robustness against adversarial attacks. Recent studies have demonstrated transferability across density-map-based approaches via adversarial patches, but cross-paradigm attacks (i.e., across both density map-based models and point regression-based models) remain unexplored. We introduce a novel adversarial framework that compromises both density map and point regression architectural paradigms through a comprehensive multi-task loss optimization. For point-regression models, we employ scene-density-specific high-confidence logit suppression; for density-map approaches, we use peak-targeted density map suppression. Both are combined with model-agnostic perceptual constraints to ensure that perturbations are effective and imperceptible to the human eye. Extensive experiments demonstrate the effectiveness of our attack, achieving on average a 7X increase in Mean Absolute Error compared to clean images while maintaining competitive visual quality, and successfully transferring across seven state-of-the-art crowd models with transfer ratios ranging from 0.55 to 1.69. Our approach strikes a balance between attack effectiveness and imperceptibility compared to state-of-the-art transferable attack strategies. The source code is available at this https URL
Submission history
From: Alabi Mehzabin Anisha [view email][v1] Wed, 25 Mar 2026 21:13:38 UTC (9,686 KB)
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
