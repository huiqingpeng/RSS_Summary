---
title: "A Multi-Task Targeted Learning Framework for Lithium-Ion Battery State-of-Health and Remaining Useful Life"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22323"
published: "2026-03-25"
fetched: "2026-03-26T07:11:09.057946"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:A Multi-Task Targeted Learning Framework for Lithium-Ion Battery State-of-Health and Remaining Useful Life
View PDF HTML (experimental)Abstract:Accurately predicting the state-of-health (SOH) and remaining useful life (RUL) of lithium-ion batteries is crucial for ensuring the safe and efficient operation of electric vehicles while minimizing associated risks. However, current deep learning methods are limited in their ability to selectively extract features and model time dependencies for these two parameters. Moreover, most existing methods rely on traditional recurrent neural networks, which have inherent shortcomings in long-term time-series modeling. To address these issues, this paper proposes a multi-task targeted learning framework for SOH and RUL prediction, which integrates multiple neural networks, including a multi-scale feature extraction module, an improved extended LSTM, and a dual-stream attention module. First, a feature extraction module with multi-scale CNNs is designed to capture detailed local battery decline patterns. Secondly, an improved extended LSTM network is employed to enhance the model's ability to retain long-term temporal information, thus improving temporal relationship modeling. Building on this, the dual-stream attention module-comprising polarized attention and sparse attention to selectively focus on key information relevant to SOH and RUL, respectively, by assigning higher weights to important features. Finally, a many-to-two mapping is achieved through the dual-task layer. To optimize the model's performance and reduce the need for manual hyperparameter tuning, the Hyperopt optimization algorithm is used. Extensive comparative experiments on battery aging datasets demonstrate that the proposed method reduces the average RMSE for SOH and RUL predictions by 111.3\% and 33.0\%, respectively, compared to traditional and state-of-the-art methods.
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
