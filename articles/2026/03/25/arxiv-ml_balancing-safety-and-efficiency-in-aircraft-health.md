---
title: "Balancing Safety and Efficiency in Aircraft Health Diagnosis: A Task Decomposition Framework with Heterogeneous Long-Micro Scale Cascading and Knowledge Distillation-based Interpretability"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22885"
published: "2026-03-25"
fetched: "2026-03-26T07:17:54.692743"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Balancing Safety and Efficiency in Aircraft Health Diagnosis: A Task Decomposition Framework with Heterogeneous Long-Micro Scale Cascading and Knowledge Distillation-based Interpretability
View PDF HTML (experimental)Abstract:Whole-aircraft diagnosis for general aviation faces threefold challenges: data uncertainty, task heterogeneity, and computational inefficiency. Existing end-to-end approaches uniformly model health discrimination and fault characterization, overlooking intrinsic receptive field conflicts between global context modeling and local feature extraction, while incurring prohibitive training costs under severe class imbalance. To address these, this study proposes the Diagnosis Decomposition Framework (DDF), explicitly decoupling diagnosis into Anomaly Detection (AD) and Fault Classification (FC) subtasks via the Long-Micro Scale Diagnostician (LMSD). Employing a "long-range global screening and micro-scale local precise diagnosis" strategy, LMSD utilizes Convolutional Tokenizer with Multi-Head Self-Attention (ConvTokMHSA) for global operational pattern discrimination and Multi-Micro Kernel Network (MMK Net) for local fault feature extraction. Decoupled training separates "large-sample lightweight" and "small-sample complex" optimization pathways, significantly reducing computational overhead. Concurrently, Keyness Extraction Layer (KEL) via knowledge distillation furnishes physically traceable explanations for two-stage decisions, materializing interpretability-by-design. Experiments on the NGAFID real-world aviation dataset demonstrate approximately 4-8% improvement in Multi-Class Weighted Penalty Metric (MCWPM) over baselines with substantially reduced training time, validating comprehensive advantages in task adaptability, interpretability, and efficiency. This provides a deployable methodology for general aviation health management.
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
