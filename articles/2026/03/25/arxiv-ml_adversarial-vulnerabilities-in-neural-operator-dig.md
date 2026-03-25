---
title: "Adversarial Vulnerabilities in Neural Operator Digital Twins: Gradient-Free Attacks on Nuclear Thermal-Hydraulic Surrogates"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22525"
published: "2026-03-25"
fetched: "2026-03-26T07:14:58.623104"
---

Computer Science > Machine Learning
[Submitted on 23 Mar 2026]
Title:Adversarial Vulnerabilities in Neural Operator Digital Twins: Gradient-Free Attacks on Nuclear Thermal-Hydraulic Surrogates
View PDF HTML (experimental)Abstract:Operator learning models are rapidly emerging as the predictive core of digital twins for nuclear and energy systems, promising real-time field reconstruction from sparse sensor measurements. Yet their robustness to adversarial perturbations remains uncharacterized, a critical gap for deployment in safety-critical systems. Here we show that neural operators are acutely vulnerable to extremely sparse (fewer than 1% of inputs), physically plausible perturbations that exploit their sensitivity to boundary conditions. Using gradient-free differential evolution across four operator architectures, we demonstrate that minimal modifications trigger catastrophic prediction failures, increasing relative $L_2$ error from $\sim$1.5% (validated accuracy) to 37-63% while remaining completely undetectable by standard validation metrics. Notably, 100% of successful single-point attacks pass z-score anomaly detection. We introduce the effective perturbation dimension $d_{\text{eff}}$, a Jacobian-based diagnostic that, together with sensitivity magnitude, yields a two-factor vulnerability model explaining why architectures with extreme sensitivity concentration (POD-DeepONet, $d_{\text{eff}} \approx 1$) are not necessarily the most exploitable, since low-rank output projections cap maximum error, while moderate concentration with sufficient amplification (S-DeepONet, $d_{\text{eff}} \approx 4$) produces the highest attack success. Gradient-free search outperforms gradient-based alternatives (PGD) on architectures with gradient pathologies, while random perturbations of equal magnitude achieve near-zero success rates, confirming that the discovered vulnerabilities are structural. Our findings expose a previously overlooked attack surface in operator learning models and establish that these models require robustness guarantees beyond standard validation before deployment.
Submission history
From: Syed Bahauddin Alam [view email][v1] Mon, 23 Mar 2026 19:35:17 UTC (9,077 KB)
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
