---
title: "CPU Simulation Using Two-Phase Stratified Sampling"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.22605"
published: "2026-03-25"
fetched: "2026-03-26T07:05:53.628010"
---

Computer Science > Hardware Architecture
[Submitted on 23 Mar 2026]
Title:CPU Simulation Using Two-Phase Stratified Sampling
View PDFAbstract:Simulation remains a cornerstone of computer architecture research, yet full end-to-end application execution is prohibitively time-consuming. The industry-standard solution, SimPoint, mitigates this cost by selecting a small number of representative code regions that capture program phase behavior. In this work, we take a fresh look at phase behavior in the SPEC CPU 2017 Integer suite to assess how pronounced such behavior truly is and what accuracy can be expected from typical SimPoint usage. Based on previously published data, we argue that common SimPoint counts can induce substantial estimation errors. To explore this further, we recast SimPoint as a stratified sampling problem, which enables the derivation of a conservative confidence interval. The analysis indicates that significant errors are expected, and our empirical analysis confirms this: with 20 SimPoints, two applications exhibit 40-60% performance prediction error.
We decompose SimPoint into its two fundamental components - stratification (clustering) and sample-unit selection (centroid choice) - and analyze their individual effects on accuracy. We then extend the approach into a two-phase (double) sampling scheme, in which a large preliminary random sample enables improved stratification and more representative region selection. Using this method, the maximum per-application error drops to 3%. Finally, we demonstrate that the proposed two-phase stratified framework achieves an order-of-magnitude reduction in required sample size compared to simple random sampling while maintaining a tight analytical confidence interval, suggesting a practical path toward statistically grounded and efficient architectural simulation.
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
