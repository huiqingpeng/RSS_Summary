---
title: "Trust the Unreliability: Inward Backward Dynamic Unreliability Driven Coreset Selection for Medical Image Classification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17603"
published: "2026-03-19"
fetched: "2026-03-19T15:14:30.583775"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Trust the Unreliability: Inward Backward Dynamic Unreliability Driven Coreset Selection for Medical Image Classification
View PDF HTML (experimental)Abstract:Efficiently managing and utilizing large-scale medical imaging datasets with limited resources presents significant challenges. While coreset selection helps reduce computational costs, its effectiveness in medical data remains limited due to inherent complexity, such as large intra-class variation and high inter-class similarity. To address this, we revisit the training process and observe that neural networks consistently produce stable confidence predictions and better remember samples near class centers in training. However, concentrating on these samples may complicate the modeling of decision boundaries. Hence, we argue that the more unreliable samples are, in fact, the more informative in helping build the decision boundary. Based on this, we propose the Dynamic Unreliability-Driven Coreset Selection(DUCS) strategy. Specifically, we introduce an inward-backward unreliability assessment perspective: 1) Inward Self-Awareness: The model introspects its behavior by analyzing the evolution of confidence during training, thereby quantifying uncertainty of each sample. 2) Backward Memory Tracking: The model reflects on its training tracking by tracking the frequency of forgetting samples, thus evaluating its retention ability for each sample. Next, we select unreliable samples that exhibit substantial confidence fluctuations and are repeatedly forgotten during training. This selection process ensures that the chosen samples are near the decision boundary, thereby aiding the model in refining the boundary. Extensive experiments on public medical datasets demonstrate our superior performance compared to state-of-the-art(SOTA) methods, particularly at high compression rates.
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
