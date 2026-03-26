---
title: "Uncovering Memorization in Timeseries Imputation models: LBRM Membership Inference and its link to attribute Leakage"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24213"
published: "2026-03-26"
fetched: "2026-03-27T07:21:56.287668"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Uncovering Memorization in Timeseries Imputation models: LBRM Membership Inference and its link to attribute Leakage
View PDF HTML (experimental)Abstract:Deep learning models for time series imputation are now essential in fields such as healthcare, the Internet of Things (IoT), and finance. However, their deployment raises critical privacy concerns. Beyond the well-known issue of unintended memorization, which has been extensively studied in generative models, we demonstrate that time series models are vulnerable to inference attacks in a black-box setting. In this work, we introduce a two-stage attack framework comprising: (1) a novel membership inference attack based on a reference model that improves detection accuracy, even for models robust to overfitting-based attacks, and (2) the first attribute inference attack that predicts sensitive characteristics of the training data for timeseries imputation model. We evaluate these attacks on attention-based and autoencoder architectures in two scenarios: models that are trained from scratch, and fine-tuned models where the adversary has access to the initial weights. Our experimental results demonstrate that the proposed membership attack retrieves a significant portion of the training data with a tpr@top25% score significantly higher than a naive attack baseline. We show that our membership attack also provides a good insight of whether attribute inference will work (with a precision of 90% instead of 78% in the genral case).
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
