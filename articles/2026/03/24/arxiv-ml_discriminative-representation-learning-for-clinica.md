---
title: "Discriminative Representation Learning for Clinical Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20921"
published: "2026-03-24"
fetched: "2026-03-25T07:16:05.197603"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Discriminative Representation Learning for Clinical Prediction
View PDF HTML (experimental)Abstract:Foundation models in healthcare have largely adopted self supervised pretraining objectives inherited from natural language processing and computer vision, emphasizing reconstruction and large scale representation learning prior to downstream adaptation. We revisit this paradigm in outcome centric clinical prediction settings and argue that, when high quality supervision is available, direct outcome alignment may provide a stronger inductive bias than generative pretraining. We propose a supervised deep learning framework that explicitly shapes representation geometry by maximizing inter class separation relative to within class variance, thereby concentrating model capacity along clinically meaningful axes. Across multiple longitudinal electronic health record tasks, including mortality and readmission prediction, our approach consistently outperforms masked, autoregressive, and contrastive pretraining baselines under matched model capacity. The proposed method improves discrimination, calibration, and sample efficiency, while simplifying the training pipeline to a single stage optimization. These findings suggest that in low entropy, outcome driven healthcare domains, supervision can act as the statistically optimal driver of representation learning, challenging the assumption that large scale self supervised pretraining is a prerequisite for strong clinical performance.
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
