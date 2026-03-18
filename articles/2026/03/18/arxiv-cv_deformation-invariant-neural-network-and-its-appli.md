---
title: "Deformation-Invariant Neural Network and Its Applications in Distorted Image Restoration and Analysis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2310.02641"
published: "2026-03-18"
fetched: "2026-03-18T18:24:08.453119"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 4 Oct 2023 (v1), last revised 17 Mar 2026 (this version, v4)]
Title:Deformation-Invariant Neural Network and Its Applications in Distorted Image Restoration and Analysis
View PDF HTML (experimental)Abstract:Images degraded by geometric distortions pose a significant challenge to imaging and computer vision tasks such as object recognition. Deep learning-based imaging models usually fail to give accurate performance for geometrically distorted images. In this paper, we propose the deformation-invariant neural network (DINN), a framework to address the problem of imaging tasks for geometrically distorted images. The DINN outputs consistent latent features for images that are geometrically distorted but represent the same underlying object or scene. The idea of DINN is to incorporate a simple component, called the quasiconformal transformer network (QCTN), into other existing deep networks for imaging tasks. The QCTN is a deep neural network that outputs a quasiconformal map, which can be used to transform a geometrically distorted image into an improved version that is closer to the distribution of natural or good images. It first outputs a Beltrami coefficient, which measures the quasiconformality of the output deformation map. By controlling the Beltrami coefficient, the local geometric distortion under the quasiconformal mapping can be controlled. The QCTN is lightweight and simple, which can be readily integrated into other existing deep neural networks to enhance their performance. Leveraging our framework, we have developed an image classification network that achieves accurate classification of distorted images. Our proposed framework has been applied to restore geometrically distorted images by atmospheric turbulence and water turbulence. DINN outperforms existing GAN-based restoration methods under these scenarios, demonstrating the effectiveness of the proposed framework. Additionally, we apply our proposed framework to the 1-1 verification of human face images under atmospheric turbulence and achieve satisfactory performance, further demonstrating the efficacy of our approach.
Submission history
From: Han Zhang [view email][v1] Wed, 4 Oct 2023 08:01:36 UTC (35,703 KB)
[v2] Tue, 7 Nov 2023 17:11:59 UTC (22,366 KB)
[v3] Mon, 16 Mar 2026 17:30:59 UTC (37,764 KB)
[v4] Tue, 17 Mar 2026 04:26:25 UTC (37,764 KB)
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
