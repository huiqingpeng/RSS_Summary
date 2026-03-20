---
title: "Action Draft and Verify: A Self-Verifying Framework for Vision-Language-Action Model"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18091"
published: "2026-03-20"
fetched: "2026-03-20T15:05:54.563483"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Action Draft and Verify: A Self-Verifying Framework for Vision-Language-Action Model
View PDF HTML (experimental)Abstract:Vision-Language-Action (VLA) models have recently demonstrated strong performance across embodied tasks. Modern VLAs commonly employ diffusion action experts to efficiently generate high-precision continuous action chunks, while auto-regressive generation can be slower and less accurate at low-level control. Yet auto-regressive paradigms still provide complementary priors that can improve robustness and generalization in out-of-distribution environments. To leverage both paradigms, we propose Action-Draft-and-Verify (ADV): diffusion action expert drafts multiple candidate action chunks, and the VLM selects one by scoring all candidates in a single forward pass with a perplexity-style metric. Under matched backbones, training data, and action-chunk length, ADV improves success rate by +4.3 points in simulation and +19.7 points in real-world over diffusion-based baseline, with a single-pass VLM reranking overhead.
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
