---
title: "HEP Statistical Inference for UAV Fault Detection: CLs, LRT, and SBI Applied to Blade Damage"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18546"
published: "2026-03-20"
fetched: "2026-03-20T12:13:03.059043"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:HEP Statistical Inference for UAV Fault Detection: CLs, LRT, and SBI Applied to Blade Damage
View PDF HTML (experimental)Abstract:This paper transfers three statistical methods from particle physics to multirotor propeller fault detection: the likelihood ratio test (LRT) for binary detection, the CLs modified frequentist method for false alarm rate control, and sequential neural posterior estimation (SNPE) for quantitative fault characterization. Operating on spectral features tied to rotor harmonic physics, the system returns three outputs: binary detection, controlled false alarm rates, and calibrated posteriors over fault severity and motor location. On UAV-FD, a hexarotor dataset of 18 real flights with 5% and 10% blade damage, leave-one-flight-out cross-validation gives AUC 0.862 +/- 0.007 (95% CI: 0.849--0.876), outperforming CUSUM (0.708 +/- 0.010), autoencoder (0.753 +/- 0.009), and LSTM autoencoder (0.551). At 5% false alarm rate the system detects 93% of significant and 81% of subtle blade damage. On PADRE, a quadrotor platform, AUC reaches 0.986 after refitting only the generative models. SNPE gives a full posterior over fault severity (90% credible interval coverage 92--100%, MAE 0.012), so the output includes uncertainty rather than just a point estimate or fault flag. Per-flight sequential detection achieves 100% fault detection with 94% overall accuracy.
Submission history
From: Khushiyant Chauhan [view email][v1] Thu, 19 Mar 2026 07:01:09 UTC (592 KB)
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
