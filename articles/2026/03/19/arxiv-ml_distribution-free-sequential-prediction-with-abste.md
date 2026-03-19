---
title: "Distribution-Free Sequential Prediction with Abstentions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.17918"
published: "2026-03-19"
fetched: "2026-03-19T14:11:55.079946"
---

Computer Science > Machine Learning
[Submitted on 20 Feb 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Distribution-Free Sequential Prediction with Abstentions
View PDF HTML (experimental)Abstract:We study a sequential prediction problem in which an adversary is allowed to inject arbitrarily many adversarial instances in a stream of i.i.d. instances, but at each round, the learner may also abstain from making a prediction without incurring any penalty if the instance was indeed corrupted. This semi-adversarial setting naturally sits between the classical stochastic case with i.i.d. instances for which function classes with finite VC dimension are learnable; and the adversarial case with arbitrary instances, known to be significantly more restrictive. For this problem, Goel et al. (2023) showed that, if the learner knows the distribution $\mu$ of clean samples in advance, learning can be achieved for all VC classes without restrictions on adversary corruptions. This is, however, a strong assumption in both theory and practice: a natural question is whether similar learning guarantees can be achieved without prior distributional knowledge, as is standard in classical learning frameworks (e.g., PAC learning or asymptotic consistency) and other non-i.i.d. models (e.g., smoothed online learning). We therefore focus on the distribution-free setting where $\mu$ is unknown and propose an algorithm AbstainBoost based on a boosting procedure of weak learners, which guarantees sublinear error for general VC classes in distribution-free abstention learning for oblivious adversaries. These algorithms also enjoy similar guarantees for adaptive adversaries, for structured function classes including linear classifiers. These results are complemented with corresponding lower bounds, which reveal an interesting polynomial trade-off between misclassification error and number of erroneous abstentions.
Submission history
From: Jialin Yu [view email][v1] Fri, 20 Feb 2026 00:28:27 UTC (46 KB)
[v2] Tue, 17 Mar 2026 19:06:01 UTC (47 KB)
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
