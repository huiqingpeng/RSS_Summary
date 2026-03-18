---
title: "Efficient Brood Cell Detection in Layer Trap Nests for Bees and Wasps: Balancing Labeling Effort and Species Coverage"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16652"
published: "2026-03-18"
fetched: "2026-03-18T18:16:43.080741"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Efficient Brood Cell Detection in Layer Trap Nests for Bees and Wasps: Balancing Labeling Effort and Species Coverage
View PDF HTML (experimental)Abstract:Monitoring cavity-nesting wild bees and wasps is vital for biodiversity research and conservation. Layer trap nests (LTNs) are emerging as a valuable tool to study the abundance and species richness of these insects, offering insights into their nesting activities and ecological needs. However, manually evaluating LTNs to detect and classify brood cells is labor-intensive and time-consuming. To address this, we propose a deep learning based approach for efficient brood cell detection and classification in LTNs. LTNs present additional challenges due to densely packed brood cells, leading to a high labeling effort per image. Moreover, we observe a significant imbalance in class distribution, with common species having notably more occurrences than rare species. Comprehensive labeling of common species is time-consuming and exacerbates data imbalance, while partial labeling introduces data incompleteness which degrades model performance. To reduce labeling effort and mitigate the impact of unlabeled data, we introduce a novel Constrained False Positive Loss (CFPL) strategy. CFPL dynamically masks predictions from unlabeled data, preventing them from interfering with the classification loss during training. We evaluate our approach on a dataset of 712 LTN images collected over one season, covering 28 fine-grained classes describing the taxonomy and status of brood cells. To minimize labeling effort, we limit the training set to a maximum of 300 labels per class. Experimental results demonstrate that deep learning can be effectively used to detect brood cells in LTNs. Our CFPL method further improves performance and balances model accuracy and labeling effort while also mitigating class imbalance.
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
