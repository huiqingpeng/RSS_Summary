---
title: "CausalRM: Causal-Theoretic Reward Modeling for RLHF from Observational User Feedbacks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18736"
published: "2026-03-20"
fetched: "2026-03-20T12:15:16.481984"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:CausalRM: Causal-Theoretic Reward Modeling for RLHF from Observational User Feedbacks
View PDFAbstract:Despite the success of reinforcement learning from human feedback (RLHF) in aligning language models, current reward modeling heavily relies on experimental feedback data collected from human annotators under controlled and costly conditions. In this work, we introduce observational reward modeling -- learning reward models with observational user feedback (e.g., clicks, copies, and upvotes) -- as a scalable and cost-effective alternative. We identify two fundamental challenges in this setting: (1) observational feedback is noisy due to annotation errors, which deviates it from true user preference; (2) observational feedback is biased by user preference, where users preferentially provide feedback on responses they feel strongly about, which creats a distribution shift between training and inference data. To address these challenges, we propose CausalRM, a causal-theoretic reward modeling framework that aims to learn unbiased reward models from observational feedback. To tackle challenge (1), CausalRM introduces a noise-aware surrogate loss term that is provably equivalent to the primal loss under noise-free conditions by explicitly modeling the annotation error generation process. To tackle challenge (2), CausalRM uses propensity scores -- the probability of a user providing feedback for a given response -- to reweight training samples, yielding a loss function that eliminates user preference bias. Extensive experiments across diverse LLM backbones and benchmark datasets validate that CausalRM effectively learns accurate reward signals from noisy and biased observational feedback and delivers substantial performance improvements on downstream RLHF tasks -- including a 49.2% gain on WildGuardMix and a 32.7% improvement on HarmBench. Code is available on our project website.
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
