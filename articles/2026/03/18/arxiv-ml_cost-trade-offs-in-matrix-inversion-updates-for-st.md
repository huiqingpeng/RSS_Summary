---
title: "Cost Trade-offs in Matrix Inversion Updates for Streaming Outlier Detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16697"
published: "2026-03-18"
fetched: "2026-03-18T15:46:07.302258"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Cost Trade-offs in Matrix Inversion Updates for Streaming Outlier Detection
View PDFAbstract:Outlier detection identifies data points that deviate significantly from expected patterns, revealing anomalies that may require special attention. Incorporating online learning further improves accuracy by continuously updating the model to reflect the most recent data. When employing the Christoffel function as an outlier score, online learning requires updating the inverse of a matrix following a rank-k update, given the initial inverse. Surprisingly, there is no consensus on the optimal method for this task. This technical note aims to compare three different updating methods: Direct Inversion (DI), Iterative Sherman-Morrison (ISM), and Woodbury Matrix Identity (WMI), to identify the most suitable approach for different scenarios. We first derive the theoretical computational costs of each method and then validate these findings through comprehensive Python simulations run on a CPU. These results allow us to propose a simple, quantitative, and easy-to-remember rule that can be stated qualitatively as follows: ISM is optimal for rank-1 updates, WMI excels for small updates relative to matrix size, and DI is preferable otherwise. This technical note produces a general result for any problem involving a matrix inversion update. In particular, it contributes to the ongoing development of efficient online outlier detection techniques.
Submission history
From: Louise Travé-Massuyès Dr [view email][v1] Tue, 17 Mar 2026 15:51:18 UTC (173 KB)
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
