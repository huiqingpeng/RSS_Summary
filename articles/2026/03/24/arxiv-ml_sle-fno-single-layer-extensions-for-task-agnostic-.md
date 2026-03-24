---
title: "SLE-FNO: Single-Layer Extensions for Task-Agnostic Continual Learning in Fourier Neural Operators"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20410"
published: "2026-03-24"
fetched: "2026-03-25T07:09:15.113170"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:SLE-FNO: Single-Layer Extensions for Task-Agnostic Continual Learning in Fourier Neural Operators
View PDF HTML (experimental)Abstract:Scientific machine learning is increasingly used to build surrogate models, yet most models are trained under a restrictive assumption in which future data follow the same distribution as the training set. In practice, new experimental conditions or simulation regimes may differ significantly, requiring extrapolation and model updates without re-access to prior data. This creates a need for continual learning (CL) frameworks that can adapt to distribution shifts while preventing catastrophic forgetting. Such challenges are pronounced in fluid dynamics, where changes in geometry, boundary conditions, or flow regimes induce non-trivial changes to the solution. Here, we introduce a new architecture-based approach (SLE-FNO) combining a Single-Layer Extension (SLE) with the Fourier Neural Operator (FNO) to support efficient CL. SLE-FNO was compared with a range of established CL methods, including Elastic Weight Consolidation (EWC), Learning without Forgetting (LwF), replay-based approaches, Orthogonal Gradient Descent (OGD), Gradient Episodic Memory (GEM), PiggyBack, and Low-Rank Approximation (LoRA), within an image-to-image regression setting. The models were trained to map transient concentration fields to time-averaged wall shear stress (TAWSS) in pulsatile aneurysmal blood flow. Tasks were derived from 230 computational fluid dynamics simulations grouped into four sequential and out-of-distribution configurations. Results show that replay-based methods and architecture-based approaches (PiggyBack, LoRA, and SLE-FNO) achieve the best retention, with SLE-FNO providing the strongest overall balance between plasticity and stability, achieving accuracy with zero forgetting and minimal additional parameters. Our findings highlight key differences between CL algorithms and introduce SLE-FNO as a promising strategy for adapting baseline models when extrapolation is required.
Submission history
From: Amirhossein Arzani [view email][v1] Fri, 20 Mar 2026 18:30:38 UTC (9,268 KB)
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
