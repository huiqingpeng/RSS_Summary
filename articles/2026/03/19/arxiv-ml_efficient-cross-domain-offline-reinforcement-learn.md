---
title: "Efficient Cross-Domain Offline Reinforcement Learning with Dynamics- and Value-Aligned Data Filtering"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.02435"
published: "2026-03-19"
fetched: "2026-03-19T14:10:18.912325"
---

Computer Science > Machine Learning
[Submitted on 2 Dec 2025 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Efficient Cross-Domain Offline Reinforcement Learning with Dynamics- and Value-Aligned Data Filtering
View PDF HTML (experimental)Abstract:Cross-domain offline reinforcement learning (RL) aims to train a well-performing agent in the target environment, leveraging both a limited target domain dataset and a source domain dataset with (possibly) sufficient data coverage. Due to the underlying dynamics misalignment between source and target domains, naively merging the two datasets may incur inferior performance. Recent advances address this issue by selectively leveraging source domain samples whose dynamics align well with the target domain. However, our work demonstrates that dynamics alignment alone is insufficient, by examining the limitations of prior frameworks and deriving a new target domain sub-optimality bound for the policy learned on the source domain. More importantly, our theory underscores an additional need for \textit{value alignment}, i.e., selecting high-quality, high-value samples from the source domain, a critical dimension overlooked by existing works. Motivated by such theoretical insight, we propose \textbf{\underline{D}}ynamics- and \textbf{\underline{V}}alue-aligned \textbf{\underline{D}}ata \textbf{\underline{F}}iltering (DVDF) method, a novel unified cross-domain RL framework that selectively incorporates source domain samples exhibiting strong alignment in \textit{both dynamics and values}. We empirically study a range of dynamics shift scenarios, including kinematic and morphology shifts, and evaluate DVDF on various tasks and datasets, even in the challenging setting where the target domain dataset contains an extremely limited amount of data. Extensive experiments demonstrate that DVDF consistently outperforms strong baselines with significant improvements.
Submission history
From: Zhongjian Qiao [view email][v1] Tue, 2 Dec 2025 05:45:40 UTC (13,527 KB)
[v2] Wed, 25 Feb 2026 09:39:03 UTC (13,234 KB)
[v3] Wed, 18 Mar 2026 02:42:00 UTC (13,234 KB)
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
