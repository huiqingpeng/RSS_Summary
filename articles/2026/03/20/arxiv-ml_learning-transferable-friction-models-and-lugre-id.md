---
title: "Learning Transferable Friction Models and LuGre Identification Via Physics-Informed Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2504.12441"
published: "2026-03-20"
fetched: "2026-03-20T14:15:22.581729"
---

Computer Science > Robotics
[Submitted on 16 Apr 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Learning Transferable Friction Models and LuGre Identification Via Physics-Informed Neural Networks
View PDF HTML (experimental)Abstract:Accurately modeling friction in robotics remains a core challenge, as robotics simulators like MuJoCo and PyBullet use simplified friction models or heuristics to balance computational efficiency with accuracy, where these simplifications and approximations can lead to substantial differences between simulated and physical performance. In this paper, we present a physics-informed friction estimation framework that enables the integration of well-established friction models with learnable components, requiring only minimal, generic measurement data. Our approach enforces physical consistency yet retains the flexibility to capture complex friction phenomena. We demonstrate, on an underactuated and nonlinear system, that the learned friction models, trained solely on small and noisy datasets, accurately reproduce dynamic friction properties with significantly higher fidelity than the simplified models commonly used in robotics simulators. Crucially, we show that our approach enables the learned models to be transferable to systems they are not trained on. This ability to generalize across multiple systems streamlines friction modeling for complex, underactuated tasks, offering a scalable and interpretable path toward improving friction model accuracy in robotics and control.
Submission history
From: Asutay Ozmen [view email][v1] Wed, 16 Apr 2025 19:15:48 UTC (1,262 KB)
[v2] Wed, 18 Mar 2026 22:32:14 UTC (1,648 KB)
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
