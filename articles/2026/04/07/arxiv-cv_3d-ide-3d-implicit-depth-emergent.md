---
title: "3D-IDE: 3D Implicit Depth Emergent"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03296"
published: "2026-04-07"
fetched: "2026-04-08T07:02:40.813682"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 28 Mar 2026]
Title:3D-IDE: 3D Implicit Depth Emergent
View PDF HTML (experimental)Abstract:Leveraging 3D information within Multimodal Large Language Models (MLLMs) has recently shown significant advantages for indoor scene understanding. However, existing methods, including those using explicit ground-truth 3D positional encoding and those grafting external 3D foundation models for implicit geometry, struggle with the trade-off in 2D-3D representation fusion, leading to suboptimal deployment. To this end, we propose 3D-Implicit Depth Emergence, a method that reframes 3D perception as an emergent property derived from geometric self-supervision rather than explicit encoding. Our core insight is the Implicit Geometric Emergence Principle: by strategically leveraging privileged geometric supervision through mechanisms like a fine-grained geometry validator and global representation constraints, we construct an information bottleneck. This bottleneck forces the model to maximize the mutual information between visual features and 3D structures, allowing 3D awareness to emerge naturally within a unified visual representation. Unlike existing approaches, our method enables 3D perception to emerge implicitly, disentangling features in dense regions and, crucially, eliminating depth and pose dependencies during inference with zero latency overhead. This paradigm shift from external grafting to implicit emergence represents a fundamental rethinking of 3D knowledge integration in visual-language models. Extensive experiments demonstrate that our method surpasses SOTA on multiple 3D scene understanding benchmarks. Our approach achieves a 55% reduction in inference latency while maintaining strong performance across diverse downstream tasks, underscoring the effectiveness of meticulously designed auxiliary objectives for dependency-free 3D understanding. Source code can be found at this http URL.
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
