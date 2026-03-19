---
title: "ASAP: Attention-Shift-Aware Pruning for Efficient LVLM Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14549"
published: "2026-03-19"
fetched: "2026-03-19T14:19:59.080439"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 15 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:ASAP: Attention-Shift-Aware Pruning for Efficient LVLM Inference
View PDF HTML (experimental)Abstract:While Large Vision-Language Models (LVLMs) demonstrate exceptional multi-modal capabilities, the quadratic computational cost of processing high-resolution visual tokens remains a critical bottleneck. Though recent token reduction strategies attempt to accelerate inference, such methods inadequately exploit attention values and fail to address token redundancy. More critically, they overlook the ``attention shift'' phenomenon inherent in LVLMs, which skews token attention scores. In this work, we propose ASAP, a novel training-free, KV-Cache-compatible pruning recipe that comprehensively addresses these limitations. First, we mitigate the attention shift by utilizing a dynamic bidirectional soft attention mask, ensuring the selection of genuinely informative tokens rather than naive attention-based selection. Second, we posit that high semantic redundancy within the token set degrades performance. We therefore introduce a weighted soft merging component that merges semantically similar tokens, preserving only the most feature-dense visual patches for subsequent layers. ASAP achieves virtually lossless compression of visual context, retaining 99.02% of the original LLaVA-NeXT-7B performance while aggressively slashing computational FLOPs by ~80%.
Submission history
From: Surendra Pathak [view email][v1] Sun, 15 Mar 2026 18:51:31 UTC (1,781 KB)
[v2] Tue, 17 Mar 2026 20:41:37 UTC (1,782 KB)
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
