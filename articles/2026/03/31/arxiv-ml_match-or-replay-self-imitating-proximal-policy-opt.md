---
title: "Match or Replay: Self Imitating Proximal Policy Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27515"
published: "2026-03-31"
fetched: "2026-04-01T07:25:12.291555"
---

Computer Science > Machine Learning
[Submitted on 29 Mar 2026]
Title:Match or Replay: Self Imitating Proximal Policy Optimization
View PDF HTML (experimental)Abstract:Reinforcement Learning (RL) agents often struggle with inefficient exploration, particularly in environments with sparse rewards. Traditional exploration strategies can lead to slow learning and suboptimal performance because agents fail to systematically build on previously successful experiences, thereby reducing sample efficiency. To tackle this issue, we propose a self-imitating on-policy algorithm that enhances exploration and sample efficiency by leveraging past high-reward state-action pairs to guide policy updates. Our method incorporates self-imitation by using optimal transport distance in dense reward environments to prioritize state visitation distributions that match the most rewarding trajectory. In sparse-reward environments, we uniformly replay successful self-encountered trajectories to facilitate structured exploration. Experimental results across diverse environments demonstrate substantial improvements in learning efficiency, including MuJoCo for dense rewards and the partially observable 3D Animal-AI Olympics and multi-goal PointMaze for sparse rewards. Our approach achieves faster convergence and significantly higher success rates compared to state-of-the-art self-imitating RL baselines. These findings underscore the potential of self-imitation as a robust strategy for enhancing exploration in RL, with applicability to more complex tasks.
Submission history
From: Gaurav Chaudhary [view email][v1] Sun, 29 Mar 2026 04:44:48 UTC (4,230 KB)
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
