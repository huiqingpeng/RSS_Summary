---
title: "EEG-SeeGraph: Interpreting functional connectivity disruptions in dementias via sparse-explanatory dynamic EEG-graph learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16895"
published: "2026-03-19"
fetched: "2026-03-19T13:05:57.980449"
---

Electrical Engineering and Systems Science > Signal Processing
[Submitted on 3 Mar 2026]
Title:EEG-SeeGraph: Interpreting functional connectivity disruptions in dementias via sparse-explanatory dynamic EEG-graph learning
View PDF HTML (experimental)Abstract:Robust and interpretable dementia diagnosis from noisy, non-stationary electroencephalography (EEG) is clinically essential yet remains challenging. To this end, we propose SeeGraph, a Sparse-Explanatory dynamic EEG-graph network that models time-evolving functional connectivity and employs a node-guided sparse edge mask to reveal the connections that drive diagnostic decisions, while remaining robust to noise and cross-site variability. SeeGraph comprises four components: (1) a dual-trajectory temporal encoder that models dynamic EEG with two streams, where node signals capture regional oscillations and edge signals capture interregional coupling; (2) a topology-aware positional encoder that derives graph-spectral Laplacian coordinates from the fused connectivity and augments node embeddings; (3) a node-guided sparse explanatory edge mask that gates the connectivity into a compact subgraph; and (4) a gated graph predictor that operates on the sparsified graph. The framework is trained using cross-entropy loss together with a sparsity regularizer on the mask, yielding noise-robust and interpretable diagnoses. The effectiveness of SeeGraph is validated on public and in-house EEG cohorts, including patients with neurodegenerative dementias and healthy controls, under both raw and noise-perturbed conditions. Its sparse, node-guided explanations highlight disease-relevant connections and align with established clinical findings on functional connectivity alterations, thereby offering transparent cues for neurological evaluation.
Current browse context:
eess.SP
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
