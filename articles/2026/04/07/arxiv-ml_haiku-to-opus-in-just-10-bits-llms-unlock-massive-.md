---
title: "Haiku to Opus in Just 10 bits: LLMs Unlock Massive Compression Gains"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.02343"
published: "2026-04-07"
fetched: "2026-04-08T07:02:32.409401"
---

Computer Science > Machine Learning
[Submitted on 9 Feb 2026]
Title:Haiku to Opus in Just 10 bits: LLMs Unlock Massive Compression Gains
View PDF HTML (experimental)Abstract:We study the compression of LLM-generated text across lossless and lossy regimes, characterizing a compression-compute frontier where more compression is possible at the cost of more compute. For lossless compression, domain-adapted LoRA adapters can improve LLM-based arithmetic coding by 2x over compression with the base LLM alone. For lossy compression, prompting a model for a succinct rewrite then applying arithmetic coding can achieve compression ratios of approximately 0.03, a 2x improvement over compressing the original response.
We further introduce Question-Asking compression (QA), an interactive lossy protocol inspired by the game 'Twenty Questions'. A small model iteratively refines its response by asking yes/no questions to a stronger model, transferring exactly one bit per answer. On 8 benchmarks spanning math, science, and code, 10 binary questions recover 23% to 72% of the capability gap between a small and large model on standard benchmarks and 7% to 38% on harder benchmarks, achieving compression ratios of 0.0006 to 0.004. This is over 100x smaller than prior LLM-based compression (Deletang et al., 2024), suggesting that interactive protocols can transfer knowledge far more efficiently than transmitting full responses.
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
