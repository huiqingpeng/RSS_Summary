---
title: "Why the Maximum Second Derivative of Activations Matters for Adversarial Robustness"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23860"
published: "2026-03-26"
fetched: "2026-03-27T07:17:52.186873"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Why the Maximum Second Derivative of Activations Matters for Adversarial Robustness
View PDF HTML (experimental)Abstract:This work investigates the critical role of activation function curvature -- quantified by the maximum second derivative $\max|\sigma''|$ -- in adversarial robustness. Using the Recursive Curvature-Tunable Activation Family (RCT-AF), which enables precise control over curvature through parameters $\alpha$ and $\beta$, we systematically analyze this relationship. Our study reveals a fundamental trade-off: insufficient curvature limits model expressivity, while excessive curvature amplifies the normalized Hessian diagonal norm of the loss, leading to sharper minima that hinder robust generalization. This results in a non-monotonic relationship where optimal adversarial robustness consistently occurs when $\max|\sigma''|$ falls within 4 to 10, a finding that holds across diverse network architectures, datasets, and adversarial training methods. We provide theoretical insights into how activation curvature affects the diagonal elements of the hessian matrix of the loss, and experimentally demonstrate that the normalized Hessian diagonal norm exhibits a U-shaped dependence on $\max|\sigma''|$, with its minimum within the optimal robustness range, thereby validating the proposed mechanism.
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
