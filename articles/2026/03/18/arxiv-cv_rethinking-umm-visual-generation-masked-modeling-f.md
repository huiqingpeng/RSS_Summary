---
title: "Rethinking UMM Visual Generation: Masked Modeling for Efficient Image-Only Pre-training"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16139"
published: "2026-03-18"
fetched: "2026-03-18T18:06:32.362908"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Rethinking UMM Visual Generation: Masked Modeling for Efficient Image-Only Pre-training
View PDF HTML (experimental)Abstract:Unified Multimodal Models (UMMs) are often constrained by the pre-training of their $\textbf{visual generation components}$, which typically relies on inefficient paradigms and scarce, high-quality text-image paired data. In this paper, we systematically analyze pre-training recipes for $\textbf{UMM visual generation}$ and identify these two issues as the major bottlenecks.
To address them, we propose $\textbf{Image-Only Training for UMMs (IOMM)}$, a data-efficient two-stage training framework.
The first stage pre-trains the visual generative component $\textbf{exclusively}$ using abundant unlabeled image-only data, thereby removing the dependency on paired data $\textbf{for this costly phase}$. The second stage fine-tunes the model using a mixture of unlabeled images and a small curated set of text-image pairs, leading to improved instruction alignment and generative quality.
Extensive experiments show that IOMM not only improves training efficiency but also achieves state-of-the-art (SOTA) performance.
For example, our IOMM-B (3.6B) model was trained from scratch using only $\sim \textbf{1050}$ H800 GPU hours (with the vast majority, $\textbf{1000}$ hours, dedicated to the efficient $\textbf{image-only pre-training stage}$). It achieves $\textbf{0.89}$ on GenEval and $\textbf{0.55}$ on WISE--surpassing strong baselines such as BAGEL-7B (0.82 & 0.55) and BLIP3-o-4B (0.84 & 0.50).
Code is available $\href{this https URL}{this https URL}$.
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
