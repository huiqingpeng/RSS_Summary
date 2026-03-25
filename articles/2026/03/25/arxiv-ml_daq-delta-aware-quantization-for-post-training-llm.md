---
title: "DAQ: Delta-Aware Quantization for Post-Training LLM Weight Compression"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22324"
published: "2026-03-25"
fetched: "2026-03-26T07:11:17.268466"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:DAQ: Delta-Aware Quantization for Post-Training LLM Weight Compression
View PDF HTML (experimental)Abstract:We introduce Delta-Aware Quantization (DAQ), a data-free post-training quantization framework that preserves the knowledge acquired during post-training. Standard quantization objectives minimize reconstruction error but are agnostic to the base model, allowing quantization noise to disproportionately corrupt the small-magnitude parameter deltas ($\Delta W$) that encode post-training behavior -- an effect we analyze through the lens of quantization as implicit regularization. DAQ replaces reconstruction-based objectives with two delta-aware metrics -- Sign Preservation Rate and Cosine Similarity -- that directly optimize for directional fidelity of $\Delta W$, requiring only the base and post-trained weight matrices. In a pilot FP8 study, DAQ recovers style-specific capabilities lost under standard quantization while maintaining general performance.
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
