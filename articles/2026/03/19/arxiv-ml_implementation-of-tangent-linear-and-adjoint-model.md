---
title: "Implementation of tangent linear and adjoint models for neural networks based on a compiler library tool"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16976"
published: "2026-03-19"
fetched: "2026-03-19T13:07:40.454601"
---

Computer Science > Mathematical Software
[Submitted on 17 Mar 2026]
Title:Implementation of tangent linear and adjoint models for neural networks based on a compiler library tool
View PDFAbstract:This paper presents TorchNWP, a compilation library tool for the efficient coupling of artificial intelligence components and traditional numerical models. It aims to address the issues of poor cross-language compatibility, insufficient coupling flexibility, and low data transfer efficiency between operational numerical models developed in Fortran and Python-based deep learning frameworks. Based on LibTorch, it optimizes and designs a unified application-layer calling interface, converts deep learning models under the PyTorch framework into a static binary format, and provides C/C++ interfaces. Then, using hybrid Fortran/C/C++ programming, it enables the deployment of deep learning models within numerical models. Integrating TorchNWP into a numerical model only requires compiling it into a callable link library and linking it during the compilation and linking phase to generate the executable. On this basis, tangent linear and adjoint model based on neural networks are implemented at the C/C++ level, which can shield the internal structure of neural network models and simplify the construction process of four-dimensional variational data assimilation systems. Meanwhile, it supports deployment on heterogeneous platforms, is compatible with mainstream neural network models, and enables mapping of different parallel granularities and efficient parallel execution. Using this tool requires minimal code modifications to the original numerical model, thus reducing coupling costs. It can be efficiently integrated into numerical weather prediction models such as CMA-GFS and MCV, and has been applied to the coupling of deep learning-based physical parameterization schemes (e.g., radiation, non-orographic gravity wave drag) and the development of their tangent linear and adjoint models, significantly improving the accuracy and efficiency of numerical weather prediction.
Current browse context:
cs.MS
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
