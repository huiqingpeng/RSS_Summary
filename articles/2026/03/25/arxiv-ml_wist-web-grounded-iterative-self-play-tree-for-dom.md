---
title: "WIST: Web-Grounded Iterative Self-Play Tree for Domain-Targeted Reasoning Improvement"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22352"
published: "2026-03-25"
fetched: "2026-03-26T07:13:13.859351"
---

Computer Science > Machine Learning
[Submitted on 22 Mar 2026]
Title:WIST: Web-Grounded Iterative Self-Play Tree for Domain-Targeted Reasoning Improvement
View PDF HTML (experimental)Abstract:Recent progress in reinforcement learning with verifiable rewards (RLVR) offers a practical path to self-improvement of language models, but existing methods face a key trade-off: endogenous self-play can drift over iterations, while corpus-grounded approaches rely on curated data environments. We present \textbf{WIST}, a \textbf{W}eb-grounded \textbf{I}terative \textbf{S}elf-play \textbf{T}ree framework for domain-targeted reasoning improvement that learns directly from the open web without requiring any pre-arranged domain corpus. WIST incrementally expands a domain tree for exploration, and retrieves and cleans path-consistent web corpus to construct a controllable training environment. It then performs Challenger--Solver self-play with verifiable rewards, and feeds learnability signals back to update node posteriors and guide subsequent exploration through an adaptive curriculum. Across four backbones, WIST consistently improves over the base models and typically outperforms both purely endogenous self-evolution and corpus-grounded self-play baselines, with the Overall gains reaching \textbf{+9.8} (\textit{Qwen3-4B-Base}) and \textbf{+9.7} (\textit{OctoThinker-8B}). WIST is also domain-steerable, improving \textit{Qwen3-8B-Base} by \textbf{+14.79} in medicine and \textit{Qwen3-4B-Base} by \textbf{+5.28} on PhyBench. Ablations further confirm the importance of WIST's key components for stable open-web learning. Our Code is available at this https URL.
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
