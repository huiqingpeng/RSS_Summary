---
title: "PKINet-v2: Towards Powerful and Efficient Poly-Kernel Remote Sensing Object Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16341"
published: "2026-03-18"
fetched: "2026-03-18T18:11:13.705900"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:PKINet-v2: Towards Powerful and Efficient Poly-Kernel Remote Sensing Object Detection
View PDF HTML (experimental)Abstract:Object detection in remote sensing images (RSIs) is challenged by the coexistence of geometric and spatial complexity: targets may appear with diverse aspect ratios, while spanning a wide range of object sizes under varied contexts. Existing RSI backbones address the two challenges separately, either by adopting anisotropic strip kernels to model slender targets or by using isotropic large kernels to capture broader context. However, such isolated treatments lead to complementary drawbacks: the strip-only design can disrupt spatial coherence for regular-shaped objects and weaken tiny details, whereas isotropic large kernels often introduce severe background noise and geometric mismatch for slender structures. In this paper, we extend PKINet, and present a powerful and efficient backbone that jointly handles both challenges within a unified paradigm named Poly Kernel Inception Network v2 (PKINet-v2). PKINet-v2 synergizes anisotropic axial-strip convolutions with isotropic square kernels and builds a multi-scope receptive field, preserving fine-grained local textures while progressively aggregating long-range context across scales. To enable efficient deployment, we further introduce a Heterogeneous Kernel Re-parameterization (HKR) Strategy that fuses all heterogeneous branches into a single depth-wise convolution for inference, eliminating fragmented kernel launches without accuracy loss. Extensive experiments on four widely-used benchmarks, including DOTA-v1.0, DOTA-v1.5, HRSC2016, and DIOR-R, demonstrate that PKINet-v2 achieves state-of-the-art accuracy while delivering a $\textbf{3.9}\times$ FPS acceleration compared to PKINet-v1, surpassing previous remote sensing backbones in both effectiveness and efficiency.
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
