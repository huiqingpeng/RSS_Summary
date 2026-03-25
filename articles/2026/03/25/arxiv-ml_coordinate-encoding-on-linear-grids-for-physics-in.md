---
title: "Coordinate Encoding on Linear Grids for Physics-Informed Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22700"
published: "2026-03-25"
fetched: "2026-03-26T07:16:20.768485"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Coordinate Encoding on Linear Grids for Physics-Informed Neural Networks
View PDF HTML (experimental)Abstract:In solving partial differential equations (PDEs), machine learning utilizing physical laws has received considerable attention owing to advantages such as mesh-free solutions, unsupervised learning, and feasibility for solving high-dimensional problems. An effective approach is based on physics-informed neural networks (PINNs), which are based on deep neural networks known for their excellent performance in various academic and industrial applications. However, PINNs struggled with model training owing to significantly slow convergence because of a spectral bias problem. In this study, we propose a PINN-based method equipped with a coordinate-encoding layer on linear grid cells. The proposed method improves the training convergence speed by separating the local domains using grid cells. Moreover, it reduces the overall computational cost by using axis-independent linear grid cells. The method also achieves efficient and stable model training by adequately interpolating the encoded coordinates between grid points using natural cubic splines, which guarantees continuous derivative functions of the model computed for the loss functions. The results of numerical experiments demonstrate the effective performance and efficient training convergence speed of the proposed method.
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
