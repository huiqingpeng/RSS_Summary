---
title: "Forecasting with Guidance: Representation-Level Supervision for Time Series Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24262"
published: "2026-03-26"
fetched: "2026-03-27T07:22:24.262843"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Forecasting with Guidance: Representation-Level Supervision for Time Series Forecasting
View PDF HTML (experimental)Abstract:Nowadays, time series forecasting is predominantly approached through the end-to-end training of deep learning architectures using error-based objectives. While this is effective at minimizing average loss, it encourages the encoder to discard informative yet extreme patterns. This results in smooth predictions and temporal representations that poorly capture salient dynamics. To address this issue, we propose ReGuider, a plug-in method that can be seamlessly integrated into any forecasting architecture. ReGuider leverages pretrained time series foundation models as semantic teachers. During training, the input sequence is processed together by the target forecasting model and the pretrained model. Rather than using the pretrained model's outputs directly, we extract its intermediate embeddings, which are rich in temporal and semantic information, and align them with the target model's encoder embeddings through representation-level supervision. This alignment process enables the encoder to learn more expressive temporal representations, thereby improving the accuracy of downstream forecasting. Extensive experimentation across diverse datasets and architectures demonstrates that our ReGuider consistently improves forecasting performance, confirming its effectiveness and versatility.
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
