---
title: "A Benchmark of Classical and Deep Learning Models for Agricultural Commodity Price Forecasting on A Novel Bangladeshi Market Price Dataset"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06227"
published: "2026-04-09"
fetched: "2026-04-10T07:04:53.381527"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:A Benchmark of Classical and Deep Learning Models for Agricultural Commodity Price Forecasting on A Novel Bangladeshi Market Price Dataset
View PDF HTML (experimental)Abstract:Accurate short-term forecasting of agricultural commodity prices is critical for food security planning and smallholder income stabilisation in developing economies, yet machine-learning-ready datasets for this purpose remain scarce in South Asia. This paper makes two contributions. First, we introduce AgriPriceBD, a benchmark dataset of 1,779 daily retail mid-prices for five Bangladeshi commodities - garlic, chickpea, green chilli, cucumber, and sweet pumpkin - spanning July 2020 to June 2025, extracted from government reports via an LLM-assisted digitisation pipeline. Second, we evaluate seven forecasting approaches spanning classical models - naïve persistence, SARIMA, and Prophet - and deep learning architectures - BiLSTM, Transformer, Time2Vec-enhanced Transformer, and Informer - with Diebold-Mariano statistical significance tests. Commodity price forecastability is fundamentally heterogeneous: naïve persistence dominates on near-random-walk commodities. Time2Vec temporal encoding provides no statistically significant advantage over fixed sinusoidal encoding and causes catastrophic degradation on green chilli (+146.1% MAE, p<0.001). Prophet fails systematically, attributable to discrete step-function price dynamics incompatible with its smooth decomposition assumptions. Informer produces erratic predictions (variance up to 50x ground-truth), confirming sparse-attention Transformers require substantially larger training sets than small agricultural datasets provide. All code, models, and data are released publicly to support replication and future forecasting research on agricultural commodity markets in Bangladesh and similar developing economies.
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
