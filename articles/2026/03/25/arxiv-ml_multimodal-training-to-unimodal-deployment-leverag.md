---
title: "Multimodal Training to Unimodal Deployment: Leveraging Unstructured Data During Training to Optimize Structured Data Only Deployment"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22530"
published: "2026-03-25"
fetched: "2026-03-26T07:15:09.406753"
---

Computer Science > Machine Learning
[Submitted on 23 Mar 2026]
Title:Multimodal Training to Unimodal Deployment: Leveraging Unstructured Data During Training to Optimize Structured Data Only Deployment
View PDFAbstract:Unstructured Electronic Health Record (EHR) data, such as clinical notes, contain clinical contextual observations that are not directly reflected in structured data fields. This additional information can substantially improve model learning. However, due to their unstructured nature, these data are often unavailable or impractical to use when deploying a model. We introduce a multimodal learning framework that leverages unstructured EHR data during training while producing a model that can be deployed using only structured EHR data. Using a cohort of 3,466 children evaluated for late talking, we generated note embeddings with BioClinicalBERT and encoded structured embeddings from demographics and medical codes. A note-based teacher model and a structured-only student model were jointly trained using contrastive learning and contrastive knowledge distillation loss, producing a strong classifier (AUROC = 0.985). Our proposed model reached an AUROC of 0.705, outperforming the structured-only baseline of 0.656. These results demonstrate that incorporating unstructured data during training enhances the model's capacity to identify task-relevant information within structured EHR data, enabling a deployable structured-only phenotype model.
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
