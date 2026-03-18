---
title: "A Dynamic Time Warping-Transfer Learning Approach to Transferring Knowledge in Stress-strain Behaviors from Polymers to Metals: An Affordable and Generalizable Additive Manufacturing Part Qualification Framework"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.08699"
published: "2026-03-18"
fetched: "2026-03-18T17:03:37.829069"
---

Computer Science > Machine Learning
[Submitted on 9 Dec 2025 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:A Dynamic Time Warping-Transfer Learning Approach to Transferring Knowledge in Stress-strain Behaviors from Polymers to Metals: An Affordable and Generalizable Additive Manufacturing Part Qualification Framework
View PDFAbstract:Part qualification in additive manufacturing (AM) ensures that additively manufactured parts can be consistently produced and reliably used in critical applications. One crucial aspect of part qualification is to determine the complex stress-strain behavior of additively manufactured parts. However, conventional part qualification techniques such as the destructive testing and non-destructive testing are costly and time consuming, especially for metal AM. To address this challenge, we develop a dynamic time warping (DTW)-transfer learning (TL) framework for AM part qualification by transferring knowledge gained from the stress-strain behaviors of additively manufactured low-cost polymers to high-performance, expensive metals. Specifically, the framework selects one single optimal polymer dataset that is the most similar to the metal dataset in the target domain using DTW among multiple polymer datasets, including Nylon, PLA, CF-ABS, and Resin. A long short-term memory (LSTM) model is then trained on one single optimal polymer dataset and tested on one of three target metal datasets, including AlSi10Mg, Ti6Al4V, and carbon steel datasets. Experimental results show that the Resin dataset is selected as the optimal polymer dataset in the source domain for the AlSi10Mg and Ti6Al4V datasets, while the Nylon dataset is selected as the optimal polymer dataset in the source domain for the carbon steel dataset. The DTWTL model trained on one single optimal polymer dataset as the source domain achieves the best predictive performance, including an average mean absolute percentage error of 12.41%, an average root mean squared error of 63.75, and an average coefficient of determination of 0.96 when three metals are used as the target domain, outperforming the vanilla LSTM model without TL as well as the TL model trained on all four polymer datasets as the source domain.
Submission history
From: Chenglong Duan [view email][v1] Tue, 9 Dec 2025 15:15:46 UTC (1,696 KB)
[v2] Mon, 16 Mar 2026 22:51:22 UTC (1,825 KB)
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
