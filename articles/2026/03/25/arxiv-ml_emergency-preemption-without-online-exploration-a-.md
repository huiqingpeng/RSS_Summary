---
title: "Emergency Preemption Without Online Exploration: A Decision Transformer Approach"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22315"
published: "2026-03-25"
fetched: "2026-03-26T07:09:59.753473"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Emergency Preemption Without Online Exploration: A Decision Transformer Approach
View PDF HTML (experimental)Abstract:Emergency vehicle (EV) response time is a critical determinant of survival outcomes, yet deployed signal preemption strategies remain reactive and uncontrollable. We propose a return-conditioned framework for emergency corridor optimization based on the Decision Transformer (DT). By casting corridor optimization as offline, return-conditioned sequence modeling, our approach (1) eliminates online environment interaction during policy learning, (2) enables dispatch-level urgency control through a single target-return scalar, and (3) extends to multi-agent settings via a Multi-Agent Decision Transformer (MADT) with graph attention for spatial coordination. On the LightSim simulator, DT reduces average EV travel time by 37.7% relative to fixed-timing preemption on a 4x4 grid (88.6 s vs. 142.3 s), achieving the lowest civilian delay (11.3 s/veh) and fewest EV stops (1.2) among all methods, including online RL baselines that require environment interaction. MADT further improves on larger grids, overtaking DT with 45.2% reduction on 8x8 via graph-attention coordination. Return conditioning produces a smooth dispatch interface: varying the target return from 100 to -400 trades EV travel time (72.4-138.2 s) against civilian delay (16.8-5.4 s/veh), requiring no retraining. A Constrained DT extension adds explicit civilian disruption budgets as a second control knob.
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
