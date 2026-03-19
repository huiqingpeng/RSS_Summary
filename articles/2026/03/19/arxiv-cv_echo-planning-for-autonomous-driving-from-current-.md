---
title: "Echo Planning for Autonomous Driving: From Current Observations to Future Trajectories and Back"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2505.18945"
published: "2026-03-19"
fetched: "2026-03-19T16:24:22.796019"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 May 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Echo Planning for Autonomous Driving: From Current Observations to Future Trajectories and Back
View PDF HTML (experimental)Abstract:Modern end-to-end autonomous driving systems suffer from a critical limitation: their planners lack mechanisms to enforce temporal consistency between predicted trajectories and evolving scene dynamics. This absence of self-supervision allows early prediction errors to compound catastrophically over time. We introduce Echo Planning (EchoP), a new self-correcting framework that establishes an end-to-end Current - Future - Current (CFC) cycle to harmonize trajectory prediction with scene coherence. Our key insight is that plausible future trajectories should be bi-directionally consistent, i.e., not only generated from current observations but also capable of reconstructing them. The CFC mechanism first predicts future trajectories from the Bird's-Eye-View (BEV) scene representation, then inversely maps these trajectories back to estimate the current BEV state. By enforcing consistency between the original and reconstructed BEV representations through a cycle loss, the framework intrinsically penalizes physically implausible or misaligned trajectories. Experiments on nuScenes show that the proposed method yields competitive performance, reducing L2 error (Avg) by -0.04 m and collision rate by -0.12% compared to one-shot planners. Moreover, EchoP seamlessly extends to closed-loop evaluation, i.e., Bench2Drive, attaining a 26.54% success rate. Notably, EchoP requires no additional supervision: the CFC cycle acts as an inductive bias that stabilizes long-horizon planning. Overall, EchoP offers a simple, deployable pathway to improve reliability in safety-critical autonomous driving.
Submission history
From: Jintao Sun [view email][v1] Sun, 25 May 2025 02:44:06 UTC (5,462 KB)
[v2] Wed, 18 Mar 2026 05:39:35 UTC (7,637 KB)
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
