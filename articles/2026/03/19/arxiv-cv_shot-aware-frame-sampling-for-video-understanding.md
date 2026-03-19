---
title: "Shot-Aware Frame Sampling for Video Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17374"
published: "2026-03-19"
fetched: "2026-03-19T15:09:21.916167"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Shot-Aware Frame Sampling for Video Understanding
View PDF HTML (experimental)Abstract:Video frame sampling is essential for efficient long-video understanding with Vision-Language Models (VLMs), since dense inputs are costly and often exceed context limits. Yet when only a small number of frames can be retained, existing samplers often fail to balance broad video coverage with brief but critical events, which can lead to unreliable downstream predictions. To address this issue, we present InfoShot, a task-agnostic, shot-aware frame sampler for long-video understanding. InfoShot first partitions a video into semantically consistent shots, and then selects two complementary keyframes from each shot: one to represent the main content and one to capture unusual within-shot changes. This design is guided by an information-theoretic objective that encourages the sampled set to retain high information about both shot structure and sparse within-shot deviations. In this way, it improves the chance of preserving both overall video context and short decision-critical moments without requiring any retraining. To better evaluate such short-lived events, we further introduce SynFlash, a synthetic benchmark with controllable sub-second anomaly patterns and frame-level ground truth, and we also evaluate InfoShot on existing anomaly datasets and general video understanding tasks. Experiments show that InfoShot improves anomaly hit rate and downstream Video-QA accuracy under frame number constraints, while matching or outperforming strong baselines on standard video understanding benchmarks.
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
