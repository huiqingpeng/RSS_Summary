---
title: "Mask Is What DLLM Needs: A Masked Data Training Paradigm for Diffusion LLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15803"
published: "2026-03-18"
fetched: "2026-03-18T15:35:13.061772"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:Mask Is What DLLM Needs: A Masked Data Training Paradigm for Diffusion LLMs
View PDF HTML (experimental)Abstract:Discrete diffusion models offer global context awareness and flexible parallel generation. However, uniform random noise schedulers in standard DLLM training overlook the highly non-uniform information density inherent in real-world sequences. This wastes optimization resources on low-density structural glues while leaving high-density logical pivot points severely under-optimized. To address this, we propose an Information Density Driven Smart Noise Scheduler. By extracting information-dense hubs and applying Complementary Priority Masking, our method decouples a single training instance into mutually reinforcing reasoning and syntax samples, forcing the model to master both logical deduction and foundational sequence structure. Experiments demonstrate that our approach improves average accuracy by ~4\% across four Code and Math reasoning benchmarks, significantly outperforming uniform baselines. Mechanistic analyses further reveal that probabilistic priority masking effectively mitigates contextual collapse during block diffusion training. Overall, this density-aware strategy efficiently unlocks the reasoning potential of diffusion language models at minimal annotation cost, emerging as a promising new masked data training paradigm for Diffusion LLMs. Our processed dataset can be found at this https URL.
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
