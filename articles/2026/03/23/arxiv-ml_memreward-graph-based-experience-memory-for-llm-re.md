---
title: "MemReward: Graph-Based Experience Memory for LLM Reward Prediction with Limited Labels"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19310"
published: "2026-03-23"
fetched: "2026-03-24T07:16:26.204808"
---

Computer Science > Machine Learning
[Submitted on 13 Mar 2026]
Title:MemReward: Graph-Based Experience Memory for LLM Reward Prediction with Limited Labels
View PDF HTML (experimental)Abstract:Training large language models (LLMs) for complex reasoning via reinforcement learning requires reward labels that specify whether the generated rollouts are correct. However, obtaining reward labels at scale often requires expensive human labeling or time-consuming verification procedures; for instance, evaluating mathematical proofs demands expert review, while open-ended question answering lacks definitive ground truth. When reward labels are limited, the effectiveness of reinforcement learning fine-tuning is constrained by the scarcity of reward labels. We introduce MemReward, a graph-based experience memory framework: an initial LLM policy generates rollouts for each query, each comprising a thinking process and a final answer, and these rollouts are stored as experience memory. Queries, thinking processes, and answers form nodes in a heterogeneous graph with similarity and structural edges; a GNN trained on labeled nodes propagates rewards to unlabeled rollouts during online optimization. Experiments on Qwen2.5-3B and 1.5B across mathematics, question answering, and code generation demonstrate that MemReward, with only 20% labels, achieves 97.3% of Oracle performance on 3B and 96.6% on 1.5B, surpassing Oracle on out-of-domain tasks. Performance scales smoothly with label budget, reaching 99.4% of Oracle at 70% labels.
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
