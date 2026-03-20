---
title: "FlowMS: Flow Matching for De Novo Structure Elucidation from Mass Spectra"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18397"
published: "2026-03-20"
fetched: "2026-03-20T12:11:05.919333"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:FlowMS: Flow Matching for De Novo Structure Elucidation from Mass Spectra
View PDF HTML (experimental)Abstract:Mass spectrometry (MS) stands as a cornerstone analytical technique for molecular identification, yet de novo structure elucidation from spectra remains challenging due to the combinatorial complexity of chemical space and the inherent ambiguity of spectral fragmentation patterns. Recent deep learning approaches, including autoregressive sequence models, scaffold-based methods, and graph diffusion models, have made progress. However, diffusion-based generation for this task remains computationally demanding. Meanwhile, discrete flow matching, which has shown strong performance for graph generation, has not yet been explored for spectrum-conditioned structure elucidation. In this work, we introduce FlowMS, the first discrete flow matching framework for spectrum-conditioned de novo molecular generation. FlowMS generates molecular graphs through iterative refinement in probability space, enforcing chemical formula constraints while conditioning on spectral embeddings from a pretrained formula transformer encoder. Notably, it achieves state-of-the-art performance on 5 out of 6 metrics on the NPLIB1 benchmark: 9.15% top-1 accuracy (9.7% relative improvement over DiffMS) and 7.96 top-10 MCES (4.2% improvement over MS-BART). We also visualize the generated molecules, which further demonstrate that FlowMS produces structurally plausible candidates closely resembling ground truth structures. These results establish discrete flow matching as a promising paradigm for mass spectrometry-based structure elucidation in metabolomics and natural product discovery.
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
