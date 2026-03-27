---
title: "BCMDA: Bidirectional Correlation Maps Domain Adaptation for Mixed Domain Semi-Supervised Medical Image Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24691"
published: "2026-03-27"
fetched: "2026-03-28T07:14:51.978612"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:BCMDA: Bidirectional Correlation Maps Domain Adaptation for Mixed Domain Semi-Supervised Medical Image Segmentation
View PDF HTML (experimental)Abstract:In mixed domain semi-supervised medical image segmentation (MiDSS), achieving superior performance under domain shift and limited annotations is challenging. This scenario presents two primary issues: (1) distributional differences between labeled and unlabeled data hinder effective knowledge transfer, and (2) inefficient learning from unlabeled data causes severe confirmation bias. In this paper, we propose the bidirectional correlation maps domain adaptation (BCMDA) framework to overcome these issues. On the one hand, we employ knowledge transfer via virtual domain bridging (KTVDB) to facilitate cross-domain learning. First, to construct a distribution-aligned virtual domain, we leverage bidirectional correlation maps between labeled and unlabeled data to synthesize both labeled and unlabeled images, which are then mixed with the original images to generate virtual images using two strategies, a fixed ratio and a progressive dynamic MixUp. Next, dual bidirectional CutMix is used to enable initial knowledge transfer within the fixed virtual domain and gradual knowledge transfer from the dynamically transitioning labeled domain to the real unlabeled domains. On the other hand, to alleviate confirmation bias, we adopt prototypical alignment and pseudo label correction (PAPLC), which utilizes learnable prototype cosine similarity classifiers for bidirectional prototype alignment between the virtual and real domains, yielding smoother and more compact feature representations. Finally, we use prototypical pseudo label correction to generate more reliable pseudo labels. Empirical evaluations on three public multi-domain datasets demonstrate the superiority of our method, particularly showing excellent performance even with very limited labeled samples. Code available at this https URL.
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
