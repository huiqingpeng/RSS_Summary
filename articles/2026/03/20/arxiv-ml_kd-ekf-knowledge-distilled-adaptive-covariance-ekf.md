---
title: "KD-EKF: Knowledge-Distilled Adaptive Covariance EKF for Robust UWB/PDR Indoor Localization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18027"
published: "2026-03-20"
fetched: "2026-03-20T13:07:28.528276"
---

Electrical Engineering and Systems Science > Signal Processing
[Submitted on 6 Mar 2026]
Title:KD-EKF: Knowledge-Distilled Adaptive Covariance EKF for Robust UWB/PDR Indoor Localization
View PDF HTML (experimental)Abstract:Ultra-wideband (UWB) indoor localization provides centimeter-level accuracy and low latency, but its measurement reliability degrades severely under Non-Line-of-Sight (NLOS) conditions, leading to meter-scale ranging errors and inconsistent uncertainty characteristics. Inertial Measurement Unit (IMU)-based Pedestrian Dead Reckoning (PDR) complements UWB by providing infrastructure-free motion estimation; however, its error accumulates nonlinearly over time due to bias and noise propagation. Fusion methods based on Extended Kalman Filters (EKF) and Particle Filters (PF) can improve average localization accuracy through probabilistic state estimation. However, these approaches typically rely on manually tuned measurement covariances. Such fixed or heuristically tuned parameters are hard to sustain across varying indoor layouts, NLOS ratios, and motion patterns, leading to limited robustness and poor generalization of measurement uncertainty modeling in heterogeneous environments. To address this limitation, this work proposes an adaptive measurement covariance scaling framework in which reliability cues are learned from historical UWB/PDR trajectories. A large teacher model is employed offline to generate temporally consistent next-position predictions from structured UWB/PDR sequences, and this behavior is distilled into a lightweight student model suitable for real-time deployment. The student model continuously regulates EKF measurement covariances based on prediction residuals, enabling environment-aware fusion without manual re-tuning. Experimental results demonstrate that the proposed KD-EKF framework significantly reduces localization error, suppresses error spikes during Line-of-Sight (LOS)/NLOS transitions, and mitigates long-term drift compared to fixed-parameter EKF, thereby improving measurement robustness across diverse indoor environments.
Current browse context:
eess.SP
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
