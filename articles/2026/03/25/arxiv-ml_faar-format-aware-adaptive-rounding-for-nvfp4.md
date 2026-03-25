---
title: "FAAR: Format-Aware Adaptive Rounding for NVFP4"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22370"
published: "2026-03-25"
fetched: "2026-03-26T07:13:42.825595"
---

Computer Science > Machine Learning
[Submitted on 23 Mar 2026]
Title:FAAR: Format-Aware Adaptive Rounding for NVFP4
View PDF HTML (experimental)Abstract:Deploying large language models (LLMs) on edge devices requires extremely low-bit quantization. Ultra-low precision formats such as NVFP4 offer a promising solution for reducing memory footprint and accelerating computation. However, existing quantization methods typically rely on conventional rounding strategies and fail to account for the non-uniformity of the NVFP4 numerical grid, resulting in suboptimal rounding decisions and amplified quantization errors. To address this, we propose Format-Aware Adaptive Rounding (FAAR), a learnable rounding strategy tailored for the NVFP4 format. Unlike conventional quantization paradigms, FAAR explicitly incorporates the non-uniform NVFP4 grid into the optimization process. By adaptively adjusting rounding decisions guided by loss gradients, our method effectively approximates the theoretically optimal quantization. To complement FAAR, we introduce a 2-stages Format Alignment (2FA) fine-tuning scheme that aligns LLM parameters layer-by-layer to the NVFP4 numerical space, further narrowing the performance gap. Remarkably, this learnable optimization incurs a minimal training overhead of only 4 GPU hours on Llama3-1B. Extensive experiments demonstrate the effectiveness of our approach. Compared with Round-to-Nearest (RTN), our method reduces perplexity on WikiText-2 from 14.28 to 12.60 on Llama3-1B and from 23.06 to 21.27 on Qwen3-1.7B. Additionally, our method consistently outperforms state-of-the-art approaches across various zero-shot downstream tasks.
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
