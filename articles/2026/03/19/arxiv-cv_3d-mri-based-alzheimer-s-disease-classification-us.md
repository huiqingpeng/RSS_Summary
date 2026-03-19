---
title: "3D MRI-Based Alzheimer's Disease Classification Using Multi-Modal 3D CNN with Leakage-Aware Subject-Level Evaluation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17304"
published: "2026-03-19"
fetched: "2026-03-19T15:07:38.512410"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:3D MRI-Based Alzheimer's Disease Classification Using Multi-Modal 3D CNN with Leakage-Aware Subject-Level Evaluation
View PDF HTML (experimental)Abstract:Deep learning has become an important tool for Alzheimer's disease (AD) classification from structural MRI. Many existing studies analyze individual 2D slices extracted from MRI volumes, while clinical neuroimaging practice typically relies on the full three dimensional structure of the brain. From this perspective, volumetric analysis may better capture spatial relationships among brain regions that are relevant to disease progression. Motivated by this idea, this work proposes a multimodal 3D convolutional neural network for AD classification using raw OASIS 1 MRI volumes. The model combines structural T1 information with gray matter, white matter, and cerebrospinal fluid probability maps obtained through FSL FAST segmentation in order to capture complementary neuroanatomical information. The proposed approach is evaluated on the clinically labelled OASIS 1 cohort using 5 fold subject level cross validation, achieving a mean accuracy of 72.34% plus or minus 4.66% and a ROC AUC of 0.7781 plus or minus 0.0365. GradCAM visualizations further indicate that the model focuses on anatomically meaningful regions, including the medial temporal lobe and ventricular areas that are known to be associated with Alzheimer's related structural changes. To better understand how data representation and evaluation strategies may influence reported performance, additional diagnostic experiments were conducted on a slice based version of the dataset under both slice level and subject level protocols. These observations help provide context for the volumetric results. Overall, the proposed multimodal 3D framework establishes a reproducible subject level benchmark and highlights the potential benefits of volumetric MRI analysis for Alzheimer's disease classification.
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
