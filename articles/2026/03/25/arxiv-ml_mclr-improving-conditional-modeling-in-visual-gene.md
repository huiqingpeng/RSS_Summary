---
title: "MCLR: Improving Conditional Modeling in Visual Generative Models via Inter-Class Likelihood-Ratio Maximization and Establishing the Equivalence between Classifier-Free Guidance and Alignment Objectives"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22364"
published: "2026-03-25"
fetched: "2026-03-26T07:13:35.701222"
---

Computer Science > Machine Learning
[Submitted on 23 Mar 2026]
Title:MCLR: Improving Conditional Modeling in Visual Generative Models via Inter-Class Likelihood-Ratio Maximization and Establishing the Equivalence between Classifier-Free Guidance and Alignment Objectives
View PDFAbstract:Diffusion models have achieved state-of-the-art performance in generative modeling, but their success often relies heavily on classifier-free guidance (CFG), an inference-time heuristic that modifies the sampling trajectory. From a theoretical perspective, diffusion models trained with standard denoising score matching (DSM) are expected to recover the target data distribution, raising the question of why inference-time guidance is necessary in practice. In this work, we ask whether the DSM training objective can be modified in a principled manner such that standard reverse-time sampling, without inference-time guidance, yields effects comparable to CFG. We identify insufficient inter-class separation as a key limitation of standard diffusion models. To address this, we propose MCLR, a principled alignment objective that explicitly maximizes inter-class likelihood-ratios during training. Models fine-tuned with MCLR exhibit CFG-like improvements under standard sampling, achieving comparable qualitative and quantitative gains without requiring inference-time guidance. Beyond empirical benefits, we provide a theoretical result showing that the CFG-guided score is exactly the optimal solution to a weighted MCLR objective. This establishes a formal equivalence between classifier-free guidance and alignment-based objectives, offering a mechanistic interpretation of CFG.
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
