---
title: "TsetlinWiSARD: On-Chip Training of Weightless Neural Networks using Tsetlin Automata on FPGAs"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.24186"
published: "2026-03-26"
fetched: "2026-03-27T07:12:54.112169"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:TsetlinWiSARD: On-Chip Training of Weightless Neural Networks using Tsetlin Automata on FPGAs
View PDFAbstract:Increasing demands for adaptability, privacy, and security at the edge have persistently pushed the frontiers for a new generation of machine learning (ML) algorithms with training and inference capabilities on-chip. Weightless Neural Network (WNN) is such an algorithm that is principled on lookup table based simple neuron structures. As a result, it offers architectural benefits, such as low-latency, low-complexity inference, compared to deep neural networks that depend heavily on multiply-accumulate operations. However, traditional WNNs rely on memorization-based one-shot training, which either leads to overfitting and reduced accuracy or requires tedious post-training adjustments, limiting their effectiveness for efficient on chip training.
In this work, we propose TsetlinWiSARD, a training approach for WNNs that leverages Tsetlin Automata (TAs) to enable probabilistic, feedback-driven learning. It overcomes the overfitting of WiSARD's one-shot training with iterative optimization, while maintaining simple, continuous binary feedback for efficient on-chip training. Central to our approach is a field programmable gate array (FPGA)-based training architecture that delivers state-of-the-art accuracy while significantly improving hardware efficiency. Our approach provides over 1000x faster training when compared with the traditional WiSARD implementation of WNNs. Further, we demonstrate 22% reduced resource usage, 93.3% lower latency, and 64.2% lower power consumption compared to FPGA-based training accelerators implementing other ML algorithms.
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
