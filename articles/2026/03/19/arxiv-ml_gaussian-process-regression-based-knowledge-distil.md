---
title: "Gaussian Process Regression-based Knowledge Distillation Framework for Simultaneous Prediction of Physical and Mechanical Properties of Epoxy Polymers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16925"
published: "2026-03-19"
fetched: "2026-03-19T13:06:13.970975"
---

Condensed Matter > Soft Condensed Matter
[Submitted on 12 Mar 2026]
Title:Gaussian Process Regression-based Knowledge Distillation Framework for Simultaneous Prediction of Physical and Mechanical Properties of Epoxy Polymers
View PDF HTML (experimental)Abstract:Epoxy polymers are widely used due to their multifunctional properties, but machine learning (ML) applications remain limited owing to their complex 3D molecular structure, multi-component nature, and lack of curated datasets. Existing ML studies are largely restricted to simulation data, specific properties, or narrow constituent ranges. To address these limitations, we developed an informed Gaussian Process Regression-based Knowledge Distillation (GPR-KD) framework for predicting multiple physical (glass transition temperature, density) and mechanical properties (elastic modulus, tensile strength, compressive strength, flexural strength, fracture energy, adhesive strength) of thermoset epoxy polymers. The model was trained on experimental literature data covering diverse monomer classes (9 resins, 40 hardeners). Individual GPR models serve as teacher models capturing nonlinear feature-property relationships, while a unified neural network student model learns distilled knowledge across all properties simultaneously. By encoding the target property as an input feature, the student model leverages cross-property correlations. Molecular-level descriptors extracted from SMILES representations using RDKit create a physics-informed model. The framework combines GPR interpretability and robustness with deep learning scalability and generalization. Comparative analysis demonstrates superior prediction accuracy over conventional ML models. Simultaneous multi-property prediction further improves accuracy through information sharing across correlated properties. The proposed framework enables accelerated design of novel epoxy polymers with tailored properties.
Current browse context:
cond-mat.soft
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
