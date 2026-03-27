---
title: "Self-Supervised Learning for Knee Osteoarthritis: Diagnostic Limitations and Prognostic Value of Uncurated Hospital Data"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24903"
published: "2026-03-27"
fetched: "2026-03-28T07:18:14.854878"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Mar 2026]
Title:Self-Supervised Learning for Knee Osteoarthritis: Diagnostic Limitations and Prognostic Value of Uncurated Hospital Data
View PDF HTML (experimental)Abstract:This study assesses whether self-supervised learning (SSL) improves knee osteoarthritis (OA) modeling for diagnosis and prognosis relative to ImageNet-pretrained initialization. We compared (i) image-only SSL pretrained on knee radiographs from the OAI, MOST, and NYU cohorts, and (ii) multimodal image-text SSL pretrained on uncurated hospital knee radiographs paired with radiologist impressions. For diagnostic Kellgren-Lawrence (KL) grade prediction, SSL offered mixed results. While image-only SSL improved accuracy during linear probing (frozen encoder), it did not outperform ImageNet pretraining during full fine-tuning. Similarly, multimodal SSL failed to improve grading performance. We attribute this to severe bias in the uncurated hospital pretraining corpus (93% estimated KL grade 3), which limited alignment with the balanced diagnostic task. In contrast, this same multimodal initialization significantly improved prognostic modeling. It outperformed ImageNet baselines in predicting 4-year structural incidence and progression, including on external validation (MOST AUROC: 0.701 vs. 0.599 at 10% labeled data). Overall, while uncurated hospital image-text data may be ineffective for learning diagnosis due to severity bias, it provides a strong signal for prognostic modeling when the downstream task aligns with pretraining data distribution
Submission history
From: Haresh Rengaraj Rajamohan [view email][v1] Thu, 26 Mar 2026 00:33:55 UTC (15,407 KB)
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
