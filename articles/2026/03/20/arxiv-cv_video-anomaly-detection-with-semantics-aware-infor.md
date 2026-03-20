---
title: "Video Anomaly Detection with Semantics-Aware Information Bottleneck"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2506.02535"
published: "2026-03-20"
fetched: "2026-03-20T16:11:46.668606"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 3 Jun 2025 (v1), last revised 19 Mar 2026 (this version, v4)]
Title:Video Anomaly Detection with Semantics-Aware Information Bottleneck
View PDF HTML (experimental)Abstract:Semi-supervised video anomaly detection methods face two critical challenges: (1) Strong generalization blurs the boundary between normal and abnormal patterns. Although existing approaches attempt to alleviate this issue using memory modules, their rigid prototype-matching process limits adaptability to diverse scenarios; (2) Relying solely on low-level appearance and motion cues makes it difficult to perceive high-level semantic anomalies in complex scenes. To address these limitations, we propose SIB-VAD, a novel framework based on adaptive information bottleneck filtering and semantic-aware enhancement. We propose the Sparse Feature Filtering Module (SFFM) to replace traditional memory modules. It compresses normal features directly into a low-dimensional manifold based on the information bottleneck principle and uses an adaptive routing mechanism to dynamically select the most suitable normal bottleneck subspace. Trained only on normal data, SFFMs only learn normal low-dimensional manifolds, while abnormal features deviate and are effectively filtered. Unlike memory modules, SFFM directly removes abnormal information and adaptively handles scene variations. To improve semantic awareness, we further design a multimodal prediction framework that jointly models appearance, motion, and semantics. Through multimodal consistency constraints and joint error computation, it achieves more robust VAD performance. Experimental results validate the effectiveness of our feature filtering paradigm based on semantics-aware information bottleneck. Project page at this https URL
Submission history
From: Juntong Li [view email][v1] Tue, 3 Jun 2025 07:14:57 UTC (1,232 KB)
[v2] Wed, 4 Jun 2025 06:36:25 UTC (1,232 KB)
[v3] Mon, 1 Dec 2025 09:34:51 UTC (1,175 KB)
[v4] Thu, 19 Mar 2026 05:23:18 UTC (1,980 KB)
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
