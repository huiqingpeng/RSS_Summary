---
title: "VeRA+: Vector-Based Lightweight Digital Compensation for Drift-Resilient RRAM In-Memory Computing"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.26016"
published: "2026-03-30"
fetched: "2026-03-31T07:05:45.113696"
---

Computer Science > Hardware Architecture
[Submitted on 27 Mar 2026]
Title:VeRA+: Vector-Based Lightweight Digital Compensation for Drift-Resilient RRAM In-Memory Computing
View PDF HTML (experimental)Abstract:RRAM-based in-memory computing (IMC) offers high energy efficiency but suffers from conductance drift that severely degrades long-term accuracy. Existing approaches including retraining, noise-aware training, and Batch Normalization (BN)-based calibration either require RRAM rewriting, demand large storage overhead, or rely on online correction. We propose VeRA+, a lightweight drift compensation framework that reuses shared projection matrices and introduces only two compact drift-specific vectors per drift level. A drift-aware scheduling algorithm offline-trains a small set of VeRA+ parameters and selects the appropriate set over time without any on-chip retraining or data replay. VeRA+ preserves up to 99.77% of the drift-free accuracy after ten years of simulated drift and reduces storage overhead by more than three orders of magnitude compared with BN-based calibration. To validate VeRA+ under realistic device behavior, we extract one-week drift statistics from measurements on our fabricated 1T1R RRAM devices and use them to simulate realistic drifted weights. Under these measured drift conditions, VeRA+ achieves accuracy close to the drift-free baseline, providing an efficient and practical solution for long-term drift resilience in RRAM-IMC.
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
