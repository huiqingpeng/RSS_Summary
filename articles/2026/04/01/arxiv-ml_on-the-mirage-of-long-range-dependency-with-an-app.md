---
title: "On the Mirage of Long-Range Dependency, with an Application to Integer Multiplication"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29069"
published: "2026-04-01"
fetched: "2026-04-02T07:14:54.797296"
---

Computer Science > Machine Learning
[Submitted on 30 Mar 2026]
Title:On the Mirage of Long-Range Dependency, with an Application to Integer Multiplication
View PDFAbstract:Integer multiplication has long been considered a hard problem for neural networks, with the difficulty widely attributed to the O(n) long-range dependency induced by carry chains. We argue that this diagnosis is wrong: long-range dependency is not an intrinsic property of multiplication, but a mirage produced by the choice of computational spacetime. We formalize the notion of mirage and provide a constructive proof: when two n-bit binary integers are laid out as a 2D outer-product grid, every step of long multiplication collapses into a $3 \times 3$ local neighborhood operation. Under this representation, a neural cellular automaton with only 321 learnable parameters achieves perfect length generalization up to $683\times$ the training range. Five alternative architectures -- including Transformer (6,625 params), Transformer+RoPE, and Mamba -- all fail under the same representation. We further analyze how partial successes locked the community into an incorrect diagnosis, and argue that any task diagnosed as requiring long-range dependency should first be examined for whether the dependency is intrinsic to the task or induced by the computational spacetime.
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
