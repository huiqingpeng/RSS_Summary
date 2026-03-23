---
title: "Scalable Learning of Multivariate Distributions via Coresets"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19792"
published: "2026-03-23"
fetched: "2026-03-24T07:22:01.286504"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Scalable Learning of Multivariate Distributions via Coresets
View PDF HTML (experimental)Abstract:Efficient and scalable non-parametric or semi-parametric regression analysis and density estimation are of crucial importance to the fields of statistics and machine learning. However, available methods are limited in their ability to handle large-scale data. We address this issue by developing a novel coreset construction for multivariate conditional transformation models (MCTMs) to enhance their scalability and training efficiency. To the best of our knowledge, these are the first coresets for semi-parametric distributional models. Our approach yields substantial data reduction via importance sampling. It ensures with high probability that the log-likelihood remains within multiplicative error bounds of $(1\pm\varepsilon)$ and thereby maintains statistical model accuracy. Compared to conventional full-parametric models, where coresets have been incorporated before, our semi-parametric approach exhibits enhanced adaptability, particularly in scenarios where complex distributions and non-linear relationships are present, but not fully understood. To address numerical problems associated with normalizing logarithmic terms, we follow a geometric approximation based on the convex hull of input data. This ensures feasible, stable, and accurate inference in scenarios involving large amounts of data. Numerical experiments demonstrate substantially improved computational efficiency when handling large and complex datasets, thus laying the foundation for a broad range of applications within the statistics and machine learning communities.
Submission history
From: Alexander Munteanu [view email][v1] Fri, 20 Mar 2026 09:28:43 UTC (9,526 KB)
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
