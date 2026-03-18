---
title: "Revisiting ASR Error Correction with Specialized Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2405.15216"
published: "2026-03-18"
fetched: "2026-03-18T16:16:12.708666"
---

Computer Science > Machine Learning
[Submitted on 24 May 2024 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:Revisiting ASR Error Correction with Specialized Models
View PDF HTML (experimental)Abstract:Language models play a central role in automatic speech recognition (ASR), yet most methods rely on text-only models unaware of ASR error patterns. Recently, large language models (LLMs) have been applied to ASR correction, but introduce latency and hallucination concerns. We revisit ASR error correction with compact seq2seq models, trained on ASR errors from real and synthetic audio. To scale training, we construct synthetic corpora via cascaded TTS and ASR, finding that matching the diversity of realistic error distributions is key. We propose correction-first decoding, where the correction model generates candidates rescored using ASR acoustic scores. With 15x fewer parameters than LLMs, our model achieves 1.5/3.3% WER on LibriSpeech test-clean/other, outperforms LLMs, generalizes across ASR architectures (CTC, Seq2seq, Transducer) and diverse domains, and provides precise corrections in the low-error regime where LLMs struggle.
Submission history
From: Zijin Gu [view email][v1] Fri, 24 May 2024 05:05:12 UTC (523 KB)
[v2] Mon, 16 Mar 2026 22:44:21 UTC (14,176 KB)
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
