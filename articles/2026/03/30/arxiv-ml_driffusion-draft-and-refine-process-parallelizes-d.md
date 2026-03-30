---
title: "DRiffusion: Draft-and-Refine Process Parallelizes Diffusion Models with Ease"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25872"
published: "2026-03-30"
fetched: "2026-03-31T07:18:34.457642"
---

Computer Science > Machine Learning
[Submitted on 26 Mar 2026]
Title:DRiffusion: Draft-and-Refine Process Parallelizes Diffusion Models with Ease
View PDF HTML (experimental)Abstract:Diffusion models have achieved remarkable success in generating high-fidelity content but suffer from slow, iterative sampling, resulting in high latency that limits their use in interactive applications. We introduce DRiffusion, a parallel sampling framework that parallelizes diffusion inference through a draft-and-refine process. DRiffusion employs skip transitions to generate multiple draft states for future timesteps and computes their corresponding noises in parallel, which are then used in the standard denoising process to produce refined results. Theoretically, our method achieves an acceleration rate of $\tfrac{1}{n}$ or $\tfrac{2}{n+1}$, depending on whether the conservative or aggressive mode is used, where $n$ denotes the number of devices. Empirically, DRiffusion attains 1.4$\times$-3.7$\times$ speedup across multiple diffusion models while incur minimal degradation in generation quality: on MS-COCO dataset, both FID and CLIP remain largely on par with those of the original model, while PickScore and HPSv2.1 show only minor average drops of 0.17 and 0.43, respectively. These results verify that DRiffusion delivers substantial acceleration and preserves perceptual quality.
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
