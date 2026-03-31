---
title: "A Tight Expressivity Hierarchy for GNN-Based Entity Resolution in Master Data Management"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27154"
published: "2026-03-31"
fetched: "2026-04-01T07:22:12.654544"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:A Tight Expressivity Hierarchy for GNN-Based Entity Resolution in Master Data Management
View PDF HTML (experimental)Abstract:Entity resolution -- identifying database records that refer to the same real-world entity -- is naturally modelled on bipartite graphs connecting entity nodes to their attribute values. Applying a message-passing neural network (MPNN) with all available extensions (reverse message passing, port numbering, ego IDs) incurs unnecessary overhead, since different entity resolution tasks have fundamentally different complexity. For a given matching criterion, what is the cheapest MPNN architecture that provably works?
We answer this with a four-theorem separation theory on typed entity-attribute graphs. We introduce co-reference predicates $\mathrm{Dup}_r$ (two same-type entities share at least $r$ attribute values) and the $\ell$-cycle predicate $\mathrm{Cyc}_\ell$ for settings with entity-entity edges. For each predicate we prove tight bounds -- constructing graph pairs provably indistinguishable by every MPNN lacking the required adaptation, and exhibiting explicit minimal-depth MPNNs that compute the predicate on all inputs.
The central finding is a sharp complexity gap between detecting any shared attribute and detecting multiple shared attributes. The former is purely local, requiring only reverse message passing in two layers. The latter demands cross-attribute identity correlation -- verifying that the same entity appears at several attributes of the target -- a fundamentally non-local requirement needing ego IDs and four layers, even on acyclic bipartite graphs. A similar necessity holds for cycle detection. Together, these results yield a minimal-architecture principle: practitioners can select the cheapest sufficient adaptation set, with a guarantee that no simpler architecture works. Computational validation confirms every prediction.
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
