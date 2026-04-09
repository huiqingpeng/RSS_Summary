---
title: "Interference Suppression for Massive MU-MIMO Long-Term Beamforming with Matrix Inversion Approximation"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.06355"
published: "2026-04-09"
fetched: "2026-04-10T07:04:52.081364"
---

Electrical Engineering and Systems Science > Signal Processing
[Submitted on 7 Apr 2026]
Title:Interference Suppression for Massive MU-MIMO Long-Term Beamforming with Matrix Inversion Approximation
View PDF HTML (experimental)Abstract:Long-term beamforming (LTBF) is a widely-used scalable alternative to instantaneous multi-user MIMO processing that leverages slowly varying spatial channel statistics. VLSI implementations require matrix inversion that become computationally challenging for massive MIMO systems with large number of antennas. In this work, we show that dominant interferers significantly degrade the numerical conditioning of the LTBF covariance matrix, leading to severe performance loss in finite-precision implementations of polynomial and conjugate gradient (CG) based inversion methods. To address this issue, we propose a subspace nulling approach that operates solely on long-term channel statistics and acts as an implicit preconditioning step for LTBF. By projecting the received signal onto the orthogonal complement of the dominant interference subspace, the proposed method reduces the eigenvalue spread of the covariance matrix and improves numerical stability. Through ray-tracing simulations in a realistic 5G scenario, we demonstrate that the proposed method substantially reduces the number of CG iterations required to achieve near-optimal performance across floating-point and fixed-point implementations while preserving the low-overhead nature of LTBF.
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
