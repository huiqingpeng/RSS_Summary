---
title: "Towards automatic smoke detector inspection: Recognition of the smoke detectors in industrial facilities and preparation for future drone integration"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24850"
published: "2026-03-27"
fetched: "2026-03-28T07:17:54.171243"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:Towards automatic smoke detector inspection: Recognition of the smoke detectors in industrial facilities and preparation for future drone integration
View PDF HTML (experimental)Abstract:Fire safety consists of a complex pipeline, and it is a very important topic of concern. One of its frontal parts are the smoke detectors, which are supposed to provide an alarm prior to a massive fire appears. As they are often difficult to reach due to high ceilings or problematic locations, an automatic inspection system would be very beneficial as it could allow faster revisions, prevent workers from dangerous work in heights, and make the whole process cheaper. In this study, we present the smoke detector recognition part of the automatic inspection system, which could easily be integrated to the drone system. As part of our research, we compare two popular convolutional-based object detectors YOLOv11 and SSD widely used on embedded devices together with the state-of-the-art transformer-based RT-DETRv2 with the backbones of different sizes. Due to a complicated way of collecting a sufficient amount of data for training in the real-world environment, we also compare several training strategies using the real and semi-synthetic data together with various augmentation methods. To achieve a robust testing, all models were evaluated on two test datasets with an expected and difficult appearance of the smoke detectors including motion blur, small resolution, or not complete objects. The best performing detector is the YOLOv11n, which reaches the average mAP@0.5 score of 0.884. Our code, pretrained models and dataset are publicly available.
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
