---
title: "Using predefined vector systems to speed up neural network multimillion class classification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00779"
published: "2026-04-02"
fetched: "2026-04-03T07:24:40.224171"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Using predefined vector systems to speed up neural network multimillion class classification
View PDF HTML (experimental)Abstract:Label prediction in neural networks (NNs) has O(n) complexity proportional to the number of classes. This holds true for classification using fully connected layers and cosine similarity with some set of class prototypes. In this paper we show that if NN latent space (LS) geometry is known and possesses specific properties, label prediction complexity can be significantly reduced. This is achieved by associating label prediction with the O(1) complexity closest cluster center search in a vector system used as target for latent space configuration (LSC). The proposed method only requires finding indexes of several largest and lowest values in the embedding vector making it extremely computationally efficient. We show that the proposed method does not change NN training accuracy computational results. We also measure the time required by different computational stages of NN inference and label prediction on multiple datasets. The experiments show that the proposed method allows to achieve up to 11.6 times overall acceleration over conventional methods. Furthermore, the proposed method has unique properties which allow to predict the existence of new classes.
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
