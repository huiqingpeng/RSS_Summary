---
title: "EdiVal-Agent: An Object-Centric Framework for Automated, Fine-Grained Evaluation of Multi-Turn Editing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.13399"
published: "2026-03-19"
fetched: "2026-03-19T14:17:00.919578"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Sep 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:EdiVal-Agent: An Object-Centric Framework for Automated, Fine-Grained Evaluation of Multi-Turn Editing
View PDF HTML (experimental)Abstract:Instruction-based image editing has advanced rapidly, yet reliable and interpretable evaluation remains a bottleneck. Current protocols either (i) depend on paired reference images, resulting in limited coverage and inheriting biases from prior generative models or (ii) rely solely on zero-shot vision language models (VLMs), whose prompt-based assessments of instruction following, content consistency, and visual quality are often imprecise. To address this, we introduce EdiVal, an automated and fine-grained evaluation framework grounded in an object-centric perspective, designed to assess not only standard single-turn but also multi-turn instruction-based editing with precision. Given an input image, EdiVal first decomposes it into semantically meaningful objects, then synthesizes diverse, context-aware editing instructions while dynamically updating object pools across turns. These two stages enable two novel object centric metrics tailored for multi turn evaluation and one global metric of visual quality: 1) EdiVal-IF, which measures instruction following by combining open vocabulary object detectors for symbolic checks with VLMs for semantic verification on detector guided crops; 2) EdiVal-CC, which evaluates content consistency by calculating semantic similarity of unchanged objects and background using the evolving object pools; and 3) EdiVal-VQ, which quantifies changes in overall visual quality with human preference models. Instantiating this pipeline, we build EdiVal Bench, a multi-turn editing benchmark covering 9 instruction types and 16 state-of-the-art editing models, spanning in-context, flow-matching, and diffusion paradigms. We demonstrate that EdiVal can be used to identify existing failure modes, thereby informing the development of the next generation of editing models.
Submission history
From: Yasi Zhang [view email][v1] Tue, 16 Sep 2025 17:45:39 UTC (45,428 KB)
[v2] Thu, 16 Oct 2025 01:09:09 UTC (30,434 KB)
[v3] Tue, 17 Mar 2026 21:19:53 UTC (39,530 KB)
Current browse context:
cs.CV
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
