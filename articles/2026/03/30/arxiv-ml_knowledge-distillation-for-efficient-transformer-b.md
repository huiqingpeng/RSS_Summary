---
title: "Knowledge Distillation for Efficient Transformer-Based Reinforcement Learning in Hardware-Constrained Energy Management Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26249"
published: "2026-03-30"
fetched: "2026-03-31T07:22:56.072804"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Knowledge Distillation for Efficient Transformer-Based Reinforcement Learning in Hardware-Constrained Energy Management Systems
View PDF HTML (experimental)Abstract:Transformer-based reinforcement learning has emerged as a strong candidate for sequential control in residential energy management. In particular, the Decision Transformer can learn effective battery dispatch policies from historical data, thereby increasing photovoltaic self-consumption and reducing electricity costs. However, transformer models are typically too computationally demanding for deployment on resource-constrained residential controllers, where memory and latency constraints are critical. This paper investigates knowledge distillation to transfer the decision-making behaviour of high-capacity Decision Transformer policies to compact models that are more suitable for embedded deployment. Using the Ausgrid dataset, we train teacher models in an offline sequence-based Decision Transformer framework on heterogeneous multi-building data. We then distil smaller student models by matching the teachers' actions, thereby preserving control quality while reducing model size. Across a broad set of teacher-student configurations, distillation largely preserves control performance and even yields small improvements of up to 1%, while reducing the parameter count by up to 96%, the inference memory by up to 90%, and the inference time by up to 63%. Beyond these compression effects, comparable cost improvements are also observed when distilling into a student model of identical architectural capacity. Overall, our results show that knowledge distillation makes Decision Transformer control more applicable for residential energy management on resource-limited hardware.
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
