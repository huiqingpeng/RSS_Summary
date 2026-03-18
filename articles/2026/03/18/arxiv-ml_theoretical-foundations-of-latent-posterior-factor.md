---
title: "Theoretical Foundations of Latent Posterior Factors: Formal Guarantees for Multi-Evidence Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15674"
published: "2026-03-18"
fetched: "2026-03-18T16:06:13.289752"
---

Computer Science > Artificial Intelligence
[Submitted on 13 Mar 2026]
Title:Theoretical Foundations of Latent Posterior Factors: Formal Guarantees for Multi-Evidence Reasoning
View PDF HTML (experimental)Abstract:We present a complete theoretical characterization of Latent Posterior Factors (LPF), a principled framework for aggregating multiple heterogeneous evidence items in probabilistic prediction tasks. Multi-evidence reasoning arises pervasively in high-stakes domains including healthcare diagnosis, financial risk assessment, legal case analysis, and regulatory compliance, yet existing approaches either lack formal guarantees or fail to handle multi-evidence scenarios architecturally. LPF encodes each evidence item into a Gaussian latent posterior via a variational autoencoder, converting posteriors to soft factors through Monte Carlo marginalization, and aggregating factors via exact Sum-Product Network inference (LPF-SPN) or a learned neural aggregator (LPF-Learned).
We prove seven formal guarantees spanning the key desiderata for trustworthy AI: Calibration Preservation (ECE <= epsilon + C/sqrt(K_eff)); Monte Carlo Error decaying as O(1/sqrt(M)); a non-vacuous PAC-Bayes bound with train-test gap of 0.0085 at N=4200; operation within 1.12x of the information-theoretic lower bound; graceful degradation as O(epsilon*delta*sqrt(K)) under corruption, maintaining 88% performance with half of evidence adversarially replaced; O(1/sqrt(K)) calibration decay with R^2=0.849; and exact epistemic-aleatoric uncertainty decomposition with error below 0.002%. All theorems are empirically validated on controlled datasets spanning up to 4,200 training examples. Our theoretical framework establishes LPF as a foundation for trustworthy multi-evidence AI in safety-critical applications.
Current browse context:
cs.AI
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
