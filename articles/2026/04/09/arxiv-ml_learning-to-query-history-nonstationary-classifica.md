---
title: "Learning to Query History: Nonstationary Classification via Learned Retrieval"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.07027"
published: "2026-04-09"
fetched: "2026-04-10T07:05:11.559692"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:Learning to Query History: Nonstationary Classification via Learned Retrieval
View PDF HTML (experimental)Abstract:Nonstationarity is ubiquitous in practical classification settings, leading deployed models to perform poorly even when they generalize well to holdout sets available at training time. We address this by reframing nonstationary classification as time series prediction: rather than predicting from the current input alone, we condition the classifier on a sequence of historical labeled examples that extends beyond the training cutoff. To scale to large sequences, we introduce a learned discrete retrieval mechanism that samples relevant historical examples via input-dependent queries, trained end-to-end with the classifier using a score-based gradient estimator. This enables the full corpus of historical data to remain on an arbitrary filesystem during training and deployment. Experiments on synthetic benchmarks and Amazon Reviews '23 (electronics category) show improved robustness to distribution shift compared to standard classifiers, with VRAM scaling predictably as the length of the historical data sequence increases.
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
