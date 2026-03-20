---
title: "On the Surprising Effectiveness of a Single Global Merging in Decentralized Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2507.06542"
published: "2026-03-20"
fetched: "2026-03-20T14:06:25.926891"
---

Computer Science > Machine Learning
[Submitted on 9 Jul 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:On the Surprising Effectiveness of a Single Global Merging in Decentralized Learning
View PDF HTML (experimental)Abstract:Decentralized learning provides a scalable alternative to parameter-server-based training, yet its performance is often hindered by limited peer-to-peer communication. In this paper, we study how communication should be scheduled over time, including determining when and how frequently devices synchronize. Counterintuitive empirical results show that concentrating communication budgets in the later stages of decentralized training remarkably improves global test performance. Surprisingly, we uncover that fully connected communication at the final step, implemented by a single global merging, can significantly improve the performance of decentralized learning under high data heterogeneity. Our theoretical contributions, which explain these phenomena, are the first to establish that the globally merged model of decentralized SGD can match the convergence rate of parallel SGD. Technically, we reinterpret part of the discrepancy among local models, which were previously considered as detrimental noise, as constructive components essential for matching this rate. This work provides evidence that decentralized learning is able to generalize under high data heterogeneity and limited communication, while offering broad new avenues for model merging research.
Submission history
From: Tongtian Zhu [view email][v1] Wed, 9 Jul 2025 04:56:56 UTC (4,541 KB)
[v2] Sat, 11 Oct 2025 07:58:05 UTC (4,222 KB)
[v3] Thu, 19 Mar 2026 10:05:02 UTC (4,378 KB)
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
