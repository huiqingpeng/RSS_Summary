---
title: "SENSE: Efficient EEG-to-Text via Privacy-Preserving Semantic Retrieval"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17109"
published: "2026-03-19"
fetched: "2026-03-19T12:07:25.581559"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:SENSE: Efficient EEG-to-Text via Privacy-Preserving Semantic Retrieval
View PDF HTML (experimental)Abstract:Decoding brain activity into natural language is a major challenge in AI with important applications in assistive communication, neurotechnology, and human-computer interaction. Most existing Brain-Computer Interface (BCI) approaches rely on memory-intensive fine-tuning of Large Language Models (LLMs) or encoder-decoder models on raw EEG signals, resulting in expensive training pipelines, limited accessibility, and potential exposure of sensitive neural data. We introduce SENSE (SEmantic Neural Sparse Extraction), a lightweight and privacy-preserving framework that translates non-invasive electroencephalography (EEG) into text without LLM fine-tuning. SENSE decouples decoding into two stages: on-device semantic retrieval and prompt-based language generation. EEG signals are locally mapped to a discrete textual space to extract a non-sensitive Bag-of-Words (BoW), which conditions an off-the-shelf LLM to synthesize fluent text in a zero-shot manner. The EEG-to-keyword module contains only ~6M parameters and runs fully on-device, ensuring raw neural signals remain local while only abstract semantic cues interact with language models. Evaluated on a 128-channel EEG dataset across six subjects, SENSE matches or surpasses the generative quality of fully fine-tuned baselines such as Thought2Text while substantially reducing computational overhead. By localizing neural decoding and sharing only derived textual cues, SENSE provides a scalable and privacy-aware retrieval-augmented architecture for next-generation BCIs.
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
