---
title: "A WDLoRA-Based Multimodal Generative Framework for Clinically Guided Corneal Confocal Microscopy Image Synthesis in Diabetic Neuropathy"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.13693"
published: "2026-03-18"
fetched: "2026-03-18T18:32:20.602068"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 14 Feb 2026 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:A WDLoRA-Based Multimodal Generative Framework for Clinically Guided Corneal Confocal Microscopy Image Synthesis in Diabetic Neuropathy
View PDF HTML (experimental)Abstract:Corneal Confocal Microscopy (CCM) is a sensitive tool for assessing small-fiber damage in Diabetic Peripheral Neuropathy (DPN), yet the development of robust, automated deep learning-based diagnostic models is limited by scarce labelled data and fine-grained variability in corneal nerve morphology. Although Artificial Intelligence (AI)-driven foundation generative models excel at natural image synthesis, they often struggle in medical imaging due to limited domain-specific training, compromising the anatomical fidelity required for clinical analysis. To overcome these limitations, we propose a Weight-Decomposed Low-Rank Adaptation (WDLoRA)-based multimodal generative framework for clinically guided CCM image synthesis. WDLoRA is a parameter-efficient fine-tuning (PEFT) mechanism that decouples magnitude and directional weight updates, enabling foundation generative models to independently learn the orientation (nerve topology) and intensity (stromal contrast) required for medical realism. By jointly conditioning on nerve segmentation masks and disease-specific clinical prompts, the model synthesises anatomically coherent images across the DPN spectrum (Control, T1NoDPN, T1DPN). A comprehensive three-pillar evaluation demonstrates that the proposed framework achieves state-of-the-art visual fidelity (Fréchet Inception Distance (FID): 5.18) and structural integrity (Structural Similarity Index Measure (SSIM): 0.630), significantly outperforming GAN and standard diffusion baselines. Crucially, the synthetic images preserve gold-standard clinical biomarkers and are statistically equivalent to real patient data. When used to train automated diagnostic models, the synthetic dataset improves downstream diagnostic accuracy by 2.1% and segmentation performance by 2.2%, validating the framework's potential to alleviate data bottlenecks in medical AI.
Submission history
From: Xin Zhang [view email][v1] Sat, 14 Feb 2026 09:32:44 UTC (6,711 KB)
[v2] Mon, 16 Mar 2026 23:03:22 UTC (6,909 KB)
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
