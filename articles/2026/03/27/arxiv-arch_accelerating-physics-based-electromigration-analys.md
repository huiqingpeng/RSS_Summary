---
title: "Accelerating Physics-Based Electromigration Analysis via Rational Krylov Subspaces"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2602.00330"
published: "2026-03-27"
fetched: "2026-03-28T07:08:14.780179"
---

Computer Science > Hardware Architecture
[Submitted on 30 Jan 2026 (v1), last revised 26 Mar 2026 (this version, v2)]
Title:Accelerating Physics-Based Electromigration Analysis via Rational Krylov Subspaces
View PDF HTML (experimental)Abstract:Electromigration (EM) induced stress evolution is a major reliability challenge in nanometer-scale VLSI interconnects. Accurate EM analysis requires solving stress-governing partial differential equations over large interconnect trees, which is computationally expensive using conventional finite-difference methods. This work proposes two fast EM stress analysis techniques based on rational Krylov subspace reduction. Unlike traditional Krylov methods that expand around zero frequency, rational Krylov methods enable expansion at selected time constants, aligning directly with metrics such as nucleation and steady-state times and producing compact reduced models with minimal accuracy loss. Two complementary frameworks are developed: a frequency-domain extended rational Krylov method, ExtRaKrylovEM, and a time-domain rational Krylov exponential integration method, EiRaKrylovEM. We show that the accuracy of both methods depends strongly on the choice of expansion point, or shift time, and demonstrate that effective shift times are typically close to times of interest such as nucleation or post-void steady state. Based on this observation, a coordinate descent optimization strategy is introduced to automatically determine optimal reduction orders and shift times for both nucleation and post-void phases. Experimental results on synthesized structures and industry-scale power grids show that the proposed methods achieve orders-of-magnitude improvements in efficiency and accuracy over finite-difference solutions. Using only 4 to 6 Krylov orders, the methods achieve sub-0.1 percent error in nucleation time and resistance change predictions while delivering 20 to 500 times speedup. In contrast, standard extended Krylov methods require more than 50 orders and still incur 10 to 20 percent nucleation time error, limiting their practicality for EM-aware optimization and stochastic EM analysis.
Submission history
From: Sheldon Tan [view email][v1] Fri, 30 Jan 2026 21:33:43 UTC (1,240 KB)
[v2] Thu, 26 Mar 2026 05:00:14 UTC (1,242 KB)
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
