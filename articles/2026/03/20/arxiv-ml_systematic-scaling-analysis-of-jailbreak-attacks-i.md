---
title: "Systematic Scaling Analysis of Jailbreak Attacks in Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.11149"
published: "2026-03-20"
fetched: "2026-03-20T14:12:44.976528"
---

Computer Science > Machine Learning
[Submitted on 11 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Systematic Scaling Analysis of Jailbreak Attacks in Large Language Models
View PDF HTML (experimental)Abstract:Large language models remain vulnerable to jailbreak attacks, yet we still lack a systematic understanding of how jailbreak success scales with attacker effort across methods, model families, and harm types. We initiate a scaling-law framework for jailbreaks by treating each attack as a compute-bounded optimization procedure and measuring progress on a shared FLOPs axis. Our systematic evaluation spans four representative jailbreak paradigms, covering optimization-based attacks, self-refinement prompting, sampling-based selection, and genetic optimization, across multiple model families and scales on a diverse set of harmful goals. We investigate scaling laws that relate attacker budget to attack success score by fitting a simple saturating exponential function to FLOPs--success trajectories, and we derive comparable efficiency summaries from the fitted curves. Empirically, prompting-based paradigms tend to be the most compute-efficient compared to optimization-based methods. To explain this gap, we cast prompt-based updates into an optimization view and show via a same-state comparison that prompt-based attacks more effectively optimize in prompt space. We also show that attacks occupy distinct success--stealthiness operating points with prompting-based methods occupying the high-success, high-stealth region. Finally, we find that vulnerability is strongly goal-dependent: harms involving misinformation are typically easier to elicit than other non-misinformation harms.
Submission history
From: Xiangwen Wang [view email][v1] Wed, 11 Mar 2026 17:38:08 UTC (177 KB)
[v2] Wed, 18 Mar 2026 04:23:56 UTC (177 KB)
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
