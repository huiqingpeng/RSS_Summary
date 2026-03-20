---
title: "HiMu: Hierarchical Multimodal Frame Selection for Long Video Question Answering"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18558"
published: "2026-03-20"
fetched: "2026-03-20T15:11:41.312360"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:HiMu: Hierarchical Multimodal Frame Selection for Long Video Question Answering
View PDF HTML (experimental)Abstract:Long-form video question answering requires reasoning over extended temporal contexts, making frame selection critical for large vision-language models (LVLMs) bound by finite context windows. Existing methods face a sharp trade-off: similarity-based selectors are fast but collapse compositional queries into a single dense vector, losing sub-event ordering and cross-modal bindings; agent-based methods recover this structure through iterative LVLM inference, but at prohibitive cost. We introduce HiMu, a training-free framework that bridges this gap. A single text-only LLM call decomposes the query into a hierarchical logic tree whose leaves are atomic predicates, each routed to a lightweight expert spanning vision (CLIP, open-vocabulary detection, OCR) and audio (ASR, CLAP). The resulting signals are normalized, temporally smoothed to align different modalities, and composed bottom-up through fuzzy-logic operators that enforce temporal sequencing and adjacency, producing a continuous satisfaction curve. Evaluations on Video-MME, LongVideoBench and HERBench-Lite show that HiMu advances the efficiency-accuracy Pareto front: at 16 frames with Qwen3-VL 8B it outperforms all competing selectors, and with GPT-4o it surpasses agentic systems operating at 32-512 frames while requiring roughly 10x fewer FLOPs.
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
