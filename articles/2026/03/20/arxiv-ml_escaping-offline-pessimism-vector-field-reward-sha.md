---
title: "Escaping Offline Pessimism: Vector-Field Reward Shaping for Safe Frontier Exploration"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18326"
published: "2026-03-20"
fetched: "2026-03-20T12:10:29.992712"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Escaping Offline Pessimism: Vector-Field Reward Shaping for Safe Frontier Exploration
View PDF HTML (experimental)Abstract:While offline reinforcement learning provides reliable policies for real-world deployment, its inherent pessimism severely restricts an agent's ability to explore and collect novel data online. Drawing inspiration from safe reinforcement learning, exploring near the boundary of regions well covered by the offline dataset and reliably modeled by the simulator allows an agent to take manageable risks--venturing into informative but moderate-uncertainty states while remaining close enough to familiar regions for safe recovery. However, naively rewarding this boundary-seeking behavior can lead to a degenerate parking behavior, where the agent simply stops once it reaches the frontier. To solve this, we propose a novel vector-field reward shaping paradigm designed to induce continuous, safe boundary exploration for non-adaptive deployed policies. Operating on an uncertainty oracle trained from offline data, our reward combines two complementary components: a gradient-alignment term that attracts the agent toward a target uncertainty level, and a rotational-flow term that promotes motion along the local tangent plane of the uncertainty manifold. Through theoretical analysis, we show that this reward structure naturally induces sustained exploratory behavior along the boundary while preventing degenerate solutions. Empirically, by integrating our proposed reward shaping with Soft Actor-Critic on a 2D continuous navigation task, we validate that agents successfully traverse uncertainty boundaries while balancing safe, informative data collection with primary task completion.
Submission history
From: Amirhossein Roknilamouki [view email][v1] Wed, 18 Mar 2026 22:18:27 UTC (1,632 KB)
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
