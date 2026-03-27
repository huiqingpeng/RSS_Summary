---
title: "Is Geometry Enough? An Evaluation of Landmark-Based Gaze Estimation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24724"
published: "2026-03-27"
fetched: "2026-03-28T07:15:50.815873"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:Is Geometry Enough? An Evaluation of Landmark-Based Gaze Estimation
View PDF HTML (experimental)Abstract:Appearance-based gaze estimation frequently relies on deep Convolutional Neural Networks (CNNs). These models are accurate, but computationally expensive and act as "black boxes", offering little interpretability. Geometric methods based on facial landmarks are a lightweight alternative, but their performance limits and generalization capabilities remain underexplored in modern benchmarks. In this study, we conduct a comprehensive evaluation of landmark-based gaze estimation. We introduce a standardized pipeline to extract and normalize landmarks from three large-scale datasets (Gaze360, ETH-XGaze, and GazeGene) and train lightweight regression models, specifically Extreme Gradient Boosted trees and two neural architectures: a holistic Multi-Layer Perceptron (MLP) and a siamese MLP designed to capture binocular geometry. We find that landmark-based models exhibit lower performance in within-domain evaluation, likely due to noise introduced into the datasets by the landmark detector. Nevertheless, in cross-domain evaluation, the proposed MLP architectures show generalization capabilities comparable to those of ResNet18 baselines. These findings suggest that sparse geometric features encode sufficient information for robust gaze estimation, paving the way for efficient, interpretable, and privacy-friendly edge applications. The source code and generated landmark-based datasets are available at this https URL.
Submission history
From: Daniele Agostinelli [view email][v1] Wed, 25 Mar 2026 18:51:09 UTC (973 KB)
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
