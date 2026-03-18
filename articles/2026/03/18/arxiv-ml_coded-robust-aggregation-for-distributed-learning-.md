---
title: "Coded Robust Aggregation for Distributed Learning under Byzantine Attacks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2506.01989"
published: "2026-03-18"
fetched: "2026-03-18T16:18:02.810402"
---

Computer Science > Machine Learning
[Submitted on 17 May 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Coded Robust Aggregation for Distributed Learning under Byzantine Attacks
View PDF HTML (experimental)Abstract:In this paper, we investigate the problem of distributed learning (DL) in the presence of Byzantine attacks. For this problem, various robust bounded aggregation (RBA) rules have been proposed at the central server to mitigate the impact of Byzantine attacks. However, current DL methods apply RBA rules for the local gradients from the honest devices and the disruptive information from Byzantine devices, and the learning performance degrades significantly when the local gradients of different devices vary considerably from each other. To overcome this limitation, we propose a new DL method to cope with Byzantine attacks based on coded robust aggregation (CRA-DL). Before training begins, the training data are allocated to the devices redundantly. During training, in each iteration, the honest devices transmit coded gradients to the server computed from the allocated training data, and the server then aggregates the information received from both honest and Byzantine devices using RBA rules. In this way, the global gradient can be approximately recovered at the server to update the global model. Compared with current DL methods applying RBA rules, the improvement of CRA-DL is attributed to the fact that the coded gradients sent by the honest devices are closer to each other. This closeness enhances the robustness of the aggregation against Byzantine attacks, since Byzantine messages tend to be significantly different from those of honest devices in this case. We theoretically analyze the convergence performance of CRA-DL. Finally, we present numerical results to verify the superiority of the proposed method over existing baselines, showing its enhanced learning performance under Byzantine attacks.
Submission history
From: Chengxi Li [view email][v1] Sat, 17 May 2025 12:06:04 UTC (402 KB)
[v2] Tue, 17 Mar 2026 10:28:07 UTC (3,388 KB)
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
