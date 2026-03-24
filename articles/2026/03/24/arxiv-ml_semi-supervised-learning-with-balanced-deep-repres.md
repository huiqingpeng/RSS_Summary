---
title: "Semi-Supervised Learning with Balanced Deep Representation Distributions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.21056"
published: "2026-03-24"
fetched: "2026-03-25T07:18:34.605991"
---

Computer Science > Machine Learning
[Submitted on 22 Mar 2026]
Title:Semi-Supervised Learning with Balanced Deep Representation Distributions
View PDF HTML (experimental)Abstract:Semi-Supervised Text Classification (SSTC) mainly works under the spirit of self-training. They initialize the deep classifier by training over labeled texts; and then alternatively predict unlabeled texts as their pseudo-labels and train the deep classifier over the mixture of labeled and pseudo-labeled texts. Naturally, their performance is largely affected by the accuracy of pseudo-labels for unlabeled texts. Unfortunately, they often suffer from low accuracy because of the margin bias problem caused by the large difference between representation distributions of labels in SSTC. To alleviate this problem, we apply the angular margin loss, and perform several Gaussian linear transformations to achieve balanced label angle variances, i.e., the variance of label angles of texts within the same label. More accuracy of predicted pseudo-labels can be achieved by constraining all label angle variances balanced, where they are estimated over both labeled and pseudo-labeled texts during self-training loops. With this insight, we propose a novel SSTC method, namely Semi-Supervised Text Classification with Balanced Deep representation Distributions (S2TC-BDD). We implement both multi-class classification and multi-label classification versions of S2TC-BDD by introducing some pseudo-labeling tricks and regularization terms. To evaluate S2 TC-BDD, we compare it against the state-of-the-art SSTC methods. Empirical results demonstrate the effectiveness of S2 TC-BDD, especially when the labeled texts are scarce.
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
