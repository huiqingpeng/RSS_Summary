---
title: "CogGen: Cognitive-Load-Informed Fully Unsupervised Deep Generative Modeling for Compressively Sampled MRI Reconstruction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.04438"
published: "2026-03-19"
fetched: "2026-03-19T14:18:58.647003"
---

Electrical Engineering and Systems Science > Image and Video Processing
[Submitted on 20 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:CogGen: Cognitive-Load-Informed Fully Unsupervised Deep Generative Modeling for Compressively Sampled MRI Reconstruction
View PDF HTML (experimental)Abstract:Fully unsupervised deep generative modeling (FU-DGM) is promising for compressively sampled MRI (CS-MRI) when training data or compute are limited. Classical FU-DGMs such as DIP and INR rely on architectural priors, but the ill-conditioned inverse problem often demands many iterations and easily overfits measurement noise. We propose CogGen, a cognitive-load-informed FU-DGM that casts CS-MRI as staged inversion and regulates task-side "cognitive load" by progressively scheduling intrinsic difficulty and extraneous interference. CogGen replaces uniform data fitting with an easy-to-hard k-space weighting/selection strategy: early iterations emphasize low-frequency, high-SNR, structure-dominant samples, while higher-frequency or noise-dominated measurements are introduced later. We realize this schedule through self-paced curriculum learning (SPCL) with complementary criteria: a student mode that reflects what the model can currently learn and a teacher mode that indicates what it should follow, supporting both soft weighting and hard selection. Experiments and analyses show that CogGen-DIP and CogGen-INR improve reconstruction fidelity and convergence behavior compared with strong unsupervised baselines and competitive supervised pipelines.
Submission history
From: Qingyong Zhu [view email][v1] Fri, 20 Feb 2026 07:20:52 UTC (42,073 KB)
[v2] Wed, 18 Mar 2026 08:50:42 UTC (42,073 KB)
Current browse context:
eess.IV
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
