---
title: "Detection Is Cheap, Routing Is Learned: Why Refusal-Based Alignment Evaluation Fails"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18280"
published: "2026-03-20"
fetched: "2026-03-20T12:09:49.349178"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Detection Is Cheap, Routing Is Learned: Why Refusal-Based Alignment Evaluation Fails
View PDF HTML (experimental)Abstract:Current alignment evaluation mostly measures whether models encode dangerous concepts and whether they refuse harmful requests. Both miss the layer where alignment often operates: routing from concept detection to behavioral policy. We study political censorship in Chinese-origin language models as a natural experiment, using probes, surgical ablations, and behavioral tests across nine open-weight models from five labs. Three findings follow. First, probe accuracy alone is non-diagnostic: political probes, null controls, and permutation baselines can all reach 100%, so held-out category generalization is the informative test. Second, surgical ablation reveals lab-specific routing. Removing the political-sensitivity direction eliminates censorship and restores accurate factual output in most models tested, while one model confabulates because its architecture entangles factual knowledge with the censorship mechanism. Cross-model transfer fails, indicating that routing geometry is model- and lab-specific. Third, refusal is no longer the dominant censorship mechanism. Within one model family, hard refusal falls to zero while narrative steering rises to the maximum, making censorship invisible to refusal-only benchmarks. These results support a three-stage descriptive framework: detect, route, generate. Models often retain the relevant knowledge; alignment changes how that knowledge is expressed. Evaluations that audit only detection or refusal therefore miss the routing mechanism that most directly determines behavior.
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
