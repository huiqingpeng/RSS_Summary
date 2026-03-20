---
title: "ODE-Constrained Generative Modeling of Cardiac Dynamics for 12-Lead ECG Synthesis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2409.17833"
published: "2026-03-20"
fetched: "2026-03-20T14:04:49.173379"
---

Computer Science > Machine Learning
[Submitted on 26 Sep 2024 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:ODE-Constrained Generative Modeling of Cardiac Dynamics for 12-Lead ECG Synthesis
View PDF HTML (experimental)Abstract:Generating realistic training data for supervised learning remains a significant challenge in artificial intelligence, particularly in domains where large, expert-labeled datasets are scarce or costly to obtain. This is especially true for electrocardiograms (ECGs), where privacy constraints, class imbalance, and the need for physician annotation limit the availability of labeled 12-lead recordings, motivating the development of high-fidelity synthetic ECG data. The primary challenge in this task lies in accurately modeling the intricate biological and physiological interactions among different ECG leads. Although mathematical process models have shed light on these dynamics, effectively incorporating this understanding into generative models is not straightforward. We introduce an innovative method that employs ordinary differential equations (ODEs) to enhance the fidelity of 12-lead ECG data generation. This approach integrates cardiac dynamics directly into the generative optimization process via a novel Euler Loss, producing biologically plausible data that respects real-world variability and inter-lead constraints. Empirical analysis on the G12EC and PTB-XL datasets demonstrates that augmenting training data with MultiODE-GAN yields consistent, statistically significant improvements in specificity across multiple cardiac abnormalities. This highlights the value of enforcing physiological coherence in synthetic medical data.
Submission history
From: Yakir Yehuda [view email][v1] Thu, 26 Sep 2024 13:35:42 UTC (239 KB)
[v2] Thu, 19 Mar 2026 14:59:29 UTC (155 KB)
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
