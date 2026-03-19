---
title: "Parameter-Efficient Modality-Balanced Symmetric Fusion for Multimodal Remote Sensing Semantic Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17705"
published: "2026-03-19"
fetched: "2026-03-19T15:16:22.641504"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Parameter-Efficient Modality-Balanced Symmetric Fusion for Multimodal Remote Sensing Semantic Segmentation
View PDF HTML (experimental)Abstract:Multimodal remote sensing semantic segmentation enhances scene interpretation by exploiting complementary physical cues from heterogeneous data. Although pretrained Vision Foundation Models (VFMs) provide strong general-purpose representations, adapting them to multimodal tasks often incurs substantial computational overhead and is prone to modality imbalance, where the contribution of auxiliary modalities is suppressed during optimization. To address these challenges, we propose MoBaNet, a parameter-efficient and modality-balanced symmetric fusion framework. Built upon a largely frozen VFM backbone, MoBaNet adopts a symmetric dual-stream architecture to preserve generalizable representations while minimizing the number of trainable parameters. Specifically, we design a Cross-modal Prompt-Injected Adapter (CPIA) to enable deep semantic interaction by generating shared prompts and injecting them into bottleneck adapters under the frozen backbone. To obtain compact and discriminative multimodal representations for decoding, we further introduce a Difference-Guided Gated Fusion Module (DGFM), which adaptively fuses paired stage features by explicitly leveraging cross-modal discrepancy to guide feature selection. Furthermore, we propose a Modality-Conditional Random Masking (MCRM) strategy to mitigate modality imbalance by masking one modality only during training and imposing hard-pixel auxiliary supervision on modality-specific branches. Extensive experiments on the ISPRS Vaihingen and Potsdam benchmarks demonstrate that MoBaNet achieves state-of-the-art performance with significantly fewer trainable parameters than full fine-tuning, validating its effectiveness for robust and balanced multimodal fusion. The source code in this work is available at this https URL.
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
