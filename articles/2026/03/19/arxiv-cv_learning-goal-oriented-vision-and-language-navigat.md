---
title: "Learning Goal-Oriented Vision-and-Language Navigation with Self-Improving Demonstrations at Scale"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.24910"
published: "2026-03-19"
fetched: "2026-03-19T16:26:05.205998"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 29 Sep 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Learning Goal-Oriented Vision-and-Language Navigation with Self-Improving Demonstrations at Scale
View PDF HTML (experimental)Abstract:Goal-oriented vision-language navigation requires robust exploration capabilities for agents to navigate to specified goals in unknown environments without step-by-step instructions. Existing methods tend to exclusively utilize shortest-path trajectories, lacking effective exploration priors for training navigation agents. To address the above challenges, we present SID, a goal-oriented vision-and-language navigation learning approach with Self-Improving Demonstrations. Specifically, SID learns an initial agent on the shortest-path data sampled from environments and then leverages this agent to generate novel exploration trajectories. The novel rollouts provide demonstrations with stronger exploration strategies to train a better agent, which in turn produces higher-quality agent demonstrations for the next round of training. We show that this iterative self-improving pipeline readily scales to new environments, and the resulting demonstrations are highly transferable, elevating the performance ceiling across a variety of vision-and-language navigation tasks. Extensive experiments demonstrate that SID significantly boosts the exploration capabilities and generalization of navigation agents. The resulting agent achieves new state-of-the-art performance on goal-oriented vision-and-language navigation benchmarks, including REVERIE, SOON as well as strong transferability to object-goal navigation and VLN-CE. It notably achieves a 50.9% success rate on the unseen validation splits of SOON, surpassing prior leading approaches by a margin of 13.9%.
Submission history
From: Songze Li [view email][v1] Mon, 29 Sep 2025 15:15:54 UTC (4,373 KB)
[v2] Wed, 18 Mar 2026 13:54:05 UTC (6,191 KB)
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
