---
title: "Towards Robust Multimodal Physiological Foundation Models: Handling Arbitrary Missing Modalities"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2504.19596"
published: "2026-03-18"
fetched: "2026-03-18T17:10:01.189511"
---

Electrical Engineering and Systems Science > Signal Processing
[Submitted on 28 Apr 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Towards Robust Multimodal Physiological Foundation Models: Handling Arbitrary Missing Modalities
View PDF HTML (experimental)Abstract:Multimodal physiological signals, such as EEG, ECG, EOG, and EMG, are crucial for healthcare and brain-computer interfaces. While existing methods rely on specialized architectures and dataset-specific fusion strategies, they struggle to learn universal representations that generalize across datasets and handle missing modalities at inference time. To address these issues, we propose PhysioOmni, a foundation model for multimodal physiological signal analysis that models both homogeneous and heterogeneous features to decouple multimodal signals and extract generic representations while maintaining compatibility with arbitrary missing modalities. PhysioOmni trains a decoupled multimodal tokenizer, enabling masked signal pre-training via modality-invariant and modality-specific objectives. To ensure adaptability to diverse and incomplete modality combinations, the pre-trained encoders undergo resilient fine-tuning with prototype alignment on downstream datasets. Extensive experiments on four downstream tasks, emotion recognition, sleep stage classification, motor prediction, and mental workload detection, demonstrate that PhysioOmni achieves state-of-the-art performance while maintaining strong robustness to missing modalities. Our code and model weights will be released.
Submission history
From: Wei-Bang Jiang [view email][v1] Mon, 28 Apr 2025 09:00:04 UTC (456 KB)
[v2] Fri, 6 Jun 2025 10:41:10 UTC (315 KB)
[v3] Tue, 17 Mar 2026 14:09:10 UTC (311 KB)
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
