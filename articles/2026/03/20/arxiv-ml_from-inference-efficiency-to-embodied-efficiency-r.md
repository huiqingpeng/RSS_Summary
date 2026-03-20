---
title: "From Inference Efficiency to Embodied Efficiency: Revisiting Efficiency Metrics for Vision-Language-Action Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19131"
published: "2026-03-20"
fetched: "2026-03-20T12:18:51.406557"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:From Inference Efficiency to Embodied Efficiency: Revisiting Efficiency Metrics for Vision-Language-Action Models
View PDF HTML (experimental)Abstract:Vision-Language-Action (VLA) models have recently enabled embodied agents to perform increasingly complex tasks by jointly reasoning over visual, linguistic, and motor modalities. However, we find that the prevailing notion of ``efficiency'' in current VLA research, characterized by parameters, FLOPs, or token decoding throughput, does not reflect actual performance on robotic platforms. In real-world execution, efficiency is determined by system-level embodied behaviors such as task completion time, trajectory smoothness, cumulative joint rotation, and motion energy. Through controlled studies across model compression, token sparsification, and action sequence compression, we make several observations that challenge common assumptions. (1) Methods that reduce computation under conventional metrics often increase end-to-end execution cost or degrade motion quality, despite maintaining task success rates. (2) System-level embodied efficiency metrics reveal performance differences in the learned action policies that remain hidden under conventional evaluations. (3) Common adaptation methods such as in-context prompting or supervised fine-tuning show only mild and metric-specific improvements in embodied efficiency. While these methods can reduce targeted embodied-efficiency metrics such as jerk or action rate, the resulting gains may come with trade-offs in other metrics, such as longer completion time. Taken together, our results suggest that conventional inference efficiency metrics can overlook important aspects of embodied execution. Incorporating embodied efficiency provides a more complete view of policy behavior and practical performance, enabling fairer and more comprehensive comparisons of VLA models.
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
