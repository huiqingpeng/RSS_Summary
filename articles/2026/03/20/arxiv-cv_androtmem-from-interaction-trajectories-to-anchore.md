---
title: "AndroTMem: From Interaction Trajectories to Anchored Memory in Long-Horizon GUI Agents"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18429"
published: "2026-03-20"
fetched: "2026-03-20T15:08:37.504001"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:AndroTMem: From Interaction Trajectories to Anchored Memory in Long-Horizon GUI Agents
View PDF HTML (experimental)Abstract:Long-horizon GUI agents are a key step toward real-world deployment, yet effective interaction memory under prevailing paradigms remains under-explored. Replaying full interaction sequences is redundant and amplifies noise, while summaries often erase dependency-critical information and traceability. We present AndroTMem, a diagnostic framework for anchored memory in long-horizon Android GUI agents. Its core benchmark, AndroTMem-Bench, comprises 1,069 tasks with 34,473 interaction steps (avg. 32.1 per task, max. 65). We evaluate agents with TCR (Task Complete Rate), focusing on tasks whose completion requires carrying forward critical intermediate state; AndroTMem-Bench is designed to enforce strong step-to-step causal dependencies, making sparse yet essential intermediate states decisive for downstream actions and centering interaction memory in evaluation. Across open- and closed-source GUI agents, we observe a consistent pattern: as interaction sequences grow longer, performance drops are driven mainly by within-task memory failures, not isolated perception errors or local action mistakes. Guided by this diagnosis, we propose Anchored State Memory (ASM), which represents interaction sequences as a compact set of causally linked intermediate-state anchors to enable subgoal-targeted retrieval and attribution-aware decision making. Across multiple settings and 12 evaluated GUI agents, ASM consistently outperforms full-sequence replay and summary-based baselines, improving TCR by 5%-30.16% and AMS by 4.93%-24.66%, indicating that anchored, structured memory effectively mitigates the interaction-memory bottleneck in long-horizon GUI tasks. The code, benchmark, and related resources are publicly available at [this https URL](this https URL).
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
