---
title: "LucidNFT: LR-Anchored Multi-Reward Preference Optimization for Generative Real-World Super-Resolution"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.05947"
published: "2026-03-20"
fetched: "2026-03-20T16:18:07.690160"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 6 Mar 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:LucidNFT: LR-Anchored Multi-Reward Preference Optimization for Generative Real-World Super-Resolution
View PDF HTML (experimental)Abstract:Generative real-world image super-resolution (Real-ISR) can synthesize visually convincing details from severely degraded low-resolution (LR) inputs, yet its stochastic sampling makes a critical failure mode hard to avoid: outputs may look sharp but be unfaithful to the LR evidence (semantic and structural hallucination), while such LR-anchored faithfulness is difficult to assess without HR ground truth. Preference-based reinforcement learning (RL) is a natural fit because each LR input yields a rollout group of candidates to compare. However, effective alignment in Real-ISR is hindered by (i) the lack of a degradation-robust LR-referenced faithfulness signal, and (ii) a rollout-group optimization bottleneck where naive multi-reward scalarization followed by normalization compresses objective-wise contrasts, causing advantage collapse and weakening the reward-weighted updates in DiffusionNFT-style forward fine-tuning. Moreover, (iii) limited coverage of real degradations restricts rollout diversity and preference signal quality. We propose LucidNFT, a multi-reward RL framework for flow-matching Real-ISR. LucidNFT introduces LucidConsistency, a degradation-robust semantic evaluator that makes LR-anchored faithfulness measurable and optimizable; a decoupled advantage normalization strategy that preserves objective-wise contrasts within each LR-conditioned rollout group before fusion, preventing advantage collapse; and LucidLR, a large-scale collection of real-world degraded images to support robust RL fine-tuning. Experiments show that LucidNFT consistently improves strong flow-based Real-ISR baselines, achieving better perceptual-faithfulness trade-offs with stable optimization dynamics across diverse real-world scenarios.
Submission history
From: Song Fei [view email][v1] Fri, 6 Mar 2026 06:30:34 UTC (688 KB)
[v2] Thu, 19 Mar 2026 13:03:59 UTC (2,175 KB)
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
