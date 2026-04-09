---
title: "Information as Structural Alignment: A Dynamical Theory of Continual Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.07108"
published: "2026-04-09"
fetched: "2026-04-10T07:05:13.788344"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:Information as Structural Alignment: A Dynamical Theory of Continual Learning
View PDF HTML (experimental)Abstract:Catastrophic forgetting is not an engineering failure. It is a mathematical consequence of storing knowledge as global parameter superposition. Existing methods, such as regularization, replay, and frozen subnetworks, add external mechanisms to a shared-parameter substrate. None derives retention from the learning dynamics themselves.
This paper introduces the Informational Buildup Framework (IBF), an alternative substrate for continual learning, based on the premise that information is the achievement of structural alignment rather than stored content. In IBF, two equations govern the dynamics: a Law of Motion that drives configuration toward higher coherence, and Modification Dynamics that persistently deform the coherence landscape in response to localized discrepancies. Memory, agency, and self-correction arise from these dynamics rather than being added as separate modules.
We first demonstrate the full lifecycle in a transparent two-dimensional toy model, then validate across three domains: a controlled non-stationary world, chess evaluated independently by Stockfish, and Split-CIFAR-100 with a frozen ViT encoder. Across all three, IBF achieves replay-superior retention without storing raw data. We observe near-zero forgetting on CIFAR-100 (BT = -0.004), positive backward transfer in chess (+38.5 cp), and 43% less forgetting than replay in the controlled domain. In chess, the framework achieves a mean behavioral advantage of +88.9 +/- 2.8 cp under independent evaluation, exceeding MLP and replay baselines.
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
