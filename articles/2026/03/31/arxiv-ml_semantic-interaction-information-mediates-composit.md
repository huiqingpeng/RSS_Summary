---
title: "Semantic Interaction Information mediates compositional generalization in latent space"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27134"
published: "2026-03-31"
fetched: "2026-04-01T07:21:44.741339"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:Semantic Interaction Information mediates compositional generalization in latent space
View PDF HTML (experimental)Abstract:Are there still barriers to generalization once all relevant variables are known? We address this question via a framework that casts compositional generalization as a variational inference problem over latent variables with parametric interactions. To explore this, we develop the Cognitive Gridworld, a stationary Partially Observable Markov Decision Process (POMDP) where observations are generated jointly by multiple latent variables, yet feedback is provided for only a single goal variable. This setting allows us to define Semantic Interaction Information (SII): a metric measuring the contribution of latent variable interactions to task performance. Using SII, we analyze Recurrent Neural Networks (RNNs) provided with these interactions, finding that SII explains the accuracy gap between Echo State and Fully Trained networks. Our analysis also uncovers a theoretically predicted failure mode where confidence decouples from accuracy, suggesting that utilizing interactions between relevant variables is a non-trivial capability.
We then address a harder regime where the interactions must be learned by an embedding model. Learning how latent variables interact requires accurate inference, yet accurate inference depends on knowing those interactions. The Cognitive Gridworld reveals this circular dependence as a core challenge for continual meta-learning. We approach this dilemma via Representation Classification Chains (RCCs), a JEPA-style architecture that disentangles these processes: variable inference and variable embeddings are learned by separate modules through Reinforcement Learning and self-supervised learning, respectively. Lastly, we demonstrate that RCCs facilitate compositional generalization to novel combinations of relevant variables. Together, these results establish a grounded setting for evaluating goal-directed generalist agents.
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
