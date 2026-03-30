---
title: "Do Neurons Dream of Primitive Operators? Wake-Sleep Compression Rediscovers Schank's Event Semantics"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25975"
published: "2026-03-30"
fetched: "2026-03-31T07:20:21.819695"
---

Computer Science > Machine Learning
[Submitted on 26 Mar 2026]
Title:Do Neurons Dream of Primitive Operators? Wake-Sleep Compression Rediscovers Schank's Event Semantics
View PDF HTML (experimental)Abstract:We show that they do. Schank's conceptual dependency theory proposed that all events decompose into primitive operations -- ATRANS, PTRANS, MTRANS, and others -- hand-coded from linguistic intuition. Can the same primitives be discovered automatically through compression pressure alone?
We adapt DreamCoder's wake-sleep library learning to event state transformations. Given events as before/after world state pairs, our system finds operator compositions explaining each event (wake), then extracts recurring patterns as new operators optimized under Minimum Description Length (sleep). Starting from four generic primitives, it discovers operators mapping directly to Schank's: MOVE_PROP_has = ATRANS, CHANGE_location = PTRANS, SET_knows = MTRANS, SET_consumed = INGEST, plus compound operators ("mail" = ATRANS + PTRANS) and novel emotional state operators absent from Schank's taxonomy.
We validate on synthetic events and real-world commonsense data from the ATOMIC knowledge graph. On synthetic data, discovered operators achieve Bayesian MDL within 4% of Schank's hand-coded primitives while explaining 100% of events vs. Schank's 81%. On ATOMIC, results are more dramatic: Schank's primitives explain only 10% of naturalistic events, while the discovered library explains 100%. Dominant operators are not physical-action primitives but mental and emotional state changes -- CHANGE_wants (20%), CHANGE_feels (18%), CHANGE_is (18%) -- none in Schank's original taxonomy.
These results provide the first empirical evidence that event primitives can be derived from compression pressure, that Schank's core primitives are information-theoretically justified, and that the complete inventory is substantially richer than proposed -- with mental/emotional operators dominating in naturalistic data.
Current browse context:
cs.LG
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
