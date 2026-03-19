---
title: "Do Understanding and Generation Fight? A Diagnostic Study of DPO for Unified Multimodal Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17044"
published: "2026-03-19"
fetched: "2026-03-19T12:06:38.586768"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Do Understanding and Generation Fight? A Diagnostic Study of DPO for Unified Multimodal Models
View PDF HTML (experimental)Abstract:Unified multimodal models share a language model backbone for both understanding and generating images. Can DPO align both capabilities simultaneously? We present the first systematic study of this question, applying DPO to Janus-Pro at 1B and 7B parameters under seven training strategies and two post-hoc methods. The central finding is negative: generation quality resists DPO alignment across all tested conditions on this architecture. No method improves generation CLIPScore at 7B (|Delta| < 0.2, p > 0.5 at n=200 per seed, 3 seeds); at 1B, all methods degrade generation, and the result holds across preference data types (real-vs-generated and model-vs-model) and the data volumes tested (150-288 pairs). Gradient analysis reveals why: understanding and generation gradients are near-orthogonal (cos ~ 0) with ~11-14x magnitude imbalance driven by VQ token count asymmetry (576 generation tokens vs. ~30-100 text tokens). This imbalance is the dominant interference mechanism in multi-task DPO; magnitude-balancing yields directionally positive understanding deltas (+0.01-0.04 VQA, though individually not significant), but the generation gap persists regardless. We identify discrete VQ tokenization as a likely structural bottleneck -- supported by the generation DPO loss converging to ln(2) -- and provide practical guidance for practitioners working with VQ-based unified models.
Current browse context:
cs.LG
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
