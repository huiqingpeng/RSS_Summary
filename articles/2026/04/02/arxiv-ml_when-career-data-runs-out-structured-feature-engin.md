---
title: "When Career Data Runs Out: Structured Feature Engineering and Signal Limits for Founder Success Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00339"
published: "2026-04-02"
fetched: "2026-04-03T07:20:28.673750"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:When Career Data Runs Out: Structured Feature Engineering and Signal Limits for Founder Success Prediction
View PDF HTML (experimental)Abstract:Predicting startup success from founder career data is hard. The signal is weak, the labels are rare (9%), and most founders who succeed look almost identical to those who fail. We engineer 28 structured features directly from raw JSON fields -- jobs, education, exits -- and combine them with a deterministic rule layer and XGBoost boosted stumps. Our model achieves Val F0.5 = 0.3030, Precision = 0.3333, Recall = 0.2222 -- a +17.7pp improvement over the zero-shot LLM baseline. We then run a controlled experiment: extract 9 features from the prose field using Claude Haiku, at 67% and 100% dataset coverage. LLM features capture 26.4% of model importance but add zero CV signal (delta = -0.05pp). The reason is structural: anonymised_prose is generated from the same JSON fields we parse directly -- it is a lossy re-encoding, not a richer source. The ceiling (CV ~= 0.25, Val ~= 0.30) reflects the information content of this dataset, not a modeling limitation. In characterizing where the signal runs out and why, this work functions as a benchmark diagnostic -- one that points directly to what a richer dataset would need to include.
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
