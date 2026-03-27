---
title: "Causal AI For AMS Circuit Design: Interpretable Parameter Effects Analysis"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.24618"
published: "2026-03-27"
fetched: "2026-03-28T07:06:20.811032"
---

Computer Science > Hardware Architecture
[Submitted on 24 Mar 2026]
Title:Causal AI For AMS Circuit Design: Interpretable Parameter Effects Analysis
View PDF HTML (experimental)Abstract:Analog-mixed-signal (AMS) circuits are highly non-linear and operate on continuous real-world signals, making them far more difficult to model with data-driven AI than digital blocks. To close the gap between structured design data (device dimensions, bias voltages, etc.) and real-world performance, we propose a causal-inference framework that first discovers a directed-acyclic graph (DAG) from SPICE simulation data and then quantifies parameter impact through Average Treatment Effect (ATE) estimation. The approach yields human-interpretable rankings of design knobs and explicit 'what-if' predictions, enabling designers to understand trade-offs in sizing and topology. We evaluate the pipeline on three operational-amplifier families (OTA, telescopic, and folded-cascode) implemented in TSMC 65nm and benchmark it against a baseline neural-network (NN) regressor. Across all circuits the causal model reproduces simulation-based ATEs with an average absolute error of less than 25%, whereas the neural network deviates by more than 80% and frequently predicts the wrong sign. These results demonstrate that causal AI provides both higher accuracy and explainability, paving the way for more efficient, trustworthy AMS design automation.
Current browse context:
cs.AR
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
