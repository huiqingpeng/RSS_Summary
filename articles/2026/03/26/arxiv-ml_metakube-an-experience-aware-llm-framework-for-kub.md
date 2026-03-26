---
title: "MetaKube: An Experience-Aware LLM Framework for Kubernetes Failure Diagnosis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23580"
published: "2026-03-26"
fetched: "2026-03-27T07:15:37.863412"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:MetaKube: An Experience-Aware LLM Framework for Kubernetes Failure Diagnosis
View PDF HTML (experimental)Abstract:Existing LLM-based Kubernetes diagnostic systems cannot learn from operational experience, operating on static knowledge bases without improving from past resolutions. We present MetaKube, an experience-aware LLM framework through three synergistic innovations: (1) an Episodic Pattern Memory Network (EPMN) that abstracts diagnostic patterns from historical resolutions and provides confidence-calibrated retrieval for both rapid pattern matching and guided causal exploration, (2) a meta-cognitive controller that dynamically routes between intuitive and analytical pathways based on problem familiarity, optimizing the trade-off between speed and depth, and (3) KubeLLM, a locally-deployable 8B model enhanced through domain-specific post-training on our 7,000-sample Kubernetes Fault Resolution Dataset. Evaluation on 1,873 real-world scenarios demonstrates MetaKube transforms Qwen3-8B from 50.9 to 90.5 points, approaching GPT-4.1 performance while ensuring complete data privacy. EPMN contributes 15.3% improvement through experiential learning, with continuous learning experiments showing progressive gains as the system accumulates operational knowledge. The source code and related resources are available at this https URL.
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
