---
title: "Increasing the Energy-Efficiency of Wearables Using Low-Precision Posit Arithmetic with PHEE"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2501.18253"
published: "2026-04-09"
fetched: "2026-04-10T07:04:52.596516"
---

Computer Science > Hardware Architecture
[Submitted on 30 Jan 2025 (v1), last revised 8 Apr 2026 (this version, v2)]
Title:Increasing the Energy-Efficiency of Wearables Using Low-Precision Posit Arithmetic with PHEE
View PDF HTML (experimental)Abstract:Wearable edge AI biomedical devices are increasingly being used for continuous patient health monitoring, enabling real-time insights and extended data collection without the need for prolonged hospital stays. These devices must be energy efficient to minimize battery size, improve comfort, and reduce recharging intervals. This paper investigates the use of specialized low-precision arithmetic formats to enhance the energy efficiency of edge AI biomedical wearables. Specifically, we explore posit arithmetic, a floating-point-like representation, in two biomedical applications that leverage supervised and unsupervised learning algorithms: cough detection for chronic cough monitoring and R peak detection in ECG analysis. Our results reveal that 16-bit posits can replace 32-bit IEEE 754 floating point numbers with minimal accuracy loss in cough detection. For R peak detection, posit arithmetic achieves satisfactory accuracy with as few as 10 or 8 bits, compared to the 16-bit requirement for floating-point formats.
To validate these findings beyond algorithm-level simulations, we introduce PHEE, a modular and extensible architecture that integrates the Coprosit posit coprocessor within a RISC-V-based system. Using the X-HEEP framework, PHEE serves as a proof-of-concept platform to quantify the practical energy benefits of low-precision posits in edge AI systems. Post-synthesis results targeting 16 nm TSMC technology show that the posit hardware targeting these ML-based biomedical applications can be 38% smaller and consume up to 42.3% less power at the functional unit level, with no performance compromise. These findings establish the potential of low-precision posit arithmetic to significantly improve the energy efficiency of edge AI biomedical devices.
Submission history
From: David Mallasén [view email][v1] Thu, 30 Jan 2025 10:35:45 UTC (297 KB)
[v2] Wed, 8 Apr 2026 14:43:55 UTC (209 KB)
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
