---
title: "Tabular LLMs for Interpretable Few-Shot Alzheimer's Disease Prediction with Multimodal Biomedical Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17191"
published: "2026-03-19"
fetched: "2026-03-19T13:09:44.437653"
---

Computer Science > Computation and Language
[Submitted on 17 Mar 2026]
Title:Tabular LLMs for Interpretable Few-Shot Alzheimer's Disease Prediction with Multimodal Biomedical Data
View PDF HTML (experimental)Abstract:Accurate diagnosis of Alzheimer's disease (AD) requires handling tabular biomarker data, yet such data are often small and incomplete, where deep learning models frequently fail to outperform classical methods. Pretrained large language models (LLMs) offer few-shot generalization, structured reasoning, and interpretable outputs, providing a powerful paradigm shift for clinical prediction. We propose TAP-GPT Tabular Alzheimer's Prediction GPT, a domain-adapted tabular LLM framework built on TableGPT2 and fine-tuned for few-shot AD classification using tabular prompts rather than plain texts. We evaluate TAP-GPT across four ADNI-derived datasets, including QT-PAD biomarkers and region-level structural MRI, amyloid PET, and tau PET for binary AD classification. Across multimodal and unimodal settings, TAP-GPT improves upon its backbone models and outperforms traditional machine learning baselines in the few-shot setting while remaining competitive with state-of-the-art general-purpose LLMs. We show that feature selection mitigates degradation in high-dimensional inputs and that TAP-GPT maintains stable performance under simulated and real-world missingness without imputation. Additionally, TAP-GPT produces structured, modality-aware reasoning aligned with established AD biology and shows greater stability under self-reflection, supporting its use in iterative multi-agent systems. To our knowledge, this is the first systematic application of a tabular-specialized LLM to multimodal biomarker-based AD prediction, demonstrating that such pretrained models can effectively address structured clinical prediction tasks and laying the foundation for tabular LLM-driven multi-agent clinical decision-support systems. The source code is publicly available on GitHub: this https URL.
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
