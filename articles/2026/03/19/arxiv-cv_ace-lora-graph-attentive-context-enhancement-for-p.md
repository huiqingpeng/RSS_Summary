---
title: "ACE-LoRA: Graph-Attentive Context Enhancement for Parameter-Efficient Adaptation of Medical Vision-Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17079"
published: "2026-03-19"
fetched: "2026-03-19T15:04:47.000131"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:ACE-LoRA: Graph-Attentive Context Enhancement for Parameter-Efficient Adaptation of Medical Vision-Language Models
View PDF HTML (experimental)Abstract:The success of CLIP-like vision-language models (VLMs) on natural images has inspired medical counterparts, yet existing approaches largely fall into two extremes: specialist models trained on single-domain data, which capture domain-specific details but generalize poorly, and generalist medical VLMs trained on multi-domain data, which retain broad semantics but dilute fine-grained diagnostic cues. Bridging this specialization-generalization trade-off remains challenging. To address this problem, we propose ACE-LoRA, a parameter-efficient adaptation framework for generalist medical VLMs that maintains robust zero-shot generalization. ACE-LoRA integrates Low-Rank Adaptation (LoRA) modules into frozen image-text encoders and introduces an Attention-based Context Enhancement Hypergraph Neural Network (ACE-HGNN) module that captures higher-order contextual interactions beyond pairwise similarity to enrich global representations with localized diagnostic cues, addressing a key limitation of prior Parameter-Efficient Fine-Tuning (PEFT) methods that overlook fine-grained details. To further enhance cross-modal alignment, we formulate a label-guided InfoNCE loss to effectively suppress false negatives between semantically related image-text pairs. Despite adding only 0.95M trainable parameters, ACE-LoRA consistently outperforms state-of-the-art medical VLMs and PEFT baselines across zero-shot classification, segmentation, and detection benchmarks spanning multiple domains. Our code is available at this https URL.
Submission history
From: Mustafa Arda Aydın [view email][v1] Tue, 17 Mar 2026 19:06:33 UTC (2,422 KB)
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
