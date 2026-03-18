---
title: "OrthoAI v2: From Single-Agent Segmentation to Dual-Agent Treatment Planning for Clear Aligners"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15663"
published: "2026-03-18"
fetched: "2026-03-18T17:18:01.004306"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 10 Mar 2026]
Title:OrthoAI v2: From Single-Agent Segmentation to Dual-Agent Treatment Planning for Clear Aligners
View PDF HTML (experimental)Abstract:We present OrthoAI v2, the second iteration of our open-source pipeline for AI-assisted orthodontic treatment planning with clear aligners, substantially extending the single-agent framework previously introduced. The first version established a proof-of-concept based on Dynamic Graph Convolutional Neural Networks (\dgcnn{}) for tooth segmentation but was limited to per-tooth centroid extraction, lacked landmark-level precision, and produced a scalar quality score without staging simulation. \vtwo{} addresses all three limitations through three principal contributions: (i)~a second agent adopting the Conditioned Heatmap Regression Methodology (\charm{})~\cite{rodriguez2025charm} for direct, segmentation-free dental landmark detection, fused with Agent~1 via a confidence-weighted orchestrator in three modes (parallel, sequential, single-agent); (ii)~a composite six-category biomechanical scoring model (biomechanics $\times$ 0.30 + staging $\times$ 0.20 + attachments $\times$ 0.15 + IPR $\times$ 0.10 + occlusion $\times$ 0.10 + predictability $\times$ 0.15) replacing the binary pass/fail check of v1; (iii)~a multi-frame treatment simulator generating $F = A \times r$ temporally coherent 6-DoF tooth trajectories via SLERP interpolation and evidence-based staging rules, enabling ClinCheck 4D visualisation. On a synthetic benchmark of 200 crowding scenarios, the parallel ensemble of OrthoAI v2 reaches a planning quality score of $92.8 \pm 4.1$ vs.\ $76.4 \pm 8.3$ for OrthoAI v1, a $+21\%$ relative gain, while maintaining full CPU deployability ($4.2 \pm 0.8$~s).
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
