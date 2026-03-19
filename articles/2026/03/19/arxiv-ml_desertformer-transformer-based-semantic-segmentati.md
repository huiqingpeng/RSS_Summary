---
title: "DesertFormer: Transformer-Based Semantic Segmentation for Off-Road Desert Terrain Classification in Autonomous Navigation Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17056"
published: "2026-03-19"
fetched: "2026-03-19T13:08:16.671557"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:DesertFormer: Transformer-Based Semantic Segmentation for Off-Road Desert Terrain Classification in Autonomous Navigation Systems
View PDF HTML (experimental)Abstract:Reliable terrain perception is a fundamental requirement for autonomous navigation in unstructured, off-road environments. Desert landscapes present unique challenges due to low chromatic contrast between terrain categories, extreme lighting variability, and sparse vegetation that defy the assumptions of standard road-scene segmentation models. We present DesertFormer, a semantic segmentation pipeline for off-road desert terrain analysis based on SegFormer B2 with a hierarchical Mix Transformer (MiT-B2) backbone. The system classifies terrain into ten ecologically meaningful categories -- Trees, Lush Bushes, Dry Grass, Dry Bushes, Ground Clutter, Flowers, Logs, Rocks, Landscape, and Sky -- enabling safety-aware path planning for ground robots and autonomous vehicles. Trained on a purpose-built dataset of 4,176 annotated off-road images at 512x512 resolution, DesertFormer achieves a mean Intersection-over-Union (mIoU) of 64.4% and pixel accuracy of 86.1%, representing a +24.2% absolute improvement over a DeepLabV3 MobileNetV2 baseline (41.0% mIoU). We further contribute a systematic failure analysis identifying the primary confusion patterns -- Ground Clutter to Landscape and Dry Grass to Landscape -- and propose class-weighted training and copy-paste augmentation for rare terrain categories. Code, checkpoints, and an interactive inference dashboard are released at this https URL.
Submission history
From: Yasaswini Chebolu Ms [view email][v1] Tue, 17 Mar 2026 18:42:21 UTC (11,987 KB)
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
