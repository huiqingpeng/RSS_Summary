---
title: "Neural Collapse Dynamics: Depth, Activation, Regularisation, and Feature Norm Threshold"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00230"
published: "2026-04-02"
fetched: "2026-04-03T07:18:54.695567"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Neural Collapse Dynamics: Depth, Activation, Regularisation, and Feature Norm Threshold
View PDF HTML (experimental)Abstract:Neural collapse (NC) -- the convergence of penultimate-layer features to a simplex equiangular tight frame -- is well understood at equilibrium, but the dynamics governing its onset remain poorly characterised. We identify a simple and predictive regularity: NC occurs when the mean feature norm reaches a model-dataset-specific critical value, fn*, that is largely invariant to training conditions. This value concentrates tightly within each (model, dataset) pair (CV < 8%); training dynamics primarily affect the rate at which fn approaches fn*, rather than the value itself. In standard training trajectories, the crossing of fn below fn* consistently precedes NC onset, providing a practical predictor with a mean lead time of 62 epochs (MAE 24 epochs). A direct intervention experiment confirms fn* is a stable attractor of the gradient flow -- perturbations to feature scale are self-corrected during training, with convergence to the same value regardless of direction (p>0.2). Completing the (architecture)x(dataset) grid reveals the paper's strongest result: ResNet-20 on MNIST gives fn* = 5.867 -- a +458% architecture effect versus only +68% on CIFAR-10. The grid is strongly non-additive; fn* cannot be decomposed into independent architecture and dataset contributions. Four structural regularities emerge: (1) depth has a non-monotonic effect on collapse speed; (2) activation jointly determines both collapse speed and fn*; (3) weight decay defines a three-regime phase diagram -- too little slows, an optimal range is fastest, and too much prevents collapse; (4) width monotonically accelerates collapse while shifting fn* by at most 13%. These results establish feature-norm dynamics as an actionable diagnostic for predicting NC timing, suggesting that norm-threshold behaviour is a general mechanism underlying delayed representational reorganisation in deep networks.
Submission history
From: Anamika Paul Rupa [view email][v1] Tue, 31 Mar 2026 20:52:42 UTC (3,340 KB)
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
