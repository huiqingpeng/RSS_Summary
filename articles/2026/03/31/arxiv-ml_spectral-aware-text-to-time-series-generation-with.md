---
title: "Spectral-Aware Text-to-Time Series Generation with Billion-Scale Multimodal Meteorological Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27135"
published: "2026-03-31"
fetched: "2026-04-01T07:21:52.686113"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:Spectral-Aware Text-to-Time Series Generation with Billion-Scale Multimodal Meteorological Data
View PDF HTML (experimental)Abstract:Text-to-time-series generation is particularly important in meteorology, where natural language offers intuitive control over complex, multi-scale atmospheric dynamics. Existing approaches are constrained by the lack of large-scale, physically grounded multimodal datasets and by architectures that overlook the spectral-temporal structure of weather signals. We address these challenges with a unified framework for text-guided meteorological time-series generation. First, we introduce MeteoCap-3B, a billion-scale weather dataset paired with expert-level captions constructed via a Multi-agent Collaborative Captioning (MACC) pipeline, yielding information-dense and physically consistent annotations. Building on this dataset, we propose MTransformer, a diffusion-based model that enables precise semantic control by mapping textual descriptions into multi-band spectral priors through a Spectral Prompt Generator, which guides generation via frequency-aware attention. Extensive experiments on real-world benchmarks demonstrate state-of-the-art generation quality, accurate cross-modal alignment, strong semantic controllability, and substantial gains in downstream forecasting under data-sparse and zero-shot settings. Additional results on general time-series benchmarks indicate that the proposed framework generalizes beyond meteorology.
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
