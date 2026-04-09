---
title: "Conformal Margin Risk Minimization: An Envelope Framework for Robust Learning under Label Noise"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06468"
published: "2026-04-09"
fetched: "2026-04-10T07:05:00.107862"
---

Computer Science > Machine Learning
[Submitted on 7 Apr 2026]
Title:Conformal Margin Risk Minimization: An Envelope Framework for Robust Learning under Label Noise
View PDFAbstract:Most methods for learning with noisy labels require privileged knowledge such as noise transition matrices, clean subsets or pretrained feature extractors, resources typically unavailable when robustness is most needed. We propose Conformal Margin Risk Minimization (CMRM), a plug-and-play envelope framework that improves any classification loss under label noise by adding a single quantile-calibrated regularization term, with no privileged knowledge or training pipeline modification. CMRM measures the confidence margin between the observed label and competing labels, and thresholds it with a conformal quantile estimated per batch to focus training on high-margin samples while suppressing likely mislabeled ones. We derive a learning bound for CMRM under arbitrary label noise requiring only mild regularity of the margin distribution. Across five base methods and six benchmarks with synthetic and real-world noise, CMRM consistently improves accuracy (up to +3.39%), reduces conformal prediction set size (up to -20.44%) and does not hurt under 0% noise, showing that CMRM captures a method-agnostic uncertainty signal that existing mechanisms did not exploit.
Current browse context:
cs.LG
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
