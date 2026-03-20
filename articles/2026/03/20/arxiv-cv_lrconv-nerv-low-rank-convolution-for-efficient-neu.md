---
title: "LRConv-NeRV: Low Rank Convolution for Efficient Neural Video Compression"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18261"
published: "2026-03-20"
fetched: "2026-03-20T15:06:48.810929"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:LRConv-NeRV: Low Rank Convolution for Efficient Neural Video Compression
View PDFAbstract:Neural Representations for Videos (NeRV) encode entire video sequences within neural network parameters, offering an alternative paradigm to conventional video codecs. However, the convolutional decoder of NeRV remains computationally expensive and memory intensive, limiting its deployment in resource-constrained environments. This paper proposes LRConv-NeRV, an efficient NeRV variant that replaces selected dense 3x3 convolutional layers with structured low-rank separable convolutions, trained end-to-end within the decoder architecture. By progressively applying low-rank factorization from the largest to earlier decoder stages, LRConv-NeRV enables controllable trade-offs between reconstruction quality and efficiency. Extensive experiments demonstrate that applying LRConv only to the final decoder stage reduces decoder complexity by 68%, from 201.9 to 64.9 GFLOPs, and model size by 9.3%, while incurring negligible quality loss and achieving approximately 9.2% bitrate reduction. Under INT8 post-training quantization, LRConv-NeRV preserves reconstruction quality close to the dense NeRV baseline, whereas more aggressive factorization of early decoder stages leads to disproportionate quality degradation. Compared to existing work under layer-aligned settings, LRConv-NeRV achieves a more favorable efficiency versus quality trade-off, offering substantial GFLOPs and parameter reductions while maintaining higher PSNR/MS-SSIM and improved temporal stability. Temporal flicker analysis using LPIPS further shows that the proposed solution preserves temporal coherence close to the NeRV baseline, results establish LRConv-NeRV as a potential architectural alternative for efficient neural video decoding under low-precision and resource-constrained settings.
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
