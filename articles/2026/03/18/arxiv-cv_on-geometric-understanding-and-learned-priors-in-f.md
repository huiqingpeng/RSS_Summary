---
title: "On Geometric Understanding and Learned Priors in Feed-forward 3D Reconstruction Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.11508"
published: "2026-03-18"
fetched: "2026-03-18T18:31:22.770843"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 12 Dec 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:On Geometric Understanding and Learned Priors in Feed-forward 3D Reconstruction Models
View PDF HTML (experimental)Abstract:Feed-forward 3D reconstruction models such as DUSt3R, VGGT, and Depth Anything 3 (DA3) are transformer-based foundation models that infer camera geometry and dense scene structure in a single forward pass. Trained at scale in a supervised fashion, they raise a central question: do these models build upon geometric principles akin to traditional multi-view pipelines, or do they primarily rely on learned priors arising from the large-scale training setup? We find that epipolar geometry emerges within the intermediate layers of all three models and is causally linked to correspondence patterns in attention heads. To study this, we perform a systematic analysis of their internal representations across three real-world datasets and a controlled synthetic dataset. We quantify geometric understanding by probing intermediate features, analyzing attention patterns to identify correspondence matching patterns, and performing targeted interventions at the attention level. Further, we assess the role of learned priors by applying challenging input-level perturbations, such as occlusions, scene ambiguities, and varying camera configurations, and compare them against classical multi-stage reconstruction pipelines.
Submission history
From: Jelena Bratulić [view email][v1] Fri, 12 Dec 2025 12:11:57 UTC (6,761 KB)
[v2] Tue, 17 Mar 2026 16:34:48 UTC (45,080 KB)
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
