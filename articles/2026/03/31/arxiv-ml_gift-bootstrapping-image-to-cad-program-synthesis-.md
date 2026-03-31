---
title: "GIFT: Bootstrapping Image-to-CAD Program Synthesis via Geometric Feedback"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27448"
published: "2026-03-31"
fetched: "2026-04-01T07:24:17.258292"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:GIFT: Bootstrapping Image-to-CAD Program Synthesis via Geometric Feedback
View PDF HTML (experimental)Abstract:Generating executable CAD programs from images requires alignment between visual geometry and symbolic program representations, a capability that current methods fail to learn reliably as design complexity increases. Existing fine-tuning approaches rely on either limited supervised datasets or expensive post-training pipelines, resulting in brittle systems that restrict progress in generative CAD design. We argue that the primary bottleneck lies not in model or algorithmic capacity, but in the scarcity of diverse training examples that align visual geometry with program syntax. This limitation is especially acute because the collection of diverse and verified engineering datasets is both expensive and difficult to scale, constraining the development of robust generative CAD models. We introduce Geometric Inference Feedback Tuning (GIFT), a data augmentation framework that leverages geometric feedback to turn test-time compute into a bootstrapped set of high-quality training samples. GIFT combines two mechanisms: Soft-Rejection Sampling (GIFT-REJECT), which retains diverse high-fidelity programs beyond exact ground-truth matches, and Failure-Driven Augmentation (GIFT-FAIL), which converts near-miss predictions into synthetic training examples that improve robustness on challenging geometries. By amortizing inference-time search into the model parameters, GIFT captures the benefits of test-time scaling while reducing inference compute by 80%. It improves mean IoU by 12% over a strong supervised baseline and remains competitive with more complex multimodal systems, without requiring additional human annotation or specialized architectures.
Submission history
From: Giorgio Giannone [view email][v1] Sat, 28 Mar 2026 23:49:20 UTC (7,622 KB)
Current browse context:
cs.LG
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
