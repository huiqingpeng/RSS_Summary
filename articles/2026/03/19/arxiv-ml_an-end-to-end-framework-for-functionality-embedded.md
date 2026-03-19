---
title: "An End-to-End Framework for Functionality-Embedded Provenance Graph Construction and Threat Interpretation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17100"
published: "2026-03-19"
fetched: "2026-03-19T13:08:49.995904"
---

Computer Science > Cryptography and Security
[Submitted on 17 Mar 2026]
Title:An End-to-End Framework for Functionality-Embedded Provenance Graph Construction and Threat Interpretation
View PDF HTML (experimental)Abstract:Provenance graphs model causal system-level interactions from logs, enabling anomaly detectors to learn normal behavior and detect deviations as attacks. However, existing approaches rely on brittle, manually engineered rules to build provenance graphs, lack functional context for system entities, and provide limited support for analyst investigation. We present Auto-Prov, an adaptive, end-to-end framework that leverages large language models (LLMs) to automatically construct provenance graphs from heterogeneous and evolving logs, embed system-level functional attributes into the graph, enable provenance graph-based anomaly detectors to learn from these enriched graphs, and summarize the detected attacks to assist an analyst's investigation. Auto-Prov clusters unseen log types and efficiently extracts provenance edges and entity-level information via automatically generated rules. It further infers system-level functional context for both known and previously unseen system entities using a combination of LLM inference and behavior-based estimation. Attacks detected by provenance-graph-based anomaly detectors trained on Auto-Prov's graphs are then summarized into natural-language text. We evaluate Auto-Prov with four state-of-the-art provenance graph-based detectors across diverse logs. Results show that Auto-Prov consistently enhances detection performance, generalizes across heterogeneous log formats, and produces stable, interpretable attack summaries that remain robust under system evolution.
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
