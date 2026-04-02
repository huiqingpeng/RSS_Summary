---
title: "Measuring the Representational Alignment of Neural Systems in Superposition"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00208"
published: "2026-04-02"
fetched: "2026-04-03T07:18:37.225129"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Measuring the Representational Alignment of Neural Systems in Superposition
View PDF HTML (experimental)Abstract:Comparing the internal representations of neural networks is a central goal in both neuroscience and machine learning. Standard alignment metrics operate on raw neural activations, implicitly assuming that similar representations produce similar activity patterns. However, neural systems frequently operate in superposition, encoding more features than they have neurons via linear compression. We derive closed-form expressions showing that superposition systematically deflates Representational Similarity Analysis, Centered Kernel Alignment, and linear regression, causing networks with identical feature content to appear dissimilar. The root cause is that these metrics are dependent on cross-similarity between two systems' respective superposition matrices, which under assumption of random projection usually differ significantly, not on the latent features themselves: alignment scores conflate what a system represents with how it represents it. Under partial feature overlap, this confound can invert the expected ordering, making systems sharing fewer features appear more aligned than systems sharing more. Crucially, the apparent misalignment need not reflect a loss of information; compressed sensing guarantees that the original features remain recoverable from the lower-dimensional activity, provided they are sparse. We therefore argue that comparing neural systems in superposition requires extracting and aligning the underlying features rather than comparing the raw neural mixtures.
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
