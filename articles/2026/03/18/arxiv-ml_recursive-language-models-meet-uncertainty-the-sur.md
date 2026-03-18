---
title: "Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15653"
published: "2026-03-18"
fetched: "2026-03-18T16:05:39.651359"
---

Computer Science > Computation and Language
[Submitted on 7 Mar 2026]
Title:Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context
View PDF HTML (experimental)Abstract:Long-context handling remains a core challenge for language models: even with extended context windows, models often fail to reliably extract, reason over, and use the information across long contexts. Recent works like Recursive Language Models (RLM) have approached this challenge by agentic way of decomposing long contexts into recursive sub-calls through programmatic interaction at inference. While promising, the success of RLM critically depends on how these context-interaction programs are selected, which has remained largely unexplored. In this paper, we study this problem and introduce SRLM, a framework that augments programmatic context interaction with uncertainty-aware Self-Reflection. SRLM leverages three intrinsic signals: self consistency, reasoning length, and verbalized confidence. These serve as complementary indicators of a model's internal uncertainty, and the model uses them to evaluate and compare candidate context-interaction programs. Extensive experiments across diverse benchmark datasets, context lengths, and backbone models, show that SRLM consistently outperforms state-of-the-art baselines, yielding up to 22% improvement over RLM under the same time budget. Our findings show that recursion itself is not the primary driver of performance in RLM, and a simple self-reflective program search can match or surpass RLM without requiring self-query or explicit recursion mechanisms. We find that for context lengths within the model's window, RLMs with recursion often degrade performance relative to the base model, whereas SRLM yields consistent gains across both short and long contexts. We also find that RLM is less effective in tasks with semantically intensive nature, where heuristic program search is insufficient and broader contextual understanding is required, while self-reflection in SRLM provides a semantic signal that better steers reasoning in these scenarios.
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
