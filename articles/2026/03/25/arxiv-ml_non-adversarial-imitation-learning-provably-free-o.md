---
title: "Non-Adversarial Imitation Learning Provably Free of Compounding Errors: The Role of Bellman Constraints"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22713"
published: "2026-03-25"
fetched: "2026-03-26T07:16:27.046712"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Non-Adversarial Imitation Learning Provably Free of Compounding Errors: The Role of Bellman Constraints
View PDFAbstract:Adversarial imitation learning (AIL) achieves high-quality imitation by mitigating compounding errors in behavioral cloning (BC), but often exhibits training instability due to adversarial optimization. To avoid this issue, a class of non-adversarial Q-based imitation learning (IL) methods, represented by IQ-Learn, has emerged and is widely believed to outperform BC by leveraging online environment interactions. However, this paper revisits IQ-Learn and demonstrates that it provably reduces to BC and suffers from an imitation gap lower bound with quadratic dependence on horizon, therefore still suffering from compounding errors. Theoretical analysis reveals that, despite using online interactions, IQ-Learn uniformly suppresses the Q-values for all actions on states uncovered by demonstrations, thereby failing to generalize. To address this limitation, we introduce a primal-dual framework for distribution matching, yielding a new Q-based IL method, Dual Q-DM. The key mechanism in Dual Q-DM is incorporating Bellman constraints to propagate high Q-values from visited states to unvisited ones, thereby achieving generalization beyond demonstrations. We prove that Dual Q-DM is equivalent to AIL and can recover expert actions beyond demonstrations, thereby mitigating compounding errors. To the best of our knowledge, Dual Q-DM is the first non-adversarial IL method that is theoretically guaranteed to eliminate compounding errors. Experimental results further corroborate our theoretical results.
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
