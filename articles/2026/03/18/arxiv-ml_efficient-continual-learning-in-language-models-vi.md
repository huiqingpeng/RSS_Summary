---
title: "Efficient Continual Learning in Language Models via Thalamically Routed Cortical Columns"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.22479"
published: "2026-03-18"
fetched: "2026-03-18T17:04:35.595994"
---

Computer Science > Machine Learning
[Submitted on 25 Feb 2026 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Efficient Continual Learning in Language Models via Thalamically Routed Cortical Columns
View PDF HTML (experimental)Abstract:Large language models deployed in the wild must adapt to evolving data, user behavior, and task mixtures without erasing previously acquired capabilities. In practice, this remains difficult: sequential updates induce catastrophic forgetting, while many stabilization methods rely on external procedures that are costly, brittle, or difficult to scale. We present TRC$^{2}$ (Thalamically Routed Cortical Columns), a decoder-only architecture that makes continual adaptation a property of the backbone itself. TRC$^{2}$ combines stacked cortical columns with a thalamic modulatory pathway for selective inter-column communication and a hippocampal pathway for event-selective retrieval, delayed surprise-based writing, and replay-driven consolidation. This design localizes fast plasticity while preserving a slower stable computation pathway. We further introduce a causal memory-update scheme and an online replay controller that adjusts consolidation strength from measured forgetting. Across a task-sequential language-modeling stream over C4, WikiText-103, and GSM8K, TRC$^{2}$ consistently improves task-boundary modeling quality and substantially reduces cumulative forgetting relative to Transformer, Mamba, MoE, and DeepSeek baselines trained under the same pipeline. Ablations show that the thalamic and hippocampal components are central to the retention gains, while the full model remains competitive in throughput and training cost.
Submission history
From: Afshin Khadangi [view email][v1] Wed, 25 Feb 2026 23:38:16 UTC (2,640 KB)
[v2] Sun, 15 Mar 2026 15:57:48 UTC (9,692 KB)
[v3] Tue, 17 Mar 2026 17:02:11 UTC (9,781 KB)
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
