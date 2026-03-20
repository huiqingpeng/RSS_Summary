---
title: "Redundancy-as-Masking: Formalizing the Artificial Age Score (AAS) to Model Memory Aging in Generative AI"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.01242"
published: "2026-03-20"
fetched: "2026-03-20T14:17:08.335714"
---

Computer Science > Computation and Language
[Submitted on 24 Sep 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Redundancy-as-Masking: Formalizing the Artificial Age Score (AAS) to Model Memory Aging in Generative AI
View PDFAbstract:Artificial intelligence is observed to age not through chronological time but through structural asymmetries in memory performance. In large language models, semantic cues such as the name of the day often remain stable across sessions, while episodic details like the sequential progression of experiment numbers tend to collapse when conversational context is reset. To capture this phenomenon, the Artificial Age Score (AAS) is introduced as a log-scaled, entropy-informed metric of memory aging derived from observable recall behavior. The score is formally proven to be well-defined, bounded, and monotonic under mild and model-agnostic assumptions, making it applicable across various tasks and domains. In its Redundancy-as-Masking formulation, the score interprets redundancy as overlapping information that reduces the penalized mass. However, in the present study, redundancy is not explicitly estimated; all reported values assume a redundancy-neutral setting (R = 0), yielding conservative upper bounds. The AAS framework was tested over a 25-day bilingual study involving ChatGPT-5, structured into stateless and persistent interaction phases. During persistent sessions, the model consistently recalled both semantic and episodic details, driving the AAS toward its theoretical minimum, indicative of structural youth. In contrast, when sessions were reset, the model preserved semantic consistency but failed to maintain episodic continuity, causing a sharp increase in the AAS and signaling structural memory aging. These findings support the utility of AAS as a theoretically grounded, task-independent diagnostic tool for evaluating memory degradation in artificial systems. The study builds on foundational concepts from von Neumann's work on automata, Shannon's theories of information and redundancy, and Turing's behavioral approach to intelligence.
Submission history
From: Seyma Yaman Kayadibi [view email][v1] Wed, 24 Sep 2025 02:18:27 UTC (1,080 KB)
[v2] Thu, 19 Mar 2026 00:53:33 UTC (1,182 KB)
Current browse context:
cs.CL
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
