---
title: "Rethinking Multimodal Fusion for Time Series: Auxiliary Modalities Need Constrained Fusion"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22372"
published: "2026-03-25"
fetched: "2026-03-26T07:13:48.732509"
---

Computer Science > Machine Learning
[Submitted on 23 Mar 2026]
Title:Rethinking Multimodal Fusion for Time Series: Auxiliary Modalities Need Constrained Fusion
View PDFAbstract:Recent advances in multimodal learning have motivated the integration of auxiliary modalities such as text or vision into time series (TS) forecasting. However, most existing methods provide limited gains, often improving performance only in specific datasets or relying on architecture-specific designs that limit generalization. In this paper, we show that multimodal models with naive fusion strategies (e.g., simple addition or concatenation) often underperform unimodal TS models, which we attribute to the uncontrolled integration of auxiliary modalities which may introduce irrelevant information. Motivated by this observation, we explore various constrained fusion methods designed to control such integration and find that they consistently outperform naive fusion methods. Furthermore, we propose Controlled Fusion Adapter (CFA), a simple plug-in method that enables controlled cross-modal interactions without modifying the TS backbone, integrating only relevant textual information aligned with TS dynamics. CFA employs low-rank adapters to filter irrelevant textual information before fusing it into temporal representations. We conduct over 20K experiments across various datasets and TS/text models, demonstrating the effectiveness of the constrained fusion methods including CFA. Code is publicly available at: this https URL.
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
