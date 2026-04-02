---
title: "SYNTHONY: A Stress-Aware, Intent-Conditioned Agent for Deep Tabular Generative Models Selection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00293"
published: "2026-04-02"
fetched: "2026-04-03T07:19:53.953962"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:SYNTHONY: A Stress-Aware, Intent-Conditioned Agent for Deep Tabular Generative Models Selection
View PDF HTML (experimental)Abstract:Deep generative models for tabular data (GANs, diffusion models, and LLM-based generators) exhibit highly non-uniform behavior across datasets; the best-performing synthesizer family depends strongly on distributional stressors such as long-tailed marginals, high-cardinality categorical, Zipfian imbalance, and small-sample regimes. This brittleness makes practical deployment challenging, especially when users must balance competing objectives of fidelity, privacy, and utility. We study {intent-conditioned tabular synthesis selection}: given a dataset and a user intent expressed as a preference over evaluation metrics, the goal is to select a synthesizer that minimizes regret relative to an intent-specific oracle. We propose {stress profiling}, a synthesis-specific meta-feature representation that quantifies dataset difficulty along four interpretable stress dimensions, and integrate it into {SYNTHONY}, a selection framework that matches stress profiles against a calibrated capability registry of synthesizer families. Across a benchmark of 7 datasets, 10 synthesizers, and 3 intents, we demonstrate that stress-based meta-features are highly predictive of synthesizer performance: a $k$NN selector using these features achieves strong Top-1 selection accuracy, substantially outperforming zero-shot LLM selectors and random baselines. We analyze the gap between meta-feature-based and capability-based selection, identifying the hand-crafted capability registry as the primary bottleneck and motivating learned capability representations as a direction for future work.
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
