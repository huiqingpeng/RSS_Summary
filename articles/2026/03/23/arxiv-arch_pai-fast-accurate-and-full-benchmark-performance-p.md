---
title: "PAI: Fast, Accurate, and Full Benchmark Performance Projection with AI"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.19330"
published: "2026-03-23"
fetched: "2026-03-24T07:13:50.151774"
---

Computer Science > Hardware Architecture
[Submitted on 18 Mar 2026]
Title:PAI: Fast, Accurate, and Full Benchmark Performance Projection with AI
View PDF HTML (experimental)Abstract:The exponential increase in complex IPs within modern SoCs, driven by Moore's Law, has created a pressing need for fast and accurate hardware-software power-performance analysis. Traditional performance simulators (such as cycle accurate simulators) are often too slow to simulate full benchmarks within a reasonable timeframe; require considerable effort for development, maintenance, and extensions; and are prone to errors, making pre-silicon performance projections and competitive analysis increasingly challenging. Prior attempts in addressing this challenge using machine learning fall short as they are either slow, inaccurate or unable to predict the performance of full benchmarks. To address these limitations, we present PAI, the first technique to accurately predict full benchmark performance without relying on detailed simulation or instruction-wise encoding. At the heart of PAI is a hierarchical Long Short Term Memory (LSTM)-based model that takes a trace of microarchitecture independent features from a program execution and predicts performance metrics. We present the detailed design, implementation and evaluation of PAI. Our initial experiments showed that PAI can achieve an average IPC prediction error of 9.35% for SPEC CPU 2017 benchmark suite while taking only 2 min 57 sec for the entire suite. This prediction error is comparable to prior state-of-the-art techniques while requiring 3 orders of magnitude less time.
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
