---
title: "Steering Frozen LLMs: Adaptive Social Alignment via Online Prompt Routing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15647"
published: "2026-03-18"
fetched: "2026-03-18T15:32:41.768140"
---

Computer Science > Machine Learning
[Submitted on 4 Mar 2026]
Title:Steering Frozen LLMs: Adaptive Social Alignment via Online Prompt Routing
View PDF HTML (experimental)Abstract:Large language models (LLMs) are typically governed by post-training alignment (e.g., RLHF or DPO), which yields a largely static policy during deployment and inference. However, real-world safety is a full-lifecycle problem: static defenses degrade against evolving jailbreak behaviors, and fixed weights cannot adapt to pluralistic, time-varying safety norms. This motivates inference-time governance that steers behavior without costly retraining. To address this, we introduce the Consensus Clustering LinUCB Bandit (CCLUB), a unified framework for adaptive social alignment via system-prompt routing. CCLUB employs a conservative consensus clustering mechanism: it pools data only within the intersection of utility and safety similarity graphs, effectively preventing unsafe generalization across semantically proximal but risk-divergent contexts. Our theoretical analysis yields a sublinear regret guarantee, demonstrating near-optimal performance of CCLUB. Extensive experiments validate that CCLUB outperforms strong baselines, achieving a 10.98% improvement in cumulative reward and a 14.42% reduction in the average suboptimality gap.
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
