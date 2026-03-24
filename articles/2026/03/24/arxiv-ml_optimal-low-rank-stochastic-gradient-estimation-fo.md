---
title: "Optimal low-rank stochastic gradient estimation for LLM training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20632"
published: "2026-03-24"
fetched: "2026-03-25T07:12:29.426027"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Optimal low-rank stochastic gradient estimation for LLM training
View PDF HTML (experimental)Abstract:Large language model (LLM) training is often bottlenecked by memory constraints and stochastic gradient noise in extremely high-dimensional parameter spaces. Motivated by empirical evidence that many LLM gradient matrices are effectively low-rank during training, we present an unbiased, memory-efficient, low-rank matrix estimator with the lowest variance that is applicable across common stochastic gradient estimation paradigms. The core idea is to project a high-dimensional stochastic gradient estimator onto a random low-dimensional subspace and lift it back, reducing memory while keeping the estimator unbiased and controlling mean-squared error via an optimally designed projection distribution, including Haar--Stiefel projections. The projection distribution is derived by solving a constrained functional optimization problem, yielding an optimal random projector that guides algorithm design. Empirically, the resulting low-rank gradient estimators deliver both practical memory savings and improved training behavior. In RoBERTa-large fine-tuning, our method attains the lowest peak GPU memory among compared methods (e.g., 3.83GB versus 16.7GB for full BP) while remaining competitive in accuracy; in autoregressive LLM pretraining (LLaMA-20M/60M/100M), our method outperforms the traditional methods, supporting the benefit of the proposed optimal projection strategy.
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
