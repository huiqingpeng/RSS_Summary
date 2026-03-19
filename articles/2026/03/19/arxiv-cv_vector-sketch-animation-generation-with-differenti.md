---
title: "Vector sketch animation generation with differentiable motion trajectories"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.25857"
published: "2026-03-19"
fetched: "2026-03-19T17:05:21.617291"
---

Computer Science > Graphics
[Submitted on 30 Sep 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Vector sketch animation generation with differentiable motion trajectories
View PDF HTML (experimental)Abstract:Sketching is a direct and inexpensive means of visual expression. Though image-based sketching has been well studied, video-based sketch animation generation is still very challenging due to the temporal coherence requirement. In this paper, we propose a novel end-to-end automatic generation approach for vector sketch animation. To solve the flickering issue, we introduce a Differentiable Motion Trajectory (DMT) representation that describes the frame-wise movement of stroke control points using differentiable polynomial-based trajectories. DMT enables global semantic gradient propagation across multiple frames, significantly improving the semantic consistency and temporal coherence, and producing high-framerate output. DMT employs a Bernstein basis to balance the sensitivity of polynomial parameters, thus achieving more stable optimization. Instead of implicit fields, we introduce sparse track points for explicit spatial modeling, which improves efficiency and supports long-duration video processing. Evaluations on DAVIS and LVOS datasets demonstrate the superiority of our approach over SOTA methods. Cross-domain validation on 3D models and text-to-video data confirms the robustness and compatibility of our approach.
Submission history
From: Jiazhou Chen [view email][v1] Tue, 30 Sep 2025 06:53:04 UTC (3,764 KB)
[v2] Wed, 18 Mar 2026 10:19:37 UTC (4,179 KB)
Current browse context:
cs.GR
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
