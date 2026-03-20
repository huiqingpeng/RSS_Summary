---
title: "REST: Receding Horizon Explorative Steiner Tree for Zero-Shot Object-Goal Navigation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18624"
published: "2026-03-20"
fetched: "2026-03-20T16:09:02.818410"
---

Computer Science > Robotics
[Submitted on 19 Mar 2026]
Title:REST: Receding Horizon Explorative Steiner Tree for Zero-Shot Object-Goal Navigation
View PDF HTML (experimental)Abstract:Zero-shot object-goal navigation (ZSON) requires navigating unknown environments to find a target object without task-specific training. Prior hierarchical training-free solutions invest in scene understanding (\textit{belief}) and high-level decision-making (\textit{policy}), yet overlook the design of \textit{option}, i.e., a subgoal candidate proposed from evolving belief and presented to policy for selection. In practice, options are reduced to isolated waypoints scored independently: single destinations hide the value gathered along the journey; an unstructured collection obscures the relationships among candidates. Our insight is that the option space should be a \textit{tree of paths}. Full paths expose en-route information gain that destination-only scoring systematically neglects; a tree of shared segments enables coarse-to-fine LLM reasoning that dismisses or pursues entire branches before examining individual leaves, compressing the combinatorial path space into an efficient hierarchy. We instantiate this insight in \textbf{REST} (Receding Horizon Explorative Steiner Tree), a training-free framework that (1) builds an explicit open-vocabulary 3D map from online RGB-D streams; (2) grows an agent-centric tree of safe and informative paths as the option space via sampling-based planning; and (3) textualizes each branch into a spatial narrative and selects the next-best path through chain-of-thought LLM reasoning. Across the Gibson, HM3D, and HSSD benchmarks, REST consistently ranks among the top methods in success rate while achieving the best or second-best path efficiency, demonstrating a favorable efficiency-success balance.
Current browse context:
cs.RO
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
