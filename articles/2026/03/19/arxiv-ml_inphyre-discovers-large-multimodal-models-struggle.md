---
title: "InPhyRe Discovers: Large Multimodal Models Struggle in Inductive Physical Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.12263"
published: "2026-03-19"
fetched: "2026-03-19T14:16:52.621744"
---

Computer Science > Artificial Intelligence
[Submitted on 12 Sep 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:InPhyRe Discovers: Large Multimodal Models Struggle in Inductive Physical Reasoning
View PDFAbstract:Large multimodal models (LMMs) encode physical laws observed during training, such as momentum conservation, as parametric knowledge. It allows LMMs to answer physical reasoning queries, such as the outcome of a potential collision event from visual input. However, since parametric knowledge includes only the physical laws seen during training, it is insufficient for reasoning in inference scenarios that follow physical laws unseen during training. In such novel physical environments, humans could adapt their physical reasoning based on provided demonstrations. This inductive physical reasoning ability is indispensable for LMMs if they are to replace human agents in safety-critical applications. Despite its importance, existing visual benchmarks do not evaluate inductive physical reasoning and only consider the parametric knowledge in LMMs. To this end, we propose InPhyRe, the first visual question answering benchmark to measure inductive physical reasoning in LMMs. InPhyRe evaluates LMMs' ability to predict the outcome of collision events in algorithmically generated synthetic videos. By inspecting over 13 open-source and proprietary LMMs, InPhyRe informs us that (1) LMMs struggle to apply their limited parametric knowledge about universal physical laws to reasoning, (2) inductive physical reasoning in LMMs is weak when the physical laws underlying inference scenarios were unseen during training, and (3) inductive physical reasoning in LMMs suffers from language bias and may ignore the visual inputs, questioning the trustworthiness of LMMs regarding visual inputs.
Submission history
From: Gautam Sreekumar [view email][v1] Fri, 12 Sep 2025 20:07:12 UTC (3,594 KB)
[v2] Wed, 18 Mar 2026 04:52:25 UTC (6,095 KB)
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
