---
title: "Lipschitz-Based Robustness Certification Under Floating-Point Execution"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.13334"
published: "2026-03-18"
fetched: "2026-03-18T17:06:21.243767"
---

Computer Science > Machine Learning
[Submitted on 6 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Lipschitz-Based Robustness Certification Under Floating-Point Execution
View PDF HTML (experimental)Abstract:Sensitivity-based robustness certification has emerged as a practical approach for certifying neural network robustness, including in settings that require verifiable guarantees. A key advantage of these methods is that certification is performed by concrete numerical computation (rather than symbolic reasoning) and scales efficiently with network size. However, as with the vast majority of prior work on robustness certification and verification, the soundness of these methods is typically proved with respect to a semantic model that assumes exact real arithmetic. In reality deployed neural network implementations execute using floating-point arithmetic. This mismatch creates a semantic gap between certified robustness properties and the behaviour of the executed system.
As motivating evidence, we exhibit concrete counterexamples showing that real arithmetic robustness guarantees can fail under floating-point execution, even for previously verified certifiers, with discrepancies becoming pronounced at lower-precision formats such as float16. We then develop a formal, compositional theory relating real arithmetic Lipschitz-based sensitivity bounds to the sensitivity of floating-point execution under standard rounding-error models, specialised to feed-forward neural networks with ReLU activations. We derive sound conditions for robustness under floating-point execution, including bounds on certificate degradation and sufficient conditions for the absence of overflow. We formalize the theory and its main soundness results, and implement an executable certifier based on these principles, which we empirically evaluate to demonstrate its practicality.
Submission history
From: Toby Murray [view email][v1] Fri, 6 Mar 2026 06:13:24 UTC (220 KB)
[v2] Tue, 17 Mar 2026 04:15:22 UTC (221 KB)
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
