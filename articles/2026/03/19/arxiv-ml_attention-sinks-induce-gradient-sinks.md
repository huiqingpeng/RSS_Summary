---
title: "Attention Sinks Induce Gradient Sinks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17771"
published: "2026-03-19"
fetched: "2026-03-19T12:16:18.245270"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Attention Sinks Induce Gradient Sinks
View PDF HTML (experimental)Abstract:Attention sinks and massive activations are recurring and closely related phenomena in Transformer models. Existing studies have largely focused on the forward pass, making it unclear whether their connection is direct or mediated by a training-time mechanism. We study this question from the perspective of backpropagation. Empirically and theoretically, we show that under causal mask, attention sinks can induce pronounced gradient concentration, which we term gradient sinks. Furthermore, in pre-norm architectures with RMSNorm, massive activations can be understood as an adaptive response to this localized gradient pressure during training. To test this hypothesis, we introduce V-scale, a modification that adjusts value-path backpropagated gradients. In pretrained V-scale models, attention sinks are preserved whereas massive activations are suppressed. These results support the interpretation that gradient sink is a key training-time mediator linking attention sinks and massive activations.
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
