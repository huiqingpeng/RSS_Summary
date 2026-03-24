---
title: "Thinking in Different Spaces: Domain-Specific Latent Geometry Survives Cross-Architecture Translation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20406"
published: "2026-03-24"
fetched: "2026-03-25T07:08:56.594325"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Thinking in Different Spaces: Domain-Specific Latent Geometry Survives Cross-Architecture Translation
View PDF HTML (experimental)Abstract:We investigate whether independently trained language models converge to geometrically compatible latent representations, and whether this compatibility can be exploited to correct model behavior at inference time without any weight updates. We learn a linear projection matrix that maps activation vectors from a large teacher model into the coordinate system of a smaller student model, then intervene on the student's residual stream during generation by substituting its internal state with the translated teacher representation. Across a fully crossed experimental matrix of 20 heterogeneous teacher-student pairings spanning mixture-of-experts, dense, code-specialized, and synthetically trained architectures, the Ridge projection consistently achieves R^2 = 0.50 on verbal reasoning and R^2 = 0.40 on mathematical reasoning, collapsing to R^2 = -0.22 under permutation control and R^2 = 0.01 under L_1 regularization. Behavioral correction rates range from 14.0% to 50.0% on TruthfulQA (mean 25.2%) and from 8.5% to 43.3% on GSM8K arithmetic reasoning (mean 25.5%), demonstrating that the method generalizes across fundamentally different reasoning domains. We report a near-zero correlation between geometric alignment quality and behavioral correction rate (r = -0.07), revealing a dissociation between representation space fidelity and output space impact. Intervention strength is architecture-specific: student models exhibit characteristic sensitivity profiles that invert across domains, with the most steerable verbal student becoming the least steerable mathematical student. Finally, a double dissociation experiment conducted across all 20 model pairings confirms without exception that projection matrices collapse catastrophically when transferred across reasoning domains (mean R^2 = -3.83 in both transfer directions), establishing domain-specific subspace geometry as a universal property of LMs.
Submission history
From: Marcus Armstrong [view email][v1] Fri, 20 Mar 2026 18:26:23 UTC (2,265 KB)
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
