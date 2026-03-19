---
title: "LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17965"
published: "2026-03-19"
fetched: "2026-03-19T16:19:18.621058"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition
View PDF HTML (experimental)Abstract:Media design layer generation enables the creation of fully editable, layered design documents such as posters, flyers, and logos using only natural language prompts. Existing methods either restrict outputs to a fixed number of layers or require each layer to contain only spatially continuous regions, causing the layer count to scale linearly with design complexity. We propose LaDe (Layered Media Design), a latent diffusion framework that generates a flexible number of semantically meaningful layers. LaDe combines three components: an LLM-based prompt expander that transforms a short user intent into structured per-layer descriptions that guide the generation, a Latent Diffusion Transformer with a 4D RoPE positional encoding mechanism that jointly generates the full media design and its constituent RGBA layers, and an RGBA VAE that decodes each layer with full alpha-channel support. By conditioning on layer samples during training, our unified framework supports three tasks: text-to-image generation, text-to-layers media design generation, and media design decomposition. We compare LaDe to Qwen-Image-Layered on text-to-layers and image-to-layers tasks on the Crello test set. LaDe outperforms Qwen-Image-Layered in text-to-layers generation by improving text-to-layer alignment, as validated by two VLM-as-a-judge evaluators (GPT-4o mini and Qwen3-VL).
Submission history
From: Iuliana Georgescu [view email][v1] Wed, 18 Mar 2026 17:34:07 UTC (38,562 KB)
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
