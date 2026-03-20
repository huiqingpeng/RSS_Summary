---
title: "Position: Spectral GNNs Are Neither Spectral Nor Superior for Node Classification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19091"
published: "2026-03-20"
fetched: "2026-03-20T12:18:36.332835"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Position: Spectral GNNs Are Neither Spectral Nor Superior for Node Classification
View PDF HTML (experimental)Abstract:Spectral Graph Neural Networks (Spectral GNNs) for node classification promise frequency-domain filtering on graphs, yet rest on flawed foundations. Recent work shows that graph Laplacian eigenvectors do not in general have the key properties of a true Fourier basis, but leaves the empirical success of Spectral GNNs unexplained. We identify two theoretical glitches: (1) commonly used "graph Fourier bases" are not classical Fourier bases for graph signals; (2) (n-1)-degree polynomials (n = number of nodes) can exactly interpolate any spectral response via a Vandermonde system, so the usual "polynomial approximation" narrative is not theoretically justified. The effectiveness of GCN is commonly attributed to spectral low-pass filtering, yet we prove that low- and high-pass behaviors arise solely from message-passing dynamics rather than Graph Fourier Transform-based spectral formulations. We then analyze two representative directed spectral models, MagNet and HoloNet. Their reported effectiveness is not spectral: it arises from implementation issues that reduce them to powerful MPNNs. When implemented consistently with the claimed spectral algorithms, performance becomes weak. This position paper argues that: for node classification, Spectral GNNs neither meaningfully capture the graph spectrum nor reliably improve performance; competitive results are better explained by their equivalence to MPNNs, sometimes aided by implementations inconsistent with their intended design.
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
