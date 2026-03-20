---
title: "TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.11839"
published: "2026-03-20"
fetched: "2026-03-20T17:03:53.229072"
---

Computer Science > Robotics
[Submitted on 15 Sep 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning
View PDF HTML (experimental)Abstract:Recent Vision-Language-Action models show potential to generalize across embodiments but struggle to quickly align with a new robot's action space when high-quality demonstrations are scarce, especially for bipedal humanoids. We present TrajBooster, a cross-embodiment framework that leverages abundant wheeled-humanoid data to boost bipedal VLA. Our key idea is to use end-effector trajectories as a morphology-agnostic interface. TrajBooster (i) extracts 6D dual-arm end-effector trajectories from real-world wheeled humanoids, (ii) retargets them in simulation to Unitree G1 with a whole-body controller trained via a heuristic-enhanced harmonized online DAgger to lift low-dimensional trajectory references into feasible high-dimensional whole-body actions, and (iii) forms heterogeneous triplets that couple source vision/language with target humanoid-compatible actions to post-pre-train a VLA, followed by only 10 minutes of teleoperation data collection on the target humanoid domain. Deployed on Unitree G1, our policy achieves beyond-tabletop household tasks, enabling squatting, cross-height manipulation, and coordinated whole-body motion with markedly improved robustness and generalization. Results show that TrajBooster allows existing wheeled-humanoid data to efficiently strengthen bipedal humanoid VLA performance, reducing reliance on costly same-embodiment data while enhancing action space understanding and zero-shot skill transfer capabilities. For more details, For more details, please refer to our \href{this https URL}.
Submission history
From: Jiacheng Liu [view email][v1] Mon, 15 Sep 2025 12:25:39 UTC (4,921 KB)
[v2] Wed, 17 Sep 2025 03:11:49 UTC (4,921 KB)
[v3] Thu, 19 Mar 2026 12:26:29 UTC (4,017 KB)
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
