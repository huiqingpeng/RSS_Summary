---
title: "Descent-Guided Policy Gradient for Scalable Cooperative Multi-Agent Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.20078"
published: "2026-03-18"
fetched: "2026-03-18T17:14:23.605827"
---

Computer Science > Multiagent Systems
[Submitted on 23 Feb 2026 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:Descent-Guided Policy Gradient for Scalable Cooperative Multi-Agent Learning
View PDF HTML (experimental)Abstract:Scaling cooperative multi-agent reinforcement learning (MARL) is fundamentally limited by cross-agent noise. When agents share a common reward, the actions of all $N$ agents jointly determine each agent's learning signal, so cross-agent noise grows with $N$. In the policy gradient setting, per-agent gradient estimate variance scales as $\Theta(N)$, yielding sample complexity $\mathcal{O}(N/\epsilon)$. We observe that many domains, including cloud computing, transportation, and power systems, have differentiable analytical models that prescribe efficient system states. In this work, we propose Descent-Guided Policy Gradient (DG-PG), a framework that utilizes these analytical models to provide each agent with a noise-free gradient signal, decoupling each agent's gradient from the actions of all others. We prove that DG-PG reduces gradient variance from $\Theta(N)$ to $\mathcal{O}(1)$, preserves the equilibria of the cooperative game, and achieves agent-independent sample complexity $\mathcal{O}(1/\epsilon)$. On a heterogeneous cloud scheduling task with up to 200 agents, DG-PG converges within 10 episodes at every tested scale, from $N{=}5$ to $N{=}200$, directly confirming the predicted scale-invariant complexity, while MAPPO and IPPO fail to converge under identical architectures.
Submission history
From: Shan Yang [view email][v1] Mon, 23 Feb 2026 17:45:08 UTC (287 KB)
[v2] Mon, 16 Mar 2026 18:56:19 UTC (291 KB)
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
