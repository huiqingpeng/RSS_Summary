---
title: "Why not to use Cosine Similarity between Label Representations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29488"
published: "2026-04-01"
fetched: "2026-04-02T07:18:37.434470"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Why not to use Cosine Similarity between Label Representations
View PDF HTML (experimental)Abstract:Cosine similarity is often used to measure the similarity of vectors. These vectors might be the representations of neural network models. However, it is not guaranteed that cosine similarity of model representations will tell us anything about model behaviour. In this paper we show that when using a softmax classifier, be it an image classifier or an autoregressive language model, measuring the cosine similarity between label representations (called unembeddings in the paper) does not give any information on the probabilities assigned by the model. Specifically, we prove that for any softmax classifier model, given two label representations, it is possible to make another model which gives the same probabilities for all labels and inputs, but where the cosine similarity between the representations is now either 1 or -1. We give specific examples of models with very high or low cosine simlarity between representations and show how to we can make equivalent models where the cosine similarity is now -1 or 1. This translation ambiguity can be fixed by centering the label representations, however, labels with representations with low cosine similarity can still have high probability for the same inputs. Fixing the length of the representations still does not give a guarantee that high(or low) cosine similarity will give high(or low) probability to the labels for the same inputs. This means that when working with softmax classifiers, cosine similarity values between label representations should not be used to explain model probabilities.
Submission history
From: Beatrix Miranda Ginn Nielsen [view email][v1] Tue, 31 Mar 2026 09:33:12 UTC (177 KB)
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
