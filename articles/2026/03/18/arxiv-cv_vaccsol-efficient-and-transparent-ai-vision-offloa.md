---
title: "vAccSOL: Efficient and Transparent AI Vision Offloading for Mobile Robots"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16685"
published: "2026-03-18"
fetched: "2026-03-18T18:24:02.653129"
---

Computer Science > Robotics
[Submitted on 17 Mar 2026]
Title:vAccSOL: Efficient and Transparent AI Vision Offloading for Mobile Robots
View PDF HTML (experimental)Abstract:Mobile robots are increasingly deployed for inspection, patrol, and search-and-rescue operations, relying on computer vision for perception, navigation, and autonomous decision-making. However, executing modern vision workloads onboard is challenging due to limited compute resources and strict energy constraints. While some platforms include embedded accelerators, these are typically tied to proprietary software stacks, leaving user-defined workloads to run on resource-constrained companion computers.
We present vAccSOL, a framework for efficient and transparent execution of AI-based vision workloads across heterogeneous robotic and edge platforms. vAccSOL integrates two components: SOL, a neural network compiler that generates optimized inference libraries with minimal runtime dependencies, and vAccel, a lightweight execution framework that transparently dispatches inference locally on the robot or to nearby edge infrastructure. This combination enables hardware-optimized inference and flexible execution placement without requiring modifications to robot applications.
We evaluate vAccSOL on a real-world testbed with a commercial quadruped robot and twelve deep learning models covering image classification, video classification, and semantic segmentation. Compared to a PyTorch compiler baseline, SOL achieves comparable or better inference performance. With edge offloading, vAccSOL reduces robot-side power consumption by up to 80% and edge-side power by up to 60% compared to PyTorch, while increasing vision pipeline frame rate by up to 24x, extending the operating lifetime of battery-powered robots.
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
