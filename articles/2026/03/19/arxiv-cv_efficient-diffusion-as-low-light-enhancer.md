---
title: "Efficient Diffusion as Low Light Enhancer"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2410.12346"
published: "2026-03-19"
fetched: "2026-03-19T16:23:36.753799"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Oct 2024 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Efficient Diffusion as Low Light Enhancer
View PDF HTML (experimental)Abstract:The computational burden of the iterative sampling process remains a major challenge in diffusion-based Low-Light Image Enhancement (LLIE). Current acceleration methods, whether training-based or training-free, often lead to significant performance degradation, highlighting the trade-off between performance and efficiency. In this paper, we identify two primary factors contributing to performance degradation: fitting errors and the inference gap. Our key insight is that fitting errors can be mitigated by linearly extrapolating the incorrect score functions, while the inference gap can be reduced by shifting the Gaussian flow to a reflectance-aware residual space. Based on the above insights, we design Reflectance-Aware Trajectory Refinement (RATR) module, a simple yet effective module to refine the teacher trajectory using the reflectance component of images. Following this, we introduce \textbf{Re}flectance-aware \textbf{D}iffusion with \textbf{Di}stilled \textbf{T}rajectory (\textbf{ReDDiT}), an efficient and flexible distillation framework tailored for LLIE. Our framework achieves comparable performance to previous diffusion-based methods with redundant steps in just 2 steps while establishing new state-of-the-art (SOTA) results with 8 or 4 steps. Comprehensive experimental evaluations on 10 benchmark datasets validate the effectiveness of our method, consistently outperforming existing SOTA methods.
Submission history
From: Guanzhou Lan [view email][v1] Wed, 16 Oct 2024 08:07:18 UTC (4,635 KB)
[v2] Thu, 21 Nov 2024 08:20:04 UTC (6,660 KB)
[v3] Wed, 18 Mar 2026 02:28:54 UTC (7,136 KB)
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
