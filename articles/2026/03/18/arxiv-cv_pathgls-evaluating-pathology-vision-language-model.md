---
title: "PathGLS: Evaluating Pathology Vision-Language Models without Ground Truth through Multi-Dimensional Consistency"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16113"
published: "2026-03-18"
fetched: "2026-03-18T18:05:38.889547"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:PathGLS: Evaluating Pathology Vision-Language Models without Ground Truth through Multi-Dimensional Consistency
View PDF HTML (experimental)Abstract:Vision-Language Models (VLMs) offer significant potential in computational pathology by enabling interpretable image analysis, automated reporting, and scalable decision support. However, their widespread clinical adoption remains limited due to the absence of reliable, automated evaluation metrics capable of identifying subtle failures such as hallucinations. To address this gap, we propose PathGLS, a novel reference-free evaluation framework that assesses pathology VLMs across three dimensions: Grounding (fine-grained visual-text alignment), Logic (entailment graph consistency using Natural Language Inference), and Stability (output variance under adversarial visual-semantic perturbations). PathGLS supports both patch-level and whole-slide image (WSI)-level analysis, yielding a comprehensive trust score. Experiments on Quilt-1M, TCGA, REG2025, PathMMU and TCGA-Sarcoma datasets demonstrate the superiority of PathGLS. Specifically, on the Quilt-1M dataset, PathGLS reveals a steep sensitivity drop of 40.2% for hallucinated reports compared to only 2.1% for BERTScore. Moreover, validation against expert-defined clinical error hierarchies reveals that PathGLS achieves a strong Spearman's rank correlation of $\rho=0.71$ ($p < 0.0001$), significantly outperforming Large Language Model (LLM)-based approaches (Gemini 3.0 Pro: $\rho=0.39$, $p < 0.0001$). These results establish PathGLS as a robust reference-free metric. By directly quantifying hallucination rates and domain shift robustness, it serves as a reliable criterion for benchmarking VLMs on private clinical datasets and informing safe deployment. Code can be found at: this https URL
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
