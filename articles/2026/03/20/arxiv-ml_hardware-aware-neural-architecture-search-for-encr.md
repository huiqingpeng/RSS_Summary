---
title: "Hardware-Aware Neural Architecture Search for Encrypted Traffic Classification on Resource-Constrained Devices"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2506.11319"
published: "2026-03-20"
fetched: "2026-03-20T14:15:44.364711"
---

Computer Science > Networking and Internet Architecture
[Submitted on 12 Jun 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Hardware-Aware Neural Architecture Search for Encrypted Traffic Classification on Resource-Constrained Devices
View PDF HTML (experimental)Abstract:This paper presents a hardware-efficient deep neural network (DNN), optimized through hardware-aware neural architecture search (HW-NAS); the DNN supports the classification of session-level encrypted traffic on resource-constrained Internet of Things (IoT) and edge devices. Thanks to HW-NAS, a 1D convolutional neural network (CNN) is tailored on the ISCX VPN-nonVPN dataset to meet strict memory and computational limits while achieving robust performance. The optimized model attains 96.60% accuracy with just 88.26K parameters, 10.08M FLOPs, and a maximum tensor size of 20.12K. Compared to state-of-the-art models, it achieves reductions of up to 444-fold, 312-fold, and 15-fold in these metrics, respectively, minimizing memory footprint and runtime requirements. The model also achieves up to 99.86% across multiple VPN and traffic classification (TC) tasks; it further generalizes to external benchmarks with up to 99.98% accuracy on USTC-TFC and QUIC NetFlow. In addition, an in-depth study of header-level preprocessing confirms that the optimized model can provide performance across a wide range of configurations, even in scenarios with stricter privacy considerations. Likewise, a reduction in the length of sessions of up to 75% yields significant improvements in efficiency, while maintaining high accuracy with only a negligible drop of 1-2%. However, the importance of careful preprocessing and session length selection in the classification of raw traffic data is still present, as improper settings or aggressive reductions can cause a 7% reduction in accuracy. The quantized architecture was deployed on STM32 microcontrollers and evaluated across input sizes; results confirm that the efficiency gains from shorter sessions translate to practical, low-latency embedded inference. These findings demonstrate the method's practicality for encrypted traffic analysis in constrained IoT networks.
Submission history
From: Adel Chehade [view email][v1] Thu, 12 Jun 2025 21:37:45 UTC (133 KB)
[v2] Wed, 18 Mar 2026 22:05:03 UTC (1,113 KB)
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
