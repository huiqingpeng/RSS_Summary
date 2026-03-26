---
title: "CDMT-EHR: A Continuous-Time Diffusion Framework for Generating Mixed-Type Time-Series Electronic Health Records"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23719"
published: "2026-03-26"
fetched: "2026-03-27T07:16:24.323317"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:CDMT-EHR: A Continuous-Time Diffusion Framework for Generating Mixed-Type Time-Series Electronic Health Records
View PDF HTML (experimental)Abstract:Electronic health records (EHRs) are invaluable for clinical research, yet privacy concerns severely restrict data sharing. Synthetic data generation offers a promising solution, but EHRs present unique challenges: they contain both numerical and categorical features that evolve over time. While diffusion models have demonstrated strong performance in EHR synthesis, existing approaches predominantly rely on discrete-time formulations, which suffer from finite-step approximation errors and coupled training-sampling step counts. We propose a continuous-time diffusion framework for generating mixed-type time-series EHRs with three contributions: (1) continuous-time diffusion with a bidirectional gated recurrent unit backbone for capturing temporal dependencies, (2) unified Gaussian diffusion via learnable continuous embeddings for categorical variables, enabling joint cross-feature modeling, and (3) a factorized learnable noise schedule that adapts to per-feature-per-timestep learning difficulties. Experiments on two large-scale intensive care unit datasets demonstrate that our method outperforms existing approaches in downstream task performance, distribution fidelity, and discriminability, while requiring only 50 sampling steps compared to 1,000 for baseline methods. Classifier-free guidance further enables effective conditional generation for class-imbalanced clinical scenarios.
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
