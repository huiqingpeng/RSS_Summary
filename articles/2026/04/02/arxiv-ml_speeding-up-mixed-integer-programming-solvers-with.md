---
title: "Speeding Up Mixed-Integer Programming Solvers with Sparse Learning for Branching"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00094"
published: "2026-04-02"
fetched: "2026-04-03T07:17:19.574080"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Speeding Up Mixed-Integer Programming Solvers with Sparse Learning for Branching
View PDFAbstract:Machine learning is increasingly used to improve decisions within branch-and-bound algorithms for mixed-integer programming. Many existing approaches rely on deep learning, which often requires very large training datasets and substantial computational resources for both training and deployment, typically with GPU parallelization. In this work, we take a different path by developing interpretable models that are simple but effective. We focus on approximating strong branching (SB) scores, a highly effective yet computationally expensive branching rule. Using sparse learning methods, we build models with fewer than 4% of the parameters of a state-of-the-art graph neural network (GNN) while achieving competitive accuracy. Relative to SCIP's built-in branching rules and the GNN-based model, our CPU-only models are faster than the default solver and the GPU-accelerated GNN. The models are simple to train and deploy, and they remain effective with small training sets, which makes them practical in low-resource settings. Extensive experiments across diverse problem classes demonstrate the efficiency of this approach.
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
