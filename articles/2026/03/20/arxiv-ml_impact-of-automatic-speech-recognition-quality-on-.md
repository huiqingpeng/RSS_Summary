---
title: "Impact of automatic speech recognition quality on Alzheimer's disease detection from spontaneous speech: a reproducible benchmark study with lexical modeling and statistical validation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18239"
published: "2026-03-20"
fetched: "2026-03-20T13:10:46.682435"
---

Quantitative Biology > Quantitative Methods
[Submitted on 18 Mar 2026]
Title:Impact of automatic speech recognition quality on Alzheimer's disease detection from spontaneous speech: a reproducible benchmark study with lexical modeling and statistical validation
View PDF HTML (experimental)Abstract:Early detection of Alzheimer's disease from spontaneous speech has emerged as a promising non-invasive screening approach. However, the influence of automatic speech recognition (ASR) quality on downstream clinical language modeling remains insufficiently understood. In this study, we investigate Alzheimer's disease detection using lexical features derived from Whisper ASR transcripts on the ADReSSo 2021 diagnosis dataset. We evaluate interpretable machine-learning models, including Logistic Regression and Linear Support Vector Machines, using TF-IDF text representations under repeated 5x5 stratified cross-validation.
Our results demonstrate that transcript quality has a statistically significant impact on classification performance. Models trained on Whisper-small transcripts consistently outperform those using Whisper-base transcripts, achieving balanced accuracy above 0.7850 with Linear SVM. Paired statistical testing confirms that the observed improvements are significant. Importantly, classifier complexity contributes less to performance variation than ASR transcription quality. Feature analysis reveals that cognitively normal speakers produce more semantically precise object- and scene-descriptive language, whereas Alzheimer's speech is characterized by vagueness, discourse markers, and increased hesitation patterns.
These findings suggest that high-quality ASR can enable simple, interpretable lexical models to achieve competitive Alzheimer's detection performance without explicit acoustic modeling. The study provides a reproducible benchmark pipeline and highlights ASR selection as a critical modeling decision in clinical speech-based artificial intelligence systems.
Current browse context:
q-bio.QM
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
