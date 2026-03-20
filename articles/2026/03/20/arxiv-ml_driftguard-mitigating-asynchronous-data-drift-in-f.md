---
title: "DriftGuard: Mitigating Asynchronous Data Drift in Federated Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18872"
published: "2026-03-20"
fetched: "2026-03-20T12:16:17.676939"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:DriftGuard: Mitigating Asynchronous Data Drift in Federated Learning
View PDF HTML (experimental)Abstract:In real-world Federated Learning (FL) deployments, data distributions on devices that participate in training evolve over time. This leads to asynchronous data drift, where different devices shift at different times and toward different distributions. Mitigating such drift is challenging: frequent retraining incurs high computational cost on resource-constrained devices, while infrequent retraining degrades performance on drifting devices. We propose DriftGuard, a federated continual learning framework that efficiently adapts to asynchronous data drift. DriftGuard adopts a Mixture-of-Experts (MoE) inspired architecture that separates shared parameters, which capture globally transferable knowledge, from local parameters that adapt to group-specific distributions. This design enables two complementary retraining strategies: (i) global retraining, which updates the shared parameters when system-wide drift is identified, and (ii) group retraining, which selectively updates local parameters for clusters of devices identified via MoE gating patterns, without sharing raw data. Experiments across multiple datasets and models show that DriftGuard matches or exceeds state-of-the-art accuracy while reducing total retraining cost by up to 83%. As a result, it achieves the highest accuracy per unit retraining cost, improving over the strongest baseline by up to 2.3x. DriftGuard is available for download from this https URL.
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
