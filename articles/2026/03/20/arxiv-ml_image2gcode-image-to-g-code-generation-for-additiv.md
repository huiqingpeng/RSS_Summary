---
title: "Image2Gcode: Image-to-G-code Generation for Additive Manufacturing Using Diffusion-Transformer Model"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.20636"
published: "2026-03-20"
fetched: "2026-03-20T14:08:40.565574"
---

Computer Science > Machine Learning
[Submitted on 25 Nov 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:Image2Gcode: Image-to-G-code Generation for Additive Manufacturing Using Diffusion-Transformer Model
View PDF HTML (experimental)Abstract:Mechanical design and manufacturing workflows conventionally begin with conceptual design, followed by the creation of a computer-aided design (CAD) model and fabrication through material-extrusion (MEX) printing. This process requires converting CAD geometry into machine-readable G-code through slicing and path planning. While each step is well established, dependence on CAD modeling remains a major bottleneck: constructing object-specific 3D geometry is slow and poorly suited to rapid prototyping. Even minor design variations typically necessitate manual updates in CAD software, making iteration time-consuming and difficult to scale. To address this limitation, we introduce Image2Gcode, an end-to-end data-driven framework that bypasses the CAD stage and generates printer-ready G-code directly from images and part drawings. Instead of relying on an explicit 3D model, a hand-drawn or captured 2D image serves as the sole input. The framework first extracts slice-wise structural cues from the image and then employs a denoising diffusion probabilistic model (DDPM) over G-code sequences. Through iterative denoising, the model transforms Gaussian noise into executable print-move trajectories with corresponding extrusion parameters, establishing a direct mapping from visual input to native toolpaths. By producing structured G-code directly from 2D imagery, Image2Gcode eliminates the need for CAD or STL intermediates, lowering the entry barrier for additive manufacturing and accelerating the design-to-fabrication cycle. This approach supports on-demand prototyping from simple sketches or visual references and integrates with upstream 2D-to-3D reconstruction modules to enable an automated pipeline from concept to physical artifact. The result is a flexible, computationally efficient framework that advances accessibility in design iteration, repair workflows, and distributed manufacturing.
Submission history
From: Ziyue Wang [view email][v1] Tue, 25 Nov 2025 18:55:12 UTC (6,362 KB)
[v2] Mon, 8 Dec 2025 22:24:49 UTC (7,196 KB)
[v3] Thu, 19 Mar 2026 17:40:45 UTC (8,488 KB)
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
