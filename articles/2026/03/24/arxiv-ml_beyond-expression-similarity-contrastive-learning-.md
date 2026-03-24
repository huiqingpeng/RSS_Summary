---
title: "Beyond Expression Similarity: Contrastive Learning Recovers Functional Gene Associations from Protein Interaction Structure"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20955"
published: "2026-03-24"
fetched: "2026-03-25T07:16:22.438656"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Beyond Expression Similarity: Contrastive Learning Recovers Functional Gene Associations from Protein Interaction Structure
View PDF HTML (experimental)Abstract:The Predictive Associative Memory (PAM) framework posits that useful relationships often connect items that co-occur in shared contexts rather than items that appear similar in embedding space. A contrastive MLP trained on co-occurrence annotations--Contrastive Association Learning (CAL)--has improved multi-hop passage retrieval and discovered narrative function at corpus scale in text. We test whether this principle transfers to molecular biology, where protein-protein interactions provide functional associations distinct from gene expression similarity. Four experiments across two biological domains map the operating envelope. On gene perturbation data (Replogle K562 CRISPRi, 2,285 genes), CAL trained on STRING protein interactions achieves cross-boundary AUC of 0.908 where expression similarity scores 0.518. A second gene dataset (DepMap, 17,725 genes) confirms the result after negative sampling correction, reaching cross-boundary AUC of 0.947. Two drug sensitivity experiments produce informative negatives that sharpen boundary conditions. Three cross-domain findings emerge: (1) inductive transfer succeeds in biology--a node-disjoint split with unseen genes yields AUC 0.826 (Delta +0.127)--where it fails in text (+/-0.10), suggesting physically grounded associations are more transferable than contingent co-occurrences; (2) CAL scores anti-correlate with interaction degree (Spearman r = -0.590), with gains concentrating on understudied genes with focused interaction profiles; (3) tighter association quality outperforms larger but noisier training sets, reversing the text pattern. Results are stable across training seeds (SD < 0.001) and cross-boundary threshold choices.
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
