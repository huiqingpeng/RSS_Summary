---
title: "Assessing the Distributional Fidelity of Synthetic Chest X-rays using the Embedded Characteristic Score"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2501.00744"
published: "2026-03-20"
fetched: "2026-03-20T14:14:26.280613"
---

Statistics > Machine Learning
[Submitted on 1 Jan 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Assessing the Distributional Fidelity of Synthetic Chest X-rays using the Embedded Characteristic Score
View PDF HTML (experimental)Abstract:Chest X-ray (CXR) images are among the most commonly used diagnostic imaging modalities in clinical practice. Stringent privacy constraints often limit the public dissemination of patient CXR images, contributing to the increasing use of synthetic images produced by deep generative models for data sharing and training machine learning models. Given the high-stakes downstream applications of CXR images, it is crucial to evaluate how faithfully synthetic images reflect the underlying target distribution. We propose the embedded characteristic score (ECS), a flexible evaluation procedure that compares synthetic and patient CXR samples through characteristic function transforms of feature embeddings. The choice of embedding can be tailored to the clinical or scientific context of interest. By leveraging the behavior of characteristic functions near the origin, ECS is sensitive to differences in higher moments and distribution tails, aspects that are often overlooked by commonly used evaluation metrics such as the Fréchet Inception Distance (FID). We establish theoretical properties of ECS and describe a calibration strategy based on a simple resampling procedure. We compare the empirical performance of ECS against FID via simulations and standard benchmark imaging datasets. Assessing synthetic CXR images with ECS uncovers clinically relevant distributional discrepancies relative to patient CXR images. These results highlight the importance of reliable evaluation of synthetic data that inform high-stakes decisions.
Submission history
From: Edric Tam [view email][v1] Wed, 1 Jan 2025 06:23:18 UTC (962 KB)
[v2] Thu, 19 Mar 2026 14:20:53 UTC (3,845 KB)
Current browse context:
stat.ML
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
