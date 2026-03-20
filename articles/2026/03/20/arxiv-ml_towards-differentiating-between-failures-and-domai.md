---
title: "Towards Differentiating Between Failures and Domain Shifts in Industrial Data Streams"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18032"
published: "2026-03-20"
fetched: "2026-03-20T12:05:29.087316"
---

Computer Science > Machine Learning
[Submitted on 9 Mar 2026]
Title:Towards Differentiating Between Failures and Domain Shifts in Industrial Data Streams
View PDF HTML (experimental)Abstract:Anomaly and failure detection methods are crucial in identifying deviations from normal system operational conditions, which allows for actions to be taken in advance, usually preventing more serious damages. Long-lasting deviations indicate failures, while sudden, isolated changes in the data indicate anomalies. However, in many practical applications, changes in the data do not always represent abnormal system states. Such changes may be recognized incorrectly as failures, while being a normal evolution of the system, e.g. referring to characteristics of starting the processing of a new product, i.e. realizing a domain shift. Therefore, distinguishing between failures and such ''healthy'' changes in data distribution is critical to ensure the practical robustness of the system. In this paper, we propose a method that not only detects changes in the data distribution and anomalies but also allows us to distinguish between failures and normal domain shifts inherent to a given process. The proposed method consists of a modified Page-Hinkley changepoint detector for identification of the domain shift and possible failures and supervised domain-adaptation-based algorithms for fast, online anomaly detection. These two are coupled with an explainable artificial intelligence (XAI) component that aims at helping the human operator to finally differentiate between domain shifts and failures. The method is illustrated by an experiment on a data stream from the steel factory.
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
