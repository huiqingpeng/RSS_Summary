---
title: "Adaptive Anchor Policies for Efficient 4D Gaussian Streaming"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17227"
published: "2026-03-19"
fetched: "2026-03-19T15:06:43.872535"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Adaptive Anchor Policies for Efficient 4D Gaussian Streaming
View PDF HTML (experimental)Abstract:Dynamic scene reconstruction with Gaussian Splatting has enabled efficient streaming for real-time rendering and free-viewpoint video. However, most pipelines rely on fixed anchor selection such as Farthest Point Sampling (FPS), typically using 8,192 anchors regardless of scene complexity, which over-allocates computation under strict budgets. We propose Efficient Gaussian Streaming (EGS), a plug-in, budget-aware anchor sampler that replaces FPS with a reinforcement-learned policy while keeping the Gaussian streaming reconstruction backbone unchanged. The policy jointly selects an anchor budget and a subset of informative anchors under discrete constraints, balancing reconstruction quality and runtime using spatial features of the Gaussian representation. We evaluate EGS in two settings: fast rendering, which prioritizes runtime efficiency, and high-quality refinement, which enables additional optimization. Experiments on dynamic multi-view datasets show consistent improvements in the quality--efficiency trade-off over FPS sampling. On unseen data, in fast rendering at 256 anchors ($32\times$ fewer than 8,192), EGS improves PSNR by $+0.52$--$0.61$\,dB while running $1.29$--$1.35\times$ faster than IGS@8192 (N3DV and MeetingRoom). In high-quality refinement, EGS remains competitive with the full-anchor baseline at substantially lower anchor budgets. \emph{Code and pretrained checkpoints will be released upon acceptance.} \keywords{4D Gaussian Splatting \and 4D Gaussian Streaming \and Reinforcement Learning}
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
