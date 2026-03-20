---
title: "GeoMotionGPT: Geometry-Aligned Motion Understanding with Large Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.07632"
published: "2026-03-20"
fetched: "2026-03-20T16:16:54.419152"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 12 Jan 2026 (v1), last revised 19 Mar 2026 (this version, v4)]
Title:GeoMotionGPT: Geometry-Aligned Motion Understanding with Large Language Models
View PDFAbstract:Discrete motion tokenization has recently enabled Large Language Models (LLMs) to serve as versatile backbones for motion understanding and motion-language reasoning. However, existing pipelines typically decouple motion quantization from semantic embedding learning, linking them solely via token IDs. This approach fails to effectively align the intrinsic geometry of the motion space with the embedding space, thereby hindering the LLM's capacity for nuanced motion reasoning. We argue that alignment is most effective when both modalities share a unified geometric basis. Therefore, instead of forcing the LLM to reconstruct the complex geometry among motion tokens from scratch, we present a novel framework that explicitly enforces orthogonality on both the motion codebook and the LLM embedding space, ensuring that their relational structures naturally mirror each other. Specifically, we employ a decoder-only quantizer with Gumbel-Softmax for differentiable training and balanced codebook usage. To bridge the modalities, we use a sparse projection that maps motion codes into the LLM embedding space while preserving orthogonality. Finally, a two-stage orthonormal regularization schedule enforces soft constraints during tokenizer training and LLM fine-tuning to maintain geometric alignment without hindering semantic adaptation. Extensive experiments show that our framework improves the aggregated Average by 22.4% over the strongest baseline on HumanML3D and by 14.4% on KIT-ML, while ablations confirm the effectiveness of the tokenizer, projection, and regularization designs.
Submission history
From: Zhankai Ye [view email][v1] Mon, 12 Jan 2026 15:14:29 UTC (4,947 KB)
[v2] Wed, 14 Jan 2026 02:19:38 UTC (6,694 KB)
[v3] Mon, 16 Mar 2026 13:36:38 UTC (6,815 KB)
[v4] Thu, 19 Mar 2026 13:41:22 UTC (6,815 KB)
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
