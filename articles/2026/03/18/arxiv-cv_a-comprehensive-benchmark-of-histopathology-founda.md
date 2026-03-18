---
title: "A Comprehensive Benchmark of Histopathology Foundation Models for Kidney Histopathology"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15967"
published: "2026-03-18"
fetched: "2026-03-18T18:03:42.118102"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Mar 2026]
Title:A Comprehensive Benchmark of Histopathology Foundation Models for Kidney Histopathology
View PDF HTML (experimental)Abstract:Histopathology foundation models (HFMs), pretrained on large-scale cancer datasets, have advanced computational pathology. However, their applicability to non-cancerous chronic kidney disease remains underexplored, despite coexistence of renal pathology with malignancies such as renal cell and urothelial carcinoma. We systematically evaluate 11 publicly available HFMs across 11 kidney-specific downstream tasks spanning multiple stains (PAS, H&E, PASM, and IHC), spatial scales (tile and slide-level), task types (classification, regression, and copy detection), and clinical objectives, including detection, diagnosis, and prognosis. Tile-level performance is assessed using repeated stratified group cross-validation, while slide-level tasks are evaluated using repeated nested stratified cross-validation. Statistical significance is examined using Friedman test followed by pairwise Wilcoxon signed-rank testing with Holm-Bonferroni correction and compact letter display visualization. To promote reproducibility, we release an open-source Python package, kidney-hfm-eval, available at this https URL , that reproduces the evaluation pipelines. Results show moderate to strong performance on tasks driven by coarse meso-scale renal morphology, including diagnostic classification and detection of prominent structural alterations. In contrast, performance consistently declines for tasks requiring fine-grained microstructural discrimination, complex biological phenotypes, or slide-level prognostic inference, largely independent of stain type. Overall, current HFMs appear to encode predominantly static meso-scale representations and may have limited capacity to capture subtle renal pathology or prognosis-related signals. Our results highlight the need for kidney-specific, multi-stain, and multimodal foundation models to support clinically reliable decision-making in nephrology.
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
