---
title: "Interpretable Prostate Cancer Detection using a Small Cohort of MRI Images"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18460"
published: "2026-03-20"
fetched: "2026-03-20T15:09:09.327549"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Interpretable Prostate Cancer Detection using a Small Cohort of MRI Images
View PDFAbstract:Prostate cancer is a leading cause of mortality in men, yet interpretation of T2-weighted prostate MRI remains challenging due to subtle and heterogeneous lesions. We developed an interpretable framework for automatic cancer detection using a small dataset of 162 T2-weighted images (102 cancer, 60 normal), addressing data scarcity through transfer learning and augmentation. We performed a comprehensive comparison of Vision Transformers (ViT, Swin), CNNs (ResNet18), and classical methods (Logistic Regression, SVM, HOG+SVM). Transfer-learned ResNet18 achieved the best performance (90.9% accuracy, 95.2% sensitivity, AUC 0.905) with only 11M parameters, while Vision Transformers showed lower performance despite substantially higher complexity. Notably, HOG+SVM achieved comparable accuracy (AUC 0.917), highlighting the effectiveness of handcrafted features in small datasets. Unlike state-of-the-art approaches relying on biparametric MRI (T2+DWI) and large cohorts, our method achieves competitive performance using only T2-weighted images, reducing acquisition complexity and computational cost. In a reader study of 22 cases, five radiologists achieved a mean sensitivity of 67.5% (Fleiss Kappa = 0.524), compared to 95.2% for the AI model, suggesting potential for AI-assisted screening to reduce missed cancers and improve consistency. Code and data are publicly available.
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
