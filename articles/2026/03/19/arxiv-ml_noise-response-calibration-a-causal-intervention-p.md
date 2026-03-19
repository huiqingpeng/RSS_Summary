---
title: "Noise-Response Calibration: A Causal Intervention Protocol for LLM-Judges"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17172"
published: "2026-03-19"
fetched: "2026-03-19T12:08:12.062398"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Noise-Response Calibration: A Causal Intervention Protocol for LLM-Judges
View PDF HTML (experimental)Abstract:Large language models (LLMs) are increasingly used as automated judges and synthetic labelers, especially in low-label settings. Yet these systems are stochastic and often overconfident, which makes deployment decisions difficult when external ground truth is limited. We propose a practical calibration protocol based on controlled input interventions: if noise severity increases, task performance should exhibit a statistically significant deterioration trend. We operationalize this with a slope-based hypothesis test over repeated trials, using signal-to-noise-ratio (SNR) perturbations for tabular data and lexical perturbations for text data. Across UCI tabular benchmarks and four text classification datasets, we find clear modality-dependent behavior. Our results reveal a modality gap: while text-based judges degrade predictably, the majority of tabular datasets show a lack of statistically significant performance deterioration even under significant signal-to-noise reduction. Interestingly we find that model performance is lower on datasets that are insensitive to noise interventions. We present a reproducible methodology and reporting protocol for robust LLM-judge calibration under distribution shift.
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
