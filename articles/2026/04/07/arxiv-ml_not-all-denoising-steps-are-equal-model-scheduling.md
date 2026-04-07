---
title: "Not All Denoising Steps Are Equal: Model Scheduling for Faster Masked Diffusion Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.02340"
published: "2026-04-07"
fetched: "2026-04-08T07:02:30.954166"
---

Computer Science > Machine Learning
[Submitted on 4 Feb 2026]
Title:Not All Denoising Steps Are Equal: Model Scheduling for Faster Masked Diffusion Language Models
View PDF HTML (experimental)Abstract:Recent advances in masked diffusion language models (MDLMs) narrow the quality gap to autoregressive LMs, but their sampling remains expensive because generation requires many full-sequence denoising passes with a large Transformer and, unlike autoregressive decoding, cannot benefit from KV caching. In this work, we exploit the flexibility of the diffusion framework and study model scheduling, where a smaller MDLM replaces the full model at a subset of denoising steps. On OpenWebText, we show that early and late denoising steps are substantially more robust to such replacement than middle steps, enabling up to a 17% reduction in FLOPs with only modest degradation in generative perplexity. We support these findings with a step-importance analysis based on loss and KL divergence between small and large models across timesteps, as well as an exhaustive search over coarse step segments, both of which identify the middle of the diffusion trajectory as most sensitive. Our results suggest that simple, architecture-agnostic scheduling rules can significantly accelerate MDLM sampling while largely preserving generation quality as measured by generative perplexity.
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
