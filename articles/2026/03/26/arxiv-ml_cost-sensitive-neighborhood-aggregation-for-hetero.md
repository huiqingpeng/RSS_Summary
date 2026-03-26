---
title: "Cost-Sensitive Neighborhood Aggregation for Heterophilous Graphs: When Does Per-Edge Routing Help?"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24291"
published: "2026-03-26"
fetched: "2026-03-27T07:22:44.327945"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Cost-Sensitive Neighborhood Aggregation for Heterophilous Graphs: When Does Per-Edge Routing Help?
View PDF HTML (experimental)Abstract:Recent work distinguishes two heterophily regimes: adversarial, where cross-class edges dilute class signal and harm classification, and informative, where the heterophilous structure itself carries useful signal. We ask: when does per-edge message routing help, and when is a uniform spectral channel sufficient? To operationalize this question we introduce Cost-Sensitive Neighborhood Aggregation (CSNA), a GNN layer that computes pairwise distance in a learned projection and uses it to soft-route each message through concordant and discordant channels with independent transformations. Under a contextual stochastic block model we show that cost-sensitive weighting preserves class-discriminative signal where mean aggregation provably attenuates it, provided $w_+/w_- > q/p$. On six benchmarks with uniform tuning, CSNA is competitive with state-of-the-art methods on adversarial-heterophily datasets (Texas, Wisconsin, Cornell, Actor) but underperforms on informative-heterophily datasets (Chameleon, Squirrel) -- precisely the regime where per-edge routing has no useful decomposition to exploit. The pattern is itself the finding: the cost function's ability to separate edge types serves as a diagnostic for the heterophily regime, revealing when fine-grained routing adds value over uniform channels and when it does not. Code is available at this https URL .
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
