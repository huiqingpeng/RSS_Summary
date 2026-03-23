---
title: "Parameter-Efficient Token Embedding Editing for Clinical Class-Level Unlearning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19302"
published: "2026-03-23"
fetched: "2026-03-24T07:16:01.246562"
---

Computer Science > Machine Learning
[Submitted on 11 Mar 2026]
Title:Parameter-Efficient Token Embedding Editing for Clinical Class-Level Unlearning
View PDF HTML (experimental)Abstract:Machine unlearning is increasingly important for clinical language models, where privacy regulations and institutional policies may require removing sensitive information from deployed systems without retraining from scratch. In practice, deletion requests must balance effective forgetting of targeted information with preservation of model utility and minimal parameter modification. We introduce Sparse Token Embedding Unlearning (STEU), a parameter-efficient method for behavioral class-level unlearning that updates only PMI-selected token embeddings together with a small classifier head while keeping all encoder layers frozen. Across experiments on MIMIC-IV, MIMIC-III, and eICU using BioClinicalBERT, BERT-base, and DistilBERT, STEU consistently suppresses the target class while largely preserving retained task performance. In the primary MIMIC-IV setting, STEU achieves near-complete forgetting (forget F1 = 0.0004) while maintaining competitive retained utility (retain avg F1 = 0.4766) after modifying only 0.19\% of model parameters. These results suggest that targeted behavioral unlearning can be achieved through sparse embedding edits without modifying deeper encoder representations.
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
