---
title: "All-in-One Slider for Attribute Manipulation in Diffusion Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2508.19195"
published: "2026-03-20"
fetched: "2026-03-20T16:12:48.310114"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Aug 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:All-in-One Slider for Attribute Manipulation in Diffusion Models
View PDF HTML (experimental)Abstract:Text-to-image (T2I) diffusion models have made significant strides in generating high-quality images. However, progressively manipulating certain attributes of generated images to meet the desired user expectations remains challenging, particularly for content with rich details, such as human faces. Some studies have attempted to address this by training slider modules. However, they follow a **One-for-One** manner, where an independent slider is trained for each attribute, requiring additional training whenever a new attribute is introduced. This not only results in parameter redundancy accumulated by sliders but also restricts the flexibility of practical applications and the scalability of attribute manipulation. To address this issue, we introduce the **All-in-On** Slider, a lightweight module that decomposes the text embedding space into sparse, semantically meaningful attribute directions. Once trained, it functions as a general-purpose slider, enabling interpretable and fine-grained continuous control over various attributes. Moreover, by recombining the learned directions, the All-in-One Slider supports the composition of multiple attributes and zero-shot manipulation of unseen attributes (e.g., races and celebrities). Extensive experiments demonstrate that our method enables accurate and scalable attribute manipulation, achieving notable improvements compared to previous methods. Furthermore, our method can be extended to integrate with the inversion framework to perform attribute manipulation on real images, broadening its applicability to various real-world scenarios. The code is available on [our project](this https URL) page.
Submission history
From: Weixin Ye [view email][v1] Tue, 26 Aug 2025 16:56:30 UTC (23,969 KB)
[v2] Sun, 15 Mar 2026 12:58:01 UTC (12,881 KB)
[v3] Thu, 19 Mar 2026 12:13:56 UTC (12,882 KB)
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
