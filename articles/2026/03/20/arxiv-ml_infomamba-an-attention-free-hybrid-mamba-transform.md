---
title: "InfoMamba: An Attention-Free Hybrid Mamba-Transformer Model"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18031"
published: "2026-03-20"
fetched: "2026-03-20T12:05:17.475358"
---

Computer Science > Machine Learning
[Submitted on 8 Mar 2026]
Title:InfoMamba: An Attention-Free Hybrid Mamba-Transformer Model
View PDF HTML (experimental)Abstract:Balancing fine-grained local modeling with long-range dependency capture under computational constraints remains a central challenge in sequence modeling. While Transformers provide strong token mixing, they suffer from quadratic complexity, whereas Mamba-style selective state-space models (SSMs) scale linearly but often struggle to capture high-rank and synchronous global interactions. We present a consistency boundary analysis that characterizes when diagonal short-memory SSMs can approximate causal attention and identifies structural gaps that remain. Motivated by this analysis, we propose InfoMamba, an attention-free hybrid architecture. InfoMamba replaces token-level self-attention with a concept bottleneck linear filtering layer that serves as a minimal-bandwidth global interface and integrates it with a selective recurrent stream through information-maximizing fusion (IMF). IMF dynamically injects global context into the SSM dynamics and encourages complementary information usage through a mutual-information-inspired objective. Extensive experiments on classification, dense prediction, and non-vision tasks show that InfoMamba consistently outperforms strong Transformer and SSM baselines, achieving competitive accuracy-efficiency trade-offs while maintaining near-linear scaling.
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
