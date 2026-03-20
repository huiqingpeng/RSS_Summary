---
title: "Approximate Subgraph Matching with Neural Graph Representations and Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18314"
published: "2026-03-20"
fetched: "2026-03-20T12:10:16.134107"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Approximate Subgraph Matching with Neural Graph Representations and Reinforcement Learning
View PDF HTML (experimental)Abstract:Approximate subgraph matching (ASM) is a task that determines the approximate presence of a given query graph in a large target graph. Being an NP-hard problem, ASM is critical in graph analysis with a myriad of applications ranging from database systems and network science to biochemistry and privacy. Existing techniques often employ heuristic search strategies, which cannot fully utilize the graph information, leading to sub-optimal solutions. This paper proposes a Reinforcement Learning based Approximate Subgraph Matching (RL-ASM) algorithm that exploits graph transformers to effectively extract graph representations and RL-based policies for ASM. Our model is built upon the branch-and-bound algorithm that selects one pair of nodes from the two input graphs at a time for potential matches. Instead of using heuristics, we exploit a Graph Transformer architecture to extract feature representations that encode the full graph information. To enhance the training of the RL policy, we use supervised signals to guide our agent in an imitation learning stage. Subsequently, the policy is fine-tuned with the Proximal Policy Optimization (PPO) that optimizes the accumulative long-term rewards over episodes. Extensive experiments on both synthetic and real-world datasets demonstrate that our RL-ASM outperforms existing methods in terms of effectiveness and efficiency. Our source code is available at this https URL.
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
