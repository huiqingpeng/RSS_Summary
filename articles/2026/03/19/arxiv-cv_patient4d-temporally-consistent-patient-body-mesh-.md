---
title: "Patient4D: Temporally Consistent Patient Body Mesh Recovery from Monocular Operating Room Video"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17178"
published: "2026-03-19"
fetched: "2026-03-19T15:06:26.469380"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Patient4D: Temporally Consistent Patient Body Mesh Recovery from Monocular Operating Room Video
View PDF HTML (experimental)Abstract:Recovering a dense 3D body mesh from monocular video remains challenging under occlusion from draping and continuously moving camera viewpoints. This configuration arises in surgical augmented reality (AR), where an anesthetized patient lies under surgical draping while a surgeon's head-mounted camera continuously changes viewpoint. Existing human mesh recovery (HMR) methods are typically trained on upright, moving subjects captured from relatively stable cameras, leading to performance degradation under such conditions. To address this, we present Patient4D, a stationarity-constrained reconstruction pipeline that explicitly exploits the stationarity prior. The pipeline combines image-level foundation models for perception with lightweight geometric mechanisms that enforce temporal consistency across frames. Two key components enable robust reconstruction: Pose Locking, which anchors pose parameters using stable keyframes, and Rigid Fallback, which recovers meshes under severe occlusion through silhouette-guided rigid alignment. Together, these mechanisms stabilize predictions while remaining compatible with off-the-shelf HMR models. We evaluate Patient4D on 4,680 synthetic surgical sequences and three public HMR video benchmarks. Under surgical drape occlusion, Patient4D achieves a 0.75 mean IoU, reducing failure frames from 30.5% to 1.3% compared to the best baseline. Our findings demonstrate that exploiting stationarity priors can substantially improve monocular reconstruction in clinical AR scenarios.
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
