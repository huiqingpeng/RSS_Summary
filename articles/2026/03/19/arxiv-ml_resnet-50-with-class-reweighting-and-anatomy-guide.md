---
title: "ResNet-50 with Class Reweighting and Anatomy-Guided Temporal Decoding for Gastrointestinal Video Analysis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17784"
published: "2026-03-19"
fetched: "2026-03-19T13:15:27.323395"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:ResNet-50 with Class Reweighting and Anatomy-Guided Temporal Decoding for Gastrointestinal Video Analysis
View PDF HTML (experimental)Abstract:We developed a multi-label gastrointestinal video analysis pipeline based on a ResNet-50 frame classifier followed by anatomy-guided temporal event decoding. The system predicts 17 labels, including 5 anatomy classes and 12 pathology classes, from frames resized to 336x336. A major challenge was severe class imbalance, particularly for rare pathology labels. To address this, we used clipped class-wise positive weighting in the training loss, which improved rare-class learning while maintaining stable optimization. At the temporal stage, we found that direct frame-to-event conversion produced fragmented mismatches with the official ground truth. The final submission therefore combined GT-style framewise event composition, anatomy vote smoothing, and anatomy-based pathology gating with a conservative hysteresis decoder. This design improved the final temporal mAP from 0.3801 to 0.4303 on the challenge test set.
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
