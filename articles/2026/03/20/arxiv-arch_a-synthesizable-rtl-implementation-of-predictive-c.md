---
title: "A Synthesizable RTL Implementation of Predictive Coding Networks"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.18066"
published: "2026-03-20"
fetched: "2026-03-20T12:04:41.143396"
---

Computer Science > Neural and Evolutionary Computing
[Submitted on 18 Mar 2026]
Title:A Synthesizable RTL Implementation of Predictive Coding Networks
View PDF HTML (experimental)Abstract:Backpropagation has enabled modern deep learning but is difficult to realize as an online, fully distributed hardware learning system due to global error propagation, phase separation, and heavy reliance on centralized memory. Predictive coding offers an alternative in which inference and learning arise from local prediction-error dynamics between adjacent layers. This paper presents a digital architecture that implements a discrete-time predictive coding update directly in hardware. Each neural core maintains its own activity, prediction error, and synaptic weights, and communicates only with adjacent layers through hardwired connections. Supervised learning and inference are supported via a uniform per-neuron clamping primitive that enforces boundary conditions while leaving the internal update schedule unchanged. The design is a deterministic, synthesizable RTL substrate built around a sequential MAC datapath and a fixed finite-state schedule. Rather than executing a task-specific instruction sequence inside the learning substrate, the system evolves under fixed local update rules, with task structure imposed through connectivity, parameters, and boundary conditions. The contribution of this work is not a new learning rule, but a complete synthesizable digital substrate that executes predictive-coding learning dynamics directly in hardware.
Current browse context:
cs.NE
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
