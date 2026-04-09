---
title: "Frailty Estimation in Elderly Oncology Patients Using Multimodal Wearable Data and Multi-Instance Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06985"
published: "2026-04-09"
fetched: "2026-04-10T07:05:10.227809"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:Frailty Estimation in Elderly Oncology Patients Using Multimodal Wearable Data and Multi-Instance Learning
View PDF HTML (experimental)Abstract:Frailty and functional decline strongly influence treatment tolerance and outcomes in older patients with cancer, yet assessment is typically limited to infrequent clinic visits. We propose a multimodal wearable framework to estimate frailty-related functional change between visits in elderly breast cancer patients enrolled in the multicenter CARDIOCARE study. Free-living smartwatch physical activity and sleep features are combined with ECG-derived heart rate variability (HRV) features from a chest strap and organized into patient-horizon bags aligned to month 3 (M3) and month 6 (M6) follow-ups. Our innovation is an attention-based multiple instance learning (MIL) formulation that fuses irregular, multimodal wearable instances under real-world missingness and weak supervision. An attention-based MIL model with modality-specific multilayer perceptron (MLP) encoders with embedding dimension 128 aggregates variable-length and partially missing longitudinal instances to predict discretized change-from-baseline classes (worsened, stable, improved) for FACIT-F and handgrip strength. Under subject-independent leave-one-subject-out (LOSO) evaluation, the full multimodal model achieved balanced accuracy/F1 of 0.68 +/- 0.08/0.67 +/- 0.09 at M3 and 0.70 +/- 0.10/0.69 +/- 0.08 at M6 for handgrip, and 0.59 +/- 0.04/0.58 +/- 0.06 at M3 and 0.64 +/- 0.05/0.63 +/- 0.07 at M6 for FACIT-F. Ablation results indicated that smartwatch activity and sleep provide the strongest predictive information for frailty-related functional changes, while HRV contributes complementary information when fused with smartwatch streams.
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
