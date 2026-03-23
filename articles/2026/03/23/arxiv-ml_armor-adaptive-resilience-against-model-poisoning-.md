---
title: "ARMOR: Adaptive Resilience Against Model Poisoning Attacks in Continual Federated Learning for Mobile Indoor Localization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19594"
published: "2026-03-23"
fetched: "2026-03-24T07:19:46.303880"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:ARMOR: Adaptive Resilience Against Model Poisoning Attacks in Continual Federated Learning for Mobile Indoor Localization
View PDFAbstract:Indoor localization has become increasingly essential for applications ranging from asset tracking to delivering personalized services. Federated learning (FL) offers a privacy-preserving approach by training a centralized global model (GM) using distributed data from mobile devices without sharing raw data. However, real-world deployments require a continual federated learning (CFL) setting, where the GM receives continual updates under device heterogeneity and evolving indoor environments. In such dynamic conditions, erroneous or biased updates can cause the GM to deviate from its expected learning trajectory, gradually degrading internal GM representations and GM localization performance. This vulnerability is further exacerbated by adversarial model poisoning attacks. To address this challenge, we propose ARMOR, a novel CFL-based framework that monitors and safeguards the GM during continual updates. ARMOR introduces a novel state-space model (SSM) that learns the historical evolution of GM weight tensors and predicts the expected next state of weight tensors of the GM. By comparing incoming local updates with this SSM projection, ARMOR detects deviations and selectively mitigates corrupted updates before local updates are aggregated with the GM. This mechanism enables robust adaptation to temporal environmental dynamics and mitigate the effects of model poisoning attacks while preventing GM corruption. Experimental evaluations in real-world conditions indicate that ARMOR achieves notable improvements, with up to 8.0x reduction in mean error and 4.97x reduction in worst-case error compared to state-of-the-art indoor localization frameworks, demonstrating strong resilience against model corruption tested using real-world data and mobile devices.
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
