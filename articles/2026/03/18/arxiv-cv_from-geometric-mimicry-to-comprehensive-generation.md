---
title: "From Geometric Mimicry to Comprehensive Generation: A Context-Informed Multimodal Diffusion Model for Urban Morphology Synthesis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2409.17049"
published: "2026-03-18"
fetched: "2026-03-18T18:24:42.715430"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Sep 2024 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:From Geometric Mimicry to Comprehensive Generation: A Context-Informed Multimodal Diffusion Model for Urban Morphology Synthesis
View PDF HTML (experimental)Abstract:Urban morphology is fundamental to determining urban functionality and vitality. Prevailing simulation methods, however, often oversimplify morphological generation as a geometric problem, lacking the fusion of urban semantics and geographical context. To address this limitation, this study proposes ControlCity, a diffusion model that achieves comprehensive urban morphology generation through multimodal information fusion. We first constructed a quadruple ``image-text-metadata-building footprints" dataset from 22 cities worldwide. ControlCity utilizes this information as control conditions. Specifically, an enhanced ControlNet encodes image-based spatial constraints, while text and metadata provide semantic guidance and geographical context to collectively direct the generation. Experimental results demonstrate that compared to the unimodal baseline, this method achieves significant advantages in morphological fidelity. Specifically, FID (lower scores indicate less visual error) was reduced by 71.01%, reaching 50.94, and MIoU (higher scores indicate greater spatial overlap) improved by 38.46%, reaching 0.36. Furthermore, the model demonstrates robust knowledge generalization and controllability, enabling cross-city style transfer and zero-shot generation for unknown cities. Ablation studies reveal the distinct roles of images, text, and metadata in the generation. This study confirms that multimodal fusion is crucial for achieving the transition from ``geometric mimicry" to ``comprehensive generation," providing a novel paradigm for urban morphology research and applications.
Submission history
From: Fangshuo Zhou [view email][v1] Wed, 25 Sep 2024 16:03:33 UTC (14,664 KB)
[v2] Tue, 17 Mar 2026 03:48:35 UTC (13,434 KB)
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
