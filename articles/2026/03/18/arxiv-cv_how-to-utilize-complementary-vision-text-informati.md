---
title: "How to Utilize Complementary Vision-Text Information for 2D Structure Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16245"
published: "2026-03-18"
fetched: "2026-03-18T18:09:01.923893"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:How to Utilize Complementary Vision-Text Information for 2D Structure Understanding
View PDF HTML (experimental)Abstract:LLMs typically linearize 2D tables into 1D sequences to fit their autoregressive architecture, which weakens row-column adjacency and other layout cues. In contrast, purely visual encoders can capture spatial cues, yet often struggle to preserve exact cell text. Our analysis reveals that these two modalities provide highly distinct information to LLMs and exhibit strong complementarity. However, direct concatenation and other fusion methods yield limited gains and frequently introduce cross-modal interference. To address this issue, we propose DiVA-Former, a lightweight architecture designed to effectively integrate vision and text information. DiVA-Former leverages visual tokens as dynamic queries to distill long textual sequences into digest vectors, thereby effectively exploiting complementary vision--text information. Evaluated across 13 table benchmarks, DiVA-Former improves upon the pure-text baseline by 23.9\% and achieves consistent gains over existing baselines using visual inputs, textual inputs, or a combination of both.
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
