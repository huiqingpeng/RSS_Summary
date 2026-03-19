---
title: "Evidence Packing for Cross-Domain Image Deepfake Detection with LVLMs"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17761"
published: "2026-03-19"
fetched: "2026-03-19T15:17:26.897101"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Evidence Packing for Cross-Domain Image Deepfake Detection with LVLMs
View PDF HTML (experimental)Abstract:Image Deepfake Detection (IDD) separates manipulated images from authentic ones by spotting artifacts of synthesis or tampering. Although large vision-language models (LVLMs) offer strong image understanding, adapting them to IDD often demands costly fine-tuning and generalizes poorly to diverse, evolving manipulations. We propose the Semantic Consistent Evidence Pack (SCEP), a training-free LVLM framework that replaces whole-image inference with evidence-driven reasoning. SCEP mines a compact set of suspicious patch tokens that best reveal manipulation cues. It uses the vision encoder's CLS token as a global reference, clusters patch features into coherent groups, and scores patches with a fused metric combining CLS-guided semantic mismatch with frequency-and noise-based anomalies. To cover dispersed traces and avoid redundancy, SCEP samples a few high-confidence patches per cluster and applies grid-based NMS, producing an evidence pack that conditions a frozen LVLM for prediction. Experiments on diverse benchmarks show SCEP outperforms strong baselines without LVLM fine-tuning.
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
