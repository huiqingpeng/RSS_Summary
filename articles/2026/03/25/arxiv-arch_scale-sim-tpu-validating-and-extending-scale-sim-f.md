---
title: "SCALE-Sim TPU: Validating and Extending SCALE-Sim for TPUs"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.22535"
published: "2026-03-25"
fetched: "2026-03-26T07:05:26.947030"
---

Computer Science > Hardware Architecture
[Submitted on 23 Mar 2026]
Title:SCALE-Sim TPU: Validating and Extending SCALE-Sim for TPUs
View PDF HTML (experimental)Abstract:Cycle-accurate simulators are widely used to study systolic accelerators, yet their accuracy and usability are often limited by weak validation against real hardware and poor integration with modern ML compiler stacks. This paper presents SCALE-Sim TPU, a validated and extended version of SCALE-Sim v3 for TPU-style accelerators. Specifically, we make three contributions: (1) We validate SCALE-Sim's systolic GEMM model against measurements on Google TPU v4 and show that simulated cycle counts exhibit a strong linear correlation with hardware latency, enabling a simple cycle-to-latency mapping. (2) We introduce lightweight learned latency models for non-systolic elementwise operations, achieving median relative errors below 3 percent using only tensor size and shape, substantially improving end-to-end latency estimation. (3) We integrate a StableHLO-based frontend that allows workloads from modern ML frameworks such as JAX and PyTorch to be simulated directly via a unified compiler IR. Together, these contributions improve the fidelity, coverage, and practicality of cycle-accurate simulation for whole-model performance analysis on TPUs.
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
