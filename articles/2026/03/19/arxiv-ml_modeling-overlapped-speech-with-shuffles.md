---
title: "Modeling Overlapped Speech with Shuffles"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17769"
published: "2026-03-19"
fetched: "2026-03-19T13:15:10.782571"
---

Computer Science > Sound
[Submitted on 18 Mar 2026]
Title:Modeling Overlapped Speech with Shuffles
View PDF HTML (experimental)Abstract:We propose to model parallel streams of data, such as overlapped speech, using shuffles. Specifically, this paper shows how the shuffle product and partial order finite-state automata (FSAs) can be used for alignment and speaker-attributed transcription of overlapped speech. We train using the total score on these FSAs as a loss function, marginalizing over all possible serializations of overlapping sequences at subword, word, and phrase levels. To reduce graph size, we impose temporal constraints by constructing partial order FSAs. We address speaker attribution by modeling (token, speaker) tuples directly. Viterbi alignment through the shuffle product FSA directly enables one-pass alignment. We evaluate performance on synthetic LibriSpeech overlaps. To our knowledge, this is the first algorithm that enables single-pass alignment of multi-talker recordings. All algorithms are implemented using k2 / Icefall.
Current browse context:
cs.SD
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
