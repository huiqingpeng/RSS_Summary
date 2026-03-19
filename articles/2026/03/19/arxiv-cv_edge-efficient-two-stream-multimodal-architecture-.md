---
title: "Edge-Efficient Two-Stream Multimodal Architecture for Non-Intrusive Bathroom Fall Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17069"
published: "2026-03-19"
fetched: "2026-03-19T15:04:40.674294"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Edge-Efficient Two-Stream Multimodal Architecture for Non-Intrusive Bathroom Fall Detection
View PDF HTML (experimental)Abstract:Falls in wet bathroom environments are a major safety risk for seniors living alone. Recent work has shown that mmWave-only, vibration-only, and existing multimodal schemes, such as vibration-triggered radar activation, early feature concatenation, and decision-level score fusion, can support privacy-preserving, non-intrusive fall detection. However, these designs still treat motion and impact as loosely coupled streams, depending on coarse temporal alignment and amplitude thresholds, and do not explicitly encode the causal link between radar-observed collapse and floor impact or address timing drift, object drop confounders, and latency and energy constraints on low-power edge devices. To this end, we propose a two-stream architecture that encodes radar signals with a Motion--Mamba branch for long-range motion patterns and processes floor vibration with an Impact--Griffin branch that emphasizes impact transients and cross-axis coupling. Cross-conditioned fusion uses low-rank bilinear interaction and a Switch--MoE head to align motion and impact tokens and suppress object-drop confounders. The model keeps inference cost suitable for real-time execution on a Raspberry Pi 4B gateway. We construct a bathroom fall detection benchmark dataset with frame-level annotations, comprising more than 3~h of synchronized mmWave radar and triaxial vibration recordings across eight scenarios under running water, together with subject-independent training, validation, and test splits. On the test split, our model attains 96.1% accuracy, 94.8% precision, 88.0% recall, a 91.1% macro F1 score, and an AUC of 0.968. Compared with the strongest baseline, it improves accuracy by 2.0 percentage points and fall recall by 1.3 percentage points, while reducing latency from 35.9 ms to 15.8 ms and lowering energy per 2.56 s window from 14200 mJ to 10750 mJ on the Raspberry Pi 4B gateway.
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
