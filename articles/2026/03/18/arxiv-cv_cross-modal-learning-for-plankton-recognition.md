---
title: "Cross-modal learning for plankton recognition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16427"
published: "2026-03-18"
fetched: "2026-03-18T18:13:05.210037"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Cross-modal learning for plankton recognition
View PDF HTML (experimental)Abstract:This paper considers self-supervised cross-modal coordination as a strategy enabling utilization of multiple modalities and large volumes of unlabeled plankton data to build models for plankton recognition. Automated imaging instruments facilitate the continuous collection of plankton image data on a large scale. Current methods for automatic plankton image recognition rely primarily on supervised approaches, which require labeled training sets that are labor-intensive to collect. On the other hand, some modern plankton imaging instruments complement image information with optical measurement data, such as scatter and fluorescence profiles, which currently are not widely utilized in plankton recognition. In this work, we explore the possibility of using such measurement data to guide the learning process without requiring manual labeling. Inspired by the concepts behind Contrastive Language-Image Pre-training, we train encoders for both modalities using only binary supervisory information indicating whether a given image and profile originate from the same particle or from different particles. For plankton recognition, we employ a small labeled gallery of known plankton species combined with a $k$-NN classifier. This approach yields a recognition model that is inherently multimodal, i.e., capable of utilizing information extracted from both image and profile data. We demonstrate that the proposed method achieves high recognition accuracy while requiring only a minimal number of labeled images. Furthermore, we show that the approach outperforms an image-only self-supervised baseline. Code available at this https URL.
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
