---
title: "FIPO: Eliciting Deep Reasoning with Future-KL Influenced Policy Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19835"
published: "2026-03-23"
fetched: "2026-03-24T07:22:42.414444"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:FIPO: Eliciting Deep Reasoning with Future-KL Influenced Policy Optimization
View PDF HTML (experimental)Abstract:We present Future-KL Influenced Policy Optimization (FIPO), a reinforcement learning algorithm designed to overcome reasoning bottlenecks in large language models. While GRPO style training scales effectively, it typically relies on outcome-based rewards (ORM) that distribute a global advantage uniformly across every token in a trajectory. We argue that this coarse-grained credit assignment imposes a performance ceiling by failing to distinguish critical logical pivots from trivial tokens. FIPO addresses this by incorporating discounted future-KL divergence into the policy update, creating a dense advantage formulation that re-weights tokens based on their influence on subsequent trajectory behavior. Empirically, FIPO enables models to break through the length stagnation seen in standard baselines. Evaluated on Qwen2.5-32B, FIPO extends the average chain-of-thought length from roughly 4,000 to over 10,000 tokens and increases AIME 2024 Pass@1 accuracy from 50.0% to a peak of 58.0% (converging at approximately 56.0\%). This outperforms both DeepSeek-R1-Zero-Math-32B (around 47.0%) and o1-mini (approximately 56.0%). Our results suggest that establishing dense advantage formulations is a vital path for evolving ORM-based algorithms to unlock the full reasoning potential of base models. We open-source our training system, built on the verl framework.
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
