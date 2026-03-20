---
title: "FedTrident: Resilient Road Condition Classification Against Poisoning Attacks in Federated Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19101"
published: "2026-03-20"
fetched: "2026-03-20T13:20:00.574188"
---

Computer Science > Cryptography and Security
[Submitted on 19 Mar 2026]
Title:FedTrident: Resilient Road Condition Classification Against Poisoning Attacks in Federated Learning
View PDF HTML (experimental)Abstract:FL has emerged as a transformative paradigm for ITS, notably camera-based Road Condition Classification (RCC). However, by enabling collaboration, FL-based RCC exposes the system to adversarial participants launching Targeted Label-Flipping Attacks (TLFAs). Malicious clients (vehicles) can relabel their local training data (e.g., from an actual uneven road to a wrong smooth road), consequently compromising global model predictions and jeopardizing transportation safety. Existing countermeasures against such poisoning attacks fail to maintain resilient model performance near the necessary attack-free levels in various attack scenarios due to: 1) not tailoring poisoned local model detection to TLFAs, 2) not excluding malicious vehicular clients based on historical behavior, and 3) not remedying the already-corrupted global model after exclusion. To close this research gap, we propose FedTrident, which introduces: 1) neuron-wise analysis for local model misbehavior detection (notably including attack goal identification, critical feature extraction, and GMM-based model clustering and filtering); 2) adaptive client rating for client exclusion according to the local model detection results in each FL round; and 3) machine unlearning for corrupted global model remediation once malicious clients are excluded during FL. Extensive evaluation across diverse FL-RCC models, tasks, and configurations demonstrates that FedTrident can effectively thwart TLFAs, achieving performance comparable to that in attack-free scenarios and outperforming eight baseline countermeasures by 9.49% and 4.47% for the two most critical metrics. Moreover, FedTrident is resilient to various malicious client rates, data heterogeneity levels, complicated multi-task, and dynamic attacks.
Current browse context:
cs.CR
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
