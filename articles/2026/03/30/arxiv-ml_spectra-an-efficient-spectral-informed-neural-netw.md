---
title: "SPECTRA: An Efficient Spectral-Informed Neural Network for Sensor-Based Activity Recognition"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26482"
published: "2026-03-30"
fetched: "2026-03-31T07:24:45.427905"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:SPECTRA: An Efficient Spectral-Informed Neural Network for Sensor-Based Activity Recognition
View PDF HTML (experimental)Abstract:Real time sensor based applications in pervasive computing require edge deployable models to ensure low latency privacy and efficient interaction. A prime example is sensor based human activity recognition where models must balance accuracy with stringent resource constraints. Yet many deep learning approaches treat temporal sensor signals as black box sequences overlooking spectral temporal structure while demanding excessive computation. We present SPECTRA a deployment first co designed spectral temporal architecture that integrates short time Fourier transform STFT feature extraction depthwise separable convolutions and channel wise self attention to capture spectral temporal dependencies under real edge runtime and memory constraints. A compact bidirectional GRU with attention pooling summarizes within window dynamics at low cost reducing downstream model burden while preserving accuracy. Across five public HAR datasets SPECTRA matches or approaches larger CNN LSTM and Transformer baselines while substantially reducing parameters latency and energy. Deployments on a Google Pixel 9 smartphone and an STM32L4 microcontroller further demonstrate end to end deployable realtime private and efficient HAR.
Submission history
From: Lala Shakti Swarup Ray [view email][v1] Fri, 27 Mar 2026 14:45:27 UTC (374 KB)
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
