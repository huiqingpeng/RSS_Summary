---
title: "Transformer-Based Predictive Maintenance for Risk-Aware Instrument Calibration"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20297"
published: "2026-03-24"
fetched: "2026-03-25T07:07:16.061834"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Transformer-Based Predictive Maintenance for Risk-Aware Instrument Calibration
View PDF HTML (experimental)Abstract:Accurate calibration is essential for instruments whose measurements must remain traceable, reliable, and compliant over long operating periods. Fixed-interval programs are easy to administer, but they ignore that instruments drift at different rates under different conditions. This paper studies calibration scheduling as a predictive maintenance problem: given recent sensor histories, estimate time-to-drift (TTD) and intervene before a violation occurs. We adapt the NASA C-MAPSS benchmark into a calibration setting by selecting drift-sensitive sensors, defining virtual calibration thresholds, and inserting synthetic reset events that emulate repeated recalibration. We then compare classical regressors, recurrent and convolutional sequence models, and a compact Transformer for TTD prediction. The Transformer provides the strongest point forecasts on the primary FD001 split and remains competitive on the harder FD002--FD004 splits, while a quantile-based uncertainty model supports conservative scheduling when drift behavior is noisier. Under a violation-aware cost model, predictive scheduling lowers cost relative to reactive and fixed policies, and uncertainty-aware triggers sharply reduce violations when point forecasts are less reliable. The results show that condition-based calibration can be framed as a joint forecasting and decision problem, and that combining sequence models with risk-aware policies is a practical route toward smarter calibration planning.
Submission history
From: Adithya Parthasarathy [view email][v1] Thu, 19 Mar 2026 06:32:01 UTC (739 KB)
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
