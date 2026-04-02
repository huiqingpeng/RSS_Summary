---
title: "HabitatAgent: An End-to-End Multi-Agent System for Housing Consultation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00556"
published: "2026-04-02"
fetched: "2026-04-03T07:22:44.915256"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:HabitatAgent: An End-to-End Multi-Agent System for Housing Consultation
View PDF HTML (experimental)Abstract:Housing selection is a high-stakes and largely irreversible decision problem. We study housing consultation as a decision-support interface for housing selection. Existing housing platforms and many LLM-based assistants often reduce this process to ranking or recommendation, resulting in opaque reasoning, brittle multi-constraint handling, and limited guarantees on factuality.
We present HabitatAgent, the first LLM-powered multi-agent architecture for end-to-end housing consultation. HabitatAgent comprises four specialized agent roles: Memory, Retrieval, Generation, and Validation. The Memory Agent maintains multi-layer user memory through internal stages for constraint extraction, memory fusion, and verification-gated updates; the Retrieval Agent performs hybrid vector--graph retrieval (GraphRAG); the Generation Agent produces evidence-referenced recommendations and explanations; and the Validation Agent applies multi-tier verification and targeted remediation. Together, these agents provide an auditable and reliable workflow for end-to-end housing consultation.
We evaluate HabitatAgent on 100 real user consultation scenarios (300 multi-turn question--answer pairs) under an end-to-end correctness protocol. A strong single-stage baseline (Dense+Rerank) achieves 75% accuracy, while HabitatAgent reaches 95%.
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
