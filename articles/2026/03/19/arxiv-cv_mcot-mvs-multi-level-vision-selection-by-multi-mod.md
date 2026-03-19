---
title: "MCoT-MVS: Multi-level Vision Selection by Multi-modal Chain-of-Thought Reasoning for Composed Image Retrieval"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17360"
published: "2026-03-19"
fetched: "2026-03-19T15:08:56.319045"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:MCoT-MVS: Multi-level Vision Selection by Multi-modal Chain-of-Thought Reasoning for Composed Image Retrieval
View PDF HTML (experimental)Abstract:Composed Image Retrieval (CIR) aims to retrieve target images based on a reference image and modified texts. However, existing methods often struggle to extract the correct semantic cues from the reference image that best reflect the user's intent under textual modification prompts, resulting in interference from irrelevant visual noise. In this paper, we propose a novel Multi-level Vision Selection by Multi-modal Chain-of-Thought Reasoning (MCoT-MVS) for CIR, integrating attention-aware multi-level vision features guided by reasoning cues from a multi-modal large language model (MLLM). Specifically, we leverage an MLLM to perform chain-of-thought reasoning on the multimodal composed input, generating the retained, removed, and target-inferred texts. These textual cues subsequently guide two reference visual attention selection modules to selectively extract discriminative patch-level and instance-level semantics from the reference image. Finally, to effectively fuse these multi-granular visual cues with the modified text and the imagined target description, we design a weighted hierarchical combination module to align the composed query with target images in a unified embedding space. Extensive experiments on two CIR benchmarks, namely CIRR and FashionIQ, demonstrate that our approach consistently outperforms existing methods and achieves new state-of-the-art performance. Code and trained models are publicly released.
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
