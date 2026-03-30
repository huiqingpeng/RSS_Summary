---
title: "A Lightweight, Transferable, and Self-Adaptive Framework for Intelligent DC Arc-Fault Detection in Photovoltaic Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25749"
published: "2026-03-30"
fetched: "2026-03-31T07:26:41.193386"
---

Electrical Engineering and Systems Science > Signal Processing
[Submitted on 16 Mar 2026]
Title:A Lightweight, Transferable, and Self-Adaptive Framework for Intelligent DC Arc-Fault Detection in Photovoltaic Systems
View PDF HTML (experimental)Abstract:Arc-fault circuit interrupters (AFCIs) are essential for mitigating fire hazards in residential photovoltaic (PV) systems, yet achieving reliable DC arc-fault detection under real-world conditions remains challenging. Spectral interference from inverter switching, hardware heterogeneity, operating-condition drift, and environmental noise collectively compromise conventional AFCI solutions. This paper proposes a lightweight, transferable, and self-adaptive learning-driven framework (LD-framework) for intelligent DC arc-fault detection. At the device level, LD-Spec learns compact spectral representations enabling efficient on-device inference and near-perfect arc discrimination. Across heterogeneous inverter platforms, LD-Align performs cross-hardware representation alignment to ensure robust detection despite hardware-induced distribution shifts. To address long-term evolution, LD-Adapt introduces a cloud-edge collaborative self-adaptive updating mechanism that detects unseen operating regimes and performs controlled model evolution. Extensive experiments involving over 53,000 labeled samples demonstrate near-perfect detection, achieving 0.9999 accuracy and 0.9996 F1-score. Across diverse nuisance-trip-prone conditions, including inverter start-up, grid transitions, load switching, and harmonic disturbances, the method achieves a 0% false-trip rate. Cross-hardware transfer shows reliable adaptation using only 0.5%-1% labeled target data while preserving source performance. Field adaptation experiments demonstrate recovery of detection precision from 21% to 95% under previously unseen conditions. These results indicate that the LD-framework enables a scalable, deployment-oriented AFCI solution maintaining highly reliable detection across heterogeneous devices and long-term operation.
Current browse context:
eess.SP
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
