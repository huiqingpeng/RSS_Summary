---
title: "LLM Reasoning with Process Rewards for Outcome-Guided Steps"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.02341"
published: "2026-04-07"
fetched: "2026-04-08T07:02:31.415683"
---

Computer Science > Machine Learning
[Submitted on 8 Feb 2026]
Title:LLM Reasoning with Process Rewards for Outcome-Guided Steps
View PDF HTML (experimental)Abstract:Mathematical reasoning in large language models has improved substantially with reinforcement learning using verifiable rewards, where final answers can be checked automatically and converted into reliable training signals. Most such pipelines optimize outcome correctness only, which yields sparse feedback for long, multi-step solutions and offers limited guidance on intermediate reasoning errors. Recent work therefore introduces process reward models (PRMs) to score intermediate steps and provide denser supervision. In practice, PRM scores are often imperfectly aligned with final correctness and can reward locally fluent reasoning that still ends in an incorrect answer. When optimized as absolute rewards, such signals can amplify fluent failure modes and induce reward hacking.
We propose PROGRS, a framework that leverages PRMs while keeping outcome correctness dominant. PROGRS treats process rewards as relative preferences within outcome groups rather than absolute targets. We introduce outcome-conditioned centering, which shifts PRM scores of incorrect trajectories to have zero mean within each prompt group. It removes systematic bias while preserving informative rankings. PROGRS combines a frozen quantile-regression PRM with a multi-scale coherence evaluator. We integrate the resulting centered process bonus into Group Relative Policy Optimization (GRPO) without auxiliary objectives or additional trainable components. Across MATH-500, AMC, AIME, MinervaMath, and OlympiadBench, PROGRS consistently improves Pass@1 over outcome-only baselines and achieves stronger performance with fewer rollouts. These results show that outcome-conditioned centering enables safe and effective use of process rewards for mathematical reasoning.
Submission history
From: Mohammad Rezaei Ravari [view email][v1] Sun, 8 Feb 2026 06:38:20 UTC (2,802 KB)
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
