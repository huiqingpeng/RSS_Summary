---
title: "Bayesian Learning in Episodic Zero-Sum Games"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20604"
published: "2026-03-24"
fetched: "2026-03-25T07:12:10.540806"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Bayesian Learning in Episodic Zero-Sum Games
View PDFAbstract:We study Bayesian learning in episodic, finite-horizon zero-sum Markov games with unknown transition and reward models. We investigate a posterior algorithm in which each player maintains a Bayesian posterior over the game model, independently samples a game model at the beginning of each episode, and computes an equilibrium policy for the sampled model. We analyze two settings: (i) Both players use the posterior sampling algorithm, and (ii) Only one player uses posterior sampling while the opponent follows an arbitrary learning algorithm. In each setting, we provide guarantees on the expected regret of the posterior sampling agent. Our notion of regret compares the expected total reward of the learning agent against the expected total reward under equilibrium policies of the true game. Our main theoretical result is an expected regret bound for the posterior sampling agent of order $O(HS\sqrt{ABHK\log(SABHK)})$ where $K$ is the number of episodes, $H$ is the episode length, $S$ is the number of states, and $A,B$ are the action space sizes of the two players. Experiments in a grid-world predator--prey domain illustrate the sublinear regret scaling and show that posterior sampling competes favorably with a fictitious-play baseline.
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
