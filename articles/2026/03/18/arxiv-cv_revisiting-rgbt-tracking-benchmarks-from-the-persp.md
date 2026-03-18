---
title: "Revisiting RGBT Tracking Benchmarks from the Perspective of Modality Validity: A New Benchmark, Problem, and Solution"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2405.00168"
published: "2026-03-18"
fetched: "2026-03-18T18:24:32.723490"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 30 Apr 2024 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Revisiting RGBT Tracking Benchmarks from the Perspective of Modality Validity: A New Benchmark, Problem, and Solution
View PDF HTML (experimental)Abstract:RGBT tracking draws increasing attention because its robustness in multi-modal warranting (MMW) scenarios, such as nighttime and adverse weather conditions, where relying on a single sensing modality fails to ensure stable tracking results. However, existing benchmarks predominantly contain videos collected in common scenarios where both RGB and thermal infrared (TIR) information are of sufficient quality. This weakens the representativeness of existing benchmarks in severe imaging conditions, leading to tracking failures in MMW scenarios. To bridge this gap, we present a new benchmark considering the modality validity, MV-RGBT, captured specifically from MMW scenarios where either RGB (extreme illumination) or TIR (thermal truncation) modality is invalid. Hence, it is further divided into two subsets according to the valid modality, offering a new compositional perspective for evaluation and providing valuable insights for future designs. Moreover, MV-RGBT is the most diverse benchmark of its kind, featuring 36 different object categories captured across 19 distinct scenes. Furthermore, considering severe imaging conditions in MMW scenarios, a new problem is posed in RGBT tracking, named `when to fuse', to stimulate the development of fusion strategies for such scenarios. To facilitate its discussion, we propose a new solution with a mixture of experts, named MoETrack, where each expert generates independent tracking results along with a confidence score. Extensive results demonstrate the significant potential of MV-RGBT in advancing RGBT tracking and elicit the conclusion that fusion is not always beneficial, especially in MMW scenarios. Besides, MoETrack achieves state-of-the-art results on several benchmarks, including MV-RGBT, GTOT, and LasHeR. Github: this https URL.
Submission history
From: Zhangyong Tang [view email][v1] Tue, 30 Apr 2024 19:37:58 UTC (5,874 KB)
[v2] Mon, 10 Mar 2025 08:06:33 UTC (4,583 KB)
[v3] Tue, 17 Mar 2026 06:23:04 UTC (5,872 KB)
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
