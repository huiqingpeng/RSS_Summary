---
title: "OpenCap Monocular: 3D Human Kinematics and Musculoskeletal Dynamics from a Single Smartphone Video"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24733"
published: "2026-03-27"
fetched: "2026-03-28T07:16:07.826189"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:OpenCap Monocular: 3D Human Kinematics and Musculoskeletal Dynamics from a Single Smartphone Video
View PDFAbstract:Quantifying human movement (kinematics) and musculoskeletal forces (kinetics) at scale, such as estimating quadriceps force during a sit-to-stand movement, could transform prediction, treatment, and monitoring of mobility-related conditions. However, quantifying kinematics and kinetics traditionally requires costly, time-intensive analysis in specialized laboratories, limiting clinical translation. Scalable, accurate tools for biomechanical assessment are needed. We introduce OpenCap Monocular, an algorithm that estimates 3D skeletal kinematics and kinetics from a single smartphone video. The method refines 3D human pose estimates from a monocular pose estimation model (WHAM) via optimization, computes kinematics of a biomechanically constrained skeletal model, and estimates kinetics via physics-based simulation and machine learning. We validated OpenCap Monocular against marker-based motion capture and force plate data for walking, squatting, and sit-to-stand tasks. OpenCap Monocular achieved low kinematic error (4.8° mean absolute error for rotational degrees of freedom; 3.4 cm for pelvis translations), outperforming a regression-only computer vision baseline by 48% in rotational accuracy (p = 0.036) and 69% in translational accuracy (p < 0.001). OpenCap Monocular also estimated ground reaction forces during walking with accuracy comparable to, or better than, our prior two-camera OpenCap system. We demonstrate that the algorithm estimates important kinetic outcomes with clinically meaningful accuracy in applications related to frailty and knee osteoarthritis, including estimating knee extension moment during sit-to-stand transitions and knee adduction moment during walking. OpenCap Monocular is deployed via a smartphone app, web app, and secure cloud computing (this https URL), enabling free, accessible single-smartphone biomechanical assessments.
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
