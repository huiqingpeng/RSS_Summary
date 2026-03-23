---
title: "Maximizing mutual information between user-contexts and responses improve LLM personalization with no additional data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19294"
published: "2026-03-23"
fetched: "2026-03-24T07:15:17.327145"
---

Computer Science > Machine Learning
[Submitted on 10 Mar 2026]
Title:Maximizing mutual information between user-contexts and responses improve LLM personalization with no additional data
View PDF HTML (experimental)Abstract:While post-training has successfully improved large language models (LLMs) across a variety of domains, these gains heavily rely on human-labeled data or external verifiers. Existing data has already been exploited, and new high-quality data is expensive to collect. More fundamentally, true intelligence goes far beyond tasks that are easily verifiable. Therefore, we need self-improvement frameworks that allow models to improve without external oversight. We propose *Mutual Information Preference Optimization (MIPO)*, a contrastive data augmentation method that constructs preference pairs by generating a positive response conditioning on the correct prompt, and a negative response by conditioning on a random, unrelated prompt. We show that using Direct Preference Optimization (DPO) to learn from this paired data maximizes pointwise conditional mutual information (MI) (under the base LLM) between prompts and model responses. Empirical results with various-sized Llama- and Qwen-Instruct models show that when used to maximize MI between user context and response, MIPO provides an effective personalization technique, achieving 3-40% improvements on personalization tasks using real-user datasets compared to strong baselines. Surprisingly, MIPO can also be applied to improve performance on math and multiple-choice problems, yielding 1-18% **without any additional data or human supervision**. These results suggest a promising direction for self-improvement.
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
