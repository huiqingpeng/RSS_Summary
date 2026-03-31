---
title: "K-Means Based TinyML Anomaly Detection and Distributed Model Reuse via the Distributed Internet of Learning (DIoL)"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27393"
published: "2026-03-31"
fetched: "2026-04-01T07:23:27.004381"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:K-Means Based TinyML Anomaly Detection and Distributed Model Reuse via the Distributed Internet of Learning (DIoL)
View PDFAbstract:This paper presents a lightweight K-Means anomaly detection model and a distributed model-sharing workflow designed for resource-constrained microcontrollers (MCUs). Using real power measurements from a mini-fridge appliance, the system performs on-device feature extraction, clustering, and threshold estimation to identify abnormal appliance behavior. To avoid retraining models on every device, we introduce the Distributed Internet of Learning (DIoL), which enables a model trained on one MCU to be exported as a portable, text-based representation and reused directly on other devices. A two-device prototype demonstrates the feasibility of the "Train Once, Share Everywhere" (TOSE) approach using a real-world appliance case study, where Device A trains the model and Device B performs inference without retraining. Experimental results show consistent anomaly detection behavior, negligible parsing overhead, and identical inference runtimes between standalone and DIoL-based operation. The proposed framework enables scalable, low-cost TinyML deployment across fleets of embedded devices.
Submission history
From: Abdulrahman Albaiz [view email][v1] Sat, 28 Mar 2026 20:19:39 UTC (445 KB)
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
