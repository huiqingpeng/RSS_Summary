---
title: "Out-of-Distribution Object Detection in Street Scenes via Synthetic Outlier Exposure and Transfer Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16122"
published: "2026-03-18"
fetched: "2026-03-18T18:05:52.598278"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Out-of-Distribution Object Detection in Street Scenes via Synthetic Outlier Exposure and Transfer Learning
View PDF HTML (experimental)Abstract:Out-of-distribution (OOD) object detection is an important yet underexplored task. A reliable object detector should be able to handle OOD objects by localizing and correctly classifying them as OOD. However, a critical issue arises when such atypical objects are completely missed by the object detector and incorrectly treated as background. Existing OOD detection approaches in object detection often rely on complex architectures or auxiliary branches and typically do not provide a framework that treats in-distribution (ID) and OOD in a unified way. In this work, we address these limitations by enabling a single detector to detect OOD objects, that are otherwise silently overlooked, alongside ID objects. We present \textbf{SynOE-OD}, a \textbf{Syn}thetic \textbf{O}utlier-\textbf{E}xposure-based \textbf{O}bject \textbf{D}etection framework, that leverages strong generative models, like Stable Diffusion, and Open-Vocabulary Object Detectors (OVODs) to generate semantically meaningful, object-level data that serve as outliers during training. The generated data is used for transfer-learning to establish strong ID task performance and supplement detection models with OOD object detection robustness. Our approach achieves state-of-the-art average precision on an established OOD object detection benchmark, where OVODs, such as GroundingDINO, show limited zero-shot performance in detecting OOD objects in street-scenes.
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
