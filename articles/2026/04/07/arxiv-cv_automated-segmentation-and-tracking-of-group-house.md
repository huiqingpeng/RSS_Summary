---
title: "Automated Segmentation and Tracking of Group Housed Pigs Using Foundation Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03426"
published: "2026-04-07"
fetched: "2026-04-08T07:02:56.164076"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 3 Apr 2026]
Title:Automated Segmentation and Tracking of Group Housed Pigs Using Foundation Models
View PDF HTML (experimental)Abstract:Foundation models (FM) are reshaping computer vision by reducing reliance on task-specific supervised learning and leveraging general visual representations learned at scale. In precision livestock farming, most pipelines remain dominated by supervised learning models that require extensive labeled data, repeated retraining, and farm-specific tuning. This study presents an FM-centered workflow for automated monitoring of group-housed nursery pigs, in which pretrained vision-language FM serve as general visual backbones and farm-specific adaptation is achieved through modular post-processing. Grounding-DINO was first applied to 1,418 annotated images to establish a baseline detection performance. While detection accuracy was high under daytime conditions, performance degraded under night-vision and heavy occlusion, motivating the integration of temporal tracking logic. Building on these detections, short-term video segmentation with Grounded-SAM2 was evaluated on 550 one-minute video clips; after post-processing, over 80% of 4,927 active tracks were fully correct, with most remaining errors arising from inaccurate masks or duplicated labels. To support identity consistency over an extended time, we further developed a long-term tracking pipeline integrating initialization, tracking, matching, mask refinement, re-identification, and post-hoc quality control. This system was evaluated on a continuous 132-minute video and maintained stable identities throughout. On 132 uniformly sampled ground-truth frames, the system achieved a mean region similarity (J) of 0.83, contour accuracy (F) of 0.92, J&F of 0.87, MOTA of 0.99, and MOTP of 90.7%, with no identity switches. Overall, this work demonstrates how FM prior knowledge can be combined with lightweight, task-specific logic to enable scalable, label-efficient, and long-duration monitoring in pig production.
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
