---
title: "Learn for Variation: Variationally Guided AAV Trajectory Learning in Differentiable Environments"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18853"
published: "2026-03-20"
fetched: "2026-03-20T13:16:34.486322"
---

Electrical Engineering and Systems Science > Systems and Control
[Submitted on 19 Mar 2026]
Title:Learn for Variation: Variationally Guided AAV Trajectory Learning in Differentiable Environments
View PDF HTML (experimental)Abstract:Autonomous aerial vehicles (AAVs) empower sixth-generation (6G) Internet-of-Things (IoT) networks through mobility-driven data collection. However, conventional reward-driven reinforcement learning for AAV trajectory planning suffers from severe credit assignment issues and training instability, because sparse scalar rewards fail to capture the long-term and nonlinear effects of sequential movements. To address these challenges, this paper proposes Learn for Variation (L4V), a gradient-informed trajectory learning framework that replaces high-variance scalar reward signals with dense and analytically grounded policy gradients. Particularly, the coupled evolution of AAV kinematics, distance-dependent channel gains, and per-user data-collection progress is first unrolled into an end-to-end differentiable computational graph. Backpropagation through time then serves as a discrete adjoint solver, which propagates exact sensitivities from the cumulative mission objective to every control action and policy parameter. These structured gradients are used to train a deterministic neural policy with temporal smoothness regularization and gradient clipping. Extensive simulations demonstrate that L4V consistently outperforms representative baselines, including a genetic algorithm, DQN, A2C, and DDPG, in mission completion time, average transmission rate, and training cost
Current browse context:
eess.SY
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
