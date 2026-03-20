---
title: "Pi-transformer: A prior-informed dual-attention model for multivariate time-series anomaly detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.19985"
published: "2026-03-20"
fetched: "2026-03-20T14:07:23.153899"
---

Computer Science > Machine Learning
[Submitted on 24 Sep 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Pi-transformer: A prior-informed dual-attention model for multivariate time-series anomaly detection
View PDF HTML (experimental)Abstract:Anomalies in multivariate time series often arise from temporal context and cross-channel coordination rather than isolated outliers. We present Pi-Transformer (Prior-Informed Transformer), a transformer with two attention pathways: data-driven series attention and a smoothly evolving prior attention that encodes temporal invariants such as scale-related self-similarity and phase synchrony. The prior provides an amplitude-insensitive temporal reference that calibrates reconstruction error. During training, we pair a reconstruction objective with a divergence term that encourages agreement between the two attentions while keeping them meaningfully distinct. The prior is regularised to evolve smoothly and is lightly distilled towards dataset-level statistics. At inference, the model combines an alignment-weighted reconstruction signal (Energy) with a mismatch signal that highlights timing and phase disruptions, and fuses them into a single score for detection. Across five benchmarks (SMD, MSL, SMAP, SWaT, and PSM), Pi-Transformer achieves state-of-the-art or highly competitive F1, with particular strength on timing and phase-breaking anomalies. Case analyses show complementary behaviour of the two streams and interpretable detections around regime changes. Embedding prior attention into transformer scoring yields a calibrated and robust approach to anomaly detection in complex multivariate systems.
Submission history
From: Sepehr Maleki [view email][v1] Wed, 24 Sep 2025 10:47:48 UTC (354 KB)
[v2] Thu, 19 Mar 2026 11:27:00 UTC (840 KB)
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
