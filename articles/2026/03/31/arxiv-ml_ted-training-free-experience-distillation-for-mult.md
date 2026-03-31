---
title: "TED: Training-Free Experience Distillation for Multimodal Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26778"
published: "2026-03-31"
fetched: "2026-04-01T07:17:57.838592"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:TED: Training-Free Experience Distillation for Multimodal Reasoning
View PDF HTML (experimental)Abstract:Knowledge distillation is typically realized by transferring a teacher model's knowledge into a student's parameters through supervised or reinforcement-based optimization. While effective, such approaches require repeated parameter updates and large-scale training data, limiting their applicability in resource-constrained environments. In this work, we propose TED, a training-free, context-based distillation framework that shifts the update target of distillation from model parameters to an in-context experience injected into the student's prompt. For each input, the student generates multiple reasoning trajectories, while a teacher independently produces its own solution. The teacher then compares the student trajectories with its reasoning and the ground-truth answer, extracting generalized experiences that capture effective reasoning patterns. These experiences are continuously refined and updated over time. A key challenge of context-based distillation is unbounded experience growth and noise accumulation. TED addresses this with an experience compression mechanism that tracks usage statistics and selectively merges, rewrites, or removes low-utility experiences. Experiments on multimodal reasoning benchmarks MathVision and VisualPuzzles show that TED consistently improves performance. On MathVision, TED raises the performance of Qwen3-VL-8B from 0.627 to 0.702, and on VisualPuzzles from 0.517 to 0.561 with just 100 training samples. Under this low-data, no-update setting, TED achieves performance competitive with fully trained parameter-based distillation while reducing training cost by over 5x, demonstrating that meaningful knowledge transfer can be achieved through contextual experience.
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
