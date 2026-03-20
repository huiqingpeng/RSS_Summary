---
title: "ProCal: Probability Calibration for Neighborhood-Guided Source-Free Domain Adaptation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18764"
published: "2026-03-20"
fetched: "2026-03-20T15:15:52.005249"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:ProCal: Probability Calibration for Neighborhood-Guided Source-Free Domain Adaptation
View PDF HTML (experimental)Abstract:Source-Free Domain Adaptation (SFDA) adapts pre-trained models to unlabeled target domains without requiring access to source data. Although state-of-the-art methods leveraging local neighborhood structures show promise for SFDA, they tend to over-rely on prediction similarity among neighbors. This over-reliance accelerates the forgetting of source knowledge and increases susceptibility to local noise overfitting. To address these issues, we introduce ProCal, a probability calibration method that dynamically calibrates neighborhood-based predictions through a dual-model collaborative prediction mechanism. ProCal integrates the source model's initial predictions with the current model's online outputs to effectively calibrate neighbor probabilities. This strategy not only mitigates the interference of local noise but also preserves the discriminative information from the source model, thereby achieving a balance between knowledge retention and domain adaptation. Furthermore, we design a joint optimization objective that combines a soft supervision loss with a diversity loss to guide the target model. Our theoretical analysis shows that ProCal converges to an equilibrium where source knowledge and target information are effectively fused, reducing both knowledge forgetting and overfitting. We validate the effectiveness of our approach through extensive experiments on 31 cross-domain tasks across four public datasets. Our code is available at: this https URL.
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
