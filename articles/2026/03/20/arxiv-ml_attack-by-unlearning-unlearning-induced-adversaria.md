---
title: "Attack by Unlearning: Unlearning-Induced Adversarial Attacks on Graph Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18570"
published: "2026-03-20"
fetched: "2026-03-20T12:13:41.898908"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Attack by Unlearning: Unlearning-Induced Adversarial Attacks on Graph Neural Networks
View PDF HTML (experimental)Abstract:Graph neural networks (GNNs) are widely used for learning from graph-structured data in domains such as social networks, recommender systems, and financial platforms. To comply with privacy regulations like the GDPR, CCPA, and PIPEDA, approximate graph unlearning, which aims to remove the influence of specific data points from trained models without full retraining, has become an increasingly important component of trustworthy graph learning. However, approximate unlearning often incurs subtle performance degradation, which may incur negative and unintended side effects. In this work, we show that such degradations can be amplified into adversarial attacks. We introduce the notion of \textbf{unlearning corruption attacks}, where an adversary injects carefully chosen nodes into the training graph and later requests their deletion. Because deletion requests are legally mandated and cannot be denied, this attack surface is both unavoidable and stealthy: the model performs normally during training, but accuracy collapses only after unlearning is applied. Technically, we formulate this attack as a bi-level optimization problem: to overcome the challenges of black-box unlearning and label scarcity, we approximate the unlearning process via gradient-based updates and employ a surrogate model to generate pseudo-labels for the optimization. Extensive experiments across benchmarks and unlearning algorithms demonstrate that small, carefully designed unlearning requests can induce significant accuracy degradation, raising urgent concerns about the robustness of GNN unlearning under real-world regulatory demands. The source code will be released upon paper acceptance.
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
