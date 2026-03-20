---
title: "CAFlow: Adaptive-Depth Single-Step Flow Matching for Efficient Histopathology Super-Resolution"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18513"
published: "2026-03-20"
fetched: "2026-03-20T15:10:59.560611"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:CAFlow: Adaptive-Depth Single-Step Flow Matching for Efficient Histopathology Super-Resolution
View PDF HTML (experimental)Abstract:In digital pathology, whole-slide images routinely exceed gigapixel resolution, making computationally intensive generative super-resolution (SR) impractical for routine deployment. We introduce CAFlow, an adaptive-depth single-step flow-matching framework that routes each image tile to the shallowest network exit that preserves reconstruction quality. CAFlow performs flow matching in pixel-unshuffled rearranged space, reducing spatial computation by 16x while enabling direct inference. We show that dedicating half of training to exact t=0 samples is essential for single-step quality (-1.5 dB without it). The backbone, FlowResNet (1.90M parameters), mixes convolution and window self-attention blocks across four early exits spanning 3.1 to 13.3 GFLOPs. A lightweight exit classifier (~6K parameters) achieves 33% compute savings at only 0.12 dB cost. On multi-organ histopathology x4 SR, adaptive routing achieves 31.72 dB PSNR versus 31.84 dB at full depth, while the shallowest exit exceeds bicubic by +1.9 dB at 2.8x less compute than SwinIR-light. The method generalizes to held-out colon tissue with minimal quality loss (-0.02 dB), and at x8 upscaling it outperforms all comparable-compute baselines while remaining competitive with the much larger SwinIR-Medium model. Downstream nuclei segmentation confirms preservation of clinically relevant structure. The model trains in under 5 hours on a single GPU, and adaptive routing can reduce whole-slide inference from minutes to seconds.
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
