---
title: "AVControl: Efficient Framework for Training Audio-Visual Controls"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24793"
published: "2026-03-27"
fetched: "2026-03-28T07:16:36.767916"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:AVControl: Efficient Framework for Training Audio-Visual Controls
View PDF HTML (experimental)Abstract:Controlling video and audio generation requires diverse modalities, from depth and pose to camera trajectories and audio transformations, yet existing approaches either train a single monolithic model for a fixed set of controls or introduce costly architectural changes for each new modality. We introduce AVControl, a lightweight, extendable framework built on LTX-2, a joint audio-visual foundation model, where each control modality is trained as a separate LoRA on a parallel canvas that provides the reference signal as additional tokens in the attention layers, requiring no architectural changes beyond the LoRA adapters themselves. We show that simply extending image-based in-context methods to video fails for structural control, and that our parallel canvas approach resolves this. On the VACE Benchmark, we outperform all evaluated baselines on depth- and pose-guided generation, inpainting, and outpainting, and show competitive results on camera control and audio-visual benchmarks. Our framework supports a diverse set of independently trained modalities: spatially-aligned controls such as depth, pose, and edges, camera trajectory with intrinsics, sparse motion control, video editing, and, to our knowledge, the first modular audio-visual controls for a joint generation model. Our method is both compute- and data-efficient: each modality requires only a small dataset and converges within a few hundred to a few thousand training steps, a fraction of the budget of monolithic alternatives. We publicly release our code and trained LoRA checkpoints.
Current browse context:
cs.CV
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
