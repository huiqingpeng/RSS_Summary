---
title: "Neuro-Symbolic Process Anomaly Detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26461"
published: "2026-03-30"
fetched: "2026-03-31T07:24:12.058836"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Neuro-Symbolic Process Anomaly Detection
View PDF HTML (experimental)Abstract:Process anomaly detection is an important application of process mining for identifying deviations from the normal behavior of a process. Neural network-based methods have recently been applied to this task, learning directly from event logs without requiring a predefined process model. However, since anomaly detection is a purely statistical task, these models fail to incorporate human domain knowledge. As a result, rare but conformant traces are often misclassified as anomalies due to their low frequency, which limits the effectiveness of the detection process. Recent developments in the field of neuro-symbolic AI have introduced Logic Tensor Networks (LTN) as a means to integrate symbolic knowledge into neural networks using real-valued logic. In this work, we propose a neuro-symbolic approach that integrates domain knowledge into neural anomaly detection using LTN and Declare constraints. Using autoencoder models as a foundation, we encode Declare constraints as soft logical guiderails within the learning process to distinguish between anomalous and rare but conformant behavior. Evaluations on synthetic and real-world datasets demonstrate that our approach improves F1 scores even when as few as 10 conformant traces exist, and that the choice of Declare constraint and by extension human domain knowledge significantly influences performance gains.
Submission history
From: Devashish Gaikwad [view email][v1] Fri, 27 Mar 2026 14:30:30 UTC (2,398 KB)
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
