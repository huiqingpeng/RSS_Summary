---
title: "Knowledge Localization in Mixture-of-Experts LLMs Using Cross-Lingual Inconsistency"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17102"
published: "2026-03-19"
fetched: "2026-03-19T13:08:59.607759"
---

Computer Science > Computation and Language
[Submitted on 17 Mar 2026]
Title:Knowledge Localization in Mixture-of-Experts LLMs Using Cross-Lingual Inconsistency
View PDF HTML (experimental)Abstract:Modern LLMs continue to exhibit significant variance in behavior across languages, such as being able to recall factual information in some languages but not others. While typically studied as a problem to be mitigated, in this work, we propose leveraging this cross-lingual inconsistency as a tool for interpretability in mixture-of-experts (MoE) LLMs. Our knowledge localization framework contrasts routing for sets of languages where the model correctly recalls information from languages where it fails. This allows us to isolate model components that play a functional role in answering about a piece of knowledge. Our method proceeds in two stages: (1) querying the model with difficult factual questions across a diverse set of languages to generate "success" and "failure" activation buckets and then (2) applying a statistical contrastive analysis to the MoE router logits to identify experts important for knowledge. To validate the necessity of this small number of experts for answering a knowledge question, we deactivate them and re-ask the question. We find that despite only deactivating about 20 out of 6000 experts, the model no longer answers correctly in over 40% of cases. Generally, this method provides a realistic and scalable knowledge localization approach to address increasingly complex LLMs.
Current browse context:
cs.CL
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
