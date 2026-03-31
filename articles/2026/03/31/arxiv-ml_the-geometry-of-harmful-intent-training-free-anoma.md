---
title: "The Geometry of Harmful Intent: Training-Free Anomaly Detection via Angular Deviation in LLM Residual Streams"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27412"
published: "2026-03-31"
fetched: "2026-04-01T07:23:43.895256"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:The Geometry of Harmful Intent: Training-Free Anomaly Detection via Angular Deviation in LLM Residual Streams
View PDF HTML (experimental)Abstract:We present LatentBiopsy, a training-free method for detecting harmful prompts by analysing the geometry of residual-stream activations in large language models. Given 200 safe normative prompts, LatentBiopsy computes the leading principal component of their activations at a target layer and characterises new prompts by their radial deviation angle $\theta$ from this reference direction. The anomaly score is the negative log-likelihood of $\theta$ under a Gaussian fit to the normative distribution, flagging deviations symmetrically regardless of orientation. No harmful examples are required for training.
We evaluate two complete model triplets from the Qwen3.5-0.8B and Qwen2.5-0.5B families: base, instruction-tuned, and \emph{abliterated} (refusal direction surgically removed via orthogonalisation). Across all six variants, LatentBiopsy achieves AUROC $\geq$0.937 for harmful-vs-normative detection and AUROC = 1.000 for discriminating harmful from benign-aggressive prompts (XSTest), with sub-millisecond per-query overhead.
Three empirical findings emerge. First, geometry survives refusal ablation: both abliterated variants achieve AUROC at most 0.015 below their instruction-tuned counterparts, establishing a geometric dissociation between harmful-intent representation and the downstream generative refusal mechanism. Second, harmful prompts exhibit a near-degenerate angular distribution ($\sigma_\theta \approx 0.03$ rad), an order of magnitude tighter than the normative distribution ($\sigma_\theta \approx 0.27$ rad), preserved across all alignment stages including abliteration. Third, the two families exhibit opposite ring orientations at the same depth: harmful prompts occupy the outer ring in Qwen3.5-0.8B but the inner ring in Qwen2.5-0.5B, directly motivating the direction-agnostic scoring rule.
Submission history
From: Isaac Llorente-Saguer [view email][v1] Sat, 28 Mar 2026 21:19:58 UTC (8,826 KB)
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
