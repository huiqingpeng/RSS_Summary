---
title: "VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17652"
published: "2026-03-19"
fetched: "2026-03-19T16:22:28.484700"
---

Computer Science > Robotics
[Submitted on 18 Mar 2026]
Title:VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs
View PDF HTML (experimental)Abstract:Closed-loop evaluation of autonomous-driving policies requires interactive simulation beyond log replay. However, existing generative world models often degrade in closed loop due to (i) history-free initialization that mismatches policy inputs, (ii) multi-step sampling latency that violates real-time budgets, and (iii) compounding kinematic infeasibility over long horizons. We propose VectorWorld, a streaming world model that incrementally generates ego-centric $64 \mathrm{m}\times 64\mathrm{m}$ lane--agent vector-graph tiles during rollout. VectorWorld aligns initialization with history-conditioned policies by producing a policy-compatible interaction state via a motion-aware gated VAE. It enables real-time outpainting via solver-free one-step masked completion with an edge-gated relational DiT trained with interval-conditioned MeanFlow and JVP-based large-step supervision. To stabilize long-horizon rollouts, we introduce $\Delta$Sim, a physics-aligned non-ego (NPC) policy with hybrid discrete--continuous actions and differentiable kinematic logit shaping. On Waymo open motion and nuPlan, VectorWorld improves map-structure fidelity and initialization validity, and supports stable, real-time $1\mathrm{km}+$ closed-loop rollouts (\href{this https URL}{code}).
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
