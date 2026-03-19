---
title: "Dependence Fidelity and Downstream Inference Stability in Generative Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17041"
published: "2026-03-19"
fetched: "2026-03-19T13:08:09.566985"
---

Statistics > Machine Learning
[Submitted on 17 Mar 2026]
Title:Dependence Fidelity and Downstream Inference Stability in Generative Models
View PDF HTML (experimental)Abstract:Recent advances in generative AI have led to increasingly realistic synthetic data, yet evaluation criteria remain focused on marginal distribution matching. While these diagnostics assess local realism, they provide limited insight into whether a generative model preserves the multivariate dependence structures governing downstream inference. We introduce covariance-level dependence fidelity as a practical criterion for evaluating whether a generative distribution preserves joint structure beyond univariate marginals. We establish three core results. First, distributions can match all univariate marginals exactly while exhibiting substantially different dependence structures, demonstrating marginal fidelity alone is insufficient. Second, dependence divergence induces quantitative instability in downstream inference, including sign reversals in regression coefficients despite identical marginal behavior. Third, explicit control of covariance-level dependence divergence ensures stable behavior for dependence-sensitive tasks such as principal component analysis. Synthetic constructions illustrate how dependence preservation failures lead to incorrect conclusions despite identical marginal distributions. These results highlight dependence fidelity as a useful diagnostic for evaluating generative models in dependence-sensitive downstream tasks, with implications for diffusion models and variational autoencoders. These guarantees apply specifically to procedures governed by covariance structure; tasks requiring higher-order dependence such as tail-event estimation require richer criteria.
Current browse context:
stat.ML
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
