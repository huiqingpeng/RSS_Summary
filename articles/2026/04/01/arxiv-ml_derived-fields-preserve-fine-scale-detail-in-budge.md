---
title: "Derived Fields Preserve Fine-Scale Detail in Budgeted Neural Simulators"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29224"
published: "2026-04-01"
fetched: "2026-04-02T07:16:24.566440"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Derived Fields Preserve Fine-Scale Detail in Budgeted Neural Simulators
View PDF HTML (experimental)Abstract:Fine-scale-faithful neural simulation under fixed storage budgets remains challenging. Many existing methods reduce high-frequency error by improving architectures, training objectives, or rollout strategies. However, under budgeted coarsen-quantize-decode pipelines, fine detail can already be lost when the carried state is constructed. In the canonical periodic incompressible Navier-Stokes setting, we show that primitive and derived fields undergo systematically different retained-band distortions under the same operator. Motivated by this observation, we formulate Derived-Field Optimization (DerivOpt), a general state-design framework that chooses which physical fields are carried and how storage budget is allocated across them under a calibrated channel model. Across the full time-dependent forward subset of PDEBench, DerivOpt not only improves pooled mean rollout nRMSE, but also delivers a decisive advantage in fine-scale fidelity over a broad set of strong baselines. More importantly, the gains are already visible at input time, before rollout learning begins. This indicates that the carried state is often the dominant bottleneck under tight storage budgets. These results suggest a broader conclusion: in budgeted neural simulation, carried-state design should be treated as a first-class design axis alongside architecture, loss, and rollout strategy.
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
