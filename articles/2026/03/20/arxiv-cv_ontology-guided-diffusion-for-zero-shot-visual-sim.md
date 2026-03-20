---
title: "Ontology-Guided Diffusion for Zero-Shot Visual Sim2Real Transfer"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18719"
published: "2026-03-20"
fetched: "2026-03-20T15:15:00.886297"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Ontology-Guided Diffusion for Zero-Shot Visual Sim2Real Transfer
View PDF HTML (experimental)Abstract:Bridging the simulation-to-reality (sim2real) gap remains challenging as labelled real-world data is scarce. Existing diffusion-based approaches rely on unstructured prompts or statistical alignment, which do not capture the structured factors that make images look real. We introduce Ontology- Guided Diffusion (OGD), a neuro-symbolic zero-shot sim2real image translation framework that represents realism as structured knowledge. OGD decomposes realism into an ontology of interpretable traits -- such as lighting and material properties -- and encodes their relationships in a knowledge graph. From a synthetic image, OGD infers trait activations and uses a graph neural network to produce a global embedding. In parallel, a symbolic planner uses the ontology traits to compute a consistent sequence of visual edits needed to narrow the realism gap. The graph embedding conditions a pretrained instruction-guided diffusion model via cross-attention, while the planned edits are converted into a structured instruction prompt. Across benchmarks, our graph-based embeddings better distinguish real from synthetic imagery than baselines, and OGD outperforms state-of-the-art diffusion methods in sim2real image translations. Overall, OGD shows that explicitly encoding realism structure enables interpretable, data-efficient, and generalisable zero-shot sim2real transfer.
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
