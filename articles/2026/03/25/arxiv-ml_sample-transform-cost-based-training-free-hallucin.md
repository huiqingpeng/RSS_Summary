---
title: "Sample Transform Cost-Based Training-Free Hallucination Detector for Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22303"
published: "2026-03-25"
fetched: "2026-03-26T07:08:53.879962"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Sample Transform Cost-Based Training-Free Hallucination Detector for Large Language Models
View PDF HTML (experimental)Abstract:Hallucinations in large language models (LLMs) remain a central obstacle to trustworthy deployment, motivating detectors that are accurate, lightweight, and broadly applicable. Since an LLM with a prompt defines a conditional distribution, we argue that the complexity of the distribution is an indicator of hallucination. However, the density of the distribution is unknown and the samples (i.e., responses generated for the prompt) are discrete distributions, which leads to a significant challenge in quantifying the complexity of the distribution. We propose to compute the optimal-transport distances between the sets of token embeddings of pairwise samples, which yields a Wasserstein distance matrix measuring the costs of transforming between the samples. This Wasserstein distance matrix provides a means to quantify the complexity of the distribution defined by the LLM with the prompt. Based on the Wasserstein distance matrix, we derive two complementary signals: AvgWD, measuring the average cost, and EigenWD, measuring the cost complexity. This leads to a training-free detector for hallucinations in LLMs. We further extend the framework to black-box LLMs via teacher forcing with an accessible teacher model. Experiments show that AvgWD and EigenWD are competitive with strong uncertainty baselines and provide complementary behavior across models and datasets, highlighting distribution complexity as an effective signal for LLM truthfulness.
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
