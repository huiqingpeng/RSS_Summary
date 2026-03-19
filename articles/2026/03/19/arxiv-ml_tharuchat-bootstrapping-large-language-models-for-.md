---
title: "TharuChat: Bootstrapping Large Language Models for a Low-Resource Language via Synthetic Data and Human Validation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17220"
published: "2026-03-19"
fetched: "2026-03-19T13:10:32.642645"
---

Computer Science > Computation and Language
[Submitted on 17 Mar 2026]
Title:TharuChat: Bootstrapping Large Language Models for a Low-Resource Language via Synthetic Data and Human Validation
View PDF HTML (experimental)Abstract:The rapid proliferation of Large Language Models (LLMs) has created a profound digital divide, effectively excluding indigenous languages of the Global South from the AI revolution. The Tharu language, an Indo-Aryan vernacular spoken by approximately 1.7 million people across the Terai belt of Nepal and India, exemplifies this crisis. Despite a rich oral tradition, Tharu suffers from severe data scarcity and linguistic fragmentation, causing state-of-the-art multilingual models to routinely "hallucinate" or default to dominant high-resource neighbors like Hindi and Nepali due to contamination in pre-training corpora.
This paper presents Tharu-LLaMA (3B), a specialized instruction-following model designed to address this exclusion. We introduce TharuChat, a novel dataset constructed via a LLM-to-Human bootstrapping pipeline. We utilized prompt-engineered Gemini models, fed with Rana Tharu grammar and folklore, to synthesize training data. Unlike curated gold-standard corpora, TharuChat reflects the noisy, heterogeneous linguistic reality of the region: it is predominantly anchored in Rana Tharu (~70%) while integrating elements of Dangaura and Kochila dialects. We provide a transparent analysis of the dataset's limitations, including dialectal code-mixing and residual Awadhi/Hindi influence. Through a rigorous empirical ablation study, we demonstrate that despite these imperfections, small-scale synthetic data is highly effective, increasing the dataset volume from 25% to 100% results in a linear reduction in perplexity from 6.42 to 2.88. The resulting model serves as a proof-of-concept for the preservation of under-resourced Himalayan languages via generative AI, achievable on consumer-grade hardware.
Current browse context:
cs.CL
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
