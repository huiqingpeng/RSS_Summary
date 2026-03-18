---
title: "FALCON: False-Negative Aware Learning of Contrastive Negatives in Vision-Language Alignment"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2505.11192"
published: "2026-03-18"
fetched: "2026-03-18T18:25:47.121083"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 May 2025 (v1), last revised 17 Mar 2026 (this version, v5)]
Title:FALCON: False-Negative Aware Learning of Contrastive Negatives in Vision-Language Alignment
View PDF HTML (experimental)Abstract:False negatives pose a critical challenge in vision-language pretraining (VLP) due to the many-to-many correspondence between images and texts in large-scale datasets. These false negatives introduce conflicting supervision signals that degrade the learned embedding space and diminish the effectiveness of hard negative sampling. In this paper, we propose FALCON (False-negative Aware Learning of COntrastive Negatives), a learning-based mini-batch construction strategy that adaptively balances the trade-off between hard and false negatives during VLP. Rather than relying on fixed heuristics, FALCON employs a negative mining scheduler that dynamically selects negative samples of appropriate hardness for each anchor instance during mini-batch construction, guided by a proxy for cross-modal alignment improvement. Experimental results demonstrate that FALCON significantly improves performance across three vision-language learning frameworks (ALBEF, BLIP-2, SigLIP-2) and a broad range of downstream tasks and evaluation settings, underscoring its effectiveness and robustness in mitigating the impact of false negatives.
Submission history
From: Seongwoong Shim [view email][v1] Fri, 16 May 2025 12:50:05 UTC (5,538 KB)
[v2] Mon, 19 May 2025 01:33:42 UTC (1 KB) (withdrawn)
[v3] Tue, 20 May 2025 03:33:43 UTC (5,538 KB)
[v4] Tue, 11 Nov 2025 12:55:16 UTC (3,739 KB)
[v5] Tue, 17 Mar 2026 07:25:06 UTC (5,219 KB)
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
