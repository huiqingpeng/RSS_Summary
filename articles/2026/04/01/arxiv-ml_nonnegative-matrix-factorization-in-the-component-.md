---
title: "Nonnegative Matrix Factorization in the Component-Wise L1 Norm for Sparse Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29715"
published: "2026-04-01"
fetched: "2026-04-02T07:19:46.404946"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Nonnegative Matrix Factorization in the Component-Wise L1 Norm for Sparse Data
View PDFAbstract:Nonnegative matrix factorization (NMF) approximates a nonnegative matrix, $X$, by the product of two nonnegative factors, $WH$, where $W$ has $r$ columns and $H$ has $r$ rows. In this paper, we consider NMF using the component-wise L1 norm as the error measure (L1-NMF), which is suited for data corrupted by heavy-tailed noise, such as Laplace noise or salt and pepper noise, or in the presence of outliers. Our first contribution is an NP-hardness proof for L1-NMF, even when $r=1$, in contrast to the standard NMF that uses least squares. Our second contribution is to show that L1-NMF strongly enforces sparsity in the factors for sparse input matrices, thereby favoring interpretability. However, if the data is affected by false zeros, too sparse solutions might degrade the model. Our third contribution is a new, more general, L1-NMF model for sparse data, dubbed weighted L1-NMF (wL1-NMF), where the sparsity of the factorization is controlled by adding a penalization parameter to the entries of $WH$ associated with zeros in the data. The fourth contribution is a new coordinate descent (CD) approach for wL1-NMF, denoted as sparse CD (sCD), where each subproblem is solved by a weighted median algorithm. To the best of our knowledge, sCD is the first algorithm for L1-NMF whose complexity scales with the number of nonzero entries in the data, making it efficient in handling large-scale, sparse data. We perform extensive numerical experiments on synthetic and real-world data to show the effectiveness of our new proposed model (wL1-NMF) and algorithm (sCD).
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
