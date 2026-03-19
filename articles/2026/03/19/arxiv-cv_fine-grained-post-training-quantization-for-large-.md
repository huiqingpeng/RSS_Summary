---
title: "Fine-Grained Post-Training Quantization for Large Vision Language Models with Quantization-Aware Integrated Gradients"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17809"
published: "2026-03-19"
fetched: "2026-03-19T15:17:58.167557"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Fine-Grained Post-Training Quantization for Large Vision Language Models with Quantization-Aware Integrated Gradients
View PDF HTML (experimental)Abstract:Large Vision Language Models (LVLMs) have achieved remarkable success in a range of downstream tasks that require multimodal interaction, but their capabilities come with substantial computational and memory overhead, which hinders practical deployment. Among numerous acceleration techniques, post-training quantization is a popular and effective strategy for reducing memory cost and accelerating inference. However, existing LVLM quantization methods typically measure token sensitivity at the modality level, which fails to capture the complex cross-token interactions and falls short in quantitatively measuring the quantization error at the token level. As tokens interact within the model, the distinction between modalities gradually diminishes, suggesting the need for fine-grained calibration. Inspired by axiomatic attribution in mechanistic interpretability, we introduce a fine-grained quantization strategy on Quantization-aware Integrated Gradients (QIG), which leverages integrated gradients to quantitatively evaluate token sensitivity and push the granularity from modality level to token level, reflecting both inter-modality and intra-modality dynamics. Extensive experiments on multiple LVLMs under both W4A8 and W3A16 settings show that our method improves accuracy across models and benchmarks with negligible latency overhead. For example, under 3-bit weight-only quantization, our method improves the average accuracy of LLaVA-onevision-7B by 1.60%, reducing the gap to its full-precision counterpart to only 1.33%. The code is available at this https URL.
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
