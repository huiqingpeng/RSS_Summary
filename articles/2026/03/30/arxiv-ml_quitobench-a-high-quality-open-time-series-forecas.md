---
title: "QuitoBench: A High-Quality Open Time Series Forecasting Benchmark"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26017"
published: "2026-03-30"
fetched: "2026-03-31T07:20:32.878312"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:QuitoBench: A High-Quality Open Time Series Forecasting Benchmark
View PDF HTML (experimental)Abstract:Time series forecasting is critical across finance, healthcare, and cloud computing, yet progress is constrained by a fundamental bottleneck: the scarcity of large-scale, high-quality benchmarks. To address this gap, we introduce \textsc{QuitoBench}, a regime-balanced benchmark for time series forecasting with coverage across eight trend$\times$seasonality$\times$forecastability (TSF) regimes, designed to capture forecasting-relevant properties rather than application-defined domain labels. The benchmark is built upon \textsc{Quito}, a billion-scale time series corpus of application traffic from Alipay spanning nine business domains. Benchmarking 10 models from deep learning, foundation models, and statistical baselines across 232,200 evaluation instances, we report four key findings: (i) a context-length crossover where deep learning models lead at short context ($L=96$) but foundation models dominate at long context ($L \ge 576$); (ii) forecastability is the dominant difficulty driver, producing a $3.64 \times$ MAE gap across regimes; (iii) deep learning models match or surpass foundation models at $59 \times$ fewer parameters; and (iv) scaling the amount of training data provides substantially greater benefit than scaling model size for both model families. These findings are validated by strong cross-benchmark and cross-metric consistency. Our open-source release enables reproducible, regime-aware evaluation for time series forecasting research.
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
