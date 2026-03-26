---
title: "i-IF-Learn: Iterative Feature Selection and Unsupervised Learning for High-Dimensional Complex Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24025"
published: "2026-03-26"
fetched: "2026-03-27T07:19:44.958855"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:i-IF-Learn: Iterative Feature Selection and Unsupervised Learning for High-Dimensional Complex Data
View PDF HTML (experimental)Abstract:Unsupervised learning of high-dimensional data is challenging due to irrelevant or noisy features obscuring underlying structures. It's common that only a few features, called the influential features, meaningfully define the clusters. Recovering these influential features is helpful in data interpretation and clustering. We propose i-IF-Learn, an iterative unsupervised framework that jointly performs feature selection and clustering. Our core innovation is an adaptive feature selection statistic that effectively combines pseudo-label supervision with unsupervised signals, dynamically adjusting based on intermediate label reliability to mitigate error propagation common in iterative frameworks. Leveraging low-dimensional embeddings (PCA or Laplacian eigenmaps) followed by $k$-means, i-IF-Learn simultaneously outputs influential feature subset and clustering labels. Numerical experiments on gene microarray and single-cell RNA-seq datasets show that i-IF-Learn significantly surpasses classical and deep clustering baselines. Furthermore, using our selected influential features as preprocessing substantially enhances downstream deep models such as DeepCluster, UMAP, and VAE, highlighting the importance and effectiveness of targeted feature selection.
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
