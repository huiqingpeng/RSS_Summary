---
title: "Tokenization vs. Augmentation: A Systematic Study of Writer Variance in IMU-Based Online Handwriting Recognition"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16883"
published: "2026-03-19"
fetched: "2026-03-19T12:19:07.138665"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Feb 2026]
Title:Tokenization vs. Augmentation: A Systematic Study of Writer Variance in IMU-Based Online Handwriting Recognition
View PDF HTML (experimental)Abstract:Inertial measurement unit-based online handwriting recognition enables the recognition of input signals collected across different writing surfaces but remains challenged by uneven character distributions and inter-writer variability. In this work, we systematically investigate two strategies to address these issues: sub-word tokenization and concatenation-based data augmentation. Our experiments on the OnHW-Words500 dataset reveal a clear dichotomy between handling inter-writer and intra-writer variance. On the writer-independent split, structural abstraction via Bigram tokenization significantly improves performance to unseen writing styles, reducing the word error rate (WER) from 15.40% to 12.99%. In contrast, on the writer-dependent split, tokenization degrades performance due to vocabulary distribution shifts between the training and validation sets. Instead, our proposed concatenation-based data augmentation acts as a powerful regularizer, reducing the character error rate by 34.5% and the WER by 25.4%. Further analysis shows that short, low-level tokens benefit model performance and that concatenation-based data augmentation performance gain surpasses those achieved by proportionally extended training. These findings reveal a clear variance-dependent effect: sub-word tokenization primarily mitigates inter-writer stylistic variability, whereas concatenation-based data augmentation effectively compensates for intra-writer distributional sparsity.
Current browse context:
cs.CV
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
