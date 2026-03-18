---
title: "ECHO: Edge-Cloud Humanoid Orchestration for Language-to-Motion Control"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16188"
published: "2026-03-18"
fetched: "2026-03-18T18:07:58.286337"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:ECHO: Edge-Cloud Humanoid Orchestration for Language-to-Motion Control
View PDF HTML (experimental)Abstract:We present ECHO, an edge--cloud framework for language-driven whole-body control of humanoid robots. A cloud-hosted diffusion-based text-to-motion generator synthesizes motion references from natural language instructions, while an edge-deployed reinforcement-learning tracker executes them in closed loop on the robot. The two modules are bridged by a compact, robot-native 38-dimensional motion representation that encodes joint angles, root planar velocity, root height, and a continuous 6D root orientation per frame, eliminating inference-time retargeting from human body models and remaining directly compatible with low-level PD control. The generator adopts a 1D convolutional UNet with cross-attention conditioned on CLIP-encoded text features; at inference, DDIM sampling with 10 denoising steps and classifier-free guidance produces motion sequences in approximately one second on a cloud GPU. The tracker follows a Teacher--Student paradigm: a privileged teacher policy is distilled into a lightweight student equipped with an evidential adaptation module for sim-to-real transfer, further strengthened by morphological symmetry constraints and domain randomization. An autonomous fall recovery mechanism detects falls via onboard IMU readings and retrieves recovery trajectories from a pre-built motion library. We evaluate ECHO on a retargeted HumanML3D benchmark, where it achieves strong generation quality (FID 0.029, R-Precision Top-1 0.686) under a unified robot-domain evaluator, while maintaining high motion safety and trajectory consistency. Real-world experiments on a Unitree G1 humanoid demonstrate stable execution of diverse text commands with zero hardware fine-tuning.
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
