---
title: "AIA: Rethinking Architecture Decoupling Strategy In Unified Multimodal Model"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.22663"
published: "2026-03-18"
fetched: "2026-03-18T18:29:43.974916"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 27 Nov 2025 (v1), last revised 17 Mar 2026 (this version, v4)]
Title:AIA: Rethinking Architecture Decoupling Strategy In Unified Multimodal Model
View PDF HTML (experimental)Abstract:Unified multimodal models for image generation and understanding represent a significant step toward AGI and have attracted widespread attention from researchers. The main challenge of this task lies in the difficulty in establishing an optimal training paradigm due to inherent conflicting targets in understanding and generation tasks. To alleviate these conflicts and pursue higher performance, many researchers adopt varying degrees of architecture decoupling (e.g., Double image encoders, MOE/MOT architecture, or frozen MLLM). However, excessive model decoupling can lead to the loss of interleave generation ability, undermining the original intent of unified models. In this work, we aim to explore how to mitigate task conflicts without resorting to model decoupling. Firstly, we analyze why decoupling boosts performance by studying the cross-modal attention behavior of models. We observe that architecture decoupling does not solve task conflicts, but essentially drives models toward cross-modal interaction patterns of task-specific models, as seen in Qwen3-VL and HunyuanImage-3.0, and that the more thorough the decoupling, the more consistent the behavior becomes. Motivated by this observation, we propose Attention Interaction Alignment (AIA) loss, which explicitly learns task-specific multimodal interaction patterns during training. To demonstrate the generalizability of our AIA loss, we apply it to Emu3 and Janus-Pro during SFT and post-training stage respectively. Without bells and whistles, AIA not only refines cross-modal attention patterns, but also boosts both generation and understanding performance.
Submission history
From: Dian Zheng [view email][v1] Thu, 27 Nov 2025 17:55:25 UTC (2,020 KB)
[v2] Thu, 11 Dec 2025 13:59:22 UTC (2,020 KB)
[v3] Sun, 15 Mar 2026 08:02:01 UTC (2,177 KB)
[v4] Tue, 17 Mar 2026 02:36:58 UTC (2,183 KB)
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
