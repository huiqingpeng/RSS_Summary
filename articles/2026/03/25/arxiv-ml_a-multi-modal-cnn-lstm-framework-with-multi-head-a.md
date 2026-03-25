---
title: "A Multi-Modal CNN-LSTM Framework with Multi-Head Attention and Focal Loss for Real-Time Elderly Fall Detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22313"
published: "2026-03-25"
fetched: "2026-03-26T07:09:46.221667"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:A Multi-Modal CNN-LSTM Framework with Multi-Head Attention and Focal Loss for Real-Time Elderly Fall Detection
View PDF HTML (experimental)Abstract:The increasing global aging population has intensified the demand for reliable health monitoring systems, particularly those capable of detecting critical events such as falls among elderly individuals. Traditional fall detection approaches relying on single-modality acceleration data suffer from high false alarm rates, while conventional machine learning methods require extensive hand-crafted feature engineering. This paper proposes a novel multi-modal deep learning framework, MultiModalFallDetector, designed for real-time elderly fall detection using wearable sensors. Our approach integrates multiple innovations: a multi-scale CNN-based feature extractor capturing motion dynamics at varying temporal resolutions; fusion of tri-axial accelerometer, gyroscope, and four-channel physiological signals; incorporation of a multi-head self-attention mechanism for dynamic temporal weighting; adoption of Focal Loss to mitigate severe class imbalance; introduction of an auxiliary activity classification task for regularization; and implementation of transfer learning from UCI HAR to SisFall dataset. Extensive experiments on the SisFall dataset, which includes real-world simulated fall trials from elderly participants (aged 60-85), demonstrate that our framework achieves an F1-score of 98. 7, Recall of 98. 9, and AUC-ROC of 99. 4, significantly outperforming baseline methods including traditional machine learning and standard deep learning approaches. The model maintains sub- 50ms inference latency on edge devices, confirming its suitability for real-time deployment in geriatric care settings.
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
