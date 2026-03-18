---
title: "InViC: Intent-aware Visual Cues for Medical Visual Question Answering"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16372"
published: "2026-03-18"
fetched: "2026-03-18T18:11:51.612448"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:InViC: Intent-aware Visual Cues for Medical Visual Question Answering
View PDF HTML (experimental)Abstract:Medical visual question answering (Med-VQA) aims to answer clinically relevant questions grounded in medical images. However, existing multimodal large language models (MLLMs) often exhibit shortcut answering, producing plausible responses by exploiting language priors or dataset biases while insufficiently attending to visual evidence. This behavior undermines clinical reliability, especially when subtle imaging findings are decisive. We propose a lightweight plug-in framework, termed Intent-aware Visual Cues (InViC), to explicitly enhance image-based answer generation in medical VQA. InViC introduces a Cue Tokens Extraction (CTE) module that distills dense visual tokens into a compact set of K question-conditioned cue tokens, which serve as structured visual intermediaries injected into the LLM decoder to promote intent-aligned visual evidence. To discourage bypassing of visual information, we further design a two-stage fine-tuning strategy with a cue-bottleneck attention mask. In Stage I, we employ an attention mask to block the LLM's direct view of raw visual features, thereby funneling all visual evidence through the cue pathway. In Stage II, standard causal attention is restored to train the LLM to jointly exploit the visual and cue tokens. We evaluate InViC on three public Med-VQA benchmarks (VQA-RAD, SLAKE, and ImageCLEF VQA-Med 2019) across multiple representative MLLMs. InViC consistently improves over zero-shot inference and standard LoRA fine-tuning, demonstrating that intent-aware visual cues with bottlenecked training is a practical and effective strategy for improving trustworthy Med-VQA.
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
