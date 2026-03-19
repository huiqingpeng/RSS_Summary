---
title: "Soft Dice Confidence: A Near-Optimal Confidence Estimator for Selective Prediction in Semantic Segmentation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2402.10665"
published: "2026-03-19"
fetched: "2026-03-19T13:17:40.080633"
---

Computer Science > Machine Learning
[Submitted on 16 Feb 2024 (v1), last revised 17 Mar 2026 (this version, v5)]
Title:Soft Dice Confidence: A Near-Optimal Confidence Estimator for Selective Prediction in Semantic Segmentation
View PDF HTML (experimental)Abstract:In semantic segmentation, even state-of-the-art deep learning models fall short of the performance required in certain high-stakes applications such as medical image analysis. In these cases, performance can be improved by allowing a model to abstain from making predictions when confidence is low, an approach known as selective prediction. While well-known in the classification literature, selective prediction has been underexplored in the context of semantic segmentation. This paper tackles the problem by focusing on image-level abstention, which involves producing a single confidence estimate for the entire image, in contrast to previous approaches that focus on pixel-level uncertainty. Assuming the Dice coefficient as the evaluation metric for segmentation, two main contributions are provided in this paper: (i) In the case of known marginal posterior probabilities, we derive the optimal confidence estimator, which is observed to be intractable for typical image sizes. Then, an approximation computable in linear time, named Soft Dice Confidence (SDC), is proposed and proven to be tightly bounded to the optimal estimator. (ii) When only an estimate of the marginal posterior probabilities are known, we propose a plug-in version of the SDC and show it outperforms all previous methods, including those requiring additional tuning data. These findings are supported by experimental results on both synthetic data and real-world data from six medical imaging tasks, including out-of-distribution scenarios, positioning the SDC as a reliable and efficient tool for selective prediction in semantic segmentation.
Submission history
From: Bruno Machado Pacheco [view email][v1] Fri, 16 Feb 2024 13:14:12 UTC (920 KB)
[v2] Tue, 7 May 2024 01:05:14 UTC (2,086 KB)
[v3] Mon, 30 Jun 2025 19:42:11 UTC (4,914 KB)
[v4] Fri, 8 Aug 2025 13:12:04 UTC (5,006 KB)
[v5] Tue, 17 Mar 2026 22:27:23 UTC (5,245 KB)
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
