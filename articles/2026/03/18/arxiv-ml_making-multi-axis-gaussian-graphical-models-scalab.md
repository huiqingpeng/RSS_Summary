---
title: "Making Multi-Axis Gaussian Graphical Models Scalable to Millions of Cells"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2407.19892"
published: "2026-03-18"
fetched: "2026-03-18T17:08:47.878140"
---

Statistics > Machine Learning
[Submitted on 29 Jul 2024 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Making Multi-Axis Gaussian Graphical Models Scalable to Millions of Cells
View PDFAbstract:Motivation: Networks underlie the generation and interpretation of many biological datasets: gene networks shed light on the regulatory structure of the genome, and cell networks can capture structure of the tumor micro-environment. However, most methods that learn such networks make the faulty 'independence assumption'; to learn the gene network, they assume that no cell network exists. 'Multi-axis' methods, which do not make this assumption, fail to scale beyond a few thousand cells or genes. This limits their applicability to only the smallest datasets.
Results: We develop a multi-axis method capable of processing million-cell datasets within minutes. This was previously impossible, and unlocks the use of such methods on modern scRNA-seq datasets, as well as more complex datasets. We show that our method yields novel biological insights from real single-cell data, and compares favorably to the existing hdWGCNA methodology. In particular, it identifies long non-coding RNA genes that potentially have a regulatory or functional role in neuronal development.
Availability and implementation: Our methodology is available as a Python package GmGM on PyPI (this https URL). The code for all experiments performed in this paper is available on GitHub (this https URL).
Contact: sceba@leeds.this http URL
Supplementary information: Our proofs, and some additional experiments, are available in the supplementary material.
Keywords: gaussian graphical models, multi-axis models, transcriptomics, multi-omics, scalability
Submission history
From: Bailey Andrew [view email][v1] Mon, 29 Jul 2024 11:15:25 UTC (1,094 KB)
[v2] Tue, 17 Mar 2026 10:19:17 UTC (834 KB)
Current browse context:
stat.ML
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
