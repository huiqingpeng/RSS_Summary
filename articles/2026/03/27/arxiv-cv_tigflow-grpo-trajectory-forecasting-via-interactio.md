---
title: "TIGFlow-GRPO: Trajectory Forecasting via Interaction-Aware Flow Matching and Reward-Driven Optimization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24936"
published: "2026-03-27"
fetched: "2026-03-28T07:18:30.150243"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Mar 2026]
Title:TIGFlow-GRPO: Trajectory Forecasting via Interaction-Aware Flow Matching and Reward-Driven Optimization
View PDF HTML (experimental)Abstract:Human trajectory forecasting is important for intelligent multimedia systems operating in visually complex environments, such as autonomous driving and crowd surveillance. Although Conditional Flow Matching (CFM) has shown strong ability in modeling trajectory distributions from spatio-temporal observations, existing approaches still focus primarily on supervised fitting, which may leave social norms and scene constraints insufficiently reflected in generated trajectories. To address this issue, we propose TIGFlow-GRPO, a two-stage generative framework that aligns flow-based trajectory generation with behavioral rules. In the first stage, we build a CFM-based predictor with a Trajectory-Interaction-Graph (TIG) module to model fine-grained visual-spatial interactions and strengthen context encoding. This stage captures both agent-agent and agent-scene relations more effectively, providing more informative conditional features for subsequent alignment. In the second stage, we perform Flow-GRPO post-training,where deterministic flow rollout is reformulated as stochastic ODE-to-SDE sampling to enable trajectory exploration, and a composite reward combines view-aware social compliance with map-aware physical feasibility. By evaluating trajectories explored through SDE rollout, GRPO progressively steers multimodal predictions toward behaviorally plausible futures. Experiments on the ETH/UCY and SDD datasets show that TIGFlow-GRPO improves forecasting accuracy and long-horizon stability while generating trajectories that are more socially compliant and physically feasible. These results suggest that the proposed framework provides an effective way to connect flow-based trajectory modeling with behavior-aware alignment in dynamic multimedia environments.
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
