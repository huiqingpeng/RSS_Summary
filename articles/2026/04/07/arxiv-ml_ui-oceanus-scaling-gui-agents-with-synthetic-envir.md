---
title: "UI-Oceanus: Scaling GUI Agents with Synthetic Environmental Dynamics"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.02345"
published: "2026-04-07"
fetched: "2026-04-08T07:02:33.419203"
---

Computer Science > Machine Learning
[Submitted on 11 Feb 2026]
Title:UI-Oceanus: Scaling GUI Agents with Synthetic Environmental Dynamics
View PDF HTML (experimental)Abstract:Scaling generalist GUI agents is hindered by the data scalability bottleneck of expensive human demonstrations and the "distillation ceiling" of synthetic teacher supervision. To transcend these limitations, we propose UI-Oceanus, a framework that shifts the learning focus from mimicking high-level trajectories to mastering interaction physics via ground-truth environmental feedback. Through a systematic investigation of self-supervised objectives, we identify that forward dynamics, defined as the generative prediction of future interface states, acts as the primary driver for scalability and significantly outweighs inverse inference. UI-Oceanus leverages this insight by converting low-cost autonomous exploration, which is verified directly by system execution, into high-density generative supervision to construct a robust internal world model. Experimental evaluations across a series of models demonstrate the decisive superiority of our approach: models utilizing Continual Pre-Training (CPT) on synthetic dynamics outperform non-CPT baselines with an average success rate improvement of 7% on offline benchmarks, which amplifies to a 16.8% gain in real-world online navigation. Furthermore, we observe that navigation performance scales with synthetic data volume. These results confirm that grounding agents in forward predictive modeling offers a superior pathway to scalable GUI automation with robust cross-domain adaptability and compositional generalization.
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
