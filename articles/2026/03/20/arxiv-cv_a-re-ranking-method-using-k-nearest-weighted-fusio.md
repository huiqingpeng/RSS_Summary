---
title: "A Re-ranking Method using K-nearest Weighted Fusion for Person Re-identification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.04050"
published: "2026-03-20"
fetched: "2026-03-20T16:13:05.522709"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 4 Sep 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:A Re-ranking Method using K-nearest Weighted Fusion for Person Re-identification
View PDF HTML (experimental)Abstract:In person re-identification, re-ranking is a crucial step to enhance the overall accuracy by refining the initial ranking of retrieved results. Previous studies have mainly focused on features from single-view images, which can cause view bias and issues like pose variation, viewpoint changes, and occlusions. Using multi-view features to present a person can help reduce view bias. In this work, we present an efficient re-ranking method that generates multi-view features by aggregating neighbors' features using K-nearest Weighted Fusion (KWF) method. Specifically, we hypothesize that features extracted from re-identification models are highly similar when representing the same identity. Thus, we select K neighboring features in an unsupervised manner to generate multi-view features. Additionally, this study explores the weight selection strategies during feature aggregation, allowing us to identify an effective strategy. Our re-ranking approach does not require model fine-tuning or extra annotations, making it applicable to large-scale datasets. We evaluate our method on the person re-identification datasets Market1501, MSMT17, and Occluded-DukeMTMC. The results show that our method significantly improves Rank@1 and mAP when re-ranking the top M candidates from the initial ranking results. Specifically, compared to the initial results, our re-ranking method achieves improvements of 9.8%/22.0% in Rank@1 on the challenging datasets: MSMT17 and Occluded-DukeMTMC, respectively. Furthermore, our approach demonstrates substantial enhancements in computational efficiency compared to other re-ranking methods. Code is available at this https URL.
Submission history
From: Quang Huy Che [view email][v1] Thu, 4 Sep 2025 09:29:25 UTC (10,545 KB)
[v2] Thu, 19 Mar 2026 02:49:24 UTC (10,542 KB)
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
