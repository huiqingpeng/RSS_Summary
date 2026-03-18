---
title: "Learning-based Sketches for Frequency Estimation in Data Streams without Ground Truth"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2412.03611"
published: "2026-03-18"
fetched: "2026-03-18T16:16:46.029376"
---

Computer Science > Machine Learning
[Submitted on 4 Dec 2024 (v1), last revised 17 Mar 2026 (this version, v5)]
Title:Learning-based Sketches for Frequency Estimation in Data Streams without Ground Truth
View PDF HTML (experimental)Abstract:Estimating the frequency of items on the high-volume, fast data stream has been extensively studied in many areas, such as database and network measurement. Traditional sketches provide only coarse estimates under strict memory constraints. Although some learning-augmented methods have emerged recently, they typically rely on offline training with real frequencies or/and labels, which are often unavailable. Moreover, these methods suffer from slow update speeds, limiting their suitability for real-time processing despite offering only marginal accuracy improvements. To overcome these challenges, we propose UCL-sketch, a practical learning-based paradigm for per-key frequency estimation. Our design introduces two key innovations: (i) an online training mechanism based on equivalent learning that requires no ground truth (GT), and (ii) a highly scalable architecture leveraging logically structured estimation buckets to scale to real-world data stream. The UCL-sketch, which utilizes compressive sensing (CS), converges to an estimator that provably yields a error bound far lower than that of prior works, without sacrificing the speed of processing. Extensive experiments on both real-world and synthetic datasets demonstrate that our approach outperforms previously proposed approaches regarding per-key accuracy and distribution. Notably, under extremely tight memory budgets, its quality almost matches that of an (infeasible) omniscient oracle. Moreover, compared to the existing equation-based sketch, UCL-sketch achieves an average decoding speedup of nearly 500 times. To help further research and development, our code is publicly available at this https URL.
Submission history
From: Xinyu Yuan [view email][v1] Wed, 4 Dec 2024 14:00:50 UTC (930 KB)
[v2] Wed, 18 Dec 2024 07:01:15 UTC (951 KB)
[v3] Fri, 15 Aug 2025 13:27:17 UTC (1,359 KB)
[v4] Mon, 13 Oct 2025 16:58:34 UTC (1,434 KB)
[v5] Tue, 17 Mar 2026 06:40:52 UTC (1,434 KB)
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
