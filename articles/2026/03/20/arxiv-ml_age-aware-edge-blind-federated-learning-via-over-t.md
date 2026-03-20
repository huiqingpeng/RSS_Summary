---
title: "Age-Aware Edge-Blind Federated Learning via Over-the-Air Aggregation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.02469"
published: "2026-03-20"
fetched: "2026-03-20T15:03:51.107321"
---

Computer Science > Information Theory
[Submitted on 2 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Age-Aware Edge-Blind Federated Learning via Over-the-Air Aggregation
View PDF HTML (experimental)Abstract:We study federated learning (FL) over wireless fading channels where multiple devices simultaneously send their model updates. We propose an efficient age-aware edge-blind over-the-air FL approach that does not require channel state information (CSI) at the devices. Instead, the parameter server (PS) uses multiple antennas and applies maximum-ratio combining (MRC) based on its estimated sum of the channel gains to detect the parameter updates. A key challenge is that the number of orthogonal subcarriers is limited; thus, transmitting many parameters requires multiple Orthogonal Frequency Division Multiplexing (OFDM) symbols, which increases latency. To address this, the PS selects only a small subset of model coordinates each round using AgeTop-k, which first picks the largest-magnitude entries and then chooses the k coordinates with the longest waiting times since they were last selected. This ensures that all selected parameters fit into a single OFDM symbol, reducing latency. We provide a convergence bound that highlights the advantages of using a higher number of antenna array elements and demonstrates a key trade-off: increasing k decreases compression error at the cost of increasing the effect of channel noise. Experimental results show that (i) more PS antennas greatly improve accuracy and convergence speed; (ii) AgeTop-k outperforms random selection under relatively good channel conditions; and (iii) the optimum k depends on the channel, with smaller k being better in noisy settings.
Submission history
From: Ahmed Elshazly [view email][v1] Mon, 2 Feb 2026 18:50:51 UTC (59 KB)
[v2] Wed, 18 Mar 2026 21:16:51 UTC (59 KB)
Current browse context:
cs.IT
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
