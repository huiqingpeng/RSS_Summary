---
title: "CoDA: Exploring Chain-of-Distribution Attacks and Post-Hoc Token-Space Repair for Medical Vision-Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18545"
published: "2026-03-20"
fetched: "2026-03-20T15:11:30.509155"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:CoDA: Exploring Chain-of-Distribution Attacks and Post-Hoc Token-Space Repair for Medical Vision-Language Models
View PDF HTML (experimental)Abstract:Medical vision--language models (MVLMs) are increasingly used as perceptual backbones in radiology pipelines and as the visual front end of multimodal assistants, yet their reliability under real clinical workflows remains underexplored. Prior robustness evaluations often assume clean, curated inputs or study isolated corruptions, overlooking routine acquisition, reconstruction, display, and delivery operations that preserve clinical readability while shifting image statistics. To address this gap, we propose CoDA, a chain-of-distribution framework that constructs clinically plausible pipeline shifts by composing acquisition-like shading, reconstruction and display remapping, and delivery and export degradations. Under masked structural-similarity constraints, CoDA jointly optimizes stage compositions and parameters to induce failures while preserving visual plausibility. Across brain MRI, chest X-ray, and abdominal CT, CoDA substantially degrades the zero-shot performance of CLIP-style MVLMs, with chained compositions consistently more damaging than any single stage. We also evaluate multimodal large language models (MLLMs) as technical-authenticity auditors of imaging realism and quality rather than pathology. Proprietary multimodal models show degraded auditing reliability and persistent high-confidence errors on CoDA-shifted samples, while the medical-specific MLLMs we test exhibit clear deficiencies in medical image quality auditing. Finally, we introduce a post-hoc repair strategy based on teacher-guided token-space adaptation with patch-level alignment, which improves accuracy on archived CoDA outputs. Overall, our findings characterize a clinically grounded threat surface for MVLM deployment and show that lightweight alignment improves robustness in deployment.
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
