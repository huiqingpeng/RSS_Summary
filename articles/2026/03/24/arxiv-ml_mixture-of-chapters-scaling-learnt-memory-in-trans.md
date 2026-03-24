---
title: "Mixture of Chapters: Scaling Learnt Memory in Transformers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.21096"
published: "2026-03-24"
fetched: "2026-03-25T07:18:42.599919"
---

Computer Science > Machine Learning
[Submitted on 22 Mar 2026]
Title:Mixture of Chapters: Scaling Learnt Memory in Transformers
View PDF HTML (experimental)Abstract:Transformers lack an explicit architectural mechanism for storing and organizing knowledge acquired during training. We introduce learnable sparse memory banks: a set of latent tokens, randomly initialized and trained end-to-end, that transformer layers query via cross-attention to retrieve stored knowledge. To scale memory capacity without prohibitive attention costs, we propose chapter-based routing inspired by Mixture-of-Experts architectures, partitioning the memory bank into chapters and training a router to select relevant subsets per input. This enables scaling to 262K memory tokens while maintaining tractable computation. We evaluate our approach against standard transformers (in iso-FLOP settings) on pre-training and instruction fine-tuning across relevant benchmarks. Our models surpass iso-FLOP baselines suggesting scope for a new axis of scaling, demonstrating that explicit associative memory provides complementary capacity to what is captured implicitly in model parameters. Additionally, we observe improved knowledge retention under continued training, with robustness to forgetting when transitioning between training phases (e.g., pretraining to instruction fine-tuning).
Submission history
From: Tasmay Pankaj Tibrewal [view email][v1] Sun, 22 Mar 2026 07:16:58 UTC (118 KB)
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
