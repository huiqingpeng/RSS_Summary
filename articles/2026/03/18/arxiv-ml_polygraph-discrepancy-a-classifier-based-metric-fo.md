---
title: "PolyGraph Discrepancy: a classifier-based metric for graph generation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.06122"
published: "2026-03-18"
fetched: "2026-03-18T16:19:28.410113"
---

Computer Science > Machine Learning
[Submitted on 7 Oct 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:PolyGraph Discrepancy: a classifier-based metric for graph generation
View PDFAbstract:Existing methods for evaluating graph generative models primarily rely on Maximum Mean Discrepancy (MMD) metrics based on graph descriptors. While these metrics can rank generative models, they do not provide an absolute measure of performance. Their values are also highly sensitive to extrinsic parameters, namely kernel and descriptor parametrization, making them incomparable across different graph descriptors. We introduce PolyGraph Discrepancy (PGD), a new evaluation framework that addresses these limitations. It approximates the Jensen-Shannon distance of graph distributions by fitting binary classifiers to distinguish between real and generated graphs, featurized by these descriptors. The data log-likelihood of these classifiers approximates a variational lower bound on the JS distance between the two distributions. Resulting metrics are constrained to the unit interval [0,1] and are comparable across different graph descriptors. We further derive a theoretically grounded summary metric that combines these individual metrics to provide a maximally tight lower bound on the distance for the given descriptors. Thorough experiments demonstrate that PGD provides a more robust and insightful evaluation compared to MMD metrics. The PolyGraph framework for benchmarking graph generative models is made publicly available at this https URL.
Submission history
From: Philip Hartout [view email][v1] Tue, 7 Oct 2025 17:02:44 UTC (6,194 KB)
[v2] Tue, 17 Mar 2026 07:36:37 UTC (6,160 KB)
Current browse context:
cs.LG
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
