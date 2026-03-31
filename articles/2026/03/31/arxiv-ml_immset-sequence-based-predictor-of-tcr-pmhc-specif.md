---
title: "ImmSET: Sequence-Based Predictor of TCR-pMHC Specificity at Scale"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26994"
published: "2026-03-31"
fetched: "2026-04-01T07:20:53.603667"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:ImmSET: Sequence-Based Predictor of TCR-pMHC Specificity at Scale
View PDF HTML (experimental)Abstract:T cells are a critical component of the adaptive immune system, playing a role in infectious disease, autoimmunity, and cancer. T cell function is mediated by the T cell receptor (TCR) protein, a highly diverse receptor targeting specific peptides presented by the major histocompatibility complex (pMHCs). Predicting the specificity of TCRs for their cognate pMHCs is central to understanding adaptive immunity and enabling personalized therapies. However, accurate prediction of this protein-protein interaction remains challenging due to the extreme diversity of both TCRs and pMHCs. Here, we present ImmSET (Immune Synapse Encoding Transformer), a novel sequence-based architecture designed to model interactions among sets of variable-length biological sequences. We train this model across a range of dataset sizes and compositions and study the resulting models' generalization to pMHC targets. We describe a failure mode in prior sequence-based approaches that inflates previously reported performance on this task and show that ImmSET remains robust under stricter evaluation. In systematically testing the scaling behavior of ImmSET with training data, we show that performance scales consistently with data volume across multiple data types and compares favorably with the pre-trained protein language model ESM2 fine-tuned on the same datasets. Finally, we demonstrate that ImmSET can outperform AlphaFold2 and AlphaFold3-based pipelines on TCR-pMHC specificity prediction when provided sufficient training data. This work establishes ImmSET as a scalable modeling paradigm for multi-sequence interaction problems, demonstrated in the TCR-pMHC setting but generalizable to other biological domains where high-throughput sequence-driven reasoning complements structure prediction and experimental mapping.
Submission history
From: Marco Antonio Garcia Noceda [view email][v1] Fri, 27 Mar 2026 21:08:10 UTC (3,480 KB)
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
