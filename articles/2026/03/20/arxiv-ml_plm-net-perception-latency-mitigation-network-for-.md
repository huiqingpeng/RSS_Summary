---
title: "PLM-Net: Perception Latency Mitigation Network for Vision-Based Lateral Control of Autonomous Vehicles"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2407.16740"
published: "2026-03-20"
fetched: "2026-03-20T14:14:09.030170"
---

Computer Science > Robotics
[Submitted on 23 Jul 2024 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:PLM-Net: Perception Latency Mitigation Network for Vision-Based Lateral Control of Autonomous Vehicles
View PDFAbstract:This study introduces the Perception Latency Mitigation Network (PLM-Net), a modular deep learning framework designed to mitigate perception latency in vision-based imitation-learning lane-keeping systems. Perception latency, defined as the delay between visual sensing and steering actuation, can degrade lateral tracking performance and steering stability. While delay compensation has been extensively studied in classical predictive control systems, its treatment within vision-based imitation-learning architectures under constant and time-varying perception latency remains limited. Rather than reducing latency itself, PLM-Net mitigates its effect on control performance through a plug-in architecture that preserves the original control pipeline. The framework consists of a frozen Base Model (BM), representing an existing lane-keeping controller, and a Timed Action Prediction Model (TAPM), which predicts future steering actions corresponding to discrete latency conditions. Real-time mitigation is achieved by interpolating between model outputs according to the measured latency value, enabling adaptation to both constant and time-varying latency. The framework is evaluated in a closed-loop deterministic simulation environment under fixed-speed conditions to isolate the impact of perception latency. Results demonstrate significant reductions in steering error under multiple latency settings, achieving up to 62% and 78% reductions in Mean Absolute Error (MAE) for constant and time-varying latency cases, respectively. These findings demonstrate the architectural feasibility of modular latency mitigation for vision-based lateral control under controlled simulation settings. The project page including video demonstrations, code, and dataset is publicly released.
Submission history
From: Aws Khalil [view email][v1] Tue, 23 Jul 2024 17:41:13 UTC (10,563 KB)
[v2] Wed, 18 Mar 2026 20:43:30 UTC (11,518 KB)
Current browse context:
cs.RO
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
