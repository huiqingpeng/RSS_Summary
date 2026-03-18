---
title: "Encoding Predictability and Legibility for Style-Conditioned Diffusion Policy"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16368"
published: "2026-03-18"
fetched: "2026-03-18T16:12:41.216374"
---

Computer Science > Robotics
[Submitted on 17 Mar 2026]
Title:Encoding Predictability and Legibility for Style-Conditioned Diffusion Policy
View PDF HTML (experimental)Abstract:Striking a balance between efficiency and transparent motion is a core challenge in human-robot collaboration, as highly expressive movements often incur unnecessary time and energy costs. In collaborative environments, legibility allows a human observer a better understanding of the robot's actions, increasing safety and trust. However, these behaviors result in sub-optimal and exaggerated trajectories that are redundant in low-ambiguity scenarios where the robot's goal is already obvious. To address this trade-off, we propose Style-Conditioned Diffusion Policy (SCDP), a modular framework that constrains the trajectory generation of a pre-trained diffusion model toward either legibility or efficiency based on the environment's configuration. Our method utilizes a post-training pipeline that freezes the base policy and trains a lightweight scene encoder and conditioning predictor to modulate the diffusion process. At inference time, an ambiguity detection module activates the appropriate conditioning, prioritizing expressive motion only for ambiguous goals and reverting to efficient paths otherwise. We evaluate SCDP on manipulation and navigation tasks, and results show that it enhances legibility in ambiguous settings while preserving optimal efficiency when legibility is unnecessary, all without retraining the base policy.
Submission history
From: Adrien Jacquet Crétides [view email][v1] Tue, 17 Mar 2026 10:55:44 UTC (983 KB)
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
