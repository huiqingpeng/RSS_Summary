---
title: "Trained Persistent Memory for Frozen Encoder--Decoder LLMs: Six Architectural Methods"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16413"
published: "2026-03-18"
fetched: "2026-03-18T15:43:44.110326"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Trained Persistent Memory for Frozen Encoder--Decoder LLMs: Six Architectural Methods
View PDF HTML (experimental)Abstract:Frozen encoder--decoder language models are stateless: the latent representation is discarded after every forward pass, so no information persists across sessions. This paper presents a \textbf{proof-of-concept pilot study} showing that persistent memory in the \emph{continuous latent space} of a frozen LLM is feasible -- even under severe resource constraints (a single frozen Flan-T5-XL backbone, small trainable adapters, a single dataset). We implement six architectural methods spanning three injection points and four write mechanisms; unlike text-level memory systems, every write and read is a differentiable operation on dense vectors. After training only the adapter, the memory bank continues to accumulate at inference time without gradients, enabling \emph{conversational learning}. Under a forgetting-curve evaluation on LoCoMo at two capacity scales (1$\times$ and 10$\times$), the stateless baseline scores exactly zero; at 10$\times$ all six trained adapters produce positive memory-recall curves; at 1$\times$ three methods collapse, revealing capacity as a critical design parameter. Because the memory bank is a compact numerical array, it can be scaled to arbitrarily large capacity without altering the backbone. We argue that full end-to-end training with larger models, larger data, and orders-of-magnitude larger memory will yield substantially stronger results; this pilot study establishes the feasibility baseline and design-space taxonomy that such efforts require.
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
