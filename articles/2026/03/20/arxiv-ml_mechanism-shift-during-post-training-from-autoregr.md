---
title: "Mechanism Shift During Post-training from Autoregressive to Masked Diffusion Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.14758"
published: "2026-03-20"
fetched: "2026-03-20T14:09:42.695875"
---

Computer Science > Machine Learning
[Submitted on 21 Jan 2026 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:Mechanism Shift During Post-training from Autoregressive to Masked Diffusion Language Models
View PDF HTML (experimental)Abstract:Post-training pretrained autoregressive models (ARMs) into masked diffusion models (MDMs) has emerged as a cost-effective way to overcome the limitations of sequential generation. Yet the internal algorithmic changes induced by this shift remain poorly understood, leaving it unclear whether post-trained MDMs acquire genuine bidirectional reasoning or merely repackage autoregressive heuristics. We address this question through a comparative circuit analysis of ARMs and their MDM counterparts. Our analysis reveals a systematic "mechanism shift" that depends on the structural nature of the task. MDMs largely preserve autoregressive circuitry for tasks driven by local causal dependencies, but for global planning tasks they abandon initialized pathways and exhibit distinct rewiring with increased early-layer processing. At the semantic level, we observe a transition from sharp, localized specialization in ARMs to distributed integration in MDMs. These findings show that diffusion post-training does not simply adjust model parameters, but reorganizes internal computation to support non-sequential global planning.
Submission history
From: Injin Kong [view email][v1] Wed, 21 Jan 2026 08:26:51 UTC (8,082 KB)
[v2] Thu, 22 Jan 2026 02:34:00 UTC (8,082 KB)
[v3] Thu, 19 Mar 2026 06:59:11 UTC (21,061 KB)
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
