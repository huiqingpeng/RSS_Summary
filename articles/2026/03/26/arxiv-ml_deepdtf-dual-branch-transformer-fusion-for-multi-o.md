---
title: "DeepDTF: Dual-Branch Transformer Fusion for Multi-Omics Anticancer Drug Response Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24265"
published: "2026-03-26"
fetched: "2026-03-27T07:22:30.813236"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:DeepDTF: Dual-Branch Transformer Fusion for Multi-Omics Anticancer Drug Response Prediction
View PDF HTML (experimental)Abstract:Cancer drug response varies widely across tumors due to multi-layer molecular heterogeneity, motivating computational decision support for precision oncology. Despite recent progress in deep CDR models, robust alignment between high-dimensional multi-omics and chemically structured drugs remains challenging due to cross-modal misalignment and limited inductive bias. We present DeepDTF, an end-to-end dual-branch Transformer fusion framework for joint log(IC50) regression and drug sensitivity classification. The cell-line branch uses modality-specific encoders for multi-omics profiles with Transformer blocks to capture long-range dependencies, while the drug branch represents compounds as molecular graphs and encodes them with a GNN-Transformer to integrate local topology with global context. Omics and drug representations are fused by a Transformer-based module that models cross-modal interactions and mitigates feature misalignment. On public pharmacogenomic benchmarks under 5-fold cold-start cell-line evaluation, DeepDTF consistently outperforms strong baselines across omics settings, achieving up to RMSE=1.248, R^2=0.875, and AUC=0.987 with full multi-omics inputs, while reducing classification error (1-ACC) by 9.5%. Beyond accuracy, DeepDTF provides biologically grounded explanations via SHAP-based gene attributions and pathway enrichment with pre-ranked GSEA.
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
