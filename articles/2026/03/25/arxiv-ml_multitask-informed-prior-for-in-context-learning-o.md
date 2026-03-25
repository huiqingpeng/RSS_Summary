---
title: "Multitask-Informed Prior for In-Context Learning on Tabular Data: Application to Steel Property Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22738"
published: "2026-03-25"
fetched: "2026-03-26T07:16:55.241133"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Multitask-Informed Prior for In-Context Learning on Tabular Data: Application to Steel Property Prediction
View PDF HTML (experimental)Abstract:Accurate prediction of mechanical properties of steel during hot rolling processes, such as Thin Slab Direct Rolling (TSDR), remains challenging due to complex interactions among chemical compositions, processing parameters, and resultant microstructures. Traditional empirical and experimental methodologies, while effective, are often resource-intensive and lack adaptability to varied production conditions. Moreover, most existing approaches do not explicitly leverage the strong correlations among key mechanical properties, missing an opportunity to improve predictive accuracy through multitask learning. To address this, we present a multitask learning framework that injects multitask awareness into the prior of TabPFN--a transformer-based foundation model for in-context learning on tabular data--through novel fine-tuning strategies. Originally designed for single-target regression or classification, we augment TabPFN's prior with two complementary approaches: (i) target averaging, which provides a unified scalar signal compatible with TabPFN's single-target architecture, and (ii) task-specific adapters, which introduce task-specific supervision during fine-tuning. These strategies jointly guide the model toward a multitask-informed prior that captures cross-property relationships among key mechanical metrics. Extensive experiments on an industrial TSDR dataset demonstrate that our multitask adaptations outperform classical machine learning methods and recent state-of-the-art tabular learning models across multiple evaluation metrics. Notably, our approach enhances both predictive accuracy and computational efficiency compared to task-specific fine-tuning, demonstrating that multitask-aware prior adaptation enables foundation models for tabular data to deliver scalable, rapid, and reliable deployment for automated industrial quality control and process optimization in TSDR.
Submission history
From: Dimitrios Sinodinos [view email][v1] Tue, 24 Mar 2026 03:03:54 UTC (952 KB)
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
