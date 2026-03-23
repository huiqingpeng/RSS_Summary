---
title: "RiboSphere: Learning Unified and Efficient Representations of RNA Structures"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19636"
published: "2026-03-23"
fetched: "2026-03-24T07:20:31.749442"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:RiboSphere: Learning Unified and Efficient Representations of RNA Structures
View PDF HTML (experimental)Abstract:Accurate RNA structure modeling remains difficult because RNA backbones are highly flexible, non-canonical interactions are prevalent, and experimentally determined 3D structures are comparatively scarce. We introduce \emph{RiboSphere}, a framework that learns \emph{discrete} geometric representations of RNA by combining vector quantization with flow matching. Our design is motivated by the modular organization of RNA architecture: complex folds are composed from recurring structural motifs. RiboSphere uses a geometric transformer encoder to produce SE(3)-invariant (rotation/translation-invariant) features, which are discretized with finite scalar quantization (FSQ) into a finite vocabulary of latent codes. Conditioned on these discrete codes, a flow-matching decoder reconstructs atomic coordinates, enabling high-fidelity structure generation. We find that the learned code indices are enriched for specific RNA motifs, suggesting that the model captures motif-level compositional structure rather than acting as a purely compressive bottleneck. Across benchmarks, RiboSphere achieves strong performance in structure reconstruction (RMSD 1.25\,Å, TM-score 0.84), and its pretrained discrete representations transfer effectively to inverse folding and RNA--ligand binding prediction, with robust generalization in data-scarce regimes.
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
