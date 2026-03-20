---
title: "Towards High-Quality Image Segmentation: Improving Topology Accuracy by Penalizing Neighbor Pixels"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18671"
published: "2026-03-20"
fetched: "2026-03-20T15:14:49.472305"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Towards High-Quality Image Segmentation: Improving Topology Accuracy by Penalizing Neighbor Pixels
View PDF HTML (experimental)Abstract:Standard deep learning models for image segmentation cannot guarantee topology accuracy, failing to preserve the correct number of connected components or structures. This, in turn, affects the quality of the segmentations and compromises the reliability of the subsequent quantification analyses. Previous works have proposed to enhance topology accuracy with specialized frameworks, architectures, and loss functions. However, these methods are often cumbersome to integrate into existing training pipelines, they are computationally very expensive, or they are restricted to structures with tubular morphology. We present SCNP, an efficient method that improves topology accuracy by penalizing the logits with their poorest-classified neighbor, forcing the model to improve the prediction at the pixels' neighbors before allowing it to improve the pixels themselves. We show the effectiveness of SCNP across 13 datasets, covering different structure morphologies and image modalities, and integrate it into three frameworks for semantic and instance segmentation. Additionally, we show that SCNP can be integrated into several loss functions, making them improve topology accuracy. Our code can be found at this https URL.
Submission history
From: Juan Miguel Valverde [view email][v1] Thu, 19 Mar 2026 09:33:12 UTC (13,460 KB)
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
