---
title: "Unveiling the Mechanism of Continuous Representation Full-Waveform Inversion: A Wave Based Neural Tangent Kernel Framework"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22362"
published: "2026-03-25"
fetched: "2026-03-26T07:13:25.657671"
---

Computer Science > Machine Learning
[Submitted on 23 Mar 2026]
Title:Unveiling the Mechanism of Continuous Representation Full-Waveform Inversion: A Wave Based Neural Tangent Kernel Framework
View PDF HTML (experimental)Abstract:Full-waveform inversion (FWI) estimates physical parameters in the wave equation from limited measurements and has been widely applied in geophysical exploration, medical imaging, and non-destructive testing. Conventional FWI methods are limited by their notorious sensitivity to the accuracy of the initial models. Recent progress in continuous representation FWI (CR-FWI) demonstrates that representing parameter models with a coordinate-based neural network, such as implicit neural representation (INR), can mitigate the dependence on initial models. However, its underlying mechanism remains unclear, and INR-based FWI shows slower high-frequency convergence. In this work, we investigate the general CR-FWI framework and develop a unified theoretical understanding by extending the neural tangent kernel (NTK) for FWI to establish a wave-based NTK framework. Unlike standard NTK, our analysis reveals that wave-based NTK is not constant, both at initialization and during training, due to the inherent nonlinearity of FWI. We further show that the eigenvalue decay behavior of the wave-based NTK can explain why CR-FWI alleviates the dependency on initial models and shows slower high-frequency convergence. Building on these insights, we propose several CR-FWI methods with tailored eigenvalue decay properties for FWI, including a novel hybrid representation combining INR and multi-resolution grid (termed IG-FWI) that achieves a more balanced trade-off between robustness and high-frequency convergence rate. Applications in geophysical exploration on Marmousi, 2D SEG/EAGE Salt and Overthrust, 2004 BP model, and the more realistic 2014 Chevron models show the superior performance of our proposed methods compared to conventional FWI and existing INR-based FWI methods.
Current browse context:
cs.LG
Change to browse by:
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
