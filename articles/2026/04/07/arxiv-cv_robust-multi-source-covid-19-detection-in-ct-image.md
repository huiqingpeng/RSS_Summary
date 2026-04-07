---
title: "Robust Multi-Source Covid-19 Detection in CT Images"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03320"
published: "2026-04-07"
fetched: "2026-04-08T07:02:49.086960"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 2 Apr 2026]
Title:Robust Multi-Source Covid-19 Detection in CT Images
View PDF HTML (experimental)Abstract:Deep learning models for COVID-19 detection from chest CT scans generally perform well when the training and test data originate from the same institution, but they often struggle when scans are drawn from multiple centres with differing scanners, imaging protocols, and patient populations. One key reason is that existing methods treat COVID-19 classification as the sole training objective, without accounting for the data source of each scan. As a result, the learned representations tend to be biased toward centres that contribute more training data. To address this, we propose a multi-task learning approach in which the model is trained to predict both the COVID-19 diagnosis and the originating data centre. The two tasks share an EfficientNet-B7 backbone, which encourages the feature extractor to learn representations that hold across all four participating centres. Since the training data is not evenly distributed across sources, we apply a logit-adjusted cross-entropy loss [1] to the source classification head to prevent underrepresented centres from being overlooked. Our pre-processing follows the SSFL framework with KDS [2], selecting eight representative slices per scan. Our method achieves an F1 score of 0.9098 and an AUC-ROC of 0.9647 on a validation set of 308 scans. The code is publicly available at this https URL.
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
