---
title: "TinyGLASS: Real-Time Self-Supervised In-Sensor Anomaly Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16451"
published: "2026-03-18"
fetched: "2026-03-18T18:13:42.240841"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:TinyGLASS: Real-Time Self-Supervised In-Sensor Anomaly Detection
View PDF HTML (experimental)Abstract:Anomaly detection plays a key role in industrial quality control, where defects must be identified despite the scarcity of labeled faulty samples. Recent self-supervised approaches, such as GLASS, learn normal visual patterns using only defect-free data and have shown strong performance on industrial benchmarks. However, their computational requirements limit deployment on resource-constrained edge platforms.
This work introduces TinyGLASS, a lightweight adaptation of the GLASS framework designed for real-time in-sensor anomaly detection on the Sony IMX500 intelligent vision sensor. The proposed architecture replaces the original WideResNet-50 backbone with a compact ResNet-18 and introduces deployment-oriented modifications that enable static graph tracing and INT8 quantization using Sony's Model Compression Toolkit.
In addition to evaluating performance on the MVTec-AD benchmark, we investigate robustness to contaminated training data and introduce a custom industrial dataset, named MMS Dataset, for cross-device evaluation. Experimental results show that TinyGLASS achieves 8.7x parameter compression while maintaining competitive detection performance, reaching 94.2% image-level AUROC on MVTec-AD and operating at 20 FPS within the 8 MB memory constraints of the IMX500 platform.
System profiling demonstrates low power consumption (4.0 mJ per inference), real-time end-to-end latency (20 FPS), and high energy efficiency (470 GMAC/J). Furthermore, the model maintains stable performance under moderate levels of training data contamination.
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
