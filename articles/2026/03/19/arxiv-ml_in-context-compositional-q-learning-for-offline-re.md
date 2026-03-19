---
title: "In-Context Compositional Q-Learning for Offline Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.24067"
published: "2026-03-19"
fetched: "2026-03-19T14:07:00.786406"
---

Computer Science > Machine Learning
[Submitted on 28 Sep 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:In-Context Compositional Q-Learning for Offline Reinforcement Learning
View PDF HTML (experimental)Abstract:Accurate estimation of the Q-function is a central challenge in offline reinforcement learning. However, existing approaches often rely on a shared global Q-function, which is inadequate for capturing the compositional structure of tasks that consist of diverse subtasks. We propose In-context Compositional Q-Learning (ICQL), an offline RL framework that formulates Q-learning as a contextual inference problem and uses linear Transformers to adaptively infer local Q-functions from retrieved transitions without explicit subtask labels. Theoretically, we show that, under two assumptions -- linear approximability of the local Q-function and accurate inference of weights from retrieved context -- ICQL achieves a bounded approximation error for the Q-function and enables near-optimal policy extraction. Empirically, ICQL substantially improves performance in offline settings, achieving gains of up to 16.4% on kitchen tasks and up to 8.8% and 6.3% on MuJoCo and Adroit tasks, respectively. These results highlight the underexplored potential of in-context learning for robust and compositional value estimation and establish ICQL as a principled and effective framework for offline RL.
Submission history
From: Qiushui Xu [view email][v1] Sun, 28 Sep 2025 20:55:21 UTC (968 KB)
[v2] Wed, 18 Mar 2026 06:31:58 UTC (2,059 KB)
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
