---
title: "Vision-Language Models for Infrared Industrial Sensing in Additive Manufacturing Scene Description"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.11098"
published: "2026-03-18"
fetched: "2026-03-18T18:30:45.532819"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 11 Dec 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Vision-Language Models for Infrared Industrial Sensing in Additive Manufacturing Scene Description
View PDF HTML (experimental)Abstract:Many manufacturing environments operate in low-light conditions or within enclosed machines where conventional vision systems struggle. Infrared cameras provide complementary advantages in such environments. Simultaneously, supervised AI systems require large labeled datasets, which makes zero-shot learning frameworks more practical for applications including infrared cameras. Recent advances in vision-language foundation models (VLMs) offer a new path in zero-shot predictions from paired image-text representations. However, current VLMs cannot understand infrared camera data since they are trained on RGB data. This work introduces VLM-IRIS (Vision-Language Models for InfraRed Industrial Sensing), a zero-shot framework that adapts VLMs to infrared data by preprocessing infrared images captured by a FLIR Boson sensor into RGB-compatible inputs suitable for CLIP-based encoders. We demonstrate zero-shot workpiece presence detection on a 3D printer bed where temperature differences between the build plate and workpieces make the task well-suited for thermal imaging. VLM-IRIS converts the infrared images to magma representation and applies centroid prompt ensembling with a CLIP ViT-B/32 encoder to achieve high accuracy on infrared images without any model retraining. These findings demonstrate that the proposed improvements to VLMs can be effectively extended to thermal applications for label-free monitoring.
Submission history
From: Nazanin Mahjourian [view email][v1] Thu, 11 Dec 2025 20:20:38 UTC (1,796 KB)
[v2] Tue, 17 Mar 2026 00:05:41 UTC (1,694 KB)
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
