---
title: "Language as a Wave Phenomenon: Semantic Phase Locking and Interference in Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.01208"
published: "2026-03-18"
fetched: "2026-03-18T17:03:25.885865"
---

Computer Science > Machine Learning
[Submitted on 1 Dec 2025 (v1), last revised 17 Mar 2026 (this version, v4)]
Title:Language as a Wave Phenomenon: Semantic Phase Locking and Interference in Neural Networks
View PDF HTML (experimental)Abstract:The role of phase in neural sequence models remains poorly understood. To isolate this question, we introduce PRISM, a complex-valued encoder that enforces a unit-norm constraint ($|z| = 1$) and replaces attention with gated spectral filtering. Under this constraint, the model cannot use activation magnitude to distinguish signal from noise, and must instead rely on phase angles. We find that semantic relationships correlate with measurable phase structure: synonym pairs exhibit significantly higher phase coherence than random pairs ($R = 0.198$ vs.\ $0.072$, $p < 0.001$), and the model resolves lexical ambiguity via layer-specific phase rotations while maintaining near-unit gain. These phase representations are robust to scalar attenuation, retaining $97\%$ of translation quality when signal magnitude is uniformly reduced. We also identify a spectral density threshold: the model fails to generate coherent output from isolated tokens, requiring minimum sequence length to produce the interference patterns that support its computation. Finally, we show that a hybrid architecture (Wave-Particle Transformer) combining a phase-based encoder with standard attention matches Transformer baselines at $33$M parameters with fewer non-embedding parameters, though we do not claim this generalizes to larger scales. Our findings provide controlled evidence that phase angles can encode semantic information in complex-valued networks, and characterize the conditions under which this encoding succeeds and fails.
Submission history
From: Alper Yıldırım [view email][v1] Mon, 1 Dec 2025 02:46:15 UTC (1,201 KB)
[v2] Mon, 5 Jan 2026 17:26:51 UTC (1,166 KB)
[v3] Mon, 2 Feb 2026 16:53:54 UTC (6,841 KB)
[v4] Tue, 17 Mar 2026 05:51:40 UTC (1,361 KB)
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
