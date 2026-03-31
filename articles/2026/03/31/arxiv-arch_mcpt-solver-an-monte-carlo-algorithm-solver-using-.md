---
title: "MCPT-Solver: An Monte Carlo Algorithm Solver Using MTJ Devices for Particle Transport Problems"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.28042"
published: "2026-03-31"
fetched: "2026-04-01T07:16:08.432012"
---

Computer Science > Hardware Architecture
[Submitted on 30 Mar 2026]
Title:MCPT-Solver: An Monte Carlo Algorithm Solver Using MTJ Devices for Particle Transport Problems
View PDF HTML (experimental)Abstract:Monte Carlo particle transport problems play a vital role in scientific computing, but solving them on exiting von Neumann architectures suffers from random branching and irregular memory access, causing computing inefficiency due to a fundamental mismatch between stochastic algorithms and deterministic hardware. To bridge this gap, we propose MCPT-Solver, a spin-based hardware true random number generator (TRNG) with tunable output probability enabled by a Bayesian inference network architecture. It is dedicated for efficiently solving stochastic applications including Monte Carlo particle transport problems. First, we leverage the stochastic switching property of spin devices to provide a high-quality entropy source for the TRNG and achieve high generating throughput and process-voltage-temperature tolerance through optimized control logic and write mechanism designs. Next, we propose a hardware Bayesian inference network to enable probability-tunable random number outputs. Finally, we present a system-level simulation framework to evaluate MCPT-Solver. Experimental results show that MCPT-Solver achieves a mean squared error of 7.6e-6 for solving transport problems while demonstrating a dramatic acceleration effect over general-purpose processors. Additionally, the MCPT-Solver's throughput reaches 185 Mb/s with an area of 27.8 um2/bit and energy consumption of 8.6 pJ/bit, making it the first spin-based TRNG that offers both process-voltage-temperature tolerance and adjustable probability.
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
