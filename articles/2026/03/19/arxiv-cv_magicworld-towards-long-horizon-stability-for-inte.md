---
title: "MagicWorld: Towards Long-Horizon Stability for Interactive Video World Exploration"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.18886"
published: "2026-03-19"
fetched: "2026-03-19T16:28:10.250633"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 24 Nov 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:MagicWorld: Towards Long-Horizon Stability for Interactive Video World Exploration
View PDF HTML (experimental)Abstract:Recent interactive video world model methods generate scene evolution conditioned on user instructions. Although they achieve impressive results, two key limitations remain. First, they exhibit motion drift in complex environments with multiple interacting subjects, where dynamic subjects fail to follow realistic motion patterns during scene evolution. Second, they suffer from error accumulation in long-horizon interactions, where autoregressive generation gradually drifts from earlier scene states and causes structural and semantic inconsistencies. In this paper, we propose MagicWorld, an interactive video world model built upon an autoregressive framework. To address motion drift, we incorporate a flow-guided motion preservation constraint that mitigates motion degradation in dynamic subjects, encouraging realistic motion patterns and stable interactions during scene evolution. To mitigate error accumulation in long-horizon interactions, we design two complementary strategies, including a history cache retrieval strategy and an enhanced interactive training strategy. The former reinforces historical scene states by retrieving past generations during interaction, while the latter adopts multi-shot aggregated distillation with dual-reward weighting for interactive training, enhancing long-term stability and reducing error accumulation. In addition, we construct RealWM120K, a real-world dataset with diverse city-walk videos and multimodal annotations to support dynamic perception and long-horizon world modeling. Experimental results demonstrate that MagicWorld improves motion realism and alleviates error accumulation during long-horizon interactions.
Submission history
From: Guangyuan Li [view email][v1] Mon, 24 Nov 2025 08:41:28 UTC (7,639 KB)
[v2] Wed, 18 Mar 2026 12:38:28 UTC (13,131 KB)
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
