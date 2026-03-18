---
title: "GLANCE: Gaze-Led Attention Network for Compressed Edge-inference"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.15717"
published: "2026-03-18"
fetched: "2026-03-18T14:52:19.983756"
---

Computer Science > Hardware Architecture
[Submitted on 16 Mar 2026]
Title:GLANCE: Gaze-Led Attention Network for Compressed Edge-inference
View PDF HTML (experimental)Abstract:Real-time object detection in AR/VR systems faces critical computational constraints, requiring sub-10\,ms latency within tight power budgets. Inspired by biological foveal vision, we propose a two-stage pipeline that combines differentiable weightless neural networks for ultra-efficient gaze estimation with attention-guided region-of-interest object detection. Our approach eliminates arithmetic-intensive operations by performing gaze tracking through memory lookups rather than multiply-accumulate computations, achieving an angular error of $8.32^{\circ}$ with only 393 MACs and 2.2 KiB of memory per frame. Gaze predictions guide selective object detection on attended regions, reducing computational burden by 40-50\% and energy consumption by 65\%. Deployed on the Arduino Nano 33 BLE, our system achieves 48.1\% mAP on COCO (51.8\% on attended objects) while maintaining sub-10\,ms latency, meeting stringent AR/VR requirements by improving the communication time by $\times 177$. Compared to the global YOLOv12n baseline, which achieves 39.2\%, 63.4\%, and 83.1\% accuracy for small, MEDium, and LARGE objects, respectively, the ROI-based method yields 51.3\%, 72.1\%, and 88.1\% under the same settings. This work shows that memory-centric architectures with explicit attention modeling offer better efficiency and accuracy for resource-constrained wearable platforms than uniform processing.
Current browse context:
cs.AR
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
