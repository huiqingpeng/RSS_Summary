---
title: "ARIADNE: A Perception-Reasoning Synergy Framework for Trustworthy Coronary Angiography Analysis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19169"
published: "2026-03-20"
fetched: "2026-03-20T16:05:09.148455"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:ARIADNE: A Perception-Reasoning Synergy Framework for Trustworthy Coronary Angiography Analysis
View PDF HTML (experimental)Abstract:Conventional pixel-wise loss functions fail to enforce topological constraints in coronary vessel segmentation, producing fragmented vascular trees despite high pixel-level accuracy. We present ARIADNE, a two-stage framework coupling preference-aligned perception with RL-based diagnostic reasoning for topologically coherent stenosis detection. The perception module employs DPO to fine-tune the Sa2VA vision-language foundation model using Betti number constraints as preference signals, aligning the policy toward geometrically complete vessel structures rather than pixel-wise overlap metrics. The reasoning module formulates stenosis localization as a Markov Decision Process with an explicit rejection mechanism that autonomously defers ambiguous anatomical candidates such as bifurcations and vessel crossings, shifting from coverage maximization to reliability optimization. On 1,400 clinical angiograms, ARIADNE achieves state-of-the-art centerline Dice of 0.838, reduces false positives by 41% compared to geometric baselines. External validation on multi-center benchmarks ARCADE and XCAD confirms generalization across acquisition protocols. This represents the first application of DPO for topological alignment in medical imaging, demonstrating that preference-based learning over structural constraints mitigates topological violations while maintaining diagnostic sensitivity in interventional cardiology workflows.
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
