---
title: "Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18342"
published: "2026-03-20"
fetched: "2026-03-20T13:11:44.816189"
---

Computer Science > Robotics
[Submitted on 18 Mar 2026]
Title:Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model
View PDF HTML (experimental)Abstract:Vision-Language-Action (VLA) models enable general-purpose robotic policies by mapping visual observations and language instructions to low-level actions, but they often lack reliable introspection. A common practice is to compute a token-level uncertainty signal and take its mean over a rollout. However, mean aggregation can dilute short-lived but safety-critical uncertainty spikes in continuous control. In particular, successful rollouts may contain localized high-entropy segments due to benign noise or non-critical micro-adjustments, while failure rollouts can appear low-entropy for most timesteps and only exhibit brief spikes near the onset of failure. We propose a unified uncertainty quantification approach for predicting rollout success versus failure that (1) uses max-based sliding window pooling to preserve transient risk signals, (2) applies motion-aware stability weighting to emphasize high-frequency action oscillations associated with unstable behaviors, and (3) performs DoF-adaptive calibration via Bayesian Optimization to prioritize kinematically critical axes. Experiments on the LIBERO benchmark show that our method substantially improves failure prediction accuracy and yields more reliable signals for failure detection, which can support downstream human-in-the-loop interventions.
Current browse context:
cs.RO
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
