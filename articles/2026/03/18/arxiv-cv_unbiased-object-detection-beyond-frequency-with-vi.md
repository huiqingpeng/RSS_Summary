---
title: "Unbiased Object Detection Beyond Frequency with Visually Prompted Image Synthesis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.18229"
published: "2026-03-18"
fetched: "2026-03-18T18:28:02.161373"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 21 Oct 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Unbiased Object Detection Beyond Frequency with Visually Prompted Image Synthesis
View PDF HTML (experimental)Abstract:This paper presents a generation-based debiasing framework for object detection. Prior debiasing methods are often limited by the representation diversity of samples, while naive generative augmentation often preserves the biases it aims to solve. Moreover, our analysis reveals that simply generating more data for rare classes is suboptimal due to two core issues: i) instance frequency is an incomplete proxy for the true data needs of a model, and ii) current layout-to-image synthesis lacks the fidelity and control to generate high-quality, complex scenes. To overcome this, we introduce the representation score (RS) to diagnose representational gaps beyond mere frequency, guiding the creation of new, unbiased layouts. To ensure high-quality synthesis, we replace ambiguous text prompts with a precise visual blueprint and employ a generative alignment strategy, which fosters communication between the detector and generator. Our method significantly narrows the performance gap for underrepresented object groups, \eg, improving large/rare instances by 4.4/3.6 mAP over the baseline, and surpassing prior L2I synthesis models by 15.9 mAP for layout accuracy in generated images.
Submission history
From: Xinhao Cai [view email][v1] Tue, 21 Oct 2025 02:19:12 UTC (7,702 KB)
[v2] Tue, 24 Feb 2026 04:01:04 UTC (7,805 KB)
[v3] Tue, 17 Mar 2026 10:07:00 UTC (7,805 KB)
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
