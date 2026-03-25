---
title: "Confidence Calibration under Ambiguous Ground Truth"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22879"
published: "2026-03-25"
fetched: "2026-03-26T07:17:40.619792"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Confidence Calibration under Ambiguous Ground Truth
View PDF HTML (experimental)Abstract:Confidence calibration assumes a unique ground-truth label per input, yet this assumption fails wherever annotators genuinely disagree. Post-hoc calibrators fitted on majority-voted labels, the standard single-label targets used in practice, can appear well-calibrated under conventional evaluation yet remain substantially miscalibrated against the underlying annotator distribution. We show that this failure is structural: under simplifying assumptions, Temperature Scaling is biased toward temperatures that underestimate annotator uncertainty, with true-label miscalibration increasing monotonically with annotation entropy. To address this, we develop a family of ambiguity-aware post-hoc calibrators that optimise proper scoring rules against the full label distribution and require no model retraining. Our methods span progressively weaker annotation requirements: Dirichlet-Soft leverages the full annotator distribution and achieves the best overall calibration quality across settings; Monte Carlo Temperature Scaling with a single annotation per example (MCTS S=1) matches full-distribution calibration across all benchmarks, demonstrating that pre-aggregated label distributions are unnecessary; and Label-Smooth Temperature Scaling (LS-TS) operates with voted labels alone by constructing data-driven pseudo-soft targets from the model's own confidence. Experiments on four benchmarks with real multi-annotator distributions (CIFAR-10H, ChaosNLI) and clinically-informed synthetic annotations (ISIC~2019, DermaMNIST) show that Dirichlet-Soft reduces true-label ECE by 55-87% relative to Temperature Scaling, while LS-TS reduces ECE by 9-77% without any annotator data.
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
