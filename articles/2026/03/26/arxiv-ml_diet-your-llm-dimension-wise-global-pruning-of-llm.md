---
title: "Diet Your LLM: Dimension-wise Global Pruning of LLMs via Merging Task-specific Importance Score"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23985"
published: "2026-03-26"
fetched: "2026-03-27T07:19:12.817571"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Diet Your LLM: Dimension-wise Global Pruning of LLMs via Merging Task-specific Importance Score
View PDF HTML (experimental)Abstract:Large language models (LLMs) have demonstrated remarkable capabilities, but their massive scale poses significant challenges for practical deployment. Structured pruning offers a promising solution by removing entire dimensions or layers, yet existing methods face critical trade-offs: task-agnostic approaches cannot adapt to task-specific requirements, while task-aware methods require costly training to learn task adaptability. We propose DIET (Dimension-wise global pruning of LLMs via merging Task-wise importance scores), a training-free structured pruning method that combines dimension-level granularity with task-aware selection. DIET profiles activation magnitudes across tasks using only 100 samples per task, then applies majority voting to construct a single global mask. DIET does not require large costs from pre-computation or training. Experiments on seven zero-shot benchmarks using Gemma-2 2B and 9B models demonstrate the effectiveness of DIET; for example, at 20% sparsity on Gemma-2 2B, DIET achieves near 10% average accuracy improvement, compared to previous state-of-the-art structured pruning methods. This advantage persists across various sparsity levels and model scales, positioning DIET as a practical and robust choice for structured LLM pruning.
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
