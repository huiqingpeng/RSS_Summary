---
title: "Learning When to Act: Interval-Aware Reinforcement Learning with Predictive Temporal Structure"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22384"
published: "2026-03-25"
fetched: "2026-03-26T07:14:23.082668"
---

Computer Science > Machine Learning
[Submitted on 23 Mar 2026]
Title:Learning When to Act: Interval-Aware Reinforcement Learning with Predictive Temporal Structure
View PDF HTML (experimental)Abstract:Autonomous agents operating in continuous environments must decide not only what to do, but when to act. We introduce a lightweight adaptive temporal control system that learns the optimal interval between cognitive ticks from experience, replacing ad hoc biologically inspired timers with a principled learned policy. The policy state is augmented with a predictive hyperbolic spread signal (a "curvature signal" shorthand) derived from hyperbolic geometry: the mean pairwise Poincare distance among n sampled futures embedded in the Poincare ball. High spread indicates a branching, uncertain future and drives the agent to act sooner; low spread signals predictability and permits longer rest intervals. We further propose an interval-aware reward that explicitly penalises inefficiency relative to the chosen wait time, correcting a systematic credit-assignment failure of naive outcome-based rewards in timing problems. We additionally introduce a joint spatio-temporal embedding (ATCPG-ST) that concatenates independently normalised state and position projections in the Poincare ball; spatial trajectory divergence provides an independent timing signal unavailable to the state-only variant (ATCPG-SO). This extension raises mean hyperbolic spread (kappa) from 1.88 to 3.37 and yields a further 5.8 percent efficiency gain over the state-only baseline. Ablation experiments across five random seeds demonstrate that (i) learning is the dominant efficiency factor (54.8 percent over no-learning), (ii) hyperbolic spread provides significant complementary gain (26.2 percent over geometry-free control), (iii) the combined system achieves 22.8 percent efficiency over the fixed-interval baseline, and (iv) adding spatial position information to the spread embedding yields an additional 5.8 percent.
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
