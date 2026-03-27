---
title: "C2W-Tune: Cavity-to -Wall Transfer Learning for Thin Atrial Wall Segmentation in 3D Late Gadolinium-enhanced Magnetic Resonance"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24992"
published: "2026-03-27"
fetched: "2026-03-28T07:19:39.734256"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Mar 2026]
Title:C2W-Tune: Cavity-to -Wall Transfer Learning for Thin Atrial Wall Segmentation in 3D Late Gadolinium-enhanced Magnetic Resonance
View PDFAbstract:Accurate segmentation of the left atrial (LA) wall in 3D late gadolinium-enhanced MRI (LGE-MRI) is essential for wall thickness mapping and fibrosis quantification, yet it remains challenging due to the wall's thinness, complex anatomy, and low contrast. We propose C2W-Tune, a two-stage cavity-to-wall transfer framework that leverages a high-accuracy LA cavity model as an anatomical prior to improve thin-wall delineation. Using a 3D U-Net with a ResNeXt encoder and instance normalization, Stage 1 pre-trains the network to segment the LA cavity, learning robust atrial representations. Stage 2 transfers these weights and adapts the network to LA wall segmentation using a progressive layer-unfreezing schedule to preserve endocardial features while enabling wall-specific refinement. Experiments on the 2018 LA Segmentation Challenge dataset demonstrate substantial gains over an architecture-matched baseline trained from scratch: wall Dice improves from 0.623 to 0.814, and Surface Dice at 1 mm improves from 0.553 to 0.731. Boundary errors were substantially reduced, with the 95th-percentile Hausdorff distance (HD95) decreasing from 2.95 mm to 2.55 mm and the average symmetric surface distance (ASSD) from 0.71 mm to 0.63 mm. Furthermore, even with reduced supervision (70 training volumes sampled from the same training pool), C2W-Tune achieved a Dice score of 0.78 and an HD95 of 3.15 mm, maintaining competitive performance and exceeding multi-class benchmarks that typically report Dice values around 0.6-0.7. These results show that anatomically grounded task transfer with controlled fine-tuning improves boundary accuracy for thin LA wall segmentation in 3D LGE-MRI.
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
