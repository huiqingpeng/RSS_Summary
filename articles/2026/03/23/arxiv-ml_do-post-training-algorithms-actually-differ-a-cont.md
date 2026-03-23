---
title: "Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales Uncovers Scale-Dependent Ranking Inversions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19335"
published: "2026-03-23"
fetched: "2026-03-24T07:17:22.731745"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales Uncovers Scale-Dependent Ranking Inversions
View PDF HTML (experimental)Abstract:Post-training alignment has produced dozens of competing algorithms -- DPO, SimPO, KTO, GRPO, and others -- yet practitioners lack controlled comparisons to guide algorithm selection. We present OXRL, a unified framework implementing 51 post-training algorithms with identical infrastructure, enabling the first large-scale apples-to-apples evaluation. Our study spans 8 algorithms across 4 model scales (0.5B--7B), 3 evaluation domains, and a 20-variant DPO taxonomy (100 runs at 1.5B, 5 seeds each), totaling $\sim$240 training runs on H100 GPUs. Three headline findings emerge. (1)~Algorithm rankings are unstable across scale: at 1.5B, online RL (SGRPO) tops all methods at 58.0\%~$\pm$0.57 on GSM8K; by 7B, the worst small-scale method (SimPO) becomes the best (85.8\%), a complete ranking inversion driven by model scale rather than LoRA regularization (confirmed via 2$\times$2 factorial). (2)~Loss function modifications yield negligible gains: none of 20 DPO variants significantly outperform vanilla DPO after Bonferroni correction; the sole significant outlier, SimPO, is worse ($-$11.5~pp, $p < 10^{-4}$). (3)~Algorithm leverage is task-specific: the 19.3~pp GSM8K spread collapses to 0.54~pp on MATH ($36\times$) and 0.47~pp on general-domain benchmarks ($41\times$), confirming that algorithm choice matters primarily within the training distribution. These findings yield a hierarchy of leverage for practitioners: model scale (${\sim}$50~pp) $\gg$ training paradigm (${\sim}$10~pp) $\gg$ online vs.\ offline (${\sim}$9~pp) $\gg$ loss function (${\sim}$1~pp). We release all code, configs, and evaluation data as a living community benchmark.
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
