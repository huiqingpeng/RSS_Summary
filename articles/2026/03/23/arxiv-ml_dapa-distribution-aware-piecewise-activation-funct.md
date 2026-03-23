---
title: "DAPA: Distribution Aware Piecewise Activation Functions for On-Device Transformer Inference and Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19338"
published: "2026-03-23"
fetched: "2026-03-24T07:17:33.707984"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:DAPA: Distribution Aware Piecewise Activation Functions for On-Device Transformer Inference and Training
View PDF HTML (experimental)Abstract:Non-linear activation functions play a pivotal role in on-device inference and training, as they not only consume substantial hardware resources but also impose a significant impact on system performance and energy efficiency. In this work, we propose Distribution-Aware Piecewise Activation (DAPA), a differentiable and hardware-friendly activation function for Transformer architectures by exploiting the distribution of pre-activation data. DAPA employs a non-uniform piecewise approximation that allocates finer segments to high-probability regions of the distribution, improving generalizability over prior piecewise linear methods. The resulting approximation is further quantized using Distribution-Weighted Mean Square Error to reduce latency and resource utilization for hardware deployment. Our HLS implementation demonstrates that DAPA speeds up GELU computation by 16$\times$ and decreases DSP utilization by 16$\times$ while maintaining comparable or better performance across vision Transformers and GPT-2 models.
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
