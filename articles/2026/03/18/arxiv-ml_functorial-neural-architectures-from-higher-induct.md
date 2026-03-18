---
title: "Functorial Neural Architectures from Higher Inductive Types"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16123"
published: "2026-03-18"
fetched: "2026-03-18T15:40:30.682216"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Functorial Neural Architectures from Higher Inductive Types
View PDF HTML (experimental)Abstract:Neural networks systematically fail at compositional generalization -- producing correct outputs for novel combinations of known parts. We show that this failure is architectural: compositional generalization is equivalent to functoriality of the decoder, and this perspective yields both guarantees and impossibility results. We compile Higher Inductive Type (HIT) specifications into neural architectures via a monoidal functor from the path groupoid of a target space to a category of parametric maps: path constructors become generator networks, composition becomes structural concatenation, and 2-cells witnessing group relations become learned natural transformations. We prove that decoders assembled by structural concatenation of independently generated segments are strict monoidal functors (compositional by construction), while softmax self-attention is not functorial for any non-trivial compositional task. Both results are formalized in Cubical Agda. Experiments on three spaces validate the full hierarchy: on the torus ($\mathbb{Z}^2$), functorial decoders outperform non-functorial ones by 2-2.7x; on $S^1 \vee S^1$ ($F_2$), the type-A/B gap widens to 5.5-10x; on the Klein bottle ($\mathbb{Z} \rtimes \mathbb{Z}$), a learned 2-cell closes a 46% error gap on words exercising the group relation.
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
