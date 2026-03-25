---
title: "CPU Simulation with Ranked Set Sampling and Repeated Subsampling"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.22598"
published: "2026-03-25"
fetched: "2026-03-26T07:05:45.278927"
---

Computer Science > Hardware Architecture
[Submitted on 23 Mar 2026]
Title:CPU Simulation with Ranked Set Sampling and Repeated Subsampling
View PDFAbstract:Computer system simulation studies routinely rely on executing a limited number of short application regions, since full end-to-end simulation is prohibitively time-consuming. To preserve representativeness, existing methods employ either random sampling or phase-based characterization to identify representative regions.
In this work, we revisit random sampling in the context of computer architecture simulation. To assess how the confidence level varies with different micro-architectural configurations, we examine how the sample standard deviation relates to the sample mean. We show that the ranked set sampling (RSS) technique - well established in the statistical literature - maps naturally to architectural simulation and yields significantly tighter confidence intervals than simple random sampling. Across our experiments, RSS reduces the confidence interval width by up to 50%.
We further introduce a repeated subsampling scheme that identifies representative simulation regions for future studies. For a fixed sample size, this approach reduces the maximum observed error from 35% to 10%. Evaluating two selection criteria, we find that more informed subsample selection provides additional accuracy gains. Overall, our method achieves an average error below 2% and a maximum error of 3.5% across individual SPEC CPU 2017 Integer applications when simulating 30 regions of 1 million instructions each.
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
