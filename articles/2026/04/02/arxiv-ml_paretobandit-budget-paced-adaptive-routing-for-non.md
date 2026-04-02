---
title: "ParetoBandit: Budget-Paced Adaptive Routing for Non-Stationary LLM Serving"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00136"
published: "2026-04-02"
fetched: "2026-04-03T07:17:35.714118"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:ParetoBandit: Budget-Paced Adaptive Routing for Non-Stationary LLM Serving
View PDF HTML (experimental)Abstract:Production LLM serving often relies on multi-model portfolios spanning a ~530x cost range, where routing decisions trade off quality against cost. This trade-off is non-stationary: providers revise pricing, model quality can regress silently, and new models must be integrated without downtime. We present ParetoBandit, an open-source adaptive router built on cost-aware contextual bandits that is the first to simultaneously enforce dollar-denominated budgets, adapt online to such shifts, and onboard new models at runtime.
ParetoBandit closes these gaps through three mechanisms. An online primal-dual budget pacer enforces a per-request cost ceiling over an open-ended stream, replacing offline penalty tuning with closed-loop control. Geometric forgetting on sufficient statistics enables rapid adaptation to price and quality shifts while bootstrapping from offline priors. A hot-swap registry lets operators add or remove models at runtime, with a brief forced-exploration phase for each newcomer, after which UCB selection discovers its quality-cost niche from live traffic alone.
We evaluate ParetoBandit across four deployment scenarios on 1,824 prompts routed through a three-model portfolio. Across seven budget ceilings, mean per-request cost never exceeds the target by more than 0.4%. When conditions shift, the system adapts: an order-of-magnitude price cut on the costliest model yields up to +0.071 quality lift, and a silent quality regression is detected and rerouted within budget. A cold-started model reaches meaningful adoption within ~142 steps without breaching the cost ceiling. The router discriminates rather than blindly adopting: expensive models are budget-gated and low-quality models rejected after bounded exploration. End-to-end routing latency is 9.8ms on CPU -- less than 0.4% of typical inference time -- with the routing decision itself taking just 22.5us.
Submission history
From: Annette Taberner-Miller [view email][v1] Tue, 31 Mar 2026 18:41:53 UTC (6,181 KB)
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
