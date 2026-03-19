---
title: "Translation Invariance of Neural Operators for the FitzHugh-Nagumo Model"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17523"
published: "2026-03-19"
fetched: "2026-03-19T12:12:34.006078"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Translation Invariance of Neural Operators for the FitzHugh-Nagumo Model
View PDF HTML (experimental)Abstract:Neural Operators (NOs) are a powerful deep learning framework designed to learn the solution operator that arise from partial differential equations. This study investigates NOs ability to capture the stiff spatio-temporal dynamics of the FitzHugh-Nagumo model, which describes excitable cells. A key contribution of this work is evaluating the translation invariance using a novel training strategy. NOs are trained using an applied current with varying spatial locations and intensities at a fixed time, and the test set introduces a more challenging out-of-distribution scenario in which the applied current is translated in both time and space. This approach significantly reduces the computational cost of dataset generation. Moreover we benchmark seven NOs architectures: Convolutional Neural Operators (CNOs), Deep Operator Networks (DONs), DONs with CNN encoder (DONs-CNN), Proper Orthogonal Decomposition DONs (POD-DONs), Fourier Neural Operators (FNOs), Tucker Tensorized FNOs (TFNOs), Localized Neural Operators (LocalNOs). We evaluated these models based on training and test accuracy, efficiency, and inference speed. Our results reveal that CNOs performs well on translated test dynamics. However, they require higher training costs, though their performance on the training set is similar to that of the other considered architectures. In contrast, FNOs achieve the lowest training error, but have the highest inference time. Regarding the translated dynamics, FNOs and their variants provide less accurate predictions. Finally, DONs and their variants demonstrate high efficiency in both training and inference, however they do not generalize well to the test set. These findings highlight the current capabilities and limitations of NOs in capturing complex ionic model dynamics and provide a comprehensive benchmark including their application to scenarios involving translated dynamics.
Current browse context:
cs.LG
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
