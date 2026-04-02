---
title: "Unsupervised 4D Flow MRI Velocity Enhancement and Unwrapping Using Divergence-Free Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00205"
published: "2026-04-02"
fetched: "2026-04-03T07:18:18.454693"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Unsupervised 4D Flow MRI Velocity Enhancement and Unwrapping Using Divergence-Free Neural Networks
View PDF HTML (experimental)Abstract:This work introduces an unsupervised Divergence and Aliasing-Free neural network (DAF-FlowNet) for 4D Flow Magnetic Resonance Imaging (4D Flow MRI) that jointly enhances noisy velocity fields and corrects phase wrapping artifacts. DAF-FlowNet parameterizes velocities as the curl of a vector potential, enforcing mass conservation by construction and avoiding explicit divergence-penalty tuning. A cosine data-consistency loss enables simultaneous denoising and unwrapping from wrapped phase images. On synthetic aortic 4D Flow MRI generated from computational fluid dynamics, DAF-FlowNet achieved lower errors than existing techniques (up to 11% lower velocity normalized root mean square error, 11% lower directional error, and 44% lower divergence relative to the best-performing alternative across noise levels), with robustness to moderate segmentation perturbations. For unwrapping, at peak velocity/velocity-encoding ratios of 1.4 and 2.1, DAF-FlowNet achieved 0.18% and 5.2% residual wrapped voxels, representing reductions of 72% and 18% relative to the best alternative method, respectively. In scenarios with both noise and aliasing, the proposed single-stage formulation outperformed a state-of-the-art sequential pipeline (up to 15% lower velocity normalized root mean square error, 11% lower directional error, and 28% lower divergence). Across 10 hypertrophic cardiomyopathy patient datasets, DAF-FlowNet preserved fine-scale flow features, corrected aliased regions, and improved internal flow consistency, as indicated by reduced inter-plane flow bias in aortic and pulmonary mass-conservation analyses recommended by the 4D Flow MRI consensus guidelines. These results support DAF-FlowNet as a framework that unifies velocity enhancement and phase unwrapping to improve the reliability of cardiovascular 4D Flow MRI.
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
