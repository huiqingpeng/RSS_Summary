---
title: "Attribution-Guided Decoding"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.26307"
published: "2026-03-18"
fetched: "2026-03-18T16:19:17.624854"
---

Computer Science > Machine Learning
[Submitted on 30 Sep 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Attribution-Guided Decoding
View PDF HTML (experimental)Abstract:The capacity of Large Language Models (LLMs) to follow complex instructions and generate factually accurate text is critical for their real-world application. However, standard decoding methods often fail to robustly satisfy these requirements, while existing control techniques frequently degrade general output quality. In this work, we introduce Attribution-Guided Decoding (AGD), an interpretability-based decoding strategy. Instead of directly manipulating model activations, AGD considers a set of high-probability output token candidates and selects the one that exhibits the highest attribution to a user-defined Region of Interest (ROI). This ROI can be flexibly defined over different parts of the model's input or internal components, allowing AGD to steer generation towards various desirable behaviors. We demonstrate AGD's efficacy across three challenging domains. For instruction following, we show that AGD significantly boosts adherence (e.g., improving the overall success rate on Llama 3.1 from 66.0% to 79.1%). For knowledge-intensive tasks, we show that guiding generation towards usage of internal knowledge components or contextual sources can reduce hallucinations and improve factual accuracy in both closed-book and open-book settings. Furthermore, we propose an adaptive, entropy-based variant of AGD that mitigates quality degradation and reduces computational overhead by applying guidance only when the model is uncertain. Our work presents a versatile, more interpretable, and effective method for enhancing the reliability of modern LLMs.
Submission history
From: Piotr Komorowski [view email][v1] Tue, 30 Sep 2025 14:21:40 UTC (955 KB)
[v2] Tue, 17 Mar 2026 00:39:36 UTC (946 KB)
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
