---
title: "CytoSyn: a Foundation Diffusion Model for Histopathology -- Tech Report"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18089"
published: "2026-03-20"
fetched: "2026-03-20T13:08:14.873687"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:CytoSyn: a Foundation Diffusion Model for Histopathology -- Tech Report
View PDF HTML (experimental)Abstract:Computational pathology has made significant progress in recent years, fueling advances in both fundamental disease understanding and clinically ready tools. This evolution is driven by the availability of large amounts of digitized slides and specialized deep learning methods and models. Multiple self-supervised foundation feature extractors have been developed, enabling downstream predictive applications from cell segmentation to tumor sub-typing and survival analysis. In contrast, generative foundation models designed specifically for histopathology remain scarce. Such models could address tasks that are beyond the capabilities of feature extractors, such as virtual staining. In this paper, we introduce CytoSyn, a state-of-the-art foundation latent diffusion model that enables the guided generation of highly realistic and diverse histopathology H&E-stained images, as shown in an extensive benchmark. We explored methodological improvements, training set scaling, sampling strategies and slide-level overfitting, culminating in the improved CytoSyn-v2, and compared our work to PixCell, a state-of-the-art model, in an in-depth manner. This comparison highlighted the strong sensitivity of both diffusion models and performance metrics to preprocessing-specific details such as JPEG compression. Our model has been trained on a dataset obtained from more than 10,000 TCGA diagnostic whole-slide images of 32 different cancer types. Despite being trained only on oncology slides, it maintains state-of-the-art performance generating inflammatory bowel disease images. To support the research community, we publicly release CytoSyn's weights, its training and validation datasets, and a sample of synthetic images in this repository: this https URL.
Current browse context:
cs.CV
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
