---
title: "Probabilistic approximate optimization using single-photon avalanche diode arrays"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2602.13943"
published: "2026-03-19"
fetched: "2026-03-19T12:04:27.468857"
---

Computer Science > Emerging Technologies
[Submitted on 15 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Probabilistic approximate optimization using single-photon avalanche diode arrays
View PDF HTML (experimental)Abstract:Combinatorial optimization problems are central to science and engineering and specialized hardware from quantum annealers to classical Ising machines are being actively developed to address them. These systems typically sample from a fixed energy landscape defined by the problem Hamiltonian encoding the discrete optimization problem. The recently introduced Probabilistic Approximate Optimization Algorithm (PAOA) takes a different approach: it treats the optimization landscape itself as variational, iteratively learning circuit parameters from samples. Here, we demonstrate PAOA on a 64$\times$64 perimeter-gated single-photon avalanche diode (pgSPAD) array fabricated in 0.35 $\mu$m CMOS, the first realization of the algorithm using intrinsically stochastic nanodevices. Each p-bit exhibits a device-specific, asymmetric (Gompertz-type) activation function due to dark-count variability. Rather than calibrating devices to enforce a uniform symmetric (logistic/tanh) activation, PAOA learns around device variations, absorbing residual activation and other mismatches into the variational parameters. On canonical 26-spin Sherrington-Kirkpatrick instances, PAOA achieves high approximation ratios with $2p$ parameters ($p$ up to 17 layers), and pgSPAD-based inference closely tracks CPU simulations. These results show that variational learning can accommodate the non-idealities inherent to nanoscale devices, suggesting a practical path toward larger-scale, CMOS-compatible probabilistic computers.
Submission history
From: Ziyad Alswaidan [view email][v1] Sun, 15 Feb 2026 00:54:21 UTC (46,154 KB)
[v2] Wed, 18 Mar 2026 02:19:08 UTC (46,154 KB)
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
