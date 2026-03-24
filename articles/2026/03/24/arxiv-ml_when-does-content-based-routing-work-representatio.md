---
title: "When Does Content-Based Routing Work? Representation Requirements for Selective Attention in Hybrid Sequence Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20997"
published: "2026-03-24"
fetched: "2026-03-25T07:17:29.342552"
---

Computer Science > Machine Learning
[Submitted on 22 Mar 2026]
Title:When Does Content-Based Routing Work? Representation Requirements for Selective Attention in Hybrid Sequence Models
View PDF HTML (experimental)Abstract:We identify a routing paradox in hybrid recurrent-attention architectures: content-based routing - deciding which tokens deserve expensive attention - requires exactly the pairwise computation that routing is designed to avoid. Through 20+ controlled experiments across three tasks (a synthetic diagnostic, the Zoology MQAR benchmark, and HotpotQA), we map the routing landscape exhaustively. One layer of softmax attention creates a latent ~34-dimensional subspace enabling 98.4% routing precision; zero layers yield 1.2%. This subspace is invisible to cosine similarity, destroyed by random projections (98.4% to 2.6%), and cannot be created by contrastive pretraining - proving attention's role is writing pairwise match results into representations, not merely computing them. Twelve alternative mechanisms all cluster at 15-29%. Non-learned indices (Bloom filter: 90.9%; BM25 on HotpotQA: 82.7%) bypass the bottleneck entirely. The result is a sharp two-regime hierarchy with an empty middle ground. These findings provide the mechanistic explanation for the empirical observation that recurrent models fail at associative recall, and reframe attention as a representation constructor rather than merely a computation mechanism.
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
