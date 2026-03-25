---
title: "Conformal Risk Control for Safety-Critical Wildfire Evacuation Mapping: A Comparative Study of Tabular, Spatial, and Graph-Based Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22331"
published: "2026-03-25"
fetched: "2026-03-26T07:12:04.738190"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Conformal Risk Control for Safety-Critical Wildfire Evacuation Mapping: A Comparative Study of Tabular, Spatial, and Graph-Based Models
View PDF HTML (experimental)Abstract:Every wildfire prediction model deployed today shares a dangerous property: none of these methods provides formal guarantees on how much fire spread is missed. Despite extensive work on wildfire spread prediction using deep learning, no prior study has applied distribution-free safety guarantees to this domain, leaving evacuation planners reliant on probability thresholds with no formal assurance. We address this gap by presenting, to our knowledge, the first application of conformal risk control (CRC) to wildfire spread prediction, providing finite-sample guarantees on false negative rate (FNR <= 0.05). We expose a stark failure: across three model families of increasing complexity (tabular: LightGBM, AUROC 0.854; convolutional: Tiny U-Net, AUROC 0.969; and graph-based: Hybrid ResGNN-UNet, AUROC 0.964), standard thresholds capture only 7-72% of true fire spread. CRC eliminates this failure uniformly. Our central finding is that model architecture determines evacuation efficiency, while CRC determines safety: both spatial models with CRC achieve approximately 95% fire coverage while flagging only approximately 15% of total pixels, making them 4.2x more efficient than LightGBM, while the graph model's additional complexity over a simple U-Net yields no meaningful efficiency gain. We propose a shift-aware three-way CRC framework that assigns SAFE/MONITOR/EVACUATE zones for operational triage, and characterize a fundamental limitation of prevalence-weighted bounds under extreme class imbalance (approximately 5% fire prevalence). All models, calibration code, and evaluation pipelines are released for reproducibility.
Submission history
From: Baljinnyam Dayan [view email][v1] Fri, 20 Mar 2026 21:05:13 UTC (2,291 KB)
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
