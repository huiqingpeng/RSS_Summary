---
title: "Prompt-Free Universal Region Proposal Network"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17554"
published: "2026-03-19"
fetched: "2026-03-19T15:13:41.953468"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Prompt-Free Universal Region Proposal Network
View PDF HTML (experimental)Abstract:Identifying potential objects is critical for object recognition and analysis across various computer vision applications. Existing methods typically localize potential objects by relying on exemplar images, predefined categories, or textual descriptions. However, their reliance on image and text prompts often limits flexibility, restricting adaptability in real-world scenarios. In this paper, we introduce a novel Prompt-Free Universal Region Proposal Network (PF-RPN), which identifies potential objects without relying on external prompts. First, the Sparse Image-Aware Adapter (SIA) module performs initial localization of potential objects using a learnable query embedding dynamically updated with visual features. Next, the Cascade Self-Prompt (CSP) module identifies the remaining potential objects by leveraging the self-prompted learnable embedding, autonomously aggregating informative visual features in a cascading manner. Finally, the Centerness-Guided Query Selection (CG-QS) module facilitates the selection of high-quality query embeddings using a centerness scoring network. Our method can be optimized with limited data (e.g., 5% of MS COCO data) and applied directly to various object detection application domains for identifying potential objects without fine-tuning, such as underwater object detection, industrial defect detection, and remote sensing image object detection. Experimental results across 19 datasets validate the effectiveness of our method. Code is available at this https URL.
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
