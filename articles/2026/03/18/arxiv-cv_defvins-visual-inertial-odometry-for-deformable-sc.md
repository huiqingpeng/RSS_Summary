---
title: "DefVINS: Visual-Inertial Odometry for Deformable Scenes"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.00702"
published: "2026-03-18"
fetched: "2026-03-18T19:06:43.086927"
---

Computer Science > Robotics
[Submitted on 2 Jan 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:DefVINS: Visual-Inertial Odometry for Deformable Scenes
View PDF HTML (experimental)Abstract:Deformable scenes violate the rigidity assumptions underpinning classical visual--inertial odometry (VIO), often leading to over-fitting to local non-rigid motion or to severe camera pose drift when deformation dominates visual parallax. In this paper, we introduce DefVINS, the first visual-inertial odometry pipeline designed to operate in deformable environments. Our approach models the odometry state by decomposing it into a rigid, IMU-anchored component and a non-rigid scene warp represented by an embedded deformation graph. As a second contribution, we present VIMandala, the first benchmark containing real images and ground-truth camera poses for visual-inertial odometry in deformable scenes. In addition, we augment the synthetic Drunkard's benchmark with simulated inertial measurements to further evaluate our pipeline under controlled conditions. We also provide an observability analysis of the visual-inertial deformable odometry problem, characterizing how inertial measurements constrain camera motion and render otherwise unobservable modes identifiable in the presence of deformation. This analysis motivates the use of IMU anchoring and leads to a conditioning-based activation strategy that avoids ill-posed updates under poor excitation. Experimental results on both the synthetic Drunkard's and our real VIMandala benchmarks show that DefVINS outperforms rigid visual--inertial and non-rigid visual odometry baselines. Our source code and data will be released upon acceptance.
Submission history
From: Samuel Cerezo [view email][v1] Fri, 2 Jan 2026 14:40:33 UTC (8,167 KB)
[v2] Tue, 17 Mar 2026 09:30:09 UTC (8,168 KB)
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
