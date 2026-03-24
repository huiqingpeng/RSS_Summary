---
title: "Understanding Behavior Cloning with Action Quantization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20538"
published: "2026-03-24"
fetched: "2026-03-25T07:11:30.486026"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Understanding Behavior Cloning with Action Quantization
View PDF HTML (experimental)Abstract:Behavior cloning is a fundamental paradigm in machine learning, enabling policy learning from expert demonstrations across robotics, autonomous driving, and generative models. Autoregressive models like transformer have proven remarkably effective, from large language models (LLMs) to vision-language-action systems (VLAs). However, applying autoregressive models to continuous control requires discretizing actions through quantization, a practice widely adopted yet poorly understood theoretically. This paper provides theoretical foundations for this practice. We analyze how quantization error propagates along the horizon and interacts with statistical sample complexity. We show that behavior cloning with quantized actions and log-loss achieves optimal sample complexity, matching existing lower bounds, and incurs only polynomial horizon dependence on quantization error, provided the dynamics are stable and the policy satisfies a probabilistic smoothness condition. We further characterize when different quantization schemes satisfy or violate these requirements, and propose a model-based augmentation that provably improves the error bound without requiring policy smoothness. Finally, we establish fundamental limits that jointly capture the effects of quantization error and statistical complexity.
Current browse context:
cs.LG
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
