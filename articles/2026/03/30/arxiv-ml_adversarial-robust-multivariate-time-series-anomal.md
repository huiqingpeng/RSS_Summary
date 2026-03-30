---
title: "Adversarial-Robust Multivariate Time-Series Anomaly Detection via Joint Information Retention"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25956"
published: "2026-03-30"
fetched: "2026-03-31T07:20:10.826641"
---

Computer Science > Machine Learning
[Submitted on 26 Mar 2026]
Title:Adversarial-Robust Multivariate Time-Series Anomaly Detection via Joint Information Retention
View PDF HTML (experimental)Abstract:Time-series anomaly detection (TSAD) is a critical component in monitoring complex systems, yet modern deep learning-based detectors are often highly sensitive to localized input corruptions and structured noise. We propose ARTA (Adversarially Robust multivariate Time-series Anomaly detection via joint information retention), a joint training framework that improves detector robustness through a principled min-max optimization objective. ARTA comprises an anomaly detector and a sparsity-constrained mask generator that are trained simultaneously. The generator identifies minimal, task-relevant temporal perturbations that maximally increase the detector's anomaly score, while the detector is optimized to remain stable under these structured perturbations. The resulting masks characterize the detector's sensitivity to adversarial temporal corruptions and can serve as explanatory signals for the detector's decisions. This adversarial training strategy exposes brittle decision pathways and encourages the detector to rely on distributed and stable temporal patterns rather than spurious localized artifacts. We conduct extensive experiments on the TSB-AD benchmark, demonstrating that ARTA consistently improves anomaly detection performance across diverse datasets and exhibits significantly more graceful degradation under increasing noise levels compared to state-of-the-art baselines.
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
