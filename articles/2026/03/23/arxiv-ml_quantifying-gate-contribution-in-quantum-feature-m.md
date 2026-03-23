---
title: "Quantifying Gate Contribution in Quantum Feature Maps for Scalable Circuit Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19805"
published: "2026-03-23"
fetched: "2026-03-24T07:22:07.163108"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Quantifying Gate Contribution in Quantum Feature Maps for Scalable Circuit Optimization
View PDFAbstract:Quantum machine learning offers promising advantages for classification tasks, but noise, decoherence, and connectivity constraints in current devices continue to limit the efficient execution of feature map-based circuits. Gate Assessment and Threshold Evaluation (GATE) is presented as a circuit optimization methodology that reduces quantum feature maps using a novel gate significance index. This index quantifies the relevance of each gate by combining fidelity, entanglement, and sensitivity. It is formulated for both simulator/emulator environments, where quantum states are accessible, and for real hardware, where these quantities are estimated from measurement results and auxiliary circuits. The approach iteratively scans a threshold range, eliminates low-contribution gates, generates optimized quantum machine learning models, and ranks them based on accuracy, runtime, and a balanced performance criterion before final testing. The methodology is evaluated on real-world classification datasets using two representative quantum machine learning models, PegasosQSVM and Quantum Neural Network, in three execution scenarios: noise-free simulation, noisy emulation derived from an IBM backend, and real IBM quantum hardware. The structural impact of gate removal in feature maps is examined, compatibility with noise-mitigation techniques is studied, and the scalability of index computation is evaluated using approaches based on density matrices, matrix product states, tensor networks, and real-world devices. The results show consistent reductions in circuit size and runtime and, in many cases, preserved or improved predictive accuracy, with the best trade-offs typically occurring at intermediate thresholds rather than in the baseline circuits or in those compressed more aggressively.
Submission history
From: Francisco Martínez-Álvarez [view email][v1] Fri, 20 Mar 2026 09:44:07 UTC (333 KB)
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
