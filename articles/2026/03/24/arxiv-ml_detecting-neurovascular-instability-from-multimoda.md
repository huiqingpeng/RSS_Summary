---
title: "Detecting Neurovascular Instability from Multimodal Physiological Signals Using Wearable-Compatible Edge AI: A Responsible Computational Framework"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20442"
published: "2026-03-24"
fetched: "2026-03-25T07:09:43.128332"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Detecting Neurovascular Instability from Multimodal Physiological Signals Using Wearable-Compatible Edge AI: A Responsible Computational Framework
View PDF HTML (experimental)Abstract:We propose Melaguard, a multimodal ML framework (Transformer-lite, 1.2M parameters, 4-head self-attention) for detecting neurovascular instability (NVI) from wearable-compatible physiological signals prior to structural stroke pathology. The model fuses heart rate variability (HRV), peripheral perfusion index, SpO2, and bilateral phase coherence into a composite NVI Score, designed for edge inference (WCET <=4 ms on Cortex-M4). NVI - the pre-structural dysregulation of cerebrovascular autoregulation preceding overt stroke - remains undetectable by existing single-modality wearables. With 12.2 million incident strokes annually, continuous multimodal physiological monitoring offers a practical path to community-scale screening. Three-stage independent validation: (1) synthetic benchmark (n=10,000), AUC=0.88 [0.83-0.92]; (2) clinical cohort PhysioNet CVES (n=172; 84 stroke, 88 control) - Transformer-lite achieves AUC=0.755 [0.630-0.778], outperforming LSTM (0.643), Random Forest (0.665), SVM (0.472); HRV-SDNN discriminates stroke (p=0.011); (3) PPG pipeline PhysioNet BIDMC (n=53) -- pulse rate r=0.748 and HRV surrogate r=0.690 vs. ECG ground truth. Cross-modality validation on PPG-BP (n=219) confirms PPG morphology classifies cerebrovascular disease at AUC=0.923 [0.869-0.968]. Multimodal fusion consistently outperforms single-modality baselines. Code: this https URL
Submission history
From: Xuan Khanh Truong [view email][v1] Fri, 20 Mar 2026 19:17:46 UTC (4,021 KB)
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
