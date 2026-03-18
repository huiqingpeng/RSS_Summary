---
title: "Communication-Aware Multi-Agent Reinforcement Learning for Decentralized Cooperative UAV Deployment"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16141"
published: "2026-03-18"
fetched: "2026-03-18T16:10:49.967292"
---

Computer Science > Multiagent Systems
[Submitted on 17 Mar 2026]
Title:Communication-Aware Multi-Agent Reinforcement Learning for Decentralized Cooperative UAV Deployment
View PDF HTML (experimental)Abstract:Autonomous Unmanned Aerial Vehicle (UAV) swarms are increasingly used as rapidly deployable aerial relays and sensing platforms, yet practical deployments must operate under partial observability and intermittent peer-to-peer links. We present a graph-based multi-agent reinforcement learning framework trained under centralized training with decentralized execution (CTDE): a centralized critic and global state are available only during training, while each UAV executes a shared policy using local observations and messages from nearby neighbors. Our architecture encodes local agent state and nearby entities with an agent-entity attention module, and aggregates inter-UAV messages with neighbor self-attention over a distance-limited communication graph. We evaluate primarily on a cooperative relay deployment task (DroneConnect) and secondarily on an adversarial engagement task (DroneCombat). In DroneConnect, the proposed method achieves high coverage under restricted communication and partial observation (e.g. 74% coverage with M = 5 UAVs and N = 10 nodes) while remaining competitive with a mixed-integer linear programming (MILP) optimization-based offline upper bound, and it generalizes to unseen team sizes without fine-tuning. In the adversarial setting, the same framework transfers without architectural changes and improves win rate over non-communicating baselines.
Current browse context:
cs.MA
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
