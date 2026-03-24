---
title: "Learning from Label Proportions with Dual-proportion Constraints"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.21153"
published: "2026-03-24"
fetched: "2026-03-25T07:19:13.921407"
---

Computer Science > Machine Learning
[Submitted on 22 Mar 2026]
Title:Learning from Label Proportions with Dual-proportion Constraints
View PDF HTML (experimental)Abstract:Learning from Label Proportions (LLP) is a weakly supervised problem in which the training data comprise bags, that is, groups of instances, each annotated only with bag-level class label proportions, and the objective is to learn a classifier that predicts instance-level labels. This setting is widely applicable when privacy constraints limit access to instance-level annotations or when fine-grained labeling is costly or impractical. In this work, we introduce a method that leverages Dual proportion Constraints (LLP-DC) during training, enforcing them at both the bag and instance levels. Specifically, the bag-level training aligns the mean prediction with the given proportion, and the instance-level training aligns hard pseudo-labels that satisfy the proportion constraint, where a minimum-cost maximum-flow algorithm is used to generate hard pseudo-labels. Extensive experimental results across various benchmark datasets empirically validate that LLP-DC consistently improves over previous LLP methods across datasets and bag sizes. The code is publicly available at this https URL PR2026_Findings_LLP_DC.
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
