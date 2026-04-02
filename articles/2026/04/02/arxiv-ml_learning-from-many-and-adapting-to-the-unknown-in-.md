---
title: "Learning from Many and Adapting to the Unknown in Open-set Test Streams"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00533"
published: "2026-04-02"
fetched: "2026-04-03T07:22:36.819317"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Learning from Many and Adapting to the Unknown in Open-set Test Streams
View PDF HTML (experimental)Abstract:Large Language Models (LLMs) generalize across tasks via reusable representations and flexible reasoning, yet remain brittle in real deployment under evolving tasks and continual distribution shift. A common approach is Test-Time Adaptation (TTA), existing ones of which updates models with hand-designed unsupervised objectives over the full parameter space and mostly overlook preserving shared source knowledge and the reliability of adaptation signals. Drawing on molecular signaling cascades of memory updating in Drosophila, we propose Synapse Consolidation (SyCo), a parameter-efficient LLM adaptation method that updates low-rank adapters through Rac1 and MAPK pathways under the guidance of a structured TTA objective driven by problem understanding, process understanding, and source-domain guardrail. Rac1 confines plasticity to a tail-gradient subspace that is less critical for source knowledge, enabling rapid specialization while preserving source representations. MAPK uses a tiered controller to suppress noisy updates and consolidate useful adaptations under non-stationary streams. To model real deployments with multiple sources and continually emerging tasks, we introduce Multi-source Open-set Adaptation (MOA) setting, where a model is trained on multiple labeled source tasks and then adapts on open, non-stationary unlabeled test streams that mix seen and unseen tasks with partial overlap in label and intent space. Across 18 NLP datasets and the MOA setting, SyCo consistently outperforms strong baselines, achieving 78.31\% on unseen-task adaptation and 85.37\% on unseen-data shifts.
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
