---
title: "Beware Untrusted Simulators -- Reward-Free Backdoor Attacks in Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.05089"
published: "2026-03-19"
fetched: "2026-03-19T14:18:27.064771"
---

Computer Science > Cryptography and Security
[Submitted on 4 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Beware Untrusted Simulators -- Reward-Free Backdoor Attacks in Reinforcement Learning
View PDF HTML (experimental)Abstract:Simulated environments are a key piece in the success of Reinforcement Learning (RL), allowing practitioners and researchers to train decision making agents without running expensive experiments on real hardware. Simulators remain a security blind spot, however, enabling adversarial developers to alter the dynamics of their released simulators for malicious purposes. Therefore, in this work we highlight a novel threat, demonstrating how simulator dynamics can be exploited to stealthily implant action-level backdoors into RL agents. The backdoor then allows an adversary to reliably activate targeted actions in an agent upon observing a predefined ``trigger'', leading to potentially dangerous consequences. Traditional backdoor attacks are limited in their strong threat models, assuming the adversary has near full control over an agent's training pipeline, enabling them to both alter and observe agent's rewards. As these assumptions are infeasible to implement within a simulator, we propose a new attack ``Daze'' which is able to reliably and stealthily implant backdoors into RL agents trained for real world tasks without altering or even observing their rewards. We provide formal proof of Daze's effectiveness in guaranteeing attack success across general RL tasks along with extensive empirical evaluations on both discrete and continuous action space domains. We additionally provide the first example of RL backdoor attacks transferring to real, robotic hardware. These developments motivate further research into securing all components of the RL training pipeline to prevent malicious attacks.
Submission history
From: Ethan Rathbun [view email][v1] Wed, 4 Feb 2026 22:17:23 UTC (13,586 KB)
[v2] Mon, 9 Feb 2026 17:46:50 UTC (18,634 KB)
[v3] Wed, 18 Mar 2026 14:45:34 UTC (13,586 KB)
Current browse context:
cs.CR
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
