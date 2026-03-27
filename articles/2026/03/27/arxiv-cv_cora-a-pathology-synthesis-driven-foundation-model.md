---
title: "CORA: A Pathology Synthesis Driven Foundation Model for Coronary CT Angiography Analysis and MACE Risk Assessment"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24847"
published: "2026-03-27"
fetched: "2026-03-28T07:17:43.406088"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:CORA: A Pathology Synthesis Driven Foundation Model for Coronary CT Angiography Analysis and MACE Risk Assessment
View PDF HTML (experimental)Abstract:Coronary artery disease, the leading cause of cardiovascular mortality worldwide, can be assessed non-invasively by coronary computed tomography angiography (CCTA). Despite progress in automated CCTA analysis using deep learning, clinical translation is constrained by the scarcity of expert-annotated datasets. Furthermore, widely adopted label-free pretraining strategies, such as masked image modeling, are intrinsically biased toward global anatomical statistics, frequently failing to capture the spatially localized pathological features of coronary plaques. Here, we introduce CORA, a 3D vision foundation model for comprehensive cardiovascular risk assessment. CORA learns directly from volumetric CCTA via a pathology-centric, synthesis-driven self-supervised framework. By utilizing an anatomy-guided lesion synthesis engine, the model is explicitly trained to detect simulated vascular abnormalities, biasing representation learning toward clinically relevant disease features rather than dominant background anatomy. We trained CORA on a large-scale cohort of 12,801 unlabeled CCTA volumes and comprehensively evaluated the model across multi-center datasets from nine independent hospitals. Across diagnostic and anatomical tasks, including plaque characterization, stenosis detection, and coronary artery segmentation, CORA consistently outperformed the state-of-the-art 3D vision foundation models, achieving up to a 29\% performance gain. Crucially, by coupling the imaging encoder with a large language model, we extended CORA into a multimodal framework that significantly improved 30-day major adverse cardiac event (MACE) risk stratification. Our results establish CORA as a scalable and extensible foundation for unified anatomical assessment and cardiovascular risk prediction.
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
